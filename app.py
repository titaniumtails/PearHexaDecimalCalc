print("\n")
print("=================================================================")
print("========== WELCOME TO THE 🍏 HEXIDECIMAL CALCULATOR ==========")
print("=================================================================")

ans = 'y'

def calculator(n):
    h = str(hex(int(n)))
    z = '00000'
    apple = ''
    h = h[2:]

    if len(h) == 3:
        pear = h + z
    elif len (h) == 2:
        pear = '0' + h + z
    else:
        pear = '00' + h + z

    for i in range(len(pear)-1, 0, -2):
        apple += pear[i-1:i+1]
    
    print("\n")    
    print("The hexidecimal is: ", h, "\nThe Apple hexidecimal conversion is: ", apple)
    print("---------------------------------------------------------------------------")
    print("\n")

    return apple

while ans == 'y':
    print("\n")
    n = input("Enter the number or MB to convert: ")
    try:
        calculator(n)
    except ValueError:
        print("*****YOU MAY ONLY ENTER A NUMBER. Please try again*****")
        print("\n")


    ans = input("Would you like to calculate another number? Please answer 'y' or 'n': ")
        
    if ans == 'n':
        print("\n")
        print("=============================================================")
        print("======================= GOOD BYE ============================")
        print("=============================================================")
        print("\n")
        break