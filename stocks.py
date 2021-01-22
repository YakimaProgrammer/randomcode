import easygui, os, importlib
from time import sleep
import random
"""
global rapidsave
rapidsave = 0
"""
global savegame
savegame = "undefined"
import_save = easygui.buttonbox("A save file has been detected. Would you like to import it, or start the game fresh?",
                                choices = ["Load", "Reset"])
if import_save == "Load":
    #Allows multiple save files. In earlier versions you could only have one named "variables.py".
    savegame = easygui.enterbox("Please enter the savegame you would like to use:")
    load = importlib.import_module(savegame, package=None)
    #Converts variables from savegame file to local variables.
    savegame = load.savegame
    gameisreset = load.gameisreset
    BankT = load.BankT
    BankD = load.BankD
    SGD = load.SGD
    DAHJ = load.DAHJ
    MFHG = load.MFHG
    SGDowned = load.SGDowned
    DAHJowned = load.DAHJowned
    MFHGowned = load.MFHGowned
    SGDy = load.SGDy
    MFHGy = load.MFHGy
    DAHJy = load.DAHJy
    days = load.days
    daystobonus = load.daystobonus
    gamemode = load.gamemode
    rEseta = load.rEseta
    rEsetb = load.rEsetb
    rEsetc = load.rEsetc
    rEsetd = load.rEsetd
    rEsete = load.rEsete
    rEsetf = load.rEsetf
    gold = load.gold
    silver = load.silver
    platinum = load.platinum
    unobtainium = load.unobtainium
    oil = load.oil
    HasLoan = load.HasLoan
    DaysToPayLoan = load.DaysToPayLoan
    LoanAmount = load.LoanAmount
    SGDa = load.SGDa
    MFHGa = load.MFHGa
    DAHJa = load.DAHJa
