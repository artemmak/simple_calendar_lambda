from datetime import date

from flask import Flask

app = Flask(__name__)
@app.route("/")
def index():
    today = date.today()
    formatted_date = today.strftime("%d.%m.%Y")
    return formatted_date

if __name__ == "__main__":
    app.run(debug=True)