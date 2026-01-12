from flask import Flask, request, redirect, url_for, render_template, send_from_directory

app = Flask(__name__)

# Simple in-memory users (no DB)
USERS = {
    "student1": {"password": "pass123", "name": "Student One"},
    "admin": {"password": "admin123", "name": "Admin User"},
    "rajat": {"password": "rajat", "name": "rajat"},
}

@app.route("/")
def index():
    # Serve the existing static index.html from project root
    return render_template("index.html")

@app.route("/account/login", methods=["POST"]) 
def account_login():
    username = request.form.get("email", "").strip()
    password = request.form.get("password", "").strip()

    print("username", username)
    print("password", password)

    user = USERS.get(username)
    # print("user get----->",user)

    if user and user["password"] == password:
        return redirect(url_for("success", user=username))

    return redirect(url_for("failed"))

@app.route("/success")
def success():
    user = request.args.get("user", "")
    return render_template("success.html", user=user, ok=True)

@app.route("/failed")
def failed():
    return render_template("success.html", user="", ok=False)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
