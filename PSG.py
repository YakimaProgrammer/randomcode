from flask import make_response, request, redirect
from ast import literal_eval
from functools import wraps
import random, easygui, flask

app = flask.Flask(__name__)

def session(func):
    @wraps(func)
    def action(*args,**kwargs):
        s = dict(request.cookies.items())
        session = {}
        for x,y in s.items():
            if x.startswith("PSG "): session[x[4:]] = y
        s = {}
        for x,y in session.items():
            if x.startswith("stock "):
                s[x[6:]] = literal_eval(y)
        for x in s.keys():
            del session[f"stock {x}"]
        session["stocks"] = s
        for x,y in session.items():
            try:
                session[x] = literal_eval(str(y))
            except:
                session[x] = y
        res = make_response(func(session,*args,**kwargs))
        if "stocks" in session.keys():
            s = {}
            for x,y in session["stocks"].items():
                s[f"stock {x}"] = y
            session.update(s)
            del session["stocks"]
        for x,y in session.items():
            res.set_cookie(f"PSG {x}",str(y))
            if type(y) == dict:
                if 'is crashed' in y:
                    if y['is crashed']:
                        res.delete_cookie(f"PSG {x}")
                        res.delete_cookie(f"PSG {x} stock data")
        
        return res
    return action
    

