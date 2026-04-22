from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "this is sample python deployment in azure"

if __name__ == '__main__':
    app.run()
