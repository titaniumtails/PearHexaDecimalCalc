print("\n")
print("=================================================================")
print("========== WELCOME TO THE 🍐 HEXIDECIMAL CALCULATOR ==========")
print("=================================================================")

selection = ['y', 'n']

# selection = ['y', 'n', 'menu', 'exit']
#     for m in selection[2::]:
#         print(m)
#         if m == n.lower():
#             break
user_sel = 'y'

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

while user_sel == 'y':
    print("\n")
    try:
        n = input("Enter the number or MB to convert: ")
        calculator(n)
    except ValueError:
        print("*****YOU MAY ONLY ENTER A NUMBER. Please try again*****")
        # print("To exit the calculator, please type 'exit'. ")
        continue
    
    user_sel = input("Would you like to calculate another number? Please type 'y' or 'n': ")
    user_sel_bad = True

    while user_sel_bad:
        try:
            next(user_sel for s in selection if user_sel == s)
            user_sel_bad = False
        except StopIteration:
            user_sel = input("Please ONLY type 'y' or 'n': ")
        
    if user_sel == 'n':
        print("\n")
        print("=============================================================")
        print("======================= GOOD BYE ============================")
        print("=============================================================")
        print("\n")
        break

#help(pyinputplus.parameters)