else:
    savegame = easygui.enterbox("Please enter the savegame name you would like to use:")
    savegame1 = savegame
    savegame = str(savegame) + ".py"
    gamemode = easygui.buttonbox("Chose your game difficulty:\nEasy: Stock prices stay above 15 dollars. Bank Balance can't fall below 1 dollar.\nNormal: If stock crashes you get 15 multiplied by the number of shares added to your bank account.\nHard:If a stock crashes, there is no insurance!\nUltrahard: Each advance costs 500 dollars. If a stock crashes, shares * stock avaerage will be subtracted from your bank account.\nImpossable: Each advance costs 2,000 dollars. If a stock crashes, 5(shares * stock avaerage) will be subtracted from your bank account. Stock transactions have a 200 commission fee. And finally, stock prices can't exceed 50 dollars. If they do, their stock price goes back to 5 dollars.",
                                 choices = ["Easy","Normal","Hard","Ultrahard","Impossable"])
    print "Welcome to StockSimulator!"
    print "Starting..."
    gameisreset = 0 #if reset it would be 1
    print "Setting bank variables"
    BankT = 10000
    BankD = 0
    HasLoan = 0
    DaysToPayLoan = 5
    LoanAmount = 0
    print "Bank variables set!"
    print "Adding Stocks"
    SGD = random.randint(1, 50)
    DAHJ = random.randint(20, 105)
    MFHG = random.randint(1, 30)
    gold = random.randint(1200, 5000)
    silver = random.randint(10, 30)
    platinum = random.randint(800, 1200)
    unobtainium = random.randint(2300, 54902)
    oil = random.randint(50, 130)
    SGDowned = 0
    DAHJowned = 0
    MFHGowned = 0
    rEseta = 0
    rEsetb = 0
    rEsetc = 0
    rEsetd = 0
    rEsete = 0
    rEsetf = 0
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
    #Save first!
    S()
    global rEseta
    global rEsetb
    global rEsetc
    global rEsetd
    global rEsete
    global rEsetf
    global gold
    global silver
    global platinum
    global unobtainium
    global oil
    gold = random.randint(1200, 5000)
    silver = random.randint(10, 30)
    platinum = random.randint(800, 1200)
    unobtainium = random.randint(2300, 54902)
    oil = random.randint(50, 130)
    goldm = random.randint(12, 500)
    silverm = random.randint(10, 300)
    platinumm = random.randint(80, 120)
    unobtainiumm = random.randint(23, 549)
    oilm = random.randint(50, 130)
    global BankT
    global days
    days = days + 1
    SGDm = random.randint(89, 117)
    DAHJm = random.randint(87, 115)
    MFHGm = random.randint(85, 119)
    global SGD
    global DAHJ
    global MFHG
    SGD = SGD*SGDm
    DAHJ = DAHJ*DAHJm
    MFHG = MFHG*MFHGm
    gold = gold * goldm
    silver = silver * silverm
    platinum = platinum * platinumm
    unobtainium = unobtainium * unobtainiumm
    oil = oil * oilm
    SGD = SGD/100
    DAHJ = DAHJ/100
    MFHG = MFHG/100
    gold = gold/100
    silver = silver/100
    platinum = platinum/100
    unobtainium = unobtainium/100
    oil = oil/100
    global SGDowned
    global daystobonus
    daystobonus = daystobonus - 1
    #Tests if Daystobonus is 0
    if daystobonus == 0:
        daystobonus = 10
        #Add new 10 day bonuses. Fix random prize.
        prize = int(random.uniform(1,3))
        if prize == 2:
            choice = easygui.buttonbox("10 day bonus aquired! You can accept and gain 10,000 dollars and 10 shares of unobtainium at " + str(unobtainium) +" dollars, but have a 50% chance of losing everything!",
                                      choices = ['Accept','Pass'])
            if choice == "Pass":
                easygui.msgbox("You declined the 10 day bonus!")
            if choice == "Accept":
                chance = int(random.uniform(1,3))
                if chance == 2:
                    BankT = BankT + 10000
                    Un = unobtainium * 10
                    BankT = BankT + Un
                    easygui.msgbox("You won the 10 day bonus!")
                    print "You just won the Ten Day Bonus!"
                else:
                    easygui.msgbox("You lost the 10 day bonus!")
                    print "You lost the 10 day bonus!"
                    """
                    with open('variables.py','w') as v:
                        #Eracicate old file:
                        v.seek(0)
                        v.truncate()
                    print 0 / 0
                    """
        if prize == 1:
           choice = easygui.buttonbox("10 day bonus aquired! You can accept and gain 57 shares of SGD and then double SGD's current stock value, which is currently valued at " + str(SGD) + " dollars, plus an additional 5,000 dallors, but have a fifty-fifty chace of losing 99% of your current savings, or you can pass on this offer.",
                                      choices = ['Accept', 'Pass'] )
           if choice == "Pass":
                easygui.msgbox("You declined the 10 day bonus!")
                print "You declined the 10 day bonus!"
           if choice == "Accept":
                chance = int(random.uniform(1,3))
                if chance == 1:
                    SGDowned = SGDowned + 57
                    SGD = SGD*2
                    BankT = BankT + 5,000
                    if type(BankT) is tuple:
                        BankT = BankT[0]
                    print "You just won the Ten Day Bonus!"
                    easygui.msgbox("You won the 10 day bonus!")
                else:
                  if type(BankT) is tuple:
                        BankT = BankT[0]
                  BankT = BankT / 99
                  print "You just lost the Ten Day Bonus."
                  easygui.msgbox("You lost the 10 day bonus!")
    global HasLoan
    global DaysToPayLoan
    global LoanAmount        
    if HasLoan == 1:
        DaysToPayLoan = DaysToPayLoan - 1
        LoanAmount = LoanAmount * 12
        LoanAmount = LoanAmount / 10
        LoanAmount = int(LoanAmount)
        if DaysToPayLoan != 0:
            easygui.msgbox("Warning! You currently have a debt totaling " + str(LoanAmount) + " dollar(s)! You only have " + str(DaysToPayLoan) + " day(s) to pay back your debt!")
        if DaysToPayLoan == 0:
            easygui.msgbox("Warning! You ended the game with a debt totaling " + str(LoanAmount) + " dollars!")
            print "Game over! Unable to pay back loan! Save will be reset!"
            with open('variables.py','w') as v:
                #Eracicate old file:
                v.seek(0)
                v.truncate()
            print "Warning! Game will now throw a 0 / 0 error. Please ignore this error and start program again."
            print 0 / 0
    global SGDa
    global DAHJa
    global MFHGa
    global SGDy
    global DAHJy
    global MFHGy
    SGDy = SGD + SGDy
    DAHJy = DAHJ + DAHJy
    MFHGy = MFHG + MFHGy
    SGDa = SGDy / days
    DAHJa = DAHJy / days
    MFHGa = MFHGy / days
    #Gamemode Implementation
    if gamemode == "Easy":
        if SGD < 15:
            SGD = 15
        if DAHJ < 15:
            DAHJ = 15
        if MFHG < 15:
            MFHG = 15
        if BankT == 0:
            BankT = 1
    if gamemode == "Normal":
        if SGD == 0:
            if rEsetd == 0:
                Sshares = SGDowned * 15
                BankT = BankT + Sshares
                rEsetd = 0
        if DAHJ == 0:
            if rEsete == 0:
                Sshares = DAHJowned * 15
                BankT = BankT + Sshares
                rEsete = 0
        if MFHG == 0:
            if rEsetf == 0:
                Sshares = MFHGowned * 15
                BankT = BankT + Sshares
                rEsetf = 0
    #if gamemode == "Hard":
    #    Nothing Happens!
    if gamemode == "Ultrahard":
        BankT = BankT - 500
        if SGD == 0:
            if rEseta == 0:
                Sshares = SGDowned * SGDa
                BankT = BankT - Sshares
                rEset = 1
        if DAHJ == 0:
            if rEsetb == 0:
                Sshares = DAHJowned * DAHJa
                BankT = BankT - Sshares
                rEset = 1
        if MFHG == 0:
            if rEsetc == 0:
                Sshares = MFHGowned * MFHGa
                BankT = BankT - Sshares
                rEset = 1
    if gamemode == "Impossable":
        BankT = BankT - 2000
        if SGD == 0:
            if rEseta == 0:
                Sshares = SGDowned * SGDa * 5
                BankT = BankT - Sshares
                rEset = 1
    print "================================================================================"
    print "Day", days
    print "The new stock value's are:","SGD:", SGD,"|","DAHJ:", DAHJ,"|","MFHG", MFHG
    if BankT == 0:
        print "================================================================================"
        print "Game over! All money was lost! Save will be reset!"
        with open('variables.py','w') as v:
            #Eracicate old file:
            v.seek(0)
            v.truncate()
        print "Warning! Game will now throw a 0 / 0 error. Please ignore this error and start program again."
        print 0 / 0
    #Secondary Save!
    S()    
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
     #No sale of stock if price == 0
    if SGD == 0:
        easygui.msgbox("Company went out of business! Unable to compleate transaction!")
    else:
        charge = SGD*shares
        if charge < BankT:
            BankT = BankT - charge
            SGDowned = SGDowned + shares
            if gamemode == "Impossable":
                BankT = BankT - 200
                print "Total shares of SGD is now:", SGDowned, "| Purchase fee was:", charge, "| An additional $200 commission fee was added to this sale!", "| Remaining Bank Balance:", BankT
            else:
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
        if gamemode == "Impossable":
                BankT = BankT - 200
                print "Total shares of DAHJ is now:", DAHJowned, "| Purchase fee was:", charge, "| An additional $200 commission fee was added to this sale!", "| Remaining Bank Balance:", BankT
        else:
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
        if gamemode == "Impossable":
                BankT = BankT - 200
                print "Total shares of MFHG is now:", MFHGowned, "| Purchase fee was:", charge, "| An additional $200 commission fee was added to this sale!", "| Remaining Bank Balance:", BankT
        else:
            print "Total shares of MFHG is now:", MFHGowned, "| Purchase fee was:", charge, "| Remaining Bank Balance:", BankT
    else:
        print "Error occured purchasing stocks. The most likely cause is: Insuffiecent funds."
