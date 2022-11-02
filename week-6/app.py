# -*- coding: UTF-8 -*-
from flask import Flask
from flask import request
from flask import render_template
from flask import make_response
from flask import redirect
from flask import session
import mysql.connector
import json


app=Flask(
    __name__,
    static_folder="static",
    static_url_path="/"
)
app.secret_key="keySecret123456"
storeByCookieOrSession=2 #1: cookie, 2: session

mysql_pool=mysql.connector.pooling.MySQLConnectionPool(
            pool_name="mypool", pool_size=10, 
            host="localhost", database="websystem_week6",
            user="root", password="",
            pool_reset_session=True)

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
    try:
        conn = mysql_pool.get_connection() #get connection from connect pool
        cursor = conn.cursor()
        sql="select * from member where username=%s"
        cursor.execute(sql,[username])
        myresult = cursor.fetchall()
    except Exception as e:
        print(e)
        cursor.close()
        conn.close()
    
    if len(myresult)==0:
        sql = "INSERT INTO member(fullName,username,password)VALUES (%s, %s, MD5(%s))"
        cursor.execute(sql, (fullName, username, password))
        conn.commit()
        return redirect("/")
    else:
        message="帳號已經被註冊"
        return redirect("/error?message="+message)
    cursor.close()
    conn.close()

@app.route("/error")
def errorHandler():
    errorMessage=request.args.get("message","")
    return render_template("error.html",errorMessageShowInPage=errorMessage)
   
@app.route("/signin",methods=["POST"])
def checkSignin():
    username=request.form["username"]
    password=request.form["password"]

    try:
        conn = mysql_pool.get_connection() #get connection from connect pool
        cursor = conn.cursor()
        sql ="select * from member where username=%s and password=MD5(%s)"
        cursor.execute(sql,(username,password))
        myresult = cursor.fetchall()
    except Exception as e:
        print(e)
    finally: # must close cursor and conn!!
        cursor.close()
        conn.close()
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
    try:
        conn = mysql_pool.get_connection() #get connection from connect pool
        cursor = conn.cursor()
        sql ="SELECT member.fullName,message.content FROM message INNER JOIN member ON message.member_id=member.id"
        cursor.execute(sql)
        messageBoard = cursor.fetchall()
    except Exception as e:
        print(e)
    finally: # must close cursor and conn!!
        cursor.close()
        conn.close()
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
    try:
        conn = mysql_pool.get_connection() #get connection from connect pool
        cursor = conn.cursor()
        sql ="INSERT INTO message(member_id,content)VALUES (%s, %s)"
        cursor.execute(sql, (userId, messageContent))
        conn.commit()
    except Exception as e:
        print(e)
    finally: # must close cursor and conn!!
        cursor.close()
        conn.close()
    return redirect("/member")

@app.route("/api/member",methods=["GET"])
def apiGetMemberName():
    try:
        memberThatYouSearch=request.args.get("username","")
        conn = mysql_pool.get_connection() #get connection from connect pool
        cursor = conn.cursor()
        sql='select json_object("id",id,"name",fullName,"username",username) from member where username=%s'
        print(sql)
        cursor.execute(sql,[memberThatYouSearch])
        myresult = cursor.fetchone()
        
    except Exception as e:
        print(e)
    finally: # must close cursor and conn!!
        cursor.close()
        conn.close()

    #Return result with json format
    if myresult:
        GetMemberName={"data":json.loads(myresult[0])}
    else:
        GetMemberName={"data":None}
    return json.dumps(GetMemberName)


app.run(port=3000)
