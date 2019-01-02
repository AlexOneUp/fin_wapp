from flask import Flask, render_template, request, redirect
# from db import engine, result, aRet
from jinja_temp_dir import template_dir, jinja_environment
from database_handlers.db import aRet

app = Flask(__name__)

a=str(aRet)

@app.route("/index.html")
def main():
    temp = jinja_environment.get_template("index.html")
    return render_template(temp)

@app.route("/hi.html", methods=['POST'])       
def hello():
    f = request.form['f']
    temp = jinja_environment.get_template("hi.html")
    return render_template(temp,name=a)

if __name__ == "__main__":
    main()