from flask import Flask, render_template, request
app = Flask("SuperScapper")

@app.route("/")
def home():
  return render_template("index.html")


@app.route("/report")
def report():
  word = request.args.get("word")
  word = word.lower()
  return render_template("report.html", word=word, searchingBy=word)
  
app.run(host="0.0.0.0")  



# @app.route("/contact")
# def contact():
#   return "Contact me "

# @app.route("/<username>")
# def potato(username):
#     return f"Hello{username}" 
