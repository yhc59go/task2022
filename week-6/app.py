from flask import Flask
from flask import request
from flask import render_template
from flask import make_response
from flask import redirect
from flask import session
import mysql.connector
from flask import abort,jsonify,json

app=Flask(
    __name__,
    static_folder="static",
    static_url_path="/"
)
app.secret_key="keySecret123456"
storeByCookieOrSession=2 #1: cookie, 2: session

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="websystem_week6"
)
mycursor = mydb.cursor()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/signup",methods=["POST"])
def signup():
    username=request.form["usernameSignUp"]
    fullName=request.form["fullName"]
    password=request.form["passwordSignUp"]
    if (not fullName) or (not username) or (not password):
        message="請輸入姓名、帳號、密碼"
        return redirect("/error?message="+message)
        
    sql ="select * from member where username=\""+username+"\""
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    if len(myresult)==0:
        sql = "INSERT INTO member(fullName,username,password)VALUES (%s, %s, MD5(%s))"
        val = (fullName, username, password)
        mycursor.execute(sql, val)
        mydb.commit()
        return redirect("/")
    else:
        message="帳號已經被註冊"
        return redirect("/error?message="+message)

@app.route("/error")
def errorHandler():
    errorMessage=request.args.get("message","")
    return render_template("error.html",errorMessageShowInPage=errorMessage)
   
@app.route("/signin",methods=["POST"])
def checkSignin():
    username=request.form["username"]
    password=request.form["password"]
    sql ="select * from member where username=\""+username+"\" and password=MD5(\""+password+"\")"
 
    mycursor.execute(sql)
    myresult = mycursor.fetchall()

    if (not username) or (not password):
        message="請輸入帳號、密碼"
        return redirect("/error?message="+message)
    elif len(myresult)==0:
        message="帳號、或密碼輸入錯誤"
        return redirect("/error?message="+message)
    elif len(myresult)==1:
        if storeByCookieOrSession==1:
            resp = make_response(redirect("/member"))
            resp.set_cookie('userId',myresult[0][0], max_age=30*24*60*60) # 30天
            resp.set_cookie('username',myresult[0][2], max_age=30*24*60*60) # 30天
            resp.set_cookie('fullName',myresult[0][1], max_age=30*24*60*60) # 30天
            return resp
        elif storeByCookieOrSession==2:
            session["userId"]=myresult[0][0]
            session["fullName"]=myresult[0][1]
            session["username"]=myresult[0][2]   
            return redirect("/member")

@app.route("/member")
def member():  
    sql ="SELECT member.fullName,message.content FROM message INNER JOIN member ON message.member_id=member.id"
    mycursor.execute(sql)
    messageBoard = mycursor.fetchall()
    if storeByCookieOrSession==1:
        userId=request.cookies.get('userId')
        fullName=request.cookies.get('fullName')
        username=request.cookies.get('username')
        if username and userId and fullName:
            return render_template("loginSuccess.html",fullName=fullName,messageBoard=messageBoard)
    elif storeByCookieOrSession==2:
        if "username" in session and "userId" in session:   
            return render_template("loginSuccess.html",fullName=session["fullName"],messageBoard=messageBoard) 
             
    return redirect("/")

@app.route("/signout")
def signout():
    if storeByCookieOrSession==1:
        resp = make_response(redirect("/"))
        resp.set_cookie('userId','', expires=0) 
        resp.set_cookie('username','', expires=0) 
        resp.set_cookie('fullName','', expires=0) 
        return resp
    elif storeByCookieOrSession==2:
        session.pop("userId", None)
        session.pop("username", None)
        session.pop("fullName", None)
        return redirect("/")

@app.route("/messageIncrease",methods=["POST"])
def messageIncrease():
    messageContent=request.form["message"]
    userId=session["userId"]
    
    sql ="INSERT INTO message(member_id,content)VALUES (%s, %s)"
    val = (userId, messageContent)
    mycursor.execute(sql, val)
    mydb.commit()
    return redirect("/member")

app.run(port=3000)
