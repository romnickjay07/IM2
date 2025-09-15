def convert_currency(dollar):
    rate_rupee = 83.12   
    rate_pound = 0.76    
    rate_yuan = 7.31     
    rupee = dollar * rate_rupee
    pound = dollar * rate_pound
    yuan = dollar * rate_yuan
    return rupee, pound, yuan

dollars = []

while True:
    value = input("Enter dollar ($) (* to exit): ")
    if value == "*":
        print("\nBye\n")
        break
    try:
        dollar = float(value)
        dollars.append(dollar)
    except ValueError:
        print("Invalid input, please enter a number or * to exit.\n")

if dollars:
    print(f"\n{'Dollar ($)':<15}{'Indian Rupee (₹)':<20}{'British Pound (£)':<20}{'Chinese Yuan (¥)':<20}")
    for d in dollars:
        rupee, pound, yuan = convert_currency(d)
        print(f"{d:<15.2f}{rupee:<20.2f}{pound:<20.2f}{yuan:<20.2f}")