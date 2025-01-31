from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def greet():
    if request.method == "POST":
        name = request.form.get("name")
        greeting_type = request.form.get("greeting_type")
        return render_template("greet.html", name=name, greeting_type=greeting_type)
    return render_template("form.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
