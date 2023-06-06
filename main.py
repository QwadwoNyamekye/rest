import flask
import werkzeug
from flask import request, Flask, render_template
# from replit import db

app = Flask(__name__)

app.config["TEMPLATES_AUTO_RELOAD"] = True

version_number = 0.1


@app.get("/version")
def version():
  return str(version_number)


@app.errorhandler(werkzeug.exceptions.NotFound)
def notfound_404(e):
  return render_template("404.html"), 404


@app.get("/docs")
def documentation():
  return render_template("docs.html")


@app.post("/name_form")
def name_form():
  return f"Your name is {request.form['name']}"


@app.get("/")
def response():
  return {
    "first_name": "David",
    "last_name": "Oppong-Nkrumah",
    "contact": "+233505100602",
    "email": "doppongnkrumah@test.com",
    "socials": {
      "linkedin": "someone@linkedin.net",
      "instagram": "someone@instagram.net",
      "facebook": "someone@facebook.net"
    }
  }

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=80)