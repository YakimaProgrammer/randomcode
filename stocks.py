import easygui
from time import sleep
import random
print "Welcome to StockSimulator!"
print "Starting..."
gameisreset = 0 #if reset it would be 1
print "Setting bank variables"
BankT = 10000
BankD = 0
print "Bank variables set!"
print "Adding Stocks"
SGD = random.randint(1, 50)
DAHJ = random.randint(20, 105)
MFHG = random.randint(1, 30)

SGDowned = 0
DAHJowned = 0
MFHGowned = 0

print "Adding Game Bonus counter"
daystobonus = 10

print "Adding day counter!"
days = 1
print "Adding stock averages variables"

SGDy = SGD
DAHJy = DAHJ
MFHGy = MFHG

SGDa = SGDy / days
DAHJa = DAHJy / days
MFHGa = MFHGy / days
#***************************
#random.randint breaks if you use decimals
#This might be a good thing, as I can use 1.4 multiplier, then divide, to get
#exactly how many decimals I need!
#***************************
print "Stock values added!"
print "The stock starter values are:","SGD:", SGD,"|","DAHJ:", DAHJ,"|","MFHG", MFHG
print "Setting game functions"

#***************************
#Use function(V) or function("v") or function(v,x) to add custom variables to program
#***************************

#Advance day counter
#When calling a varible in a function, use global then the varible name. No idea why it works, it just does!

def advance():
    global BankT
    global days
    days = days + 1
    SGDm = random.randint(66, 170)
    DAHJm = random.randint(20, 200)
    MFHGm = random.randint(62, 190)
    global SGD
    global DAHJ
    global MFHG
    SGD = SGD*SGDm
    DAHJ = DAHJ*DAHJm
    MFHG = MFHG*MFHGm
    
    SGD = SGD/100
    DAHJ = DAHJ/100
    MFHG = MFHG/100

    global daystobonus
    daystobonus = daystobonus - 1

    #Tests if Daystobonus is 0
    if daystobonus == 0:
        daystobonus = 10
        prize = 1
        if prize == 1:
           choice = easygui.buttonbox("10 day bonus aquired! You can accept and gain 57 shares of SGD and then double SGD's current stock value, plus an additional 5,000 dallors, but have a fifty-fifty chace of losing 99% of your current savings, or you can pass on this offer.",
                                      choices = ['Accept', 'Pass'] )
          
        if choice == "Pass":
            print "You declined the 10 day bonus offer."
        else:
                chance = random.randint(1, 2)
        if chance == 1:
                SGDowned == SGDowned + 57
                SGD = SGD*2
                BankT = BankT + 5,000
                print "You just won the Ten Day Bonus!"
                BB()
        else:
                BankT = BankT / 99
                print "You just lost the Ten Day Bonus."
                BB()




    
    global SGDa
    global DAHJa
    global MFHGa

    global SGDy
    global DAHJy
    global MFHGy

    SGDa = SGDy / days
    DAHJa = DAHJy / days
    MFHGa = MFHGy / days


    print "================================================================================"
    print "Day", days
    print "The new stock value's are:","SGD:", SGD,"|","DAHJ:", DAHJ,"|","MFHG", MFHG

    if BankT == 0:
        print "================================================================================"
        print "Game over! All money was lost! Save will be reset!"
        print "Warning! Game will now throw a 0 / 0 error. Please ignore this error and start program again."
        print 0 / 0
      
    
#purchase functions
#SGDowned
    #if SGDowned < BankT
        #purchase stocks()
    #else:
    #print error purchasing stocks. Most likely cause: Insuffiecent funds.
#SGD purchase function
def purchaseSGD(shares):
    global SGD
    global BankT
    global SGDowned
    charge = SGD*shares
    if charge < BankT:
        BankT = BankT - charge
        SGDowned = SGDowned + shares
        
        print "Total shares of SGD is now:", SGDowned, "| Purchase fee was:", charge, "| Remaining Bank Balance:", BankT
    else:
        print "Error occured purchasing stocks. The most likely cause was: Insuffiecent funds."
