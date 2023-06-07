from flask import Flask
from flask import redirect, url_for,render_template,request  # to redirect users to different webpages if necessary
app = Flask(__name__)  # instance of a flask web application

# how we can access this specific page
@app.route("/")# this will take to home page when we click it
def home():
    return render_template("loginpage.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["name"]
        password=request.form["password"]
        if user=="arun2110763@ssn.edu.in" and password=="a": # Replace this line with the code that checks details from a database.
            return redirect("/levelpage")
    else:
        return render_template("loginpage.html")


@app.route('/levelpage')# parameter inside <> will pass to the function below it 
def level():
    return render_template("sudokupage.html")

@app.route("/difficulty/<level>")
def difficulty(level):
    if level=="easy":
        return redirect("/easy")
    elif level=="medium":
        return redirect("/medium")
    elif level=="hard":
        return redirect("/hard")

@app.route("/easy")
def easy():
    return render_template("start.html")

@app.route("/medium")
def medium():
    return render_template("start.html")

@app.route("/hard")
def hard():
    return render_template("start.html")

'''
@app.route("/admin")  
def admin():
    return redirect(url_for("user",name="Admin"))    #  syntax to redirect '''

if __name__ == '__main__':
    app.run(debug=True)
    