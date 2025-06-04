from flask import Flask, request, render_template_string

app = Flask(__name__)

USERNAME = "admin"
PASSWORD = "admin123"

HTML_FORM = """
<!doctype html>
<title>Login</title>
<h2>Login Page</h2>
<form method="POST">
  Username: <input type="text" name="username"><br><br>
  Password: <input type="password" name="password"><br><br>
  <input type="submit" value="Login">
</form>
{% if message %}
<p>{{ message }}</p>
{% endif %}
"""

@app.route("/login", methods=["GET", "POST"])
def login():
    message = ""
    if request.method == "POST":
        user = request.form.get("username")
        pwd = request.form.get("password")
        if user == USERNAME and pwd == PASSWORD:
            message = "Login successful"
        else:
            message = "Invalid credentials"
    return render_template_string(HTML_FORM, message=message)

if __name__ == "__main__":
    app.run(debug=True)