#DAHJ purchase function
def purchaseDAHJ(shares):
    global DAHJ
    global BankT
    global DAHJowned
    charge = DAHJ*shares
    if charge < BankT:
        BankT = BankT - charge
        DAHJowned = DAHJowned + shares
        
        print "Total shares of DAHJ is now:", DAHJowned, "| Purchase fee was:", charge, "| Remaining Bank Balance:", BankT
    else:
        print "Error occured purchasing stocks. The most likely cause was: Insuffiecent funds."
#MFHG purchase function
def purchaseMFHG(shares):
    global MFHG
    global BankT
    global MFHGowned
    charge = MFHG*shares
    if charge < BankT:
        BankT = BankT - charge
        MFHGowned = MFHGowned + shares
        
        print "Total shares of MFHG is now:", MFHGowned, "| Purchase fee was:", charge, "| Remaining Bank Balance:", BankT
    else:
        print "Error occured purchasing stocks. The most likely cause is: Insuffiecent funds."

#SGD sell function

def sellSGD(shares):
    global SGD
    global BankT
    global SGDowned
    soldC = SGDowned*shares
    if shares < SGDowned:
        SGDowned = SGDowned - shares
        BankT = BankT + soldC
        BankT = BankT - 10
        print "Total shares of SGD is now:", SGDowned, "| You earned", soldC, "| New Bank Balance:", BankT
    else:
        print "Error occured selling stocks. The most likely cause was: Insuffiecent amount of stocks."

#DAHJ sell function

def sellDAHJ(shares):
    global DAHJ
    global BankT
    global DAHJowned
    soldC = DAHJowned*shares
    if shares < DAHJowned:
        DAHJowned = DAHJowned - shares
        BankT = BankT + soldC
        BankT = BankT - 10
        print "Total shares of DAHJ is now:", DAHJowned, "| You earned", soldC, "| New Bank Balance:", BankT
    else:
        print "Error occured selling stocks. The most likely cause was: Insuffiecent amount of stocks."

#MFHG sell function

def sellMFHG(shares):
    global MFHG
    global BankT
    global MFHGowned
    soldC = MFHGowned*shares
    if shares < MFHGowned:
        MFHGowned = MFHGowned - shares
        BankT = BankT + soldC
        BankT = BankT - 10
        print "Total shares of MFHG is now:", MFHGowned, "| You earned", soldC, "| New Bank Balance:", BankT
    else:
        print "Error occured selling stocks. The most likely cause was: Insuffiecent amount of stocks."

#***************************
#DisplayStocks
#***************************
def DisplayStocks():
    print "The stocks you can invest in are SGD, DAHJ, and MFHG"
    print "Stock Information"
    print "================================================================================"
    print "SGD information:"
    print "Value:", SGD
    print "Average:", SGDa

    if SGD < SGDa:
        print "SGD is currently below average!"
    else:
        print "SDG is currently above average!"
    
    print "Owned:", SGDowned
    print "================================================================================"
    print "DAHJ information:"
    print "Value:", DAHJ
    print "Average:", DAHJa
    
    if DAHJ < DAHJa:
        print "DAHJ is currently below average!"
    else:
        print "DAHJ is currently above average!"
    
    print "Owned:", DAHJowned
    print "================================================================================"
    print "MFHG information:"
    print "Value:", MFHG
    print "Average:", MFHGa

    if MFHG < MFHGa:
        print "MFHG is currently below average!"
    else:
        print "MFHG is currently above average!"
    
    print "Owned:", MFHGowned

