from flask import Flask
from models.Diet import Diet
from database import db

app = Flask(__name__)
app.config["SECRET_KEY"] = "your_secret_key"
app.config["SQLALCHEMY_DATABASE_URI"] = (
    "mysql+pymysql://root:admin123@127.0.0.1:3306/diet-crud"
)

db.init_app(app)


@app.route("/")
def hello_world():
    return "Hello World"


if __name__ == "__main__":
    app.run(debug=True)