def generate_stocks(names):
    stocks = {}
    data = {}
    for n in range(len(names)):
        dividend_amount = random.choice([0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.02, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.03, 0.04, 0.04, 0.04, 0.04, 0.04, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        stocks[names[n]] = {"price":random.randint(2500,8000)/100,"daily change":random.randint(10,35),'shares':0,"previous day":random.randint(2500,12000)/100,"previous buy price":-1,"is crashed":False,"is crashing":False,"not notified is crashing":False,"days left of crash":0,"days to dividend":random.randint(4,10),"dividend amount":dividend_amount,"split":False}
    return stocks

def advance_stocks(session):
    for x,y in session["stocks"].items():
        y["previous day"] = y["price"]
        session[f"{x} stock data"].append(y["previous day"])
        if y["price"] >= 200: #stock split limit
           splits = y["price"] // random.randint(15,35)
           y["price"] = round(y["price"]/splits,2)
           y["shares"] *= splits
           y["split"] = True
           y["previous day"] = y['previous buy price'] = y["price"]

        y["days to dividend"] -= 1
        
        if not y["is crashing"]:
            y["price"] += (random.randint(0,y["daily change"]*100) * random.choice([1,-1]))/100
            if y["price"] < 60:
                if random.choice([False]*49 + [True]):
                    y["is crashing"] = True
                    y["not notified is crashing"] = True
                    y["days left of crash"] = random.randint(15,45)
            elif y["price"] < 30:
                if random.choice([False]*14 + [True]):
                    y["is crashing"] = True
                    y["not notified is crashing"] = True
                    y["days left of crash"] = random.randint(10,25)
            elif y["price"] < 15:
                if random.choice([False]*9 + [True]):
                    y["is crashing"] = True
                    y["not notified is crashing"] = True
                    y["days left of crash"] = random.randint(10,25)
            elif y["price"] < 10:
                if random.choice([False]*3 + [True]):
                    y["is crashing"] = True
                    y["not notified is crashing"] = True
                    y["days left of crash"] = random.randint(10,15)
            elif y["price"] < 5:
                if random.choice([False] + [True]*4):
                    y["is crashing"] = True
                    y["not notified is crashing"] = True
                    y["days left of crash"] = random.randint(2,8)
        else:
            y["price"] += (random.randint(0,y["daily change"]*100) * random.choice([0.125]*3+[-0.75]*4+[-2]*4))/100
        
        if y["price"] <= 0:
            y["is crashed"] = True

@app.route("/",methods=("GET","POST"))
@session
def game(session):
    if session == {'stocks': {}}:
        #The player has not started the game, so initalize all the variables
        session["stocks"] = generate_stocks(["SDG","MFHG","DAHJ"])
        session["bank balance"] = 10000
        session["init bank balance"] = session["bank balance"]
        session["day"] = 0
        session["is timed"] = False
        session["days left"] = -1
        session["menu"] = "set gamemode"
        session["version"] = "2b"
        return easygui.msg_box("Welcome to Python Stock Game Beta in the browser!","Welcome!",button_label = "Let\'s play!")

    if "version" in session:
        if session["version"] != "2b":
            msg = """Gamemodes!
- Whether you choose to slowly dominate the market or race against the clock, these new gamemodes add a new challenge to the game!
Info tabs!
- Find out more before you buy!""" #Coming soon: inside scoop and loans!
            return easygui.msg_box(msg,"What's new:",destination_page="/reset")

    if request.form.get("next menu"):
        session["menu"] = request.form.get("next menu")

    if session["menu"] == "set gamemode":
        gamemode_choice = request.form.get("gamemode choice")
        if gamemode_choice:
            if gamemode_choice == "Trainer":
                session["stocks"] = generate_stocks(["SDG"])
                session["bank balance"] = 5000
            elif gamemode_choice == "Easy":
                session["stocks"] = generate_stocks(["SDG","MFHG","DAHJ"])
                session["bank balance"] = 10000
            elif gamemode_choice == "Normal":
                session["stocks"] = generate_stocks(["SDG","MFHG","DAHJ","Gold Co","Silver Co","Lumber Co","Oil Co"])
                session["bank balance"] = 5000
            elif gamemode_choice == "Hard":
                session["stocks"] = generate_stocks(["SDG","MFHG","DAHJ","Gold Co","Silver Co","Lumber Co","Oil Co"])
                session["bank balance"] = 100
            elif gamemode_choice == "20 Day Rush":
                session["stocks"] = generate_stocks(["SDG","MFHG","DAHJ","Gold Co","Silver Co","Lumber Co","Oil Co"])
                session["bank balance"] = 100
                session["is timed"] = True
                session["days left"] = 21
            elif gamemode_choice == "10 Day Rush":
                session["stocks"] = generate_stocks(["SDG","MFHG","DAHJ","Gold Co","Silver Co","Lumber Co","Oil Co"])
                session["bank balance"] = 50
                session["is timed"] = True
                session["days left"] = 11

            elif gamemode_choice == "One Day Roulette":
                session["stocks"] = generate_stocks(["SDG","MFHG","DAHJ","Gold Co","Silver Co","Lumber Co","Oil Co"])
                session["bank balance"] = 500
                session["is timed"] = True
                session["days left"] = 2

            for x in session["stocks"].keys():
                session[f"{x} stock data"] = []
            session["menu"] = "Advance"
            session["init bank balance"] = session["bank balance"]
        else:
            msg = """Trainer:
One stock and $5,000 dollars to invest.
Easy:
Three stocks and $10,000 dollars to invest.
Normal:
Eight stocks and $5,000 dollars to invest.
Hard:
Eight stocks and $100 dollars to invest.
20 Day Rush:
Twenty days to make the most money possible with eight stocks and $100!
10 Day Rush:
Ten days to make the most money possible with eight stocks and $50!
One Day Roulette:
One day to make the most money possible with eight stocks and $500!"""            
            return easygui.button_box(msg,["Trainer","Easy","Normal","Hard","20 Day Rush","10 Day Rush","One Day Roulette"],"gamemode choice","Which gamemode do you want to play?")

    if session["menu"] == "New Game":
        conf = request.form.get("confirm")
        if conf == "Yes":
            return redirect("/reset")
        elif conf == "No":
            session["menu"] = "main menu"
        else:
            return easygui.button_box("All progress will be reset!",["Yes","No"],"confirm","Are you sure you want to start a new game?")

    if session["menu"] == "Info":
        tab = request.form.get("tab")
        if tab:
            session["menu"] = "main menu"
            if tab == "Dividends":
                msg = ""
                for x,y in sorted(session["stocks"].items(),key=lambda k: k[1]['dividend amount'],reverse=True):
                    msg += f"{x} will pay a dividend of {y['dividend amount']*100}% in {y['days to dividend']} {'days' if y['days to dividend'] != 1 else 'day'}!\n"
                return easygui.msg_box(msg,"Dividends:")
            elif tab == "Stock Data":
                msg = ""
                for x,y in session["stocks"].items():
                    z = session[f"{x} stock data"]
                    average = sum(z)/len(z)
                    tda = sum(z[-3:])/len(z[-3:])
                    msg += f"{x} is {'above' if average < y['price'] else 'below'} it's average price of ${round(average,2)}!\n"
                    msg += f"{x} is {'above' if tda < y['price'] else 'below'} it's recent 3-day average price of ${round(tda,2)}!\n\n"

                return easygui.msg_box(msg,"Stock Data")
            elif tab == "Current Data":
                msg = ""
                for x,y in sorted(session["stocks"].items()):
                    if not y["is crashed"]:
                        msg += f"{x}: ${round(y['price'],2)}, "
                        msg += f"{'up' if y['previous day'] < y['price'] else 'down'} ${round(abs(y['previous day'] - y['price']),2)} {'dollars' if round(abs(y['previous day'] - y['price']),2) != 1 else 'dollar'} from yesterday."
                        if y['shares'] > 0:
                            msg += f" {x} is {'up' if y['previous buy price'] < y['price'] else 'down'} ${round(abs(y['previous buy price'] - y['price']),2)} {'dollars' if round(abs(y['previous buy price'] - y['price']),2) != 1 else 'dollar'} from when you last bought shares.\n"
                        else:
                            msg += "\n"
                return easygui.msg_box(msg,"Today's Market Data:")

        else:
            return easygui.button_box("",["Dividends","Stock Data","Current Data"],"tab","Which do you want to view?")

    if request.form.get("_ stock to buy"):
        session["_ stock to buy"] = request.form.get("_ stock to buy")
    else:
        if not "_ stock to buy" in session:
            session["_ stock to buy"] = None

    if session["_ stock to buy"] == "[Back]":
        session["_ stock to buy"] = None
        session["menu"] = "main menu"
    if session["menu"] == "Buy Shares":
        if request.form.get("number of shares"):
            numshares = abs(int(request.form.get("number of shares")))
            if session["bank balance"] - (numshares*session["stocks"][session["_ stock to buy"]]["price"]) >= 0:
                session["stocks"][session["_ stock to buy"]]["shares"] += numshares
                session["stocks"][session["_ stock to buy"]]["previous buy price"] = session["stocks"][session["_ stock to buy"]]["price"]
                session["bank balance"] -= (numshares*session["stocks"][session["_ stock to buy"]]["price"])
                session["menu"] = "main menu"
                stb = session["_ stock to buy"]
                session["_ stock to buy"] = None
                return easygui.msg_box("",f"Successfully purchased {numshares} {'shares' if session['stocks'][stb]['shares'] != 1 else 'share'} of {stb}!")
            else:
                return easygui.msg_box("","Unable to purchase shares due to an insufficient amount of funds!")
        
        if session["_ stock to buy"]:
            return easygui.enter_box(f"You currently have {session['stocks'][session['_ stock to buy']]['shares']} {'shares' if session['stocks'][session['_ stock to buy']]['shares'] != 1 else 'share'} of {session['_ stock to buy']}. You can buy up to {int(session['bank balance']/session['stocks'][session['_ stock to buy']]['price'])} {'shares' if int(session['bank balance']/session['stocks'][session['_ stock to buy']]['price']) != 1 else 'share'}.","number of shares",f"How many shares do you want to buy?")
        else:   
            return easygui.button_box("",sorted([x for x,y in session["stocks"].items() if y["price"] < session["bank balance"]]),"_ stock to buy","Which stock do you want to buy?")

    ###
    if request.form.get("_ stock to sell"):
        session["_ stock to sell"] = request.form.get("_ stock to sell")
    else:
        if not "_ stock to sell" in session:
            session["_ stock to sell"] = None

    if session["_ stock to sell"] == "[Back]":
        session["_ stock to sell"] = None
        session["menu"] = "main menu"
            
    if session["menu"] == "Sell Shares":
        if request.form.get("number of shares"):
            numshares = abs(int(request.form.get("number of shares")))
            if session["stocks"][session["_ stock to sell"]]["shares"] >= numshares:
                session["stocks"][session["_ stock to sell"]]["shares"] -= numshares
                session["bank balance"] += (numshares*session["stocks"][session["_ stock to sell"]]["price"])
                session["menu"] = "main menu"
                stb = session["_ stock to sell"]
                session["_ stock to sell"] = None
                return easygui.msg_box("",f"Successfully sold {numshares} {'shares' if session['stocks'][stb]['shares'] != 1 else 'share'} of {stb}!")
            else:
                return easygui.msg_box("","Unable to sell shares due to an insufficient amount of shares owned!")
        
        if session["_ stock to sell"]:
            return easygui.enter_box(f"You currently have {session['stocks'][session['_ stock to sell']]['shares']} {'shares' if session['stocks'][session['_ stock to sell']]['shares'] != 1 else 'share'} of {session['_ stock to sell']}.","number of shares",f"How many shares do you want to sell?")
        else:
            return easygui.button_box("",sorted([x for x,y in session["stocks"].items() if y["shares"] > 0]),"_ stock to sell","Which stock do you want to sell?")
    ###
    if session["menu"] == "View Bank Balance":
        session['menu'] = 'main menu'
        msg = f"Balance: ${round(session['bank balance'],2)}\n"
        worths = {}
        for x,y in session["stocks"].items():
            worths[x] = y["shares"] * y["price"]

        nw = sum(worths.values()) + session['bank balance']
        msg += f"Net worth: ${round(nw,2)}\n"
        msg += "Your financial worth by stock:\n"
        for x,y in worths.items():
            msg += f"{x}: ${round(y,2)}\n"
        msg += f"You have {'made' if nw - session['init bank balance'] >= 0 else 'lost'} ${round(abs(nw - session['init bank balance']),2)} so far!"
        return easygui.msg_box(msg,"Bank Balance Statistics")

    if session["menu"] == "Advance":
        #Now include info on wether the price increased or decreased compared to yesterday and 
        advance_stocks(session)
        session["menu"] = "main menu"
        if not session["stocks"] or (session["is timed"] and (session["days left"] <= 1)):
            worths = {}  #This is nessisary for the second part of the above conditional
            for x,y in session["stocks"].items():
                worths[x] = y["shares"] * y["price"]
            nw = sum(worths.values()) + session['bank balance']
            return easygui.msg_box(f"You {'made' if nw - session['init bank balance'] >= 0 else 'lost'} ${round(abs(nw - session['init bank balance']),2)} over {session['day']} {'day' if session['day'] == 1 else 'days'}!",f"{'Time;s Up!' if session['is timed'] else 'Congratulations! You won the game!'}".replace(";","'"),button_label="Play again",destination_page="/reset")
        session["day"] += 1
        msg = f"Day {session['day']}:\n"
        if session["is timed"]:
            session["days left"] -= 1
            msg = f"You have {session['days left']} {'days' if session['days left'] != 1 else 'day'} left!\n"
        for x,y in sorted(session["stocks"].items()):
            if y["is crashed"]:
                msg += f"{x} crashed!\n"
            elif y["not notified is crashing"]:
                msg += f"{x} is about to hit some hard times!\n"
                y["not notified is crashing"] = False

        for x,y in sorted(session["stocks"].items()):
            if y["shares"] > 0:
                if y["days to dividend"] <= 0:
                    if y["dividend amount"]:
                        amount = round(y["dividend amount"] * y["price"] * y["shares"],2)
                        session["bank balance"] += amount
                        y["days to dividend"] = 10
                        msg += f"{x} paid a dividend of ${amount}!\n"
            elif y["days to dividend"] <= 0:
                y["days to dividend"] = 10

        for x,y in sorted(session["stocks"].items()):
            if y["split"]:
                y["split"] = False
                msg += f"{x} just split!"
                if y["shares"] > 0:
                    msg += f" You now own {y['shares']} shares!\n"
                else:
                    msg += "\n"
        for x,y in sorted(session["stocks"].items()):
            if not y["is crashed"]:
                msg += f"{x}: ${round(y['price'],2)}, "
                msg += f"{'up' if y['previous day'] < y['price'] else 'down'} ${round(abs(y['previous day'] - y['price']),2)} {'dollars' if round(abs(y['previous day'] - y['price']),2) != 1 else 'dollar'} from yesterday."
                if y['shares'] > 0:
                    msg += f" {x} is {'up' if y['previous buy price'] < y['price'] else 'down'} ${round(abs(y['previous buy price'] - y['price']),2)} {'dollars' if round(abs(y['previous buy price'] - y['price']),2) != 1 else 'dollar'} from when you last bought shares.\n"
                else:
                    msg += "\n"
        return easygui.msg_box(msg)

    if session["menu"] == "main menu":
        return easygui.button_box("",["Buy Shares","Sell Shares","View Bank Balance","Info","Advance","New Game"],"next menu","What do you want to do?")
    
    return "Nothing!"

@app.route("/reset",methods=("get","post"))
def psg_reset():
    res = make_response(redirect("/"))
    cookies = list(request.cookies.keys())
    for c in cookies:
        if c.startswith("PSG"):
            res.set_cookie(c,"0",0)
    return res

if __name__ == "__main__":
    app.run(host="0.0.0.0")
