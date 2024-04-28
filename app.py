from flask import Flask

app = Flask(__name__)

@app.route("/",methods=["GET"])
def root():
    return "Hello Flask 20240428"

if __name__ == "__main__":
    app.run(port=5000,debug=True)