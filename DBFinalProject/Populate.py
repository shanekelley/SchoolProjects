import os
import sqlite3
import random
from flask import Flask, request, render_template, g
from datetime import datetime
import time
#conn = sqlite3.connect('CryptoSite.db')


# Create the application
app = Flask(__name__)

currUser = 0

#####################################################
# Database handling 
  
def connect_db():
    """Connects to the database."""
    debug("Connecting to DB.")
    conn = sqlite3.connect(os.path.join(app.root_path, 'CryptoSite.db'))
    conn.row_factory = sqlite3.Row
    return conn
    
def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db
    
@app.teardown_appcontext
def close_db(error):
    """Closes the database automatically when the application
    context ends."""
    debug("Disconnecting from DB.")
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()



#####################################################
# Debugging

def debug(s):
    """Prints a message to the screen (not web browser) 
    if FLASK_DEBUG is set."""
    if app.config['DEBUG']:
        print(s)
        
        
######################################################
@app.route("/")
def homepage():
    db = get_db()
    rows = db.execute('select * from CoinData order by name')
    rowlist = rows.fetchall()
    return render_template("home.html", CoinData = rowlist)         
        
        
        
        
@app.route("/login", methods=['get', 'post'])
def login():
    if "step" not in request.form:     
        return render_template('login.html', step="compose_entry")
    
    elif request.form["step"] == "add_entry":
        db = get_db()
        #username1 = request.form['uname']
        #username2 = str(username1)
        password1 = db.execute("Select password from AccountInfo where username = (?)",
                   [request.form['uname']])
        pass1 = password1.fetchone()
        password2 = request.form['pword']
        
        #print(password2)
        if (str(pass1["password"]) == str(password2)):
            num = db.execute("Select AccNum from AccountInfo where username = (?)",
                   [request.form['uname']])
            num1 = num.fetchone()
            global currUser
            currUser = num1["AccNum"]
            print(currUser)
            return render_template("login1.html", step="compose_entry")
        else:
            return render_template("login2.html", step="compose_entry")
        
        
# Sign Up      
@app.route("/signup", methods = ['get', 'post'])
def signup():
    global colNum
    
    if "step" not in request.form:
        return render_template('signup.html', step = "compose_entry") 
    
    elif request.form["step"] == "add_entry":
        db = get_db()   
        accNum2 = random.randint(10000000000, 99999999999)
#        sql = 'SELECT * FROM AccountInfo'
#        db.cursor().execute(sql)
#        colNum = db.cursor.description[colNum][0]
#        sql_search = 'SELECT * FROM AccountInfo WHERE ' + colNum + ' LIKE "%' + ' ' + accNum2 + '%"'
#        print(sql_search)
#        
#        if(accNum2 != sql_search):
#            
        db.execute("insert into AccountInfo(AccNum, username, password, email) values (?, ?, ?, ?)",
                   [accNum2, request.form['username'], request.form['password'], request.form['email']])
        db.execute("insert into AccountBal(AccNum, bitcoinBal, moneroBal,ethereumBal, totalBal) values (?, ?, ?, ?, ?)",
                   [accNum2, 0, 0, 0, 0])
        db.commit()
        return render_template("signup.html", step = "add_entry")
#        else: 
#            accNum2 += 1
    
        
        
        
@app.route("/dashboard", methods=['get', 'post'])
def dashboard():
   db = get_db()
   rows = db.execute('select * from CoinData order by name')
   rowlist = rows.fetchall()
   return render_template("dashboard.html", CoinData = rowlist)












@app.route("/buysell", methods = ['get', 'post'])
def buysell():
    if "step" not in request.form:
        db = get_db()
        userBals = db.execute('select * from AccountBal where AccNum = (?)', [currUser])
        listBals = userBals.fetchall()
        return render_template("buysell.html", step="compose_entry", AccountBal = listBals)
    elif request.form["step"] == "add_entry":
        db = get_db()
        userBals = db.execute('select * from AccountBal where AccNum = (?)', [currUser])
        listBals = userBals.fetchall()
        transactAmount = request.form['transAmount']
        intTransactAmount = int(transactAmount)
        accoChoice = request.form['accChoice']
        bitBal = db.execute('select bitcoinBal from AccountBal where AccNum = (?)', [currUser])
        bitBal2 = bitBal.fetchone()
        intBitBal = int(bitBal2["bitcoinBal"])
        monBal = db.execute('select moneroBal from AccountBal where AccNum = (?)', [currUser])
        monBal2 = monBal.fetchone()
        intMonBal = int(monBal2["moneroBal"])
        ethBal = db.execute('select ethereumBal from AccountBal where AccNum = (?)', [currUser])
        ethBal2 = ethBal.fetchone()
        intEthBal = int(ethBal2["ethereumBal"])
        totBal = db.execute('select totalBal from AccountBal where AccNum = (?)', [currUser])
        totBal2 = totBal.fetchone()
        intTotBal = int(totBal2["totalBal"])
        newTotBal = intTotBal + intTransactAmount
        if accoChoice == "bitcoinBal":
            newBitBal = intBitBal + intTransactAmount
            newMonBal = intMonBal
            newEthBal = intEthBal
            symbol = "BTC"
        elif accoChoice == "moneroBal":
            newBitBal = intBitBal
            newMonBal = intMonBal + intTransactAmount
            newEthBal = intEthBal
            symbol = "XMR"
        elif accoChoice == "ethereumBal":
            newBitBal = intBitBal
            newMonBal = intMonBal
            newEthBal = intEthBal + intTransactAmount
            symbol = "ETH"
        
        now = time.strftime("%m/%d/%Y")
        print (str(now))
        transNum = db.execute('select MAX(transactionNum) from Transactions')
        transNum2 = transNum.fetchone()
        intTransNum = int(transNum2["MAX(transactionNum)"])
        newTransNum = intTransNum + 1
        transFee = intTransactAmount * -0.015
        if intTransactAmount < 0:
            depWith = "w"
        else:
            depWith = "d"
            transFee = 0

        recentDate = db.execute('select MAX(date) from Fee')
        recentDate2 = recentDate.fetchone()
        strRecentDate = str(recentDate2["MAX(date)"])
        compBal = db.execute('select updatedCompBal from Fee as f1 where date = (?)', [strRecentDate])
        compBal2 = compBal.fetchone()
        intCompBal = int(compBal2["updatedCompBal"])
        newCompBal = intCompBal + transFee
        
        db.execute('update AccountBal set bitcoinBal = (?), moneroBal = (?), ethereumBal = (?), totalBal = (?) where AccNum = (?)',
                   [newBitBal, newMonBal, newEthBal, newTotBal, currUser])
        db.execute('insert into Transactions(transactionNum, DepositWithdrawal, AccNum, amount, coinSymbol, transactionFee, date) values (?, ?, ?, ?, ?, ?, ?)',
                   [newTransNum, depWith, currUser, intTransactAmount, symbol, transFee, now])
        db.execute("insert into Fee(transactionNum, transactionFee, coinSymbol, updatedCompBal, date) values (?, ?, ?, ?, ?)",
                   [newTransNum, transFee, symbol, newCompBal, now])
        db.commit()
        db = get_db()
        userBals = db.execute('select * from AccountBal where AccNum = (?)', [currUser])
        listBals = userBals.fetchall()
        return render_template("successTrans.html", AccountBal = listBals)

















@app.route("/totalmarketinfo", methods=['get', 'post'])
def totalmarketinfo():
   db = get_db()
   rows = db.execute('select * from TotalMarketInfo order by coinSymbol')
   rowlist = rows.fetchall()
   db2 = get_db()
   rows2 = db2.execute('select * from CoinChanges order by symbol')
   rowlist2 = rows2.fetchall()
   return render_template("totalmarketinfo.html", TotalMarketInfo = rowlist, CoinChanges = rowlist2 )











@app.route("/methodofpayment", methods = ['get', 'post'])
def methodOfPayment():
    return render_template('methodofpayment.html')
        
        

@app.route("/debitCredit", methods = ['get', 'post'])
def debitCredit(): 
    if "step" not in request.form:
        return render_template('debitCredit.html', step = "add_entry")
    elif request.form["step"] == "submitted":    
        db = get_db()
        global currUser
        accNumS = currUser
        db.execute("insert into CreditDebit(AccNum, nameOnCard, cardNum, CVC, expirationDate) values (?, ?, ?, ?, ?)",
                   [accNumS, request.form['nameOnCard'], request.form['cardNum'], request.form['CVC'], request.form['expDate']])
        db.commit()
        return render_template("debitCredit.html", step="submitted")
    
@app.route("/payPal", methods = ['get', 'post'])
def payPal(): 
    if "step" not in request.form:
        return render_template('paypal.html', step = "add_entry")
    elif request.form["step"] == "submitted":    
        db = get_db()
        global currUser
        accNumS = currUser
        db.execute("insert into paypal(AccNum, PaypalAccNum, nameOnAcc) values(?, ?, ?)",
                   [accNumS, request.form['payPalNum'], request.form['nameOnCard']])
        db.commit()
        
        return render_template("paypal.html", step="submitted")





@app.route("/delete", methods=['get', 'post'])
def delete():
    if "step" not in request.form:
        return render_template('delete.html', step = "ask") 
    
    elif request.form["step"] == "Yes":
        db = get_db()
        print(currUser)
        db.execute("delete from AccountInfo where AccNum = (?)",
                   [currUser])
        db.execute("delete from AccountBal where AccNum = (?)",
                   [currUser])
        db.execute("delete from CreditDebit where AccNum = (?)",
                   [currUser])
        db.execute("delete from paypal where AccNum = (?)",
                   [currUser])
        db.execute("delete from MethodOfPayment where AccNum = (?)",
                   [currUser])
        db.commit()
        
            
        return render_template('delete.html', step = "Yes")
    elif request.form["step"] == "No":
        return render_template('delete.html', step = "No")
    
######################################################
# Command line utilities 
        
def init_db():
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()

@app.cli.command('initdb')
def init_db_command():
    """Initializes the database."""
    print("Initializing DB.")
    init_db()
    
    
    
#Populate DB
@app.cli.command('populatedb')
def populate_db_command():
    """Populates the databalse."""
    print("Populating DB.")
    populate_db()
    
    
    
def populate_db():
    populateAccInfo()
    populateAccBal()
    populateCoinData()
    populateCoinChanges()
    populateTransactions()
    populateFee()
    populateMoP()
    populateCoD()
    populatePaypal()
    populateTMI()
    populateAccInfoHasMP()
    populateRelies()
    populateCoinDataHasCoinChanges()
    populateAccBalHasTrans()
    populateAffects()
        
        
        
        
def populateAccInfo():
    db=get_db()
    accNum1 = [line.rstrip('\n') for line in open('accNum.txt')]
    accNum1 = list(map(int, accNum1))
    user1 = [line.rstrip('\n') for line in open('id.txt')]
    pass1 = [line.rstrip('\n') for line in open('passWord.txt')]
    email1 = [line.rstrip('\n') for line in open('email.txt')]
    for x in range (0, 1000):
        accNum2 = accNum1[x]
        user2 = user1[x]
        pass2 = pass1[x]
        email2 = email1[x]
        db.execute("insert into AccountInfo(AccNum, username, password, email) values (?, ?, ?, ?)",
                   [accNum2, user2, pass2, email2])
    db.commit()
        
        
        
def populateAccBal():
    db=get_db()
    accNum1 = [line.rstrip('\n') for line in open('accNum.txt')]
    accNum1 = list(map(int, accNum1))
    bitBal1= [line.rstrip('\n') for line in open('bitBal.txt')]
    bitBal1= list(map(float, bitBal1))
    xmrBal1= [line.rstrip('\n') for line in open('XMRbal.txt')]
    xmrBal1= list(map(float, xmrBal1))
    ethBal1= [line.rstrip('\n') for line in open('ethBal.txt')]
    ethBal1= list(map(float, ethBal1))
    for x in range(0,1000):
        accNum2 = accNum1[x]
        bitBal2 = bitBal1[x]
        xmrBal2 = xmrBal1[x]
        ethBal2 = ethBal1[x]
        totBal = bitBal2 + xmrBal2 + ethBal2
        db.execute("insert into AccountBal(AccNum, bitcoinBal, moneroBal, ethereumBal, totalBal) values (?, ?, ?, ?, ?)",
                   [accNum2, bitBal2, xmrBal2, ethBal2, totBal])
    db.commit()
        
        
        
        
def populateCoinData():
    db=get_db()
    db.execute("insert into CoinData(symbol, name, tradeVolume, price) values ('BTC', 'Bitcoin', 5408000000, 7823.85); ")
    db.execute("insert into CoinData(symbol, name, tradeVolume, price) values ('ETH', 'Ethereum', 1630030000, 446.25); ")
    db.execute("insert into CoinData(symbol, name, tradeVolume, price) values ('XMR', 'Monero', 54281300, 186.47); ")
    db.commit()

    
def populateCoinChanges():
    db=get_db()
    db.execute("insert into CoinChanges(symbol, oneday, oneweek, onemonth, threemonths, oneyear) values ('BTC', -0.0113, -0.1258, -0.1883, -0.4840, 6.6538); ")
    db.execute("insert into CoinChanges(symbol, oneday, oneweek, onemonth, threemonths, oneyear) values ('ETH', -0.0619, -0.2057, -0.4714, -0.4028, 7.7717); ")
    db.execute("insert into CoinChanges(symbol, oneday, oneweek, onemonth, threemonths, oneyear) values ('XMR', -0.0104, -0.1853, -0.3276, -0.5278, 8.8481); ")
    db.commit()
        
        
        
def populateTransactions():
    db=get_db()
    transNum1 = [line.rstrip('\n') for line in open('transNum.txt')]
    transNum1 = list(map(int, transNum1))
    deposWithd1 = [line.rstrip('\n') for line in open('deposWithdraw.txt')]
    accNum1 = [line.rstrip('\n') for line in open('accNum.txt')]
    accNum1 = list(map(int, accNum1))
    amount1 = [line.rstrip('\n') for line in open('transAmount.txt')]
    amount1 = list(map(float, amount1))
    coinSym1 = [line.rstrip('\n') for line in open('transSymbol.txt')]
    date1 = [line.rstrip('\n') for line in open('transDate.txt')]
    for x in range (0, 1000):
        transNum2 = transNum1[x]
        deposWithd2 = deposWithd1[x]
        accNum2 = accNum1[x]
        amount2 = amount1[x]
        coinSym2 = coinSym1[x]
        fee2 = amount1[x]*.015 #calculation for fee
        date2 = date1[x]
        date3 = datetime.strptime(date2, '%m/%d/%Y')
        db.execute("insert into Transactions(transactionNum, DepositWithdrawal, AccNum, amount, coinSymbol, transactionFee, date) values (?, ?, ?, ?, ?, ?, ?)",
                   [transNum2, deposWithd2, accNum2, amount2, coinSym2, fee2, date3])
    db.commit()
        
        
def populateFee():
    db=get_db()
    transNum1 = [line.rstrip('\n') for line in open('transNum.txt')]
    transNum1 = list(map(int, transNum1))
    amount1 = [line.rstrip('\n') for line in open('transAmount.txt')]
    coinSym1 = [line.rstrip('\n') for line in open('transSymbol.txt')]
    date1 = [line.rstrip('\n') for line in open('transDate.txt')]
    compBal = 0
    amount1 = list(map(float, amount1))
    for x in range (0, 1000):
        transNum2 = transNum1[x]
        feeAmount = amount1[x]*.015
        coinSym2 = coinSym1[x]
        date2 = date1[x]
        date3 = datetime.strptime(date2, '%m/%d/%Y')
        compBal = compBal + feeAmount
        db.execute("insert into Fee(transactionNum, transactionFee, coinSymbol, updatedCompBal, date) values (?, ?, ?, ?, ?)",
                   [transNum2, feeAmount, coinSym2, compBal, date3])
    db.commit()
        
        
def populateMoP():
    db=get_db()
    accNum1 = [line.rstrip('\n') for line in open('accNum.txt')]
    accNum1 = list(map(int, accNum1))
    methodPay1 = [line.rstrip('\n') for line in open('methodofPayment.txt')]
    authAmount1 = [line.rstrip('\n') for line in open('authAmount.txt')]
    authAmount1 = list(map(int, authAmount1))
    coinSym1 = [line.rstrip('\n') for line in open('transSymbol.txt')]
    for x in range (0, 1000):
        accNum2 = accNum1[x]
        methodPay2 = methodPay1[x]
        authAmount2 = authAmount1[x]
        coinSym2 = coinSym1[x]
        db.execute("insert into MethodOfPayment(AccNum, methodOfPayment, AuthorizationAmount, coinSymbol) values (?, ?, ?, ?)",
                   [accNum2, methodPay2, authAmount2, coinSym2])
    db.commit()
        
        
        
def populateCoD():
    db=get_db()
    accNum1 = [line.rstrip('\n') for line in open('accNum.txt')]
    accNum1 = list(map(int, accNum1))
    cNum1= [line.rstrip('\n') for line in open('cNumber.txt')]
    lastname1 = [line.rstrip('\n') for line in open('last_name.txt')]
    cNum1= list(map(float, cNum1))
    cvc1= [line.rstrip('\n') for line in open('CVC_data.txt')]
    cvc1= list(map(float, cvc1))
    date1 = [line.rstrip('\n') for line in open('expDate.txt')]
    for x in range (0, 1000):
        accNum2 = accNum1[x]
        cNum2 = cNum1[x]
        lastname2 = lastname1[x]
        cvc2 = cvc1[x]
        date2 = date1[x]
        date3 = datetime.strptime(date2, '%m/%d/%Y')
        db.execute("insert into CreditDebit(AccNum, nameOnCard, cardNum, CVC, expirationDate) values (?, ?, ?, ?, ?)",
                   [accNum2, lastname2, cNum2, cvc2, date3])
    db.commit()
        
        
        
def populatePaypal():
    db=get_db()
    accNum1 = [line.rstrip('\n') for line in open('accNum.txt')]
    accNum1 = list(map(int, accNum1))
    paypalNum1 = [line.rstrip('\n') for line in open('paypalAccNum.txt')]
    paypalNum1 = list(map(int, paypalNum1))
    lastname1 = [line.rstrip('\n') for line in open('last_name.txt')]
    for x in range (0, 1000):
        accNum2 = accNum1[x]
        paypalNum2 = paypalNum1[x]
        lastname2 = lastname1[x]
        db.execute("insert into Paypal(AccNum, PaypalAccNum, nameOnAcc) values (?, ?, ?)",
                   [accNum2, paypalNum2, lastname2])
    db.commit()
        
        
        
def populateTMI():
    db=get_db()
    db.execute("insert into TotalMarketInfo(coinSymbol, marketCap, TwentyFourHourVol, marketSupply) values ('BTC', 132561735995, 5408000000, 16943287); ")
    db.execute("insert into TotalMarketInfo(coinSymbol, marketCap, TwentyFourHourVol, marketSupply) values ('ETH', 43936069354, 1630030000, 98456840); ")
    db.execute("insert into TotalMarketInfo(coinSymbol, marketCap, TwentyFourHourVol, marketSupply) values ('XMR', 2825152674, 54281300, 15871250); ")
    db.commit()
        
        
        
def populateAccInfoHasMP():
    db=get_db()
    accNum1 = [line.rstrip('\n') for line in open('accNum.txt')]
    accNum1 = list(map(int, accNum1))
    for x in range (0, 1000):
        accNum2 = accNum1[x]
        db.execute("insert into AccInfoHasMP(AccNum) values (?)",
                   [accNum2])
    db.commit()

        
        
def populateRelies():
    db=get_db()
    accNum1 = [line.rstrip('\n') for line in open('accNum.txt')]
    accNum1 = list(map(int, accNum1))
    coinSym1 = [line.rstrip('\n') for line in open('transSymbol.txt')]
    for x in range (0, 1000):
        accNum2 = accNum1[x]
        coinSym2 = coinSym1[x]
        db.execute("insert into Relies(AccNum, coinSymbol) values (?, ?)",
                   [accNum2, coinSym2])
    db.commit()
        
        
        
def populateCoinDataHasCoinChanges():
    db=get_db()
    coinSym1 = [line.rstrip('\n') for line in open('transSymbol.txt')]
    for x in range (0, 1000):
        coinSym2 = coinSym1[x]
        db.execute("insert into CoinDataHasCoinChanges(coinSymbol) values (?)",
                   [coinSym2])
    db.commit()
        
        
        
def populateAccBalHasTrans():
    db=get_db()
    accNum1 = [line.rstrip('\n') for line in open('accNum.txt')]
    accNum1 = list(map(int, accNum1))
    transNum1 = [line.rstrip('\n') for line in open('transNum.txt')]
    transNum1 = list(map(int, transNum1))
    for x in range (0, 1000):
        accNum2 = accNum1[x]
        transNum2 = transNum1[x]
        db.execute("insert into AccbalHasTrans(AccNum, transactionNum) values (?, ?)",
                   [accNum2, transNum2])
    db.commit()
        
        
        
        
def populateAffects():
    db=get_db()
    coinSym1 = [line.rstrip('\n') for line in open('transSymbol.txt')]
    for x in range (0, 1000):
        coinSym2 = coinSym1[x]
        db.execute("insert into Affects(coinSymbol) values (?)",
                   [coinSym2])
    db.commit()
        
#connect_db()
#init_db()
#populate_db()
        
