from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import session
from flask import make_response
app=Flask(
    __name__,
    static_folder="static",
    static_url_path="/"
)
storeByCookieOrSession=1 #1: cookie, 2: session

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/signin",methods=["POST"])
def checkSignin():
    username=request.form["username"]
    password=request.form["password"]
    
    if (not username) or (not password):
        message="請輸入帳號、密碼"
        return redirect("/error?message="+message)
    elif username!="test" or password!="test":
        message="帳號、或密碼輸入錯誤"
        return redirect("/error?message="+message)
    elif username=="test" and password=="test":
        if storeByCookieOrSession==1:
            resp = make_response(redirect("/member"))
            resp.set_cookie('username',username, max_age=30*24*60*60) # 30天
            resp.set_cookie('password',password, max_age=30*24*60*60) # 30天
            return resp
        elif storeByCookieOrSession==2:
            session["username"]=username
            session["password"]=password
            return redirect("/member")
        
@app.route("/error")
def errorHandler():
    errorMessage=request.args.get("message","")
    return render_template("error.html",errorMessageShowInPage=errorMessage)

@app.route("/member")
def member():  
    if storeByCookieOrSession==1:
        username=request.cookies.get('username')
        password=request.cookies.get('password')
        if username and password:
            return render_template("loginSuccess.html")
    elif storeByCookieOrSession==2:
        if 'username' in session:
            return render_template("loginSuccess.html")  
    return redirect("/")

@app.route("/signout")
def signout():
    if storeByCookieOrSession==1:
        resp = make_response(redirect("/"))
        resp.set_cookie('username','', expires=0) 
        resp.set_cookie('password','', expires=0) 
        return resp
    elif storeByCookieOrSession==2:
        session.pop("username", None)
        return redirect("/")

#Flask Dynamic Routing
@app.route("/square/<number>")
def square(number):
    try:
        numberData=int(number)
    except Exception:
        numberData=0
    result=numberData*numberData
    return render_template("square.html",squareShowInPage=result)
    
app.secret_key="keySecret123456"
app.run(port=3000)