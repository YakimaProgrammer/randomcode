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

#***************************
#random.randint breaks if you use decimals
#This might be a good thing, as I can use 1.4 multiplier, then divide, to get
#exactly how many decimals I need!
#***************************
print "Stock values added!"
print "The stock starter values are:","SGD:", SGD,"|","DAHJ:", DAHJ,"|","MFHG", MFHG
days = 0
print "Added day counter!"
print "Setting game functions"

#***************************
#Use function(V) or function("v") or function(v,x) to add custom variables to program
#***************************

#Advance day counter
#When calling a varible in a function, use global then the varible name. No idea why it works, it just does!

def advance():
    global days
    days = days + 1
    SGDm = random.randint(83, 170)
    DAHJm = random.randint(67, 670)
    MFHGm = random.randint(81, 190)
    global SGD
    global DAHJ
    global MFHG
    SGD = SGD*SGDm
    DAHJ = DAHJ*DAHJm
    MFHG = MFHG*MFHGm
    
    SGD = SGD/100
    DAHJ = DAHJ/100
    MFHG = MFHG/100

    print days
    print "The new stock value's are:","SGD:", SGD,"|","DAHJ:", DAHJ,"|","MFHG", MFHG

#purchase functions
#SGDowned
    #if SGDowned < BankT
        #purchase stocks()
    #else:
    #print error purchasing stocks. Most likely cause: Insuffiecent funds.
def purchaseSGD(shares):
    global SGD
    global BankT
    global SGDowned
    charge = SGD*shares
    if charge < BantT:
        BankT = BankT - charge
        SGDowned = SGDowned + shares
    else:
        print "Error occured purchasing stocks. The most likely cause is: Insuffiecent funds."

#***************************
#print "Controls"
#add controls/functions
#***************************
print "Game start"
print "Day", days
print "Today's stock value's are:","SGD:", SGD,"|","DAHJ:", DAHJ,"|","MFHG", MFHG