#SGD sell function
def sellSGD(shares):
    global SGD
    global BankT
    global SGDowned
    soldC = SGD*shares
    if shares <= SGDowned:
        SGDowned = SGDowned - shares
        BankT = BankT + soldC
        if gamemode == "Impossable":
                BankT = BankT - 200
                print "Total shares of MFHG is now:", SGDowned, "| You earned:", soldC, "| An additional $200 commission fee was added to this sale!", "| Remaining Bank Balance:", BankT
        else:
            print "Total shares of SGD is now:", SGDowned, "| You earned", soldC, "| New Bank Balance:", BankT
    else:
        print "Error occured selling stocks. The most likely cause was: Insuffiecent amount of stocks."
#DAHJ sell function
def sellDAHJ(shares):
    global DAHJ
    global BankT
    global DAHJowned
    soldC = DAHJ*shares
    if shares <= DAHJowned:
        DAHJowned = DAHJowned - shares
        BankT = BankT + soldC
        if gamemode == "Impossable":
                BankT = BankT - 200
                print "Total shares of DAHJ is now:", DAHJowned, "| You earned:", soldC, "| An additional $200 commission fee was added to this sale!", "| Remaining Bank Balance:", BankT
        else:
            print "Total shares of DAHJ is now:", DAHJowned, "| You earned", soldC, "| New Bank Balance:", BankT
    else:
        print "Error occured selling stocks. The most likely cause was: Insuffiecent amount of stocks."
