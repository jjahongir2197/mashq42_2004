from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def index():

    result = None

    if request.method == "POST":

        a = int(request.form.get("a"))
        b = int(request.form.get("b"))

        result = a + b

    return render_template("index.html", result=result)

app.run(debug=True)
