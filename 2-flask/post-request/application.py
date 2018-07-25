from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/hello", methods=["POST"])
def hello():
    # Request for sensitive information should always be "POST" because when requests are "GET", the information submitted will appear on the url as data sent
    name = request.form.get("name")
    return render_template("hello.html", name=name)


if __name__ == "__main__":
    app.run()