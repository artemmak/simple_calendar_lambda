from datetime import date

from flask import Flask, Response

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
        .date {
            font-size: 28px;
            font-weight: bold;
        }
    </style>
</head>

<body>
    <div class="card">
        <div class="date">{{ formatted_date }}</div>
    </div>
</body>
</html>
"""

@app.route("/")
def index():
    today = date.today()
    formatted_date = today.strftime("%d.%m.%Y")
    html = HTML_TEMPLATE.replace("{{ formatted_date }}", formatted_date)
    return Response(html, mimetype="text/html; charset=utf-8")

if __name__ == "__main__":
    app.run(debug=True)