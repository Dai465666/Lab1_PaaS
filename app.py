from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
  return """
    <h1>Chao mung den voi ung dung PaaS!</h1>
    <p>Ung dung Python Flask dang hoat dong.</p>
    <p>Duoc trien khai tren Render Cloud.</p>
    """


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000)
