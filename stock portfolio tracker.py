def stock_portfolio():
    
    prices = {
        "AAPL": 180,
        "TSLA": 250,
        "GOOG": 140,
        "AMZN": 155,
        "META": 330
    }

    print("📈 Stock Portfolio Tracker")
    total_value = 0
    details = []

    while True:
        stock = input("\nEnter stock symbol (AAPL/TSLA/GOOG/AMZN/META) or 'done' to finish: ").upper()

        if stock == "DONE":
            break

        if stock not in prices:
            print("❌ Invalid stock symbol. Try again.")
            continue

        qty = int(input(f"Enter quantity of {stock}: "))
        value = prices[stock] * qty
        total_value += value

        details.append(f"{stock} × {qty} = ${value}")

    print("\n💰 Total Investment Value:", total_value)

    with open("portfolio_summary.txt", "w") as file:
        file.write("Stock Portfolio Summary\n")
        file.write("------------------------\n")
        for item in details:
            file.write(item + "\n")
        file.write(f"\nTotal Investment = ${total_value}\n")

    print("\n📄 Summary saved as portfolio_summary.txt")

stock_portfolio()
