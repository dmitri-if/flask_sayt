from flask import Flask, url_for, request, render_template
import json
from loginform import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

#@app.route('/')
@app.route('/index/<text>')
def index(text):
    user = "И на Марсе будут яблони цвести!"
    return render_template('index.html', title=text,
                           username=user)


@app.route('/odd_even')
def odd_even():
    return render_template('odd-ev.html', number=2)


@app.route('/news')
def news():
    with open("news.json", "rt", encoding="utf8") as f:
        news_list = json.loads(f.read())
    print(news_list)
    return render_template('news.html', news=news_list)


@app.route('/prof/<prof>')
def prof(prof):
    return render_template('prof.html', prof=prof)



@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Авторизация', form=form)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
