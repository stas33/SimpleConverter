
while True:
    try:
        str = float(input("Enter an amount in euro: "))
        break
    except ValueError as v:
        print(v)
    finally:
        choice = input("Enter the currency type you want to convert (USD,GBP,CHF,CAD,JPY): ")
        if choice == "USD":
            usd = str * 0.84
            print(f"Converted to US Dollar: {usd}")
            break
        elif choice == "GBP":
            gbp = str * 1.10
            print(f"Converted to Pound Sterling: {gbp}")
            break
        elif choice == "CHF":
            chf = str * 0.93
            print(f"Converted to Swiss Franc: {chf}")
            break
        elif choice == "CAD":
            cad = str * 0.64
            print(f"Converted to Canadian Dollar: {cad}")
            break
        elif choice == "JPY":
            jpy = str * 0.008
            print(f"Converted to Japanese Yen: {jpy}")
            break
        else:
            choice = input("Error. Please enter a valid currency type: ")