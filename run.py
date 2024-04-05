from flask import Flask
from dotenv import load_dotenv

import os

app = Flask(__name__)

load_dotenv()


@app.route("/")
def hello_world():
    return os.environ["MESSAGE"]


if __name__ == "__main__":
    app.run("0.0.0.0", 80)
