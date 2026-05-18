from flask import Flask
import os

app = Flask(__name__)

DATA_DIR = "/app/data"
FILE_PATH = os.path.join(DATA_DIR, "visits.txt")

os.makedirs(DATA_DIR, exist_ok=True)

@app.route("/")
def home():

    count = 1

    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, "r") as f:
            count = int(f.read()) + 1

    with open(FILE_PATH, "w") as f:
        f.write(str(count))

    return f"Persistent Visit Count: {count}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
