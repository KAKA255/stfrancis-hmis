
from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return "St. Francis Mission Hospital HMIS is live!"
if __name__ == "__main__":
    app.run()
