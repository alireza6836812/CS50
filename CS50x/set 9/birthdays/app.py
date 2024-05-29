import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///birthdays.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        # TODO: Add the user's entry into the database

        # Initialize an empty message string
        message = ""

        # Get the user's input from the form
        inputname = request.from.get("name")
        inputmonth = request.from.get("month")
        inputday = request.form.get("day")

        # Check if the user has entered all the required information
        if not inputname:
            message = "You didn't enter any name!"
        elif not inputday:
            message = "Birthday is missing from your input"
        elif not inputmonth:
            message = "You didn't enter birth month"
        else:
            # If all the required information is present, insert it into the database
            db.execute(
                "INSERT INTO birthday (name, month, day) VALUES(?, ?, ?)",
                inputname,
                inputmonth,
                inputday,
            )
        # Fetch all the birthdays from the database
        birthdays = db.execute("SELECT * FROM birthdays")

        # Render the index.html template with the message and birthdays
        return render_template("index.html", message = message, birthdays = birthdays)

    else:

        # TODO: Display the entries in the database on index.html

        # Fetch all the birthdays from the database
        birthdays = db.execute("SELECT * FROM birthdays")

        # Render the index.html template with the birthdays
        return render_template("index.html", birthdays = birthdays)



