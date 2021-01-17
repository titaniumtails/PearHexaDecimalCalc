print("\n")
print("=================================================================")
print("========== WELCOME TO THE 🍐 HEXIDECIMAL CALCULATOR =============")
print("=================================================================")
print("\n")
print("This calculator will help convert values listed in Whatever Green's framebuffer guide, to enter as data into your config.plist")

#VARIABLES
contd_selection = ['y', 'n']
main_menu_selection = [1, 2]
user_cont_sel = 'y'
user_sel_bad = True

#FUNCTIONS

##MENUS
def sel_list_string(sel_list):
    return "'" + "' or '".join(map(str,sel_list)) + "'"


##CALCULATORS
def hexify(n):
    h = str(hex(int(n)))
    z = '00000'
    h = h[2:]

    if len(h) == 3:
        pear = h + z
    elif len (h) == 2:
        pear = '0' + h + z
    else:
        pear = '00' + h + z
    return pear

def appleify(n):
    pear = hexify(n)
    apple = ''
    
    for i in range(len(pear)-1, 0, -2):
        apple += pear[i-1:i+1]
    return apple

#LETS GO PROGRAM
print("\n")
print("Would you like to...")
print("1. I have the hexidecimal value already, I just need to REVERSE it into data readable config.plist data")
print("2. I just have the decimal number, I want to CONVERT & REVERSE (2-in-1) it into data readable config.plist")
print("\n")


while user_sel_bad:
    try:
        user_main_sel = int(input("Please enter the number of the calculator you wish to use: "))
        next(user_main_sel for s in main_menu_selection if user_main_sel == s)
        user_sel_bad = False
    except (ValueError, StopIteration):
        print("*****YOU MAY ONLY ENTER NUMBERS " + sel_list_string(main_menu_selection) +". Please try again*****")
        continue


while user_cont_sel == 'y':
    print("\n")
    try:
        n = input("Enter the number or MB to convert: ")
        print("\n")    
        print("The hexidecimal is: ", hexify(n), "\nThe Apple hexidecimal reversed conversion is: ", appleify(n))
        print("---------------------------------------------------------------------------")
        print("\n")
    except ValueError:
        print("*****YOU MAY ONLY ENTER A NUMBER. Please try again*****")
        #print("To calculate something else, or exit the calculator, please type 'exit' or 'menu'. ")
        continue
    
    user_cont_sel = input("Would you like to calculate another number? Please type " + sel_list_string(contd_selection) + ": ")

    while user_sel_bad:
        try:
            next(user_cont_sel for s in contd_selection if user_cont_sel == s)
            user_sel_bad = False
        except StopIteration:
            user_cont_sel = input("Please ONLY type "+ sel_list_string(contd_selection) + ": ")
        
    if user_cont_sel == 'n':
        print("\n")
        print("=============================================================")
        print("======================= GOOD BYE ============================")
        print("=============================================================")
        print("\n")
        break

#help(pyinputplus.parameters)