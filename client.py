from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/about")
def about():
    return " World!"


@app.route("/stadies")
def stadies():
    return " give me the first offer"

@app.route('/user/<string:name>/<int:id>')
def user(name, id):
    return "user page" + name + "-" + id


if __name__=='__main__':
    app.run(debug=True)