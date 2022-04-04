from flask import Flask

app = Flask(__name__)

counter = 1

@app.route("/")
def main():
    global counter
    counter += 1
    return str(counter)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=81, debug = True)