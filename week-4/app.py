from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import session

app=Flask(
    __name__,
    static_folder="static",
    static_url_path="/"
)

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
        session["username"]=username
        session["password"]=password
        return redirect("/member")
    
@app.route("/error")
def errorHandler():
    errorMessage=request.args.get("message","")
    return render_template("error.html",errorMessageShowInPage=errorMessage)

@app.route("/member")
def member():  
    if 'username' in session:
        return render_template("loginSuccess.html")
    else:
        return redirect("/")

@app.route("/signout")
def signout():
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