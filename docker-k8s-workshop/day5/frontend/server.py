import requests
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    try:
        response = requests.get("http://backend:5000/api")
        return f"Frontend App<br>{response.text}"
    except Exception as e:
        return f"Error: {e}"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
