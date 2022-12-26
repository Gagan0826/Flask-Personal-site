from flask import Flask,render_template
app=Flask(__name__)
@app.route("/home")
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/static/contact")
def contact():
    return render_template("Contact.html")

@app.route("/static/table")
def table():
    return render_template("Table.html")

@app.route("/static/hobbies")
def hobbies():
    return render_template("Hobbies.html")

if __name__=="__main__":
    app.run(debug=1)