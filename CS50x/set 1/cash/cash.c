#include <cs50.h>
#include <stdio.h>

int get_cents(void);
int calculate_quarters(int cents);
int calculate_dimes(int cents);
int calculate_nickels(int cents);
int calculate_pennies(int cents);

int main(void)
{
    // get the cents custumer has
    int cents = get_cents();

    // calculate the quarters we should pay to customer
    int quarters = calculate_quarters(cents);
    cents = cents - quarters * 25;

    // Calculate the dims we should pay to customer
    int dimes = calculate_dimes(cents);
    cents = cents - dimes * 10;

    // Calculate the nickels we should pay to customer
    int nickels = calculate_nickels(cents);
    cents = cents - nickels * 5;

    // Calculate the pennies we should pay to customer
    int pennies = calculate_pennies(cents);
    cents = cents - pennies * 1;

    // calculate the sum of coins
    int coins = quarters + dimes + nickels + pennies;

    // print the total number of coins
    printf("%i\n", coins);
}

int get_cents(void)
{
    // cents calculation
    int cents;

    do
    {
        cents = get_int("Change Owed: ");
    }
    while (cents < 0);

    return cents;
}

int calculate_quarters(int cents)
{
    // quarters calculation
    int quarters = cents / 25;
    return quarters;
}

int calculate_dimes(int cents)
{
    // dimes calculation
    int dimes = cents / 10;
    return dimes;
}

int calculate_nickels(int cents)
{
    // nickels calculation
    int nickels = cents / 5;
    return nickels;
}

int calculate_pennies(int cents)
{
    // pennies calculation
    int pennies = cents / 1;
    return pennies;
}
