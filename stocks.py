import easygui
from time import sleep
import random
print "Welcome to StockSimulator!"
print "Starting..."
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
    net = SGDn+ DAHJn + MFHGn + BankT - BankD
    net2 = SGDn+ DAHJn + MFHGn
    print "Current Balance is:", BankT
    print "Currect Debt is:", BankD
    print "Current Networth is:", net
    print "Current Stock Total:", net2

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
    print "Use DisplayStocks() to display the stock names, their value, their average, and if their are above or below it, and how many shares you own of that stock."
    print " "
    print "Abbreviations:"
    print "To save time on typing, you can use these abbrevations."
    print " "
    print "Purchasing. purchaseSGD(), purchaseDAHJ(), and purchaseMFHG() are the same as PS(), PD(), and PM() respectively"
    print " "
    print "Selling. sellSGD(), sellDAHJ(), and sellMFHG() are the same as SS(), SD(), and SM() respectively."
    print " "
    print "Miscellaneous. A() is the same as advance(), DS() is the same as DisplayStocks(), BB is the same as BankBalance(), and use C() or Controls() to view this list."
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

#Controls
def C():
    Controls()
 
#***************************
#print "Controls"
#add controls/functions
#***************************
print "Game start"
print " "
print "================================================================================"
print " "
C()
print "================================================================================"
print "Day", days
print "Today's stock value's are:","SGD:", SGD,"|","DAHJ:", DAHJ,"|","MFHG", MFHG

