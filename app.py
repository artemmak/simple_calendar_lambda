from _datetime import date, datetime
from utils import date_utils

from flask import Flask, render_template_string, request


app = Flask(__name__)

HTML_TEMPLATE = """
<!doctype html>
<html lang="uk">
<head>
    <meta charset="utf-8">
    <title>Simple Calendar</title>
    <style>
        body {
            background: #f5f5f5;
            margin: 0;
            height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            font-family: sans-serif;
        }
        .card {
            background: #fff;
            padding: 20px 30px;
            border-radius: 10px;
            box-shadow: 0 4px 16px rgba(0,0,0,0.1);
            text-align: center;
        }
        .text {
            font-size: 28px;
            font-weight: bold;
        }
    </style>
</head>

<body>
    <div class="card">
        <div class="text">{{ text }}</div>
    </div>
</body>
</html>
"""

@app.route("/")
def index():
    today = date.today()
    formatted_date = today.strftime("%d.%m.%Y")
    return render_template_string(HTML_TEMPLATE, text=formatted_date)


@app.route("/to_new_year")
def to_new_year():
    today = date.today()
    return render_template_string(
        HTML_TEMPLATE, text=date_utils.count_days_to_new_year(today)
    )


@app.route("/days_between")
def days_between():
    first_date_str = request.args.get("first")
    second_date_str = request.args.get("second")
    first_date = datetime.strptime(first_date_str, "%d.%m.%Y").date()
    second_date = datetime.strptime(second_date_str, "%d.%m.%Y").date()
    days_count = date_utils.count_days_between(first_date, second_date)
    return render_template_string(HTML_TEMPLATE, text=days_count)


@app.route("/is_weekend")
def is_weekend():
    input_date_str = request.args.get("date")
    input_date = datetime.strptime(input_date_str, "%d.%m.%Y").date()
    return render_template_string(
        HTML_TEMPLATE,text=date_utils.is_weekend(input_date)
    )


if __name__ == "__main__":
    app.run(debug=True)
