from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

app.secret_key = "password" 

#Shows Base HTML
@app.route("/")
def show_base_html():
    session['counter'] = 1
    return render_template("base.html")

#Adds in 1
@app.route("/count", methods=['POST'])
def click():
    verify(1)
    return render_template("processed.html",num=session['counter'])

#Adds in 2
@app.route("/count2", methods=['POST'])
def double_click():
    verify(2)
    return render_template("processed2.html",num=session['counter'])

#Adds in n
@app.route("/number", methods=['POST'])
def add_in_number():
    verify(int(request.form['number']))
    return render_template("processed3.html",num=session['counter'])

#Resets
@app.route("/destroy_session", methods=['POST'])
def delete():
    return redirect('/')

def verify(i):
    if 'counter' in session:
        session['counter'] +=i
    else:
        session['counter'] = 1

if __name__ == "__main__":
    app.run(debug=True)