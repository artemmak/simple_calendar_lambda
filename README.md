Simple Calendar

A minimal Flask web app that displays the current date.

Local Development
```bash
pip install -r requirements.txt
python app.py
```

App runs at:
```shell
http://127.0.0.1:5000/
```

Deployment (Render)

Build command:
```bash
pip install -r requirements.txt
```

Start command:
```bash
gunicorn app:app
```
