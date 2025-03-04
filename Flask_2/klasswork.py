from flask import Flask, url_for, request

app = Flask(__name__)


@app.route('/')
def index():
    return "Привет, Яндекс!"


@app.route('/index')
def index1():
    return "Привет, Яндекс!"


@app.route('/image_mars')
def image():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Привет, Яндекс!</title>
                  </head>
                  <body>
                    <h1>Жди меня Марс</h1>
                    <img src="{url_for('static', filename='img/MARS.png')}" alt="здесь должна была быть картинка, но не нашлась">
                  </body>
                </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
