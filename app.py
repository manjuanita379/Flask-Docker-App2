from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_geek():
    return 'Hello from Flask & Docker'


if __name__ == "__development__":
    app.run(debug=True)