#MFHG sell function
def sellMFHG(shares):
    global MFHG
    global BankT
    global MFHGowned
    soldC = MFHG*shares
    if shares <= MFHGowned:
        MFHGowned = MFHGowned - shares
        BankT = BankT + soldC
        if gamemode == "Impossable":
                BankT = BankT - 200
                print "Total shares of MFHG is now:", MFHGowned, "| You earned:", soldC, "| An additional $200 commission fee was added to this sale!", "| Remaining Bank Balance:", BankT
        else:
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
    print "================================================================================"
    print "Miscellaneous stocks:"
    print "These stocks cannot be purchased/sold like regular stocks! They can only be obtained through a ten day bonus!"
    print "Currently the below stocks serve as placeholders and are not yet obtainable!"
    print "Gold:", gold
    print "Silver:", silver
    print "Platinum:", platinum
    print "Unobtainum:", unobtainium
    print "Oil:", oil
#***************************
#BankBalance
#***************************
def BankBalance():
    global SGD
    global DAHJ
    global MFHG
    global BankT
    global DAHJowned
    global MFHGowned
    global SGDowned
    if type(BankT) is tuple:
        BankT = BankT[0]
    SGDn = SGD*SGDowned
    DAHJn = DAHJ*DAHJowned
    MFHGn = MFHG*MFHGowned
    net = int(SGDn) + int(DAHJn) + int(MFHGn) + int(BankT) - int(LoanAmount)
    net2 = int(SGDn) + int(DAHJn) + int(MFHGn)
    print "Current Balance is:", BankT
    print "Currect loan amount is:", LoanAmount
    print "Current Networth is:", net
    print "Current Stock Total:", net2
def Save():
    #f = open('{0}.py'.format(savegame), 'wb')
    with open(savegame, 'w') as v:
        #Eracicate old file:
        v.seek(0)
        v.truncate()
        #Save variables as string
        savegames = "savegame = " + "'" + str(savegame) + "'"
        global LoanAmount
        global HasLoan
        global DaysToPayLoan
        LoanAmounts = "LoanAmount = " + str(LoanAmount)
        HasLoans = "HasLoan = " + str(HasLoan)
        DaysToPayLoans = "DaysToPayLoan = " + str(DaysToPayLoan)
        global gold
        global silver
        global platinum
        global unobtainium
        global oil
        golds = "gold = " + str(gold)
        silvers = "silver = " + str(silver)
        platinums = "platinum = " + str(platinum)
        unobtainiums = "unobtainium = " + str(unobtainium)
        oils = "oil = " + str(oil)
        global gamemode
        global rEseta
        global rEsetb
        global rEsetc
        global rEsetd
        global rEsete
        global rEsetf
        rEsetsa = "rEseta = " + str(rEseta)
        rEsetsb = "rEsetb = " + str(rEsetb)
        rEsetsc = "rEsetc = " + str(rEsetc)
        rEsetsd = "rEsetd = " + str(rEsetd)
        rEsetse = "rEsete = " + str(rEsete)
        rEsetsf = "rEsetf = " + str(rEsetf)
        gameisresets = "gameisreset = " + str(gameisreset) 
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
        gamemodes = "gamemode = " + str('"') + str(gamemode) + str('"')
        #Save stringed variables
        v.write(savegames)
        v.write('\n')
        v.write(gameisresets)
        v.write('\n')
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
        v.write('\n')
        v.write(gamemodes)
        v.write('\n')
        v.write(rEsetsa)
        v.write('\n')
        v.write(rEsetsb)
        v.write('\n')
        v.write(rEsetsc)
        v.write('\n')
        v.write(rEsetsd)
        v.write('\n')
        v.write(rEsetse)
        v.write('\n')
        v.write(rEsetsf)
        v.write('\n')
        v.write(golds)
        v.write('\n')
        v.write(silvers)
        v.write('\n')
        v.write(platinums)
        v.write('\n')
        v.write(unobtainiums)
        v.write('\n')
        v.write(oils)
        v.write('\n')
        v.write(HasLoans)
        v.write('\n')
        v.write(DaysToPayLoans)
        v.write('\n')
        v.write(LoanAmounts)
"""
        global rapidsave
        SGD1 = SGD
        rapidsave = rapidsave + 1
        if rapidsave == 9:
            rapidsave = 0
            choice = easygui.enterbox("You have entered the cheat code interface! Enter your code below!")
            if choice == "SGD Boost":
                global SGD
                SGD1 = int(easygui.enterbox("Enter the new value for SGD:"))
                SGD = SGD1
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
#Save
def S():
    Save()
print "Game start"
print " "
print "================================================================================"
print "Day", days 
intro = "SGD:", SGD,"|","DAHJ:", DAHJ,"|","MFHG:", MFHG
easygui.msgbox("Welcome to Stock Simulator! In a moment, you will be presented with the day's stock prices. After that, you will get various options which will allow you to buy, sell, view, or otherwise interact with various aspects of this game. You will start the game with 10,000 dollars to invest in stocks.", "Welcome!")
easygui.msgbox("Warning! Hitting [OK] prematurely, such as, before entering values, for  can cause errors which will end the program and may make you lose your progress!","Warning!")
easygui.msgbox(intro, "Today's stock value's are:")
S()
#Main Loop of program
while 1 == 1:              
    choice1 = easygui.buttonbox("What would you like to do?",
                                choices = ["Purchase stocks","Sell stocks","Advance","View Info","Save","Loan Options","Exit"])
    #Purchase Stocks
    if choice1 == "Purchase stocks":
        choice2 = easygui.buttonbox("Which stock would you like to purchase?",
                                    choices = ["SGD", "DAHJ", "MFHG", "Back to main screen"])
        if choice2 == "SGD":
            if SGD == 0:
                easygui.msgbox("Company went out of business! Unable to compleate transaction!")
            else:
                choice3 = easygui.enterbox("How many shares of SGD would you like to purchase?")
                charge = SGD*abs(int(choice3))
                if charge < BankT:
                    PS(abs(int(choice3)))
                    easygui.msgbox("Purchase Successful!", "Purchase Successful!")
                else:
                    easygui.msgbox("Unable to purchase stocks. The most likely cause is insufficent funds.", "Error!")
        if choice2 == "DAHJ":
            if DAHJ == 0:
                easygui.msgbox("Company went out of business! Unable to compleate transaction!")
            else:
                choice3 = easygui.enterbox("How many shares of DAHJ would you like to purchase?")
                charge = DAHJ*abs(int(choice3))
                if charge < BankT:
                    PD(abs((int(choice3))))
                    easygui.msgbox("Purchase Successful!", "Purchase Successful!")
                else:
                    easygui.msgbox("Unable to purchase stocks. The most likely cause is insufficent funds.", "Error!")
        if choice2 == "MFHG":
            if MFHG == 0:
                easygui.msgbox("Company went out of business! Unable to compleate transaction!")
            else:
                choice3 = easygui.enterbox("How many shares of MFHG would you like to purchase?")
                charge = MFHG*abs((int(choice3)))
                if charge < BankT:
                    PM(abs(int(choice3)))
                    easygui.msgbox("Purchase Successful!", "Purchase Successful!")
                else:
                    easygui.msgbox("Unable to purchase stocks. The most likely cause is insufficent funds.", "Error!")
    #Sell stocks
    if choice1 == "Sell stocks":
        choice2 = easygui.buttonbox("Which stock would you like to Sell?",
                                    choices = ["SGD", "DAHJ", "MFHG", "Back to main screen"])
        if choice2 == "SGD":
            choice3 = easygui.enterbox("How many shares of SGD would you like to sell?")
            if abs(int(choice3)) <= SGDowned:
                SS(abs(int(choice3)))
                easygui.msgbox("Sale Successful!", "Sale Successful!")
            else:
                easygui.msgbox("Unable to sell stocks. The most likely cause is insufficent shares.", "Error!")
        if choice2 == "DAHJ":
            choice3 = easygui.enterbox("How many shares of DAHJ would you like to sell?")
            if abs(int(choice3)) <= DAHJowned:
                SD(abs(int(choice3)))
                easygui.msgbox("Sale Successful!", "Sale Successful!")
            else:
                easygui.msgbox("Unable to sell stocks. The most likely cause is insufficent shares.", "Error!")
        if choice2 == "MFHG":
            choice3 = easygui.enterbox("How many shares of MFHG would you like to sell?")
            if abs(int(choice3)) <= MFHGowned:
                SM(abs(int(choice3)))
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
                                    choices = ["Stocks", "Bank balance", "Controls", "Back to main screen"])
        if choice2 == "Stocks":
            DS()
            easygui.msgbox("Stock information will now be displayed. In 10 seconds, the main window will reopen. (This window need to be closed in order for countdown to begin)", "Stock Information")
            sleep(10)
        if choice2 == "Bank balance":
            easygui.msgbox("Bank information will now be displayed. In 10 seconds, the main window will reopen.", "Bank Information")
            BB()
            sleep(10)
        if choice2 == "Controls":
            easygui.msgbox("Controls\n \nThis game has four main controls: Purchasing, Selling, Advancing, and displaying this list.\n \nPurchasing\n \nTo purchase a stock, select the [Purchase stock] button, select the stock you want to purchase and enter the number of stocks you want. Please note that entering an incorrect format, any besides numbers will crash the program. Additionally, enter only whole numbers; entering a number like 7.4 will only purchase 7 stocks. Also purchasing -13 shares of a stock will purchase the absolute value of that number of shares.\n \nSelling\n \nSelling stocks works in a similar manner, select [Sell stocks], select the stock you want to sell. Additionally, enter only whole numbers; entering a number like 7.4 will only purchase 7 stocks.\n \nAdvancing\n \nTo move forward one day, select [Advance]. The new stock prices will display. You cannot undo a advance.\n \nDisplay controls\n \nTo find out more information on vaious things, like stocks and your bank balance, click on those catagories. The window will close and information will be displayed. After 10 seconds, the window will reopen and you can continue purchasing and selling stocks. Additionally, clicking on controls will display this list.","Controls","Next")
            easygui.msgbox("There are currently 3 stocks available for purchasing. These stocks are:\n \nSGD\n \nDAHJ\n \nMFHG.\n \nMFHG and SGD are coded to have smaller variations in price whereas DAHJ will tend to have larger variations. This won't always be true, but it is typically present.","Stocks","Next")
            easygui.msgbox("You can find a more in-depth discription of what the program is doing in the IDLE shell.","Behind the scenes","Next")
            easygui.msgbox("10 day bonus\n \nThe 10 day bonus is a randomly selected prize which are acquired every 10 in-game days. 10 day bonus have good rewards, but can also cause monotary downfalls. If a 10 day bonus goes in your favor, you will win amazing rewards, but if it doesn't, the consequences can be dire!. The better the reward the greater the risk!","10 day bonus","Next")
            easygui.msgbox("This game has saving functionality. You can save in multiple ways. First, on the main screen, you can select [save] to write all variables to the [ variables.py ]. second, you can select [Save and exit] to write all variables to [ variables.py ]. And third, you can advance, which saves by default.","Saving")
    #Save
    if choice1 == "Save":
        choice2 = easygui.buttonbox("How would you like to save?",
                    choices = ['Write to file','Copy Save','Clear Save'])
        if choice2 == "Write to file":
            S()
            easygui.msgbox("Saved game to [ " + str(savegame) + " ] ")
        if choice2 == "Clear Save":
             with open('variables.py','w') as v:
                    #Eracicate old file:
                    v.seek(0)
                    v.truncate()
        if choice2 == "Copy Save":
            choice3 = easygui.enterbox("What would you like the new save file to be called?")
            with open(savegame,"r") as s:
                new = s.read()
            choice3 = str(choice3) + ".py"
            with open(choice3,"w") as c:
                c.write(new)
            easygui.msgbox("New file created as " + str(choice3))
    #Loan Options
    if choice1 == "Loan Options":
        choice2 = easygui.buttonbox("What would you like to do?",
                                    choices = ["Take out loan","Pay back loan"])
        if choice2 == "Take out loan":
            if HasLoan == 1:
                easygui.msgbox("You already owe " + str(LoanAmount) + " dollars!")
            if HasLoan == 0:
                choice3 = easygui.enterbox("How much money would you like to take out of the bank?")
                BankT = BankT + int(choice3)
                LoanAmount = int(choice3) * 12
                LoanAmount = int(LoanAmount) / 10
                LoanAmount = int(LoanAmount)
                HasLoan = 1
                easygui.msgbox("You now owe " + str(LoanAmount) + " dollars!")
        if choice2 == "Pay back loan":
            if HasLoan == 0:
                easygui.msgbox("You do not currently have a loan!")
            if HasLoan == 1:
                Back = easygui.enterbox("How much money would you like to pay back? You currently owe " + str(LoanAmount) + " dollars!")
                LoanAmount = LoanAmount - int(Back)
                BankT = BankT - int(Back)
                if LoanAmount == 0:
                    DaysToPayLoan = 5
                    HasLoan = 0
                    LoanAmount = 0
                    easygui.msgbox("All debts settled!")
    #Exit
    if choice1 == "Exit":
        choice2 = easygui.buttonbox("How would you like to exit?",
                                    choices = ["Exit without saving", "Exit and save", "No exit"])
        if choice2 == "Exit without saving":
            choice3 = easygui.buttonbox("Are you sure you want to clear the save file and exit?\nThe save file will be cleared! This action cannot be undone!",
                                        choices = ["Yes","No"])
            if choice3 == "Yes":
                with open(savegame,'w') as v:
                    #Eracicate old file:
                    v.seek(0)
                    v.truncate()
                print "Game exited!"
                break
        if choice2 == "Exit and save":
            choice3 = easygui.buttonbox("Are you sure you want to save and exit?",
                                        choices = ["Yes","No"])
            if choice3 == "Yes":
                S()
                print "Game exited!"
                break
        if choice2 == "Clear Save":
            choice3 = easygui.buttonbox("Warning! Clearing the save cannot be undone!\nAre you sure you want to do this?",
                                        choices = ["Yes, clear the save file.", "No! Do not clear the save file!"])
            if choice3 == "Yes, clear the save file.":
                gameisreset = 1
                with open('variables.py','w') as v:
                    #Eracicate old file:
                    v.seek(0)
                    v.truncate()
    #Now you can win if all stocks are 0
    if SGD == 0:
        if MFHG == 0:
            if DAHJ == 0:
                easygui.msgbox("Congratulations! You have finished the game with a bank balance of $" + str(BankT) + "! This is a change of " + str(BankT/10000 - 100) + "%! Or a profit of " + str((10000-BankT) * -1))
                print "Program ended! Restart program if you wish."
                break 
