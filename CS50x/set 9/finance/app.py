import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

import datetime
import pytz

# Initialize Flask application
app = Flask(__name__)

# Add custom filter to Jinja environment
app.jinja_env.filters["usd"] = usd

# Set session configuration to use filesystem instead of signed cookies
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up CS50 Library to interact with SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Set headers to prevent caching"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Display user's stock portfolio"""
    user_id = session.get("user_id")

    # Get user's cash balance
    cash = usd(db.execute("SELECT cash FROM users WHERE id = ?", user_id)[0]["cash"])
    # Get stocks owned by the user
    owned = db.execute(
        "SELECT symbol, shares FROM own WHERE user_id = ? ORDER BY symbol", user_id
    )

    # List to store stock information
    stocks = []
    tmp_stock = {}
    total = 0
    for own in owned:
        symbol = own["symbol"]
        price = lookup(symbol)["price"]
        shares = own["shares"]

        # Store stock symbol, price, and shares
        tmp_stock["symbol"] = symbol
        tmp_stock["price"] = usd(price)
        tmp_stock["shares"] = shares

        # Calculate total price for the shares of a stock
        price_calc = float(price) * float(shares)
        tmp_stock["total"] = usd(price_calc)

        # Add stock information to the list
        stocks.append(tmp_stock.copy())
        # Update total value of stocks
        total += price_calc

    # Render the index page with the stock and cash information
    return render_template("index.html", cash=cash, stocks=stocks, total=usd(total))


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Handle stock purchase requests"""
    if request.method == "POST":
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")

        # Validate form inputs
        if not symbol or not shares:
            return apology("Please, fill in all fields")

        stock = lookup(symbol)

        # Validate stock symbol
        if not stock:
            return apology("Invalid stock symbol")

        # Validate shares input
        try:
            int_shares = int(shares)
            if int_shares <= 0:
                return apology("Shares must be a positive integer")
        except:
            return apology("Invalid number of shares")

        # Calculate total cost of purchase
        tot_price = float(stock["price"]) * int_shares

        # Check if user has enough cash for purchase
        user_id = session.get("user_id")
        user = db.execute("SELECT * FROM users WHERE id = ?", user_id)
        cash = float(user[0]["cash"])
        if cash < tot_price:
            return apology(
                f"You need an additional {usd(tot_price - cash)} to complete the purchase"
            )

        # Get current date and time
        purchase_date = datetime.datetime.now(pytz.timezone("US/Eastern"))

        # Update 'own' table with purchase details
        symbol = symbol.upper()
        own = db.execute(
            "SELECT * FROM own WHERE user_id = ? AND symbol = ?", user_id, symbol
        )

        if not own:
            db.execute(
                "INSERT INTO own(user_id, symbol, shares, total) VALUES(?, ?, ?, ?)",
                user_id,
                stock["symbol"],
                shares,
                tot_price,
            )
        else:
            old_shares = int(own[0]["shares"])
            old_total = float(own[0]["total"])
            new_shares = old_shares + int_shares
            new_total = old_total + tot_price
            db.execute(
                "UPDATE own SET shares = ?, total = ? WHERE user_id = ? AND symbol = ?",
                new_shares,
                new_total,
                user_id,
                symbol,
            )

        # Update user's cash balance
        new_cash = cash - tot_price
        db.execute("UPDATE users SET cash = ? WHERE id = ?", new_cash, user_id)

        # Record the purchase in 'history' table
        db.execute(
            "INSERT INTO history(user_id, symbol, shares, money, action, date) VALUES(?, ?, ?, ?, ?, ?)",
            user_id,
            symbol,
            shares,
            usd(tot_price),
            "BOUGHT",
            purchase_date,
        )

        return redirect("/")
    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    records = db.execute(
        "SELECT * FROM history WHERE user_id = ?", session.get("user_id")
    )
    return render_template("history.html", records=records)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Handle user login requests"""
    # Clear any existing user session
    session.clear()

    # Handle POST request (form submission)
    if request.method == "POST":
        # Validate username input
        if not request.form.get("username"):
            return apology("Username is required", 403)

        # Validate password input
        elif not request.form.get("password"):
            return apology("Password is required", 403)

        # Query database for the provided username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Validate username and password
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("Invalid username and/or password", 403)

        # Store user's ID in session
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # Handle GET request (page load/redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Handle user logout requests"""
    # Clear any existing user session
    session.clear()

    # Redirect user to login page
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Handle stock quote requests"""
    if request.method == "POST":
        symbol = request.form.get("symbol")

        # Validate symbol input
        if not symbol:
            return apology("Stock symbol is required")

        # Lookup stock information
        stock = lookup(symbol)

        # Validate stock symbol
        if not stock:
            return apology("Invalid stock symbol")
        else:
            # Render quoted.html with stock information
            return render_template(
                "quoted.html",
                name=stock["name"],
                price=usd(stock["price"]),
                symbol=stock["symbol"],
            )

    else:
        # Render quote.html for GET requests
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        user = db.execute("SELECT * FROM users WHERE username = ?", username)

        # Check that the username tab has been filled in and if it doesn't exist already
        if not username:
            return apology(
                "You must insert a username! How am I supposed to register you otherwise?"
            )
        elif user and username == user[0]["username"]:
            return apology("My deepest apologies. This username has already been taken")

        # Check that the password and confirmation tabs have been filled in and if they match
        if not password or not confirmation:
            return apology("I suggest you to protect your account with a password")
        elif password != confirmation:
            return apology("Better re-type the confirming password (they don't match)")

        # Encrypt password
        hashed = generate_password_hash(password, method="pbkdf2", salt_length=16)

        db.execute("INSERT INTO users(username, hash) VALUES(?, ?)", username, hashed)

        return render_template("login.html")

    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    user_id = session.get("user_id")
    owns = db.execute(
        "SELECT symbol, shares FROM own WHERE user_id = ? ORDER BY symbol", user_id
    )

    # Get all the shares symbols the user bought
    symbols = []
    for own in owns:
        symbols.append(own["symbol"])

    if request.method == "POST":
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")

        # Check if user inserted inputs
        if not symbol or not shares:
            return apology(
                "Please, fill in the blank tabs. You would make it easier for the both of us"
            )

        # Check if user owns the selected
        if symbol not in symbols:
            return apology(f"You currently do not own any shares of {symbol}")

        # Check if shares is a positive integer
        try:
            int_shares = int(shares)
            if int_shares <= 0:
                return apology("The shares value must be a positive integer")
        except:
            return apology("You can start by inserting a number in the shares tab")

        for own in owns:
            if own["symbol"] == symbol:
                if int(own["shares"]) >= int_shares:
                    # Sell shares
                    cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)[
                        0
                    ]["cash"]
                    earning = lookup(symbol)["price"] * int_shares
                    new_cash = float(cash) + float(earning)

                    # Give user the earning
                    db.execute(
                        "UPDATE users SET cash = ? WHERE id = ?", new_cash, user_id
                    )

                    # Check and remove the number of shares that have been sold
                    # if all shares have been sold, remove row from 'own' table
                    old_shares = int(own["shares"])
                    new_shares = old_shares - int_shares

                    if new_shares == 0:
                        db.execute(
                            "DELETE FROM own WHERE user_id = ? AND symbol = ?",
                            user_id,
                            symbol,
                        )
                    else:
                        db.execute(
                            "UPDATE own SET shares = ? WHERE user_id = ? AND symbol = ?",
                            new_shares,
                            user_id,
                            symbol,
                        )

                    # check if selling done
                    selling_date = datetime.datetime.now(pytz.timezone("US/Eastern"))

                    # selling record
                    db.execute(
                        "INSERT INTO history(user_id, symbol, shares, money, action, date) VALUES(?, ?, ?, ?, ?, ?)",
                        user_id,
                        symbol,
                        shares,
                        usd(earning),
                        "SOLD",
                        selling_date,
                    )

                else:
                    return apology(
                        "You don't currently own the selected amount of shares"
                    )

        return redirect("/")
    else:
        return render_template("sell.html", symbols=symbols)


@app.route("/password", methods=["GET", "POST"])
@login_required
def password():
    """Handle password change requests"""
    if request.method == "POST":
        old = request.form.get("old")
        new = request.form.get("new")
        confirmation = request.form.get("confirmation")

        # Get current user's ID and details
        user_id = session.get("user_id")
        user = db.execute("SELECT * FROM users WHERE id = ?", user_id)[0]

        # Validate form inputs
        if not old or not new or not confirmation:
            return apology("All fields are required to change password")

        # Validate old password
        if not check_password_hash(user["hash"], old):
            return apology("Incorrect old password")

        # Validate new password and confirmation match
        if new != confirmation:
            return apology("New password and confirmation do not match")

        # Hash the new password
        hashed = generate_password_hash(new, method="pbkdf2", salt_length=16)
        # Update user's password in the database
        db.execute("UPDATE users SET hash = ? WHERE id = ?", hashed, user_id)

        # Redirect user to home page after successful password change
        return redirect("/")
    else:
        # Render password change page for GET requests
        return render_template("password.html")
