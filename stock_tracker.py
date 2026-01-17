def stock_portfolio_tracker():
    # Predefined stock prices
    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "GOOGL": 140,
        "MSFT": 320
    }

    total_investment = 0
    investment_details = []

    print("Stock Portfolio Tracker")
    print("Available Stocks:", ", ".join(stock_prices.keys()))
    print("Type 'done' to finish\n")

    while True:
        stock_name = input("Enter stock name: ").upper()

        if stock_name == "DONE":
            break

        if stock_name not in stock_prices:
            print("Stock not available. Try again.")
            continue

        try:
            quantity = int(input("Enter quantity: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        value = stock_prices[stock_name] * quantity
        total_investment += value

        investment_details.append(
            f"{stock_name} x {quantity} = {value}"
        )

        print(f"Added: {stock_name}, Value = {value}\n")

    print("\nInvestment Summary:")
    for item in investment_details:
        print(item)

    print("Total Investment Value:", total_investment)

    # Save result to file
    with open("portfolio.txt", "w") as file:
        for item in investment_details:
            file.write(item + "\n")
        file.write(f"Total Investment Value: {total_investment}")

    print("\nPortfolio saved to portfolio.txt")


stock_portfolio_tracker()
