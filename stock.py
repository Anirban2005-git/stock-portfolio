
stock_prices = {
    "AAPL": 180.50,
    "TSLA": 250.75,
    "MSFT": 320.20,
    "AMZN": 135.90,
    "GOOG": 145.25
}

def main():
    print("=== Simple Stock Investment Calculator ===")
    print("Available stocks:", ", ".join(stock_prices.keys()))
    
    investments = {}
    total_value = 0.0
    
    while True:
        print("\nCurrent portfolio:")
        for stock, qty in investments.items():
            print(f"- {stock}: {qty} shares")
        
        print(f"\nTotal value: ${total_value:.2f}")
        
        stock = input("\nEnter stock symbol (or 'done' to finish): ").upper()
        if stock == 'DONE':
            break
            
        if stock not in stock_prices:
            print("Invalid stock! Available stocks are:", ", ".join(stock_prices.keys()))
            continue
            
        try:
            quantity = int(input(f"How many shares of {stock}? "))
            if quantity <= 0:
                print("Quantity must be positive!")
                continue
        except ValueError:
            print("Please enter a valid number!")
            continue
            
    
        if stock in investments:
            investments[stock] += quantity
        else:
            investments[stock] = quantity
            
       
        total_value = sum(qty * stock_prices[stock] for stock, qty in investments.items())
    
   
    save_file = input("\nSave to file? (y/n): ").lower()
    if save_file == 'y':
        filename = input("Enter filename (without extension): ")
        with open(f"{filename}.txt", 'w') as f:
            f.write("=== Stock Portfolio ===\n")
            for stock, qty in investments.items():
                f.write(f"{stock}: {qty} shares\n")
            f.write(f"\nTotal Value: ${total_value:.2f}")
        print(f"Saved to {filename}.txt")
    
    print("\nFinal Portfolio:")
    for stock, qty in investments.items():
        print(f"- {stock}: {qty} shares @ ${stock_prices[stock]:.2f} = ${qty * stock_prices[stock]:.2f}")
    print(f"\nTOTAL INVESTMENT VALUE: ${total_value:.2f}")

if __name__ == "__main__":
    main()