import csv
import os
from datetime import datetime

portfolio = {}

print("===== STOCK PORTFOLIO TRACKER =====")

while True:
    ticker = input("\nEnter stock ticker (or DONE to finish): ").upper()

    if ticker == "DONE":
        break

    try:
        buy_price = float(input("Enter buying price: "))
        quantity = int(input("Enter number of shares: "))
        current_price = float(input("Enter current price: "))

        if buy_price <= 0 or quantity <= 0 or current_price <= 0:
            print("Values must be greater than zero.")
            continue

        portfolio[ticker] = {
            "buy_price": buy_price,
            "quantity": quantity,
            "current_price": current_price
        }

    except ValueError:
        print("Please enter valid numbers.")

if not portfolio:
    print("No stocks entered.")
    exit()

total_invested = 0
total_value = 0

print("\n========== PORTFOLIO SUMMARY ==========")

for ticker, details in portfolio.items():
    invested = details["buy_price"] * details["quantity"]
    value = details["current_price"] * details["quantity"]
    profit_loss = value - invested
    percentage = (profit_loss / invested) * 100

    total_invested += invested
    total_value += value

    print("\nStock:", ticker)
    print("Invested Amount: Rs.", round(invested, 2))
    print("Current Value: Rs.", round(value, 2))
    print("Profit/Loss: Rs.", round(profit_loss, 2))
    print("Percentage: ", round(percentage, 2), "%")

total_profit_loss = total_value - total_invested

print("\n========== TOTAL PORTFOLIO ==========")
print("Total Investment: Rs.", round(total_invested, 2))
print("Current Value: Rs.", round(total_value, 2))
print("Total Profit/Loss: Rs.", round(total_profit_loss, 2))

filename = "portfolio_summary.csv"
file_exists = os.path.isfile(filename)

with open(filename, "a", newline="") as file:
    writer = csv.writer(file)

    if not file_exists:
        writer.writerow([
            "Date", "Ticker", "Buy Price", "Quantity",
            "Current Price", "Invested", "Current Value",
            "Profit/Loss", "Percentage"
        ])

    for ticker, details in portfolio.items():
        invested = details["buy_price"] * details["quantity"]
        value = details["current_price"] * details["quantity"]
        profit_loss = value - invested
        percentage = (profit_loss / invested) * 100

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            ticker,
            details["buy_price"],
            details["quantity"],
            details["current_price"],
            invested,
            value,
            profit_loss,
            round(percentage, 2)
        ])

print("\nPortfolio saved successfully to portfolio_summary.csv")