#***************************
#BankBalance
#***************************
def BankBalance():
    global SGD
    global DAHJ
    global MFHG

    global DAHJowned
    global MFHGowned

    SGDn = SGD*SGDowned
    DAHJn = DAHJ*DAHJowned
    MFHGn = MFHG*MFHGowned
    net = SGDn + DAHJn + MFHGn + BankT - BankD
    net2 = SGDn + DAHJn + MFHGn
    print "Current Balance is:", BankT
    print "Currect Debt is:", BankD
    print "Current Networth is:", net
    print "Current Stock Total:", net2
"""
def Controls ():
    print "Purchasing:"
    print "Use purchaseSGD(), purchaseDAHJ(), and purchaseMFHG() to purchase stocks. To specify the amount you want to buy, enter the number you want in the paranethesis. For example, purchaseSGD(5) will buy 5 shares of SGD, if you have enought to purchase that amount in your bank account."
    print " "
    print "Selling:"
    print "Use sellSGD(), sellDAHJ(), and sellMFHG() to sell stocks. To specify the amount you want to sell, enter the number you want in the paranethesis. For example, sellSGD(5) will sell 5 shares of SGD, if you have enought of that stock."
    print " "
    print "Advancing:"
    print "Once you have made all the transactions you want for a certain day, you can use advance(), which will change all the stock values and reduce the Time to Bonus Counter. This action cannot be undone."
    print " "
    print "Banking Details:"
    print "To view the amount of money you have in game, type in BankBalance(). This will print out the stats on your bank account, such as Bank total, debts, networth, and stock total values."
    print " "
    print "Display Stocks"
    print "Use DisplayStocks() to display the stock names, their value, their average, and if their are above or below the average, and how many shares you own of that stock."
    print " "
    print "Abbreviations:"
    print "To save time on typing, you can use these abbrevations."
    print " "
    print "Purchasing. purchaseSGD(), purchaseDAHJ(), and purchaseMFHG() are the same as PS(), PD(), and PM() respectively"
    print " "
    print "Selling. sellSGD(), sellDAHJ(), and sellMFHG() are the same as SS(), SD(), and SM() respectively."
    print " "
    print "Miscellaneous. A() is the same as advance(), DS() is the same as DisplayStocks(), BB is the same as BankBalance(), and use C() or Controls() to view this list."

#Controls work fine, however as of day 4, they become irrelevant.
"""
#***************************
#Abbrievations
#***************************
def PS(stocks):
    purchaseSGD(stocks)
def PD(stocks):
    purchaseDAHJ(stocks)
def PM(stocks):
    purchaseMFHG(stocks)

#sell
def SS(stocks):
    sellSGD(stocks)
def SD(stocks):
    sellDAHJ(stocks)
def SM (stocks):
    sellMFHG(stocks)

#Advance
def A():
    advance()

#Displaystocks
def DS():
    DisplayStocks()

#BankBalance
def BB():
    BankBalance()
"""
#Controls
def C():
    Controls()
""" 
#***************************
#print "Controls"
#add controls/functions
#***************************
print "Game start"
print " "
print "================================================================================"
print " "
#C()
print "================================================================================"
print "Day", days 
intro = "SGD:", SGD,"|","DAHJ:", DAHJ,"|","MFHG:", MFHG
easygui.msgbox("Welcome to Stock Simulator! In a moment, you will be presented with the day's stock prices. After that, you will get various options which will allow you to buy, sell, view, or otherwise interact with various aspects of this game.", "Welcome!")
easygui.msgbox("Warning! Hitting [OK] prematurely, such as, before entering values, for  can cause errors which will end the program and may make you lose your progress!","Warning!")
easygui.msgbox(intro, "Today's stock value's are:")

#Main Loop of program
while 1 == 1:
    choice1 = easygui.buttonbox("What would you like to do?",
                                choices = ["Purchase stocks","Sell stocks","Advance","View Info","Save","Exit"])
    #Purchase Stocks
    
    if choice1 == "Purchase stocks":
        choice2 = easygui.buttonbox("Which stock would you like to purchase?",
                                    choices = ["SGD", "DAHJ", "MFHG"])
        if choice2 == "SGD":
            choice3 = easygui.enterbox("How many shares of SGD would you like to purchase?")
            
            charge = SGD*int(choice3)
            if charge < BankT:
                PS(int(choice3))
                easygui.msgbox("Purchase Successful!", "Purchase Successful!")
            else:
                easygui.msgbox("Unable to purchase stocks. The most likely cause is insufficent funds.", "Error!")

               
        if choice2 == "DAHJ":
            choice3 = easygui.enterbox("How many shares of DAHJ would you like to purchase?")
            
            charge = DAHJ*int(choice3)
            if charge < BankT:
                PD(int(choice3))
                easygui.msgbox("Purchase Successful!", "Purchase Successful!")
            else:
                easygui.msgbox("Unable to purchase stocks. The most likely cause is insufficent funds.", "Error!")

        if choice2 == "MFHG":
            choice3 = easygui.enterbox("How many shares of MFHG would you like to purchase?")
            
            charge = MFHG*int(choice3)
            if charge < BankT:
                PM(int(choice3))
                easygui.msgbox("Purchase Successful!", "Purchase Successful!")
            else:
                easygui.msgbox("Unable to purchase stocks. The most likely cause is insufficent funds.", "Error!")

    #Sell stocks
                
    if choice1 == "Sell stocks":
        choice2 = easygui.buttonbox("Which stock would you like to Sell?",
                                    choices = ["SGD", "DAHJ", "MFHG"])
        if choice2 == "SGD":
            choice3 = easygui.enterbox("How many shares of SGD would you like to sell?")

            if int(choice3) < SGDowned:
                SS(int(choice3))
                easygui.msgbox("Sale Successful!", "Sale Successful!")
            else:
                easygui.msgbox("Unable to sell stocks. The most likely cause is insufficent shares.", "Error!")

        if choice2 == "DAHJ":
            choice3 = easygui.enterbox("How many shares of DAHJ would you like to sell?")

            if int(choice3) < DAHJowned:
                SD(int(choice3))
                easygui.msgbox("Sale Successful!", "Sale Successful!")
            else:
                easygui.msgbox("Unable to sell stocks. The most likely cause is insufficent shares.", "Error!")

        if choice2 == "MFHG":
            choice3 = easygui.enterbox("How many shares of MFHG would you like to sell?")

            if int(choice3) < MFHGowned:
                SM(int(choice3))
                easygui.msgbox("Sale Successful!", "Sale Successful!")
            else:
                easygui.msgbox("Unable to sell stocks. The most likely cause is insufficent shares.", "Error!")

    #Advance

    if choice1 == "Advance":
        A()
        intro = "SGD:", SGD,"|","DAHJ:", DAHJ,"|","MFHG:", MFHG
        easygui.msgbox(intro, "Today's stock value's are:")

    #View Info
        
    if choice1 == "View Info":
        choice2 = easygui.buttonbox("What would you like to view?",
                                    choices = ["Stocks", "Bank balance", "Controls"])
        if choice2 == "Stocks":
            easygui.msgbox("Stock information will now be displayed. In 10 seconds, the main window will reopen.", "Stock Information")
            DS()
            sleep(10)

        if choice2 == "Bank balance":
            easygui.msgbox("Bank information will now be displayed. In 10 seconds, the main window will reopen.", "Bank Information")
            BB()
            sleep(10)

        if choice2 == "Controls":
            easygui.msgbox("Controls\n \nThis game has four main controls: Purchasing, Selling, Advancing, and displaying this list.\n \nPurchasing\n \nTo purchase a stock, select the [Purchase stock] button, select the stock you want to purchase and enter the number of stocks you want. Please note that entering an incorrect format, any besides numbers will crash the program. Additionally, enter only whole numbers; entering a number like 7.4 will only purchase 7 stocks.\n \nSelling\n \nSelling stocks works in a similar manner, select [Sell stocks], select the stock you want to sell. Additionally, enter only whole numbers; entering a number like 7.4 will only purchase 7 stocks.\n \nAdvancing\n \nTo move forward one day, select [Advance]. The new stock prices will display. You cannot undo a advance.\n \nDisplay controls\n \nTo find out more information on vaious things, like stocks and your bank balance, click on those catagories. The window will close and information will be displayed. After 10 seconds, the window will reopen and you can continue purchasing and selling stocks. Additionally, clicking on controls will display this list.","Controls","Next")
            easygui.msgbox("There are currently 3 stocks available for purchasing. These stocks are:\n \nSGD\n \nDAHJ\n \nMFHG.\n \nMFHG and SGD are coded to have smaller variations in price whereas DAHJ will tend to have larger variations. This won't always be true, but it is typically present.","Stocks","Next")
            easygui.msgbox("You can find a more in-depth discription of what the program is doing in the IDLE shell.","Behind the scenes","Next")
            easygui.msgbox("10 day bonus\n \nThe 10 day bonus is a randomly selected prize which are acquired every 10 in-game days. 10 day bonus have good rewards, but can also cause monotary downfalls. If a 10 day bonus goes in your favor, you will win amazing rewards, but if it doesn't, the consequences can be dire!. The better the reward the greater the risk!","10 day bonus")

    #Save
    if choice1 == "Save":
        with open('variables.py','w') as v:
            #Eracicate old file:
            v.seek(0)
            v.truncate()
            #Save variables as string
            BankTs = "BankT = " + str(BankT)
            BankDs = "BankD = " + str(BankD)
            SGDs = "SGD = " + str(SGD)
            DAHJs = "DAHJ = " + str(DAHJ)
            MFHGs = "MFHG = " + str(MFHG)

            SGDowneds = "SGDowned = " + str(SGDowned)
            DAHJowneds = "DAHJowned = " + str(DAHJowned)
            MFHGowneds = "MFHGowned = " + str(MFHGowned)

            SGDys = "SGDy = " + str(SGDy)
            DAHJys = "DAHJy = " + str(DAHJy)
            MFHGys = "MFHGy = " + str(MFHGy)

            SGDas = "SGDa = " + str(SGDa)
            DAHJas = "DAHJa = " + str(DAHJa)
            MFHGas = "MFHGa = " + str(MFHGa)

            dayss = "days = " + str(days)
            daystobonuss = "daystobonus = " + str(daystobonus)
            #Save stringed variables
            v.write(BankTs)
            v.write('\n')
            v.write(BankDs)
            v.write('\n')
            v.write(SGDs)
            v.write('\n')
            v.write(DAHJs)
            v.write('\n')
            v.write(MFHGs)
            v.write('\n')
            v.write(SGDowneds)
            v.write('\n')
            v.write(DAHJowneds)
            v.write('\n')
            v.write(MFHGowneds)
            v.write('\n')
            v.write(SGDys)
            v.write('\n')
            v.write(DAHJys)
            v.write('\n')
            v.write(MFHGys)
            v.write('\n')
            v.write(SGDas)
            v.write('\n')
            v.write(DAHJas)
            v.write('\n')
            v.write(MFHGas)
            v.write('\n')
            v.write(dayss)
            v.write('\n')
            v.write(daystobonuss)
            
            
            
            
            
            
            
    
    #Exit

    if choice1 == "Exit":
        choice2 = easygui.buttonbox("How would you like to exit?",
                                    choices = ["Exit without saving", "Exit and save", "No exit"])
        if choice2 == "Exit without saving":
            choice3 = easygui.buttonbox("Are you sure?",
                                        choices = ["Yes","No"])
            if choice3 == "Yes":
                print "Game exited!"
                break
                                    
        if choice2 == "Exit and save":
            choice3 = easygui.buttonbox("Are you sure?",
                                        choices = ["Yes","No"])
            if choice3 == "Yes":
                print "Unable to save. Functionallity lacking."
                print "Game exited!"
                break
                                    
