from flask import Flask, request, redirect, url_for, render_template, send_from_directory

app = Flask(__name__)

# Simple in-memory users (no DB)
USERS = {
    "student1": {"password": "pass123", "name": "Student One", "pdf_url": "https://www.w3.org/WAI/WCAG21/Techniques/pdf/img/table.pdf"},
    "admin": {"password": "admin123", "name": "Admin User", "pdf_url": "https://www.w3.org/WAI/WCAG21/Techniques/pdf/img/table.pdf"},
    "rajat": {"password": "rajat", "name": "rajat", "pdf_url": "https://drive.google.com/file/d/1rbvxsiCmA6yZz3r8EyF3nMuDmgBXoURs/preview"},
    "R56917": {"password": "Jnu@123" , "name": "Ritika", "pdf_url":"https://drive.google.com/file/d/1_UOi-KlyToWPCC2J7Z-OXDqvXmy1j_EH/preview"},
}

@app.route("/")
def index():
    # Serve the existing static index.html from project root
    return render_template("index.html")

@app.route("/pdfs/<filename>")
def serve_pdf(filename):
    import os
    return send_from_directory(os.path.join(app.root_path, "pdfs"), filename)

@app.route("/account/login", methods=["POST"]) 
def account_login():
    username = request.form.get("email", "").strip()
    password = request.form.get("password", "").strip()

    print("username", username)
    print("password", password)

    user = USERS.get(username)
    # print("user get----->",user)

    if user and user["password"] == password:
        return redirect(url_for("success", username=username))

    return redirect(url_for("failed"))

@app.route("/success")
def success():
    username = request.args.get("username", "")
    pdf_url = ""
    user_data = USERS.get(username)

    print("user_data----->", user_data)
    if user_data:
        pdf_url = user_data.get("pdf_url", "")
    return render_template("success.html", user=user_data.get("name", "") if user_data else "", pdf_url=pdf_url, ok=True)

@app.route("/failed")
def failed():
    return render_template("success.html", user="", ok=False)

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port, debug=True)
