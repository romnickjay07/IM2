def convert_currency(dollar):
    rate_rupee = 83.12 
    rate_pound = 0.76       
    rate_yuan = 7.31        

    rupee = dollar * rate_rupee
    pound = dollar * rate_pound
    yuan = dollar * rate_yuan
    return rupee, pound, yuan 

while True:
    value = input("Enter dollar ($) (* to exit): ")
    if value == "*":
        print("Bye")
        break
    try:
        dollar = float(value)
        rupee, pound, yuan = convert_currency(dollar)
        print(f"\nDollar ($)\tIndian Rupee (₹)\tBritish Pound (£)\tChinese Yuan (¥)")
        print(f"{dollar:.2f}\t\t{rupee:.2f}\t\t{pound:.2f}\t\t{yuan:.2f}\n")
    except ValueError:
        print("Invalid input, please enter a number or * to exit.\n")