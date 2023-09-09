from flask import Flask

app = Flask(__name__)


@app.route("/id")
def get_id():
    return "hello world, your id is 36242119950912411X"


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run()

