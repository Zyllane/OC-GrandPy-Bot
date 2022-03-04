from flask import Flask,render_template

app = Flask(__name__)

app.config.from_object('config')

@app.route('/')
def index():
    return render_template("test.html",test="cequejeveux")

if __name__ == "__main__":
    app.run()