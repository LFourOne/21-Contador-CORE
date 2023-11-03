from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)

app.secret_key = "Shhhh, stay quiet!"

@app.route("/")
def index():
    counter = session.get("counter", 0)
    counter += 1
    session["counter"] = counter
    return render_template("index.html", counter=counter)

@app.route("/destroy_session")
def destroy():
    session.pop("counter")
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)