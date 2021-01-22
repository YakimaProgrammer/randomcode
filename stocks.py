import random, sys, pickle, os, easygui
print "Welcome to Python Stock Game 2!"
BankT = 10000
##BankT_init = BankT
stock_split_limit = 220 #Dictates at what value stocks split
##This sets information about the commission to charge.
##There are two commission types, "fee" and "percent"
##The commission amount is the percent or flat rate fee to charge for every stock transaction.
##Commission does not apply to stock advise! 
commision_type = "fee"
commision_amount = 10

#c, short for currancy, returns an number with 2 decimal places.
def c(number):
    number = float(number)
    number += 0.005
    number = "%.2f" %number
    return float(number)

##Setting the stock class. This handles everything about stocks.
class stock:
    def __init__(self, minvalue, maxvalue, name, daily_change, dividend_amount =
                 [0.02,0.02,0.01,0.01,0.01,0.02,0.04,0.02,0.05,0.005,0.005,0.005,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
                 dividend_delay = [8,18], dividend_cycle = 21): #daily_change is a list with two values
        self.value = random.randint(minvalue*100, maxvalue*100)
        self.value = c(c(self.value)/100)
        self.shares_owned = 0
        self.name = name
        self.change = daily_change
        self.past_prices = []
        self.past_prices.append(self.value)
        self.dividend_amount = random.choice(dividend_amount)
##        self.dividend_delay = -random.randint(dividend_delay[0], dividend_delay[1])
        self.counter = random.randint(dividend_delay[0], dividend_delay[1])
        self.dividend_cycle = dividend_cycle
    def get_current_value(self):
        return self.value
    def get_past_prices(self):
        return self.past_prices
    def get_shares_owned(self):
        return self.shares_owned
    def get_name(self):
        return self.name
    def sell(self, amount):
        global BankT, commision_type, commision_amount
        amount = int(abs(amount))
        cost = amount * self.value
        if commision_type == "fee":
            BankT -= commision_amount
        else:
            BankT -= cost * commision_amount
        if amount > self.shares_owned:
            return "E"
        else:
            BankT = BankT + cost
            self.shares_owned = int(self.shares_owned) - int(amount)
            return self.shares_owned, cost
    def buy(self, amount):
        global BankT, commision_type, commision_amount
        amount = int(abs(amount))
        cost = amount * self.value
        if commision_type == "fee":
            BankT -= commision_amount
        else:
            BankT -= cost * commision_amount
        if BankT - cost > 0:        
            BankT = BankT - cost
            self.shares_owned = int(self.shares_owned) + int(amount)
            return self.shares_owned, cost
        else:
            return "E"
    def add_stocks(self, amount):
        amount = int(amount)
        self.shares_owned += amount
        if self.shares_owned <= 0:
            self.shares_owned = 0
    def dividend(self):
        self.counter += 1
        if self.counter >= self.dividend_cycle:
            self.counter = 0
            global BankT
            BankT += self.dividend_amount * self.shares_owned * self.value
            if self.shares_owned >= 1:
                easygui.msgbox(str(self.name) + " just paid a dividend of " + str(self.dividend_amount * self.shares_owned * self.value) + " dollars!", "Dividend payment!")
    def get_next_dividend(self):
        return self.dividend_cycle - self.counter
    def get_dividend_amount(self):
        return self.dividend_amount
    def advance(self):
        global stock_split_limit
        self.past_prices.append(self.get_current_value())
        new = random.randint(self.change[0]*100,self.change[1]*100)
        new = c(new)
        new = new/100
        new = c(new)
        self.value += new
        if self.value > stock_split_limit:
            newvalue = random.randint(20,30)
            self.value = self.value / newvalue
            self.shares_owned = self.shares_owned * newvalue
            self.value = c(self.value)
            print str(self.name) + " has split! The new value is " + str(self.value) + " dollars. You now own " + str(self.shares_owned) + " shares!"
            easygui.msgbox(str(self.name) + " has split! The new value is " + str(self.value) + " dollars. You now own " + str(self.shares_owned) + " shares!","A stock has split!")
        self.dividend()

##    def restore(self, SH,V,N,C,PP):
##        self.shares_owned = SH
##        self.value = V
##        self.name = N
##        self.change = C
##        self.past_prices = PP
    def get_peak(self):
        return max(self.past_prices)
    def get_recent_average(self, days = 3):
        if len(self.past_prices) >= 3:
            average = 0
            av_list = []
            av_list = self.past_prices[::-1]
            av_list = av_list[0:days]
            for i in av_list:
                average += i
            average = average / days
            return average
        else:
            average = 0
            av_list = []
            av_list = self.past_prices[::-1]
            list_len = len(self.past_prices)
            av_list = av_list[0:list_len]
            for i in av_list:
                average += i
            average = average / list_len
            return c(average)
    def get_recommendations(self):
        global day_count, BankT
        ra = self.get_recent_average()
        a = self.get_average()
        MSG = "Advise for " + str(self.name) + ".\n\n"
        MSG = MSG + "The stock peaked at "+ str(c(self.get_peak())) + " dollars.\n\n"
        if ra > a:
            MSG = MSG + "Because " + str(self.name) + " is recently above the typical average, now could be a good time to sell.\n\n"
        else:
            MSG = MSG + "Because " + str(self.name) + " is recently below the typical average, now could be a good time to buy.\n\n"
        if self.value > 180:
            MSG = MSG + "Additionally, " + str(self.name) + " is currently near a price when shares start to split. Despite the high price, an investment may be profitable. Be wary, stocks in this stage are prone to crashing.\n\n"
        if day_count <= 3 and self.value <= 20:
            MSG = MSG + "Also to consider, because of the low price and early nature of the stock, an investment may be wise.\n\n"
        if self.value - ra > 0:
            MSG = MSG + "Further more, the stock is currently " + str(c(self.value - ra)) + " dollars above the recent average. This may be a good time to look at a short-term sell off for a profit.\n\n"
        else:    
            MSG = MSG + "Further more, the stock is currently " + str(c(self.value - ra)) + " dollars below the recent average. This may be a good time to look at a short-term investment for a profit.\n\n"
        if self.value - a > 0:
            MSG = MSG + "More over, the stock is currently " + str(c(self.value - a)) + " dollars above the average price. This suggests that a more long term departure from the stock may advisable. It may be beneficial to sell more shares in this stock.\n\n"
        else:
            MSG = MSG + "More over, the stock is currently " + str(c(self.value - a)) + " dollars below the average price. This suggests that a more long term investment in the stock may advisable. It may be beneficial to buy more shares in this stock.\n\n"
        MSG += "Another thing to consider is the stock's dividend of " + str(abs(float(self.dividend_amount)*100)) + " percent. The stock is currently " + str(self.get_next_dividend()) + " days away from paying a dividend.\n\n"
        max_shares = BankT/self.value
        max_shares = int(max_shares)
        max_shares -= 1
        MSG = MSG + "If you choose to completely invest in this stock, you could buy " + str(max_shares) + " shares. The estimated short-term return of this investment (excluding dividends) is " + str(c(max_shares*ra)) + " dollars. This is an estimated profit of " +str(c(abs(BankT-(max_shares*ra))))+" dollars. The estimated long-term return of this investment (excluding dividends) is " + str(c(abs(max_shares*a))) + " dollars. This is an estimated profit of " + str(BankT-(max_shares*a))+" dollars.\n\n"
        MSG = MSG + "If you choose to sell the " + str(self.shares_owned) + " shares you own in this stock, the total revenue would be " + str(c(self.shares_owned * self.value)) + " dollars.\n\n"
        MSG = MSG + "You currently have " + str(self.shares_owned) + " shares of this stock.\n\n"
        return MSG                    
    def get_average(self):
        average = 0
        for i in self.past_prices:
            average += i
        average = average / len(self.past_prices)
        return c(average)
##    def save(self):
##        return self.shares_owned, self.value, self.name, self.change, self.past_prices
class tendaybonus:
  def __init__(self, MSG, BankT_change, StockChange, risk, BankT_change_neg, StockChange_neg):
    #BankT_change shows the +/- change
    #StockChange shows what stocks are affected
    #Risk is the chance out of 100 that the bonus will go in your favor, greater is better
    self.BankT_Change = BankT_change
    self.StockChange = StockChange
    self.risk = risk
    self.BankT_change_neg = BankT_change_neg
    self.StockChange_neg = StockChange_neg
    self.MSG = MSG
##  def get_message(self):
##      return self.MSG
  def claim(self):
    global stocklist_init, BankT, stocklist
    num = random.randint(0, 100)
    YN = easygui.buttonbox(self.MSG,"Ten Day Bonus", choices = ["Claim", "Pass"])
    if YN == "Claim":
        if num <= self.risk:
          for i in self.StockChange:
            name = i[0]
            if name in stocklist:
                for y in stocklist_init:
                  if y.get_name() == name:
                    y.add_stocks(i[1])
          BankT = BankT + self.BankT_Change
          easygui.msgbox("You won the ten day bonus!","Ten day bonus won!")            
        else:
          for i in self.StockChange_neg:
            name = i[0]
            if name in stocklist:
                for y in stocklist_init:
                  if y.get_name() == name:
                    y.add_stocks(i[1])
          BankT = BankT + self.BankT_change_neg
          easygui.msgbox("You lost the ten day bonus!","Ten day bonus lost!")            
##Ten Day Bonus, claiming
def choose_tendaybonus(options):
    y = random.choice(options)
    y.claim()
##tendaybonuslist = []
##tendaybonus_counter = 0
##MSG = "Ten day bonus aquired!\n You have a 10% chance at receiving 2 times your current bank total, 50 shares of SGD and 90 shares of MFHG. If you lose, 500 dollars of your money will be lost, along with 50 shares of SGD."
##ten = tendaybonus(MSG, BankT*2, [["SGD",50],["MFHG",90]], 10, -500, [["SGD",-50]])
##tendaybonuslist.append(ten)
##MSG = "Ten day bonus aquired!\n You have a 80% change at receiving 1500 dollars, 5 shares of oil, 5 shares of gold, 10 shares of silver and 80 shares of SGD. If you lose, 3000 dollars will be subtracted from your bank account."
##ten = tendaybonus(MSG, 1500, [["Oil",5],["Gold Co",5],["Silver Co",10],["SGD",80]], 80, -3000, [])
##tendaybonuslist.append(ten)
##MSG = "Ten day bonus aquired!\n You won 10 shares of SGD and 2 shares of gold!"
##ten = tendaybonus(MSG,0,[["SGD",10],["Gold Co",2]], 100, 0, [])
##tendaybonuslist.append(ten)
##MSG = "Ten day bonus aquired!\n You can accept and gain 57 shares of SGD, plus an additional 5,000 dallors, but have a fifty-fifty chace of losing 99% of your bank total!"
##ten = tendaybonus(MSG,5000,[["SGD",57]],50,-BankT*0.99,[])
##tendaybonuslist.append(ten)
##MSG = "Ten day bonus aquired!\n You won 1500 dollars!"
##ten = tendaybonus(MSG,1500,[],100,0,[])
##tendaybonuslist.append(ten)
##Loans
class makeloan:
    def __init__(self, amount, rate = 1.1, days = 5, is_null = False):
        self.amount = abs(c(amount))
        self.rate = rate #10% increase
        self.has_loan = True
        if is_null:
            self.has_loan = False
        self.time_to_pay_loan = abs(int(days))
        self.null = is_null
    def check_for_loan(self):
        return self.has_loan
    def payback(self, amount):
        amount = abs(c(amount))
        global BankT
        BankT -= amount
        self.amount -= amount
        if self.amount >= 0:
            self.has_loan = False
        if self.amount >= 0:
            self.null = True
            self.has_loan = False
            BankT += abs(self.amount)
    def get_current_value(self):
        return self.amount
    def get_days_left(self):
        return self.time_to_pay_loan
    def advance(self):
        if not self.null:
            if self.time_to_pay_loan <= 0:
                return "User Defaulted"
            if self.rate < 1:
                self.rate += 1
            self.amount = self.amount * self.rate
            self.time_to_pay_loan -= 1
            self.amount = c(self.amount)
            if self.amount <= 0:
                global BankT
                self.null = True
                self.has_loan = False
                BankT += abs(self.amount)
loan = makeloan(1,1.25,5,True)
##Setting the save feature
def save(filename):
    global day_count, stocklist, stocklist_init, BankT, tendaybonuslist, tendaybonus_counter, loan
    pickled = []
    pickled.append(day_count)
    pickled.append(stocklist)
    pickled.append(stocklist_init)
    pickled.append(BankT)
    pickled.append(tendaybonus_counter)
    pickled.append(tendaybonuslist)
    pickled.append(loan)
    pickle.dump(pickled, open(filename, "wb"))
##Load from savegame
def load(savegame):
    global stocklist, stocklist_init, BankT, day_count, tendaybonuslist, tendaybonus_counter, loan
    pickled = pickle.load(open(savegame, 'rb'))
    BankT = pickled[3]
    day_count = pickled[0]
    stocklist = pickled[1]
    stocklist_init = pickled[2]
    tendaybonus_counter = pickled[4]
    tendaybonuslist = pickled[5]
    loan = pickled[6]
#Setting the advance feature
##day_count = 2
##advance_cost = 500
def advance():
    global day_count, BankT, tendaybonuslist, tendaybonus_counter, loan
    BankT = c(BankT)
    if loan.check_for_loan():    
        if loan.advance() == "User Defaulted":
            easygui.msgbox("You failed to pay back your loan, with an outstanding debt of " + str(loan.get_current_value()) + " dollars", "Failed to pay off loan")
            return "Out of Money"
        easygui.msgbox("You currently have a loan!\nYou have " + str(loan.get_days_left()) + " days left to repay the loan, and a debt of " + str(loan.get_current_value()) + " dollars.", "You currently have a loan!")
    print "Day: " + str(day_count)
    day_count += 1
    tendaybonus_counter += 1
    if tendaybonus_counter == 10:
        tendaybonus_counter = 0
        choose_tendaybonus(tendaybonuslist)
    for i in stocklist_init:
        i.advance()
        ##Remove Bankrupt stocks
        if i.get_current_value() <= 0:
            stocklist_init.remove(i)
            stocklist.remove(i.get_name())
            print "The stock, " + str(i.get_name()) +", has gone bankrupt!"
            easygui.msgbox("The stock, " + str(i.get_name()) +", has gone bankrupt!","A stock has gone bankrupt!")
    ##Check if player won
    if stocklist == []:
        return "Game Over!"
    ##Check if player went bankrupt
    if BankT <= 0:
        return "Out of Money!"
    print ""
    A_MSG = ""
    for i in stocklist_init:
        A_MSG = A_MSG +"Name: " + str(i.get_name()) + "\nValue: " + str(i.get_current_value()) + "\nAverage value: " + str(i.get_average())+ "\n\n"
    print A_MSG
##View graph of stock values
def StockTime(SGDvalues, SGDa):
    try:
        pygame.init()
        size = day_count*7+3
        screen = pygame.display.set_mode([size,450])
        screen.fill([255,255,255])
        running = True
        Position = 6
        for i in range(len(SGDvalues)):
            Var1 = int(SGDvalues[i])
            Var1 = Var1 * 2
            Var1 = Var1 * -1
            Position = Position + 6
            pygame.draw.rect(screen, [255,0,0], [Position, 450, 5, Var1], 0)
        SGDa = SGDa * 2
        SGDa = 450-SGDa
        pygame.draw.rect(screen, [255,255,0], [0, SGDa, size, 0], 0)        
        pygame.display.flip()
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        pygame.quit()
    except:
        try:
            pygame.quit()
        except:
            pass
        easygui.msgbox("It appears an invalid number was included in this data set.")
##Integer enterbox
def intbox(msg,title):
    running1 = True
    while running1:
        choice3 = easygui.enterbox(msg,title)
        try:
            choice3 = int(choice3)
            running1 = False
        except:
            pass
    return choice3
#"Inside scoop" aka general hints for which stocks to watch.
def get_inside_scoop(stocklist_init):
    global BankT
    BankT += 500
    MSG = "The 500 dollars you paid for stock advise has been refunded. A new fee of 5000 dollars is required to proceed. Do you wish to do so?"
    choice = easygui.buttonbox(MSG, "Purchase inside scoop", choices = ["Yes","No"])
    if choice == "Yes":
        BankT -= 5000
        MSG = "-The inside scoop-\n"
        MSG += "At a glance:\n"
        MSG += "Sell: \n"
        for i in stocklist_init:
            if i.get_average() < i.get_recent_average():
                if i.get_shares_owned() > 0:
                    MSG += str(i.get_name()) + "\n"
        MSG += "\n\n"
        MSG += "Buy: \n"
        for i in stocklist_init:
            if i.get_average() > i.get_recent_average():
                MSG += str(i.get_name()) + "\n"
        MSG += "\n\n------------------------------\n"
        MSG += "Stocks to sell:\n\n"
        MSG += "At a glance:\n"
        for i in stocklist_init:
            if i.get_average() < i.get_recent_average():
                MSG += str(i.get_name()) + "\n"
        MSG += "\nMore in-dept:\n\n"
        for i in stocklist_init:
            if i.get_average() < i.get_recent_average():
                MSG = MSG + str(i.get_name()) + "\nCurrent Value: " + str(i.get_current_value()) + "\nAverage: " + str(i.get_average()) + "\nRecent Average: " + str(i.get_recent_average()) + "\nCurrent Value: " + str(i.get_current_value()) + "\n"
                MSG += "Shares owned: " + str(i.get_shares_owned()) + "\n"
                MSG += "Total revenue if all shares sold: " + str(i.get_current_value()*i.get_shares_owned()) + " dollars.\n\n"
        MSG += "Stocks to buy: \n\nAt a glance:\n\n"
        for i in stocklist_init:
            if i.get_average() > i.get_recent_average():
                MSG += str(i.get_name()) + "\n"
        MSG += "\nMore in-dept:\n\n"
        for i in stocklist_init:
            if i.get_average() > i.get_recent_average():
                a = i.get_average()
                ra = i.get_recent_average()
                max_shares = BankT/i.get_current_value()
                MSG = MSG + str(i.get_name()) + "\nCurrent Value: " + str(i.get_current_value()) + "\nAverage: " + str(i.get_average()) + "\nRecent Average: " + str(i.get_recent_average()) + "\nCurrent Value: " + str(i.get_current_value()) + "\n"
                MSG += "Shares owned: " + str(i.get_shares_owned()) + "\n"
                MSG += "Maximum shares that could be bought: " + str(max_shares) + " shares.\n"
                MSG += "Short term estimated revenue: " + str(max_shares * ra) + " dollars.\n"
                MSG += "Long term estimated revenue: " + str(max_shares * a) + " dollars.\n\n"
        easygui.codebox("The inside scoop","The inside scoop",MSG)                                                                                                                                                                                                                                                                                                                                                       
    else:
        pass
##Add more stocks to the stock list to add more stocks. They still need to be initalized!
##stocklist = []
##stocklist_init = []
def init_game():
    global stocklist, stocklist_init, day_count, BankT, BankT_init, tendaybonus_counter, loan
    loan = makeloan(1,1.25,5,True)
##    tendaybonus_counter = -1
##    BankT = 10000
##    BankT_init = BankT
##    stocklist_init = []
##    stock1 = stock(1,50, "SGD", [-3, 4])
##    stocklist_init.append(stock1)
##    stock1 = stock(1,30, "MFHG", [-6, 8])
##    stocklist_init.append(stock1)
##    stock1 = stock(20,105, "DAHJ", [-9, 11])
##    stocklist_init.append(stock1)
##    stock1 = stock(10,50, "Gold Co", [-15, 25])
##    stocklist_init.append(stock1)
##    stock1 = stock(1,15, "Silver Co", [-10, 12])
##    stocklist_init.append(stock1)
##    stock1 = stock(30,200, "Platinum Co", [-100, 110])
##    stocklist_init.append(stock1)
##    stock1 = stock(800,3000, "Oil Co", [-300, 350])
##    stocklist_init.append(stock1)
##    stock1 = stock(1,50, "SDB", [-9, 13])
##    stocklist_init.append(stock1)
##    stock1 = stock(5,50, "JRA", [-16, 18])
##    stocklist_init.append(stock1)
##    stock1 = stock(1,50, "KEJ", [-10, 11])
##    stocklist_init.append(stock1)
##    stock1 = stock(1,50, "EHDA", [-15, 13])
##    stocklist_init.append(stock1)
##    stock1 = stock(1,50, "Lumber Co", [-30, 25])
##    stocklist_init.append(stock1)
##    stocklist = []
##    for i in stocklist_init:
##        stocklist.append(i.get_name())
##    ##Set day count
##    day_count = 0
##    ##Set BankT
##    BankT = 10000
    stocklist = []
    stocklist_init = []
    BankT = 10000
    BankT_init = BankT
    tendaybonus_counter = 0
    day_count = 2
init_game()
class gamemode:
    def get_name(self):
        return self.name
    def get_msg(self):
        return self.msg
##    def __init__():
    def preset(self, name, msg, BankT, commission_type, commission_amount, stocklist_init,tendaybonuslist):
        self.name = name
        self.msg = msg
        self.BankT = BankT
        self.commission_type = commission_type
        self.commission_amount = commission_amount
        self.stocklist_init = stocklist_init
        self.stocklist = []
        for i in stocklist_init:
            self.stocklist.append(i.get_name())
        self.tendaybonuslist = tendaybonuslist
    def user_defined(self):
        self.name = easygui.enterbox("What should the gamemode be called?","Name gamemode")
        self.msg = easygui.codebox("What should the gamemode's discription be?","Gamemode discription")
        self.BankT = intbox("How much money should the user start the game with?","Start amount of money")
        self.commission = easygui.buttonbox("What type of commission should be used in this gamemode?","Type of commission?", ["Percent","Flat Rate","No Commission"])
        if self.commission == "Percent":
            self.commission_amount = intbox("What percent commission would you like to charge on every stock transaction?\nEnter a number like 0.1 to represent 10% commission.","What percent commission should be used?")
            self.commission_type = "percent"
        if self.commission == "Flat Rate":
            self.commission_amount = intbox("What amount of commission should be charged for every stock transaction?","Set commission charge")
            self.commission_type = "fee"
        if self.commission == "No Commission":
            self.commission_amount = 0
            self.commission_type = "fee"
        choice1 = easygui.buttonbox("Do you want to reusing exisiting stocks, or do you want to create your own?","Create or use stocks",["Create Stocks","Reuse Stocks"])
        if choice1 == "Reuse Stocks":
            global stocklist, stocklist_init
            choice2 = easygui.multchoicebox("Which stocks should be used?","Reuse stocks", stocklist)
            self.stocklist = choice2
            stocklist_init_2 = []
            for i in stocklist_init:
                for y in self.stocklist:
                    if i.get_name() == y:
                        stocklist_init_2.append(i)
            self.stocklist_init = stocklist_init_2
        if choice1 == "Create Stocks":
            self.stocklist = []
            self.stocklist_init = []
            name = easygui.enterbox("What is the new stock's name?","Stock Name")
            min_value = intbox("What is the lower limit for the stock's inital value?","Stock lower value")
            max_value = intbox("What is the upper limit for the stock's inital value?","Stock upper value")
            d_down_value = intbox("What is the max amount the stock can go down in a single day?","Max downward change")
            d_down_value = -abs(d_down_value)
            d_up_value = intbox("What is the max amount the stock can go up in a single day?","Max upward change")
            d_up_value = abs(d_up_value)
            stock1 = stock(min_value,max_value,name,[d_down_value,d_up_value])
            self.stocklist_init.append(stock1)
            running_c = True
            while running_c:
                choice1 = easygui.buttonbox("Do you want to create a stock or quit?","Create or quit?",["Create","Quit"])
                if choice1 == "Create":
                    name = easygui.enterbox("What is the new stock's name?","Stock Name")
                    min_value = intbox("What is the lower limit for the stock's inital value?","Stock lower value")
                    max_value = intbox("What is the upper limit for the stock's inital value?","Stock upper value")
                    d_down_value = intbox("What is the max amount the stock can go down in a single day?","Max downward change")
                    d_down_value = -abs(d_down_value)
                    d_up_value = intbox("What is the max amount the stock can go up in a single day?","Max upward change")
                    d_up_value = -abs(d_down_value)
                    stock1 = stock(min_value,max_value,name,[d_down_value,d_up_value])
                    self.stocklist_init.append(stock1)
                else:
                    running_c = False
            for i in self.stocklist_init:
                self.stocklist.append(i.get_name())
        ##Add creation of 10 day bonuses reusing the stocks defined up above.
        self.tendaybonuslist = []
        msg = easygui.codebox("What should the 10 day bonus show?\nMoreover, outline the risk/reward factors of the prize, prize if won, drawbacks if lost.","Set Message")
        risk = intbox("What percent chance out of 100 will the 10 day bonus go in the user's favor?\nEnter a number like 50.","Risk factor")
        win_money = intbox("How much money should the user win if the 10 day bonus goes in the user's favor?","Prize money")
        win_stocks = easygui.multchoicebox("What stocks should the user win if the 10 day bonus goes in their favor?","Prize stocks", self.stocklist)
        win_stock_final = []
        for i in win_stocks:
            amount = intbox("How many shares should the user recieve of " + str(i) + " if the ten day bonus is won?","Prize Shares")
            win_stock_final.append([["'"+str(i)+"'"],amount])
        lose_money = intbox("How much money should the user lose if the 10 day bonus is lost?\nEnter a negative number to subtract money.","Money to subtract if 10 day bonus is lost")
        lose_stocks = easygui.multchoicebox("What stocks should the user lose if the 10 day bonus goes against their favor?","10 day bonus lost stocks", self.stocklist)
        lose_stock_final = []
        for i in lose_stocks:
            amount = intbox("How many shares should the user lose of " + str(i) + " if the ten day bonus is lost?\nEnter a negative number to subtract shares.","Prize Lost Shares")
            lose_stock_final.append([["'"+str(i)+"'"],amount])
        ten = tendaybonus(msg,win_money,win_stock_final,risk,lose_money,lose_stock_final)
        self.tendaybonuslist.append(ten)
        running_b = True
        while running_b:
            choice1 = easygui.buttonbox("Do you want to create a 10 day bonus or quit?","Create or quit?",["Create","Quit"])
            if choice1 == "Quit":
                running_b = False
            else:
                msg = easygui.codebox("What should the 10 day bonus show?\nMoreover, outline the risk/reward factors of the prize, prize if won, drawbacks if lost.","Set Message")
                risk = intbox("What percent chance out of 100 will the 10 day bonus go in the user's favor?\nEnter a number like 50.","Risk factor")
                win_money = intbox("How much money should the user win if the 10 day bonus goes in the user's favor?","Prize money")
                win_stocks = easygui.multchoicebox("What stocks should the user win if the 10 day bonus goes in their favor?","Prize stocks", self.stocklist)
                win_stock_final = []
                for i in win_stocks:
                    amount = intbox("How many shares should the user recieve of " + str(i) + " if the ten day bonus is won?","Prize Shares")
                    win_stock_final.append([["'"+str(i)+"'"],amount])
                lose_money = intbox("How much money should the user lose if the 10 day bonus is lost?\nEnter a negative number to subtract money.","Money to subtract if 10 day bonus is lost")
                lose_stocks = easygui.multchoicebox("What stocks should the user lose if the 10 day bonus goes against their favor?","10 day bonus lost stocks", self.stocklist)
                lose_stock_final = []
                for i in lose_stocks:
                    amount = intbox("How many shares should the user lose of " + str(i) + " if the ten day bonus is lost?\nEnter a negative number to subtract shares.","Prize Lost Shares")
                    lose_stock_final.append([["'"+str(i)+"'"],amount])
                ten = tendaybonus(msg,win_money,win_stock_final,risk,lose_money,lose_stock_final)
                self.tendaybonuslist.append(ten)
        easygui.msgbox("The new gamemode, " + str(self.name) + ", was successfully created!","New gamemode created!")
    def set_gamemode(self):
        return self.name, self.msg, self.BankT, self.commission_type, self.commission_amount, self.stocklist, self.stocklist_init, self.tendaybonuslist
def bonus_generator(amount, stocklist, amount_S_per_bonus = [3,5], num_shares = [10,10,10,15,15,15,15,20,20,20,20,30,30,30,30,40,50,60,70,80,90,100],
                    money = [0,0,0,0,500,1000,1000,1000,1500,1500,1500,1500,1500,2000,2000,2000,2000,2000,2000,3000,3000,3000,3000,5000,5000,10000,10000,10000],
                    do_prize_only = False, risk_factor = [10,20,25,25,25,30,40,50,60,70,70,70,80,80,80,80,90,90,90]):
    global tendaybonus
    if not do_prize_only:
        tendaybonuslist = []
        for i in range(int(amount)):
            num_of_stocks = random.randint(amount_S_per_bonus[0],amount_S_per_bonus[1])
            stocks_to_win = []
            for i in range(num_of_stocks):
                new = random.choice(stocklist)        
                shares = random.choice(num_shares)
                stocks_to_win.append([new,int(shares)])
            num_of_stocks = random.randint(amount_S_per_bonus[0],amount_S_per_bonus[1])
            stocks_to_lose = []
            for i in range(num_of_stocks):
                new = random.choice(stocklist)        
                shares = random.choice(num_shares)
                stocks_to_lose.append([new,int(shares)])
            money_to_win = random.choice(money)
            money_to_lose = random.choice(money)
            risk = random.choice(risk_factor)
            msg = "Ten day bonus acquired!\n\n"
            msg += "Chance of winning: " + str(100-int(risk)) + "%\n\n"
            msg += "Money to win: " + str(money_to_win) + " dollars.\n\n"
            msg += "Stocks to win: "
            for i in stocks_to_win:
                msg += str(i[0]) + ": " + str(i[1]) + " shares | "
            msg += "\n\nMoney to lose: " + str(money_to_lose) + " dollars.\n\n"
            msg += "Stocks to lose: "
            for i in stocks_to_lose:
                msg += str(i[0]) + ": " + str(i[1]) + " shares | "
            for i in stocks_to_lose:
                i[1] = -abs(i[1])
            ten = tendaybonus(str(msg),int(money_to_win),list(stocks_to_win),int(risk),int(money_to_lose),list(stocks_to_lose))
            tendaybonuslist.append(ten)
        return tendaybonuslist
    else:
        tendaybonuslist = []
        for i in range(int(amount)):
            num_of_stocks = random.randint(amount_S_per_bonus[0],amount_S_per_bonus[1])
            stocks_to_win = []
            for i in range(num_of_stocks):
                new = random.choice(stocklist)        
                shares = random.choice(num_shares)
                stocks_to_win.append([new,int(shares)])
            money_to_win = random.choice(money)
            msg = "Ten day bonus acquired!\n\n"
            msg += "Money to win: " + str(money_to_win) + " dollars.\n\n"
            msg += "Stocks to win: "
            for i in stocks_to_win:
                msg += str(i[0]) + ": " + str(i[1]) + " shares | "
            ten = tendaybonus(str(msg),int(money_to_win),list(stocks_to_win),100,0,[[]])
            tendaybonuslist.append(ten)
        return tendaybonuslist
def generate_stocks(amount):
    global stock
    stocklist_init = []
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    names = []
    for i in range(int(amount)):
        running = True
        while running:
            min_value = random.randint(5,100)
            max_value = random.randint(10,120)
            dcd = -random.randint(3,11)
            dcu = random.randint(3,11)
            name = []
            for i in range(random.randint(3,4)):
                name.append(random.choice(letters))
            try:
                if name in names:
                    good = False
                else:
                    good = True
            except:
                good = True
            if max_value > min_value and abs(dcd) != dcd and good:
                running = False
        name_a = ""
        for i in name:
            name_a += i
        name_a = name_a.upper()
        stock1 = stock(int(min_value), int(max_value), str(name_a), [int(dcd),int(dcu)])
        stocklist_init.append(stock1)
        names.append(name_a)
    return stocklist_init
gamemode_file = os.path.isfile("Gamemodes.py_gamemodes")
if not gamemode_file:
    print "Generating preset gamemodes...\nA random generator is used to determine the names of some stocks and possible ten day bonuses. If you wish to reset the gamemodes, you can delete the Gamemodes.py_gamemodes file to regenerate the names and ten day bonuses. This will clear any custom gamemodes made.\nYou can also go to the updater client, under [More] and under [Settings], you can choose [Reset Python Stock Game 2 Gamemodes], which will automate this process.\nThe file generation can take a moment..."
    gamemodelist = []
    game = gamemode()
    msg = "The default difficulty of gameplay. This difficulty features 6 stocks, a handful of prize and risk ten day bonuses and a starting bank balance of 10,000 dollars. There is a $50 flat-rate commission on all stock transactions."
    stocklist_init = []
    stock1 = stock(1,50, "SGD", [-3, 4])
    stocklist_init.append(stock1)
    stock1 = stock(1,30, "MFHG", [-6, 8])
    stocklist_init.append(stock1)
    stock1 = stock(20,105, "DAHJ", [-9, 11])
    stocklist_init.append(stock1)
    stock1 = stock(10,50, "Gold Co", [-15, 25])
    stocklist_init.append(stock1)
    stock1 = stock(1,15, "Silver Co", [-10, 12])
    stocklist_init.append(stock1)
    stock1 = stock(30,200, "Platinum Co", [-100, 110])
    stocklist_init.append(stock1)
    tendaybonuslist = []
    stocklist = []
    for i in stocklist_init:
        stocklist.append(i.get_name())
    tendaybonuslist = []
    tendaybonuslist = bonus_generator(10,stocklist,[1,3],do_prize_only = True)
    tendaybonuslist.append(bonus_generator(10,stocklist))
    game.preset("Normal", msg, 10000, "fee", 50, stocklist_init, tendaybonuslist)
    gamemodelist.append(game)
##
    game = gamemode()
    msg = "A reduced level of difficulty, featuring only 1 stock and a handful of randomly generated ten day bonuses. The player starts with 30,000 dollars and no commission."
    stocklist_init = []
    stock1 = stock(20,50, "SGD", [-3, 4])
    stocklist_init.append(stock1)
    tendaybonuslist = []
    stocklist = []
    for i in stocklist_init:
        stocklist.append(i.get_name())
    tendaybonuslist = []
    tendaybonuslist = bonus_generator(10,stocklist,[0,1],do_prize_only = True)
    game.preset("Trainer", msg, 30000, "fee", 0, stocklist_init, tendaybonuslist)
    gamemodelist.append(game)
##
    game = gamemode()
    msg = "A simple gamemode geared towards beginners, featuring 3 stocks - SGD, DAHJ, and MFHG - and a handful of randomly generated prize-related 10 day bonuses. There is no commission in this gamemode. The player starts with 10,000 dollars."
    stocklist_init = []
    stock1 = stock(1,50, "SGD", [-3, 4])
    stocklist_init.append(stock1)
    stock1 = stock(1,30, "MFHG", [-6, 8])
    stocklist_init.append(stock1)
    stock1 = stock(20,105, "DAHJ", [-9, 11])
    stocklist_init.append(stock1)
    tendaybonuslist = []
    stocklist = []
    for i in stocklist_init:
        stocklist.append(i.get_name())
    tendaybonuslist = []
    tendaybonuslist = bonus_generator(10,stocklist,[1,3],do_prize_only = True)
    game.preset("Easy", msg, 10000, "fee", 0, stocklist_init, tendaybonuslist)
    gamemodelist.append(game)
##
    game = gamemode()
    msg = "This gamemode is more challenging, featuring more stocks and over 50 randomly generated 10 day bonuses. There is a 100 dollar commission fee on all stock transactions and the player starts the game with 8,000 dollars."
    stocklist_init = []
    stock1 = stock(1,50, "SGD", [-3, 4])
    stocklist_init.append(stock1)
    stock1 = stock(1,30, "MFHG", [-6, 8])
    stocklist_init.append(stock1)
    stock1 = stock(20,105, "DAHJ", [-9, 11])
    stocklist_init.append(stock1)
    stock1 = stock(10,50, "Gold Co", [-15, 25])
    stocklist_init.append(stock1)
    stock1 = stock(1,15, "Silver Co", [-10, 12])
    stocklist_init.append(stock1)
    stock1 = stock(30,200, "Platinum Co", [-100, 110])
    stocklist_init.append(stock1)
    stock1 = stock(800,3000, "Oil Co", [-300, 350])
    stocklist_init.append(stock1)
    stock1 = stock(1,50, "SDB", [-9, 13])
    stocklist_init.append(stock1)
    stock1 = stock(5,50, "JRA", [-16, 18])
    stocklist_init.append(stock1)
    stock1 = stock(1,50, "KEJ", [-10, 11])
    stocklist_init.append(stock1)
    stock1 = stock(1,50, "EHDA", [-15, 13])
    stocklist_init.append(stock1)
    stock1 = stock(1,50, "Lumber Co", [-30, 25])
    stocklist_init.append(stock1)
    stocklist = []
    for i in stocklist_init:
        stocklist.append(i.get_name())
    tendaybonuslist = []
    tendaybonuslist = bonus_generator(55,stocklist)
    game.preset("Hard", msg, 8000, "fee", 100, stocklist_init, tendaybonuslist)
    gamemodelist.append(game)
##
    game = gamemode()
    #Prohibit stock splitting?
    msg = "One of the more challenging gamemodes, the impossible gamemode gives the player only 5,000 dollars and a 5 percent commission on all stock transactions. There are over 200 randomly generated ten day bonuses. There are over 200 randomly generated stocks to invest in. Do you have what it takes?"
    stocklist_init = []
    stocklist_init = generate_stocks(205)
    stock1 = stock(1,50, "SGD", [-3, 4])
    stocklist_init.append(stock1)
    stock1 = stock(1,30, "MFHG", [-6, 8])
    stocklist_init.append(stock1)
    stock1 = stock(20,105, "DAHJ", [-9, 11])
    stocklist_init.append(stock1)
    stocklist = []
    for i in stocklist_init:
        stocklist.append(i.get_name())
    tendaybonuslist = []
    tendaybonuslist = bonus_generator(205,stocklist)
    game.preset("Impossible", msg, 5000, "percent", 0.05, stocklist_init, tendaybonuslist)
    gamemodelist.append(game)
##
    game = gamemode()
    #Prohibit stock splitting?
    msg = "This is by far one of the most challenging gamemodes, but don't be decieved by the 20,000 dollars starting money and 0.5% commission. There are over 10,000 randomly generated stocks to invest in and over 10,000 randomly generated possible ten day bonuses. Do you have what it takes? (Does your computer have what it takes?)"
    stocklist_init = []
    stocklist_init = generate_stocks(9997)
    stock1 = stock(1,50, "SGD", [-3, 4])
    stocklist_init.append(stock1)
    stock1 = stock(1,30, "MFHG", [-6, 8])
    stocklist_init.append(stock1)
    stock1 = stock(20,105, "DAHJ", [-9, 11])
    stocklist_init.append(stock1)
    stocklist = []
    for i in stocklist_init:
        stocklist.append(i.get_name())
    tendaybonuslist = []
    tendaybonuslist = bonus_generator(10005,stocklist,[3,8])
    game.preset("Legendary: 10,000  stock challenge", msg, 20000, "percent", 0.005, stocklist_init, tendaybonuslist)
    gamemodelist.append(game)
    with open("Gamemodes.py_gamemodes","w") as g:
        pass
        ##Creates gamemodes file.
##    with open("Gamemodes.py_gamemodes","rb+") as g:
    with open("Gamemodes.py_gamemodes","wb") as g:
        g.seek(0)
        g.truncate()
        pickle.dump(gamemodelist,g)
def choose_gamemode():
    global stocklist_init, stocklist, BankT, BankT_init, commision_type, commision_amount, tendaybonuslist
    gamemodelist = []
    with open("Gamemodes.py_gamemodes","rb") as f:
        gamemodelist = pickle.load(f)
    gamemodenames = []
    for i in gamemodelist:
        gamemodenames.append(i.get_name())
    running_choose_gamemode = True
    while running_choose_gamemode:
        choice = easygui.choicebox("Select a gamemode.","Choose Gamemode", gamemodenames)
        for i in gamemodelist:
            if i.get_name() == choice:
                choice2 = easygui.buttonbox(str(i.get_msg()) + "\n\nDo you want to choose this gamemode?","Review gamemode choice",["Yes","No"])
                if choice2 == "Yes":
                    running_choose_gamemode = False
                    #return self.name, self.msg, self.BankT, self.commission_type, self.commission_amount, self.stocklist, self.stocklist_init, self.tendaybonus
                    settings = i.set_gamemode()
                    BankT = settings[2]
                    BankT_init = settings[2]
                    commision_type = settings[3]
                    commision_amount = settings[4]
                    stocklist = settings[5]
                    stocklist_init = settings[6]
                    tendaybonuslist = settings[7]
##Main UI of the program! Thankfully, this uses features already predetermined up above.
running = True
while True:
    try:
        with open("Gamemodes.py_gamemodes","rb") as f:
            gamemodelist = pickle.load(f)
            game = random.randint(0, len(gamemodelist)-1)
            settings = gamemodelist[game]
            settings = settings.set_gamemode()
            stocklist = settings[5]
            del gamemodelist, game, settings
        stocks = random.sample(stocklist, 3)
        stock1 = ""
        for i in stocks:
            if stocks.index(i) == len(stocks)-1:        
                stock1 = stock1 + str(i) +"!"
            if stocks.index(i) == len(stocks)-2:
                stock1 = stock1 + str(i) +", and "
            if stocks.index(i) == len(stocks)-3:
                stock1 = stock1 + str(i) +", "
        break
    except:
        pass
welcome = "Welcome to Python Stock Game 2! This simulator allows you to manage diffrent investments placed over the course of the game! You start the game with "+ str(BankT) + " dollars. This money can be invested in a variety of stocks, including: " + str(stock1)
menu_choices = ["Purchase stocks", "Sell stocks", "Advance", "Save", "Loan Options", "More Options", "Exit"]
easygui.msgbox(welcome, "Welcome to Python Stock Game 2!")
run = True
while run:
    change_save_or_exit = easygui.buttonbox("Would you like to play a game, create a gamemode, or exit?", title = "Play or exit?", choices = ["Play", "Create Gamemode", "Exit"])
##    change_save_or_exit = easygui.buttonbox("Would you like to play a game or exit?", title = "Play or exit?", choices = ["Play","Exit"])
    if change_save_or_exit == "Exit":
        run = False
        continue
    if change_save_or_exit == "Create Gamemode":
        game = gamemode()
        game.user_defined()
        with open("Gamemodes.py_gamemodes","rb+") as g:
            gamemodelist = pickle.load(g)
            g.seek(0)
            g.truncate()
            gamemodelist.append(game)
            pickle.dump(gamemodelist,g)
    if change_save_or_exit == "Play":
        savegame = easygui.enterbox("What savegame would you like to use?", "Choose save")
        savegame = str(savegame) + ".txt"
        init_game()
        try:
            load(savegame)
            A_MSG = ""
            for i in stocklist_init:
                A_MSG += "Name: " + str(i.get_name())
                A_MSG += "Current Price: " + str(i.get_current_value())
                A_MSG += "Shares Owned: " + str(i.get_shares_owned())
            print A_MSG
        except:
            print "That savegame does not exist! Creating new save file!"
            init_game()
            choose_gamemode()
        running = True
        A_MSG = ""
        for i in stocklist_init:
            A_MSG = A_MSG +"Name: " + str(i.get_name()) + "\nValue: " + str(i.get_current_value()) + "\nAverage value: " + str(i.get_average())+ "\n\n"
        print A_MSG
        while running:
            try:
                choice1 = easygui.buttonbox("What would you like to do?", title = "What would you like to do?", choices = menu_choices)
                if choice1 == "Loan Options":
                    if loan.check_for_loan():
                        choice2 = easygui.buttonbox("You currently have a loan!\nYou have " + str(loan.get_days_left()) + " days left to repay the loan, and a debt of " + str(loan.get_current_value()) + " dollars. Would you like to repay the loan?", "Repay loan?", ["Yes","No"])
                        if choice2 == "Yes":
                            amount = intbox("How much money would you like to pay back?","Pay back loan")
                            loan.payback(amount)
                            easygui.msgbox("Your remaining debt stands at " + str(loan.get_current_value()) + " dollars. You have " + str(loan.get_days_left()) + " days left to pay off the loan.","Loan confirmation")
                            continue
                    else:
                        choice2 = easygui.buttonbox("Would you like to take out a loan?", "Take out a loan?", ["Yes","No"])
                        if choice2 == "Yes":
                            loan_choices = ["3 day - 5%","5 day - 7%","10 day - 8%", "15 day - 12%","20 day - 15%"] 
                            loan_lenghth = easygui.buttonbox("How long would you like the loan to last? Longer time frames have higher intrest rates.","Loan duration",loan_choices)
                            amount = intbox("How much money would you like to borrow?","Amount to borrow")
                            if loan_lenghth == loan_choices[0]:
                                loan = ""
                                loan = makeloan(amount,1.05,3)
                            if loan_lenghth == loan_choices[1]:
                                loan = ""
                                loan = makeloan(amount,1.07,5)
                            if loan_lenghth == loan_choices[2]:
                                loan = ""
                                loan = makeloan(amount,1.08,10)
                            if loan_lenghth == loan_choices[3]:
                                loan = ""
                                loan = makeloan(amount,1.12,15)
                            if loan_lenghth == loan_choices[4]:
                                loan = ""
                                loan = makeloan(amount,1.15,20)
                            easygui.msgbox("You have borrowed " + str(loan.get_current_value()) + " dollars. You have " + str(loan.get_days_left()) + " days left to pay off the loan.","Loan confirmation")
                if choice1 == "More Options":
                    opt_list = ["View stock history (Graph)","View stock history (Data)","View shares owned","View Bank Balance","Stock Overview","View dividend information","Get advise","Back"]
                    choice_1 = easygui.buttonbox("What would you like to do?", title = "What would you like to do?", choices = opt_list)
                    if choice_1 == "View dividend information":
                        msg = []
                        for i in stocklist_init:
                            msg.append([i.get_dividend_amount(),i.get_name(),i.get_next_dividend()])
                        msg.sort()
                        msg = msg[::-1]
                        MSG = ""
                        for i in msg:
                            MSG += "Name: " + str(i[1]) + "\nDividend percent yield: " + str(i[0]*100) + "%\nDays to dividend payment: " + str(i[2]) + "\n\n"
                        easygui.codebox("Dividend information","Dividend information", MSG)
                    if choice_1 == "View stock history (Data)":
                        MSG = ""
                        for i in stocklist_init:
                            data = ""
                            data1 = []
                            data1 = i.get_past_prices()
                            if len(data1) >= 2:
                                for y in data1[:-1]:
                                    data += str(y) + ", "
                                data += "and " + str(data1[-1])
                            elif len(data1) == 1:
                                data = data1[0]
                            MSG += "The past prices of " + str(i.get_name()) + " are: " + str(data) + ".\n\n"
                        easygui.codebox("All time data for all stocks", "All time data for all stocks", MSG)
                    if choice_1 == "Get advise":
                        choice2 = easygui.buttonbox("Advise for investments costs $500 per stock. Do you wish to continue?", title = "Get advise", choices = ["Yes","No"])
                        if choice2 == "Yes":
                            BankT -= 500
                            stocklist_sliced = stocklist[:]
                            stocklist_sliced.append("[Inside Scoop]")
                            choice3 = easygui.choicebox("Which stock would you like to receive advise for?","Get advise", choices = stocklist_sliced)
                            if choice3 != "[Inside Scoop]":
                                for i in stocklist_init:
                                    if i.get_name() == choice3:
                                        easygui.msgbox(i.get_recommendations(),"Advise")
                            else:
                                get_inside_scoop(stocklist_init)
                    if choice_1 == "Stock Overview":
                        MSG = ""
                        for i in stocklist_init:
                            MSG = MSG + "Name: " + str(i.get_name()) + "\nValue: " + str(i.get_current_value()) + "\nAverage Value: " + str(i.get_average()) + "\nRecent Average Value: " + str(i.get_recent_average()) +"\nShares owned: " + str(i.get_shares_owned()) + "\n\n\n"
                        easygui.codebox("Stock overview","Stock overview",MSG)    
                    if choice_1 == "View Bank Balance":
                        easygui.msgbox("Current bank balance: " + str(BankT) + " dollars.", "Current Bank Balance")
                    if choice_1 == "View shares owned":
                        MSG = "" 
                        for i in stocklist_init:
                            if i.get_shares_owned() >= 1:
                                MSG = MSG + "Name: " + str(i.get_name()) +"\nShares owned: "+str(i.get_shares_owned()) + "\n\n\n"
                        easygui.msgbox(MSG, "Shares owned")
                    if choice_1 == "View stock history (Graph)":
                        choice2 = easygui.choicebox(msg = "Which stock history would you like to view?", title = "View stock history", choices = stocklist)
                        for i in stocklist_init:
                            if choice2 == i.get_name():
                                average = 0
                                for y in i.get_past_prices():
                                    average += y
                                average = average/len(i.get_past_prices())
                                StockTime(i.get_past_prices(),average)
                if choice1 == "Exit":
                    save(savegame)
                    running = False
                    game_is_won = "False"
                if choice1 == "Purchase stocks":
                    choice2 = easygui.choicebox(msg = "What stock would you like to purchase?", title = "Purchase a stock", choices = stocklist)
                    for i in stocklist_init:
                        if i.get_name() == choice2:
                            running1 = True
                            while running1:
                                if commision_type == "percent":
                                    max_shares = BankT/i.get_current_value()
                                    money = max_shares*commision_amount*i.get_current_value()
                                    money = BankT - money
                                    max_shares = money/i.get_current_value()
                                    max_shares = int(max_shares)
                                    max_shares -= 1
                                else:
                                    money = BankT - commision_amount
                                    max_shares = money/i.get_current_value()
                                    max_shares = int(max_shares)
                                    max_shares -= 1
                                choice3 = easygui.enterbox(msg = "How many shares would you like to purchase? The current stock price is " + str(i.get_current_value()) + " dollars per share. You have " + str(BankT) + " dollars you can spend. You can purchase up to " + str(max_shares) + " shares of this stock.", title = "Purchase shares")
                                try:
                                    choice3 = int(choice3)
                                    running1 = False
                                except:
                                    pass
                            info = i.buy(choice3)
                            if info == "E":
                                easygui.msgbox("You do not have enough money for this transaction!", "Not enough money!")
                            else:
                                if commision_amount == 0:
                                    easygui.msgbox("You purchased " + str(choice3) + " shares of " + str(i.get_name()) + " for " + str(info[1]) + " dollars, at " + str(i.get_current_value())+ " dollars a share, bringing the total shares owned to " + str(info[0]) + " and a new bank balance of " + str(BankT) + " dollars.", "Transaction recept")
                                else:
                                    if commision_type == "percent":
                                        easygui.msgbox("You purchased " + str(choice3) + " shares of " + str(i.get_name()) + " for " + str(info[1]) + " dollars, at " + str(i.get_current_value())+ " dollars a share, bringing the total shares owned to " + str(info[0]) + " and a new bank balance of " + str(BankT) + " dollars. A commission of " + str(commision_amount*choice3*i.get_current_value()) + " dollars was included in this total.", "Transaction recept")
                                    else:
                                        easygui.msgbox("You purchased " + str(choice3) + " shares of " + str(i.get_name()) + " for " + str(info[1]) + " dollars, at " + str(i.get_current_value())+ " dollars a share, bringing the total shares owned to " + str(info[0]) + " and a new bank balance of " + str(BankT) + " dollars. A commission of " + str(commision_amount) + " dollars was included in this total.", "Transaction recept")
                if choice1 == "Sell stocks":
                    choice2 = easygui.choicebox(msg = "What stock would you like to sell?", title = "Sell a stock", choices = stocklist)
                    for i in stocklist_init:
                        if i.get_name() == choice2:
                            running1 = True
                            while running1:
                                choice3 = easygui.enterbox(msg = "How many shares would you like to sell? Current stock price is " + str(i.get_current_value()) + " dollars per share. You own " + str(i.get_shares_owned()) + " shares.", title = "Sell shares")
                                try:
                                    choice3 = int(choice3)
                                    running1 = False
                                except:
                                    pass
                            info = i.sell(choice3)
                            if info == "E":
                                easygui.msgbox("You do not have enough shares for this transaction!", "Not enough shares!")
                            else:
                                if commision_amount == 0:
                                    MSG = "You sold " + str(choice3) + " shares of " + str(i.get_name()) + " for " + str(info[1]) + " dollars, at " + str(i.get_current_value())+ " dollars a share, bringing the total shares owned to " + str(i.get_shares_owned()) + " and a new bank balance of " + str(BankT) + " dollars."
                                else:
                                    if commision_type == "percent":
                                        MSG = "You sold " + str(choice3) + " shares of " + str(i.get_name()) + " for " + str(info[1]) + " dollars, at " + str(i.get_current_value())+ " dollars a share, bringing the total shares owned to " + str(i.get_shares_owned()) + " and a new bank balance of " + str(BankT) + " dollars. A commission of " + str(c(choice3*i.get_current_value()*commision_amount)) + " dollars was included in this total"
                                    else:
                                        MSG = "You sold " + str(choice3) + " shares of " + str(i.get_name()) + " for " + str(info[1]) + " dollars, at " + str(i.get_current_value())+ " dollars a share, bringing the total shares owned to " + str(i.get_shares_owned()) + " and a new bank balance of " + str(BankT) + " dollars. A commission of " + str(c(commision_amount)) + " dollars was included in this total"
                                    easygui.msgbox(MSG, "Transaction recept")
                if choice1 == "Advance":
    ##                "Out of Money!"
                    return_value = advance()
                    if return_value == "Game Over!":
                        running = False
                        game_is_won = True
                    if return_value == "Out of Money!":
                        running = False
                        game_is_won = False
                    save(savegame)
                if choice1 == "Save":
                    save(savegame)
            except:
                exc_type, exc_value, exc_traceback = sys.exc_info()
                traceback_details = {
                                     'filename: ': "Python Stock Game 2",#exc_traceback.tb_frame.f_code.co_filename,
                                     'line number: '  : exc_traceback.tb_lineno,
                                     'name: '    : exc_traceback.tb_frame.f_code.co_name,
                                     'type: '    : exc_type.__name__,
                                     'message: ' : exc_value.message, # or see traceback._some_str()
                                    }
                with open("error_log.txt","a") as l:
                    l.write(str(traceback_details))
                    l.write("\n\n")
                human_readable_msg = "An error occured. This has been logged. The below information was collected: \n\n Error Type: " + str(exc_value.message) + "\n\n Line Number: " + str(exc_traceback.tb_lineno) + "\nFilename: Updater Client"
                easygui.msgbox(human_readable_msg, "An error has occured")
                del(exc_type, exc_value, exc_traceback, human_readable_msg)
        try:
            if game_is_won == True:
                stats = "Congratulations! You won!\nYou ended the game with " + str(BankT) + " dollars! Or a " + str(BankT/BankT_init) + " percent profit!"
                easygui.msgbox(stats, "You won!")
            elif game_is_won == False:
                easygui.msgbox("You lost the game!")
        except:
            pass
