from flask import Flask, render_template, request, session, redirect, url_for
import utils
import time

app = Flask(__name__)

def fname(f):
    def inner(*arg):
        print f.func_name + ": " + str(arg)
        return f(*arg)
    return inner

def exec_time(f):
    def inner(*arg):
        s = time.time()
        q = f(*arg)
        print "execution time: " + str(time.time()-s)
        return q
    return inner

@app.route("/")
@exec_time
@fname
def home():
    return render_template("home.html")

@app.route("/about")
#@exec_time
#@fname
def about():
    return render_template("about.html")

@app.route("/login",methods=["GET","POST"])
#@exec_time
#@fname
def login():
    if 's' in session:
        return redirect(url_for("profile"))

    if request.method=="GET":
        return render_template("login.html")

    else:
        name = request.form['username']
        passwd = request.form['password']

        if utils.authenticate(name,passwd):
            session['s']=name
            return redirect(url_for("profile"))
        else:
            return render_template("login.html")

@app.route("/profile",methods=["GET","POST"])
#@exec_time
#@fname
def profile():
    if 's' not in session:
        return redirect(url_for("login"))

    if request.method=="GET":
        name = session['s']
        return render_template("profile.html",name=name)
    else:
        lbutton = request.form['lbutton']
        if lbutton=="Log Out":
            return redirect(url_for("logout"))

@app.route("/logout")
#@exec_time
#@fname
def logout():
    session.pop('s', None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.debug = True
    app.secret_key="hi"
    app.run(host='0.0.0.0',port=8000)


    
