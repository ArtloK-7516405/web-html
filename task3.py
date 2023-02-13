from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def title():
    return '''<!doctype html>
                <html lang="en">
                  <head>
                    <title>Миссия Колонизация Марса</title>
                  </head>
                </html>'''


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    list = ['Человечество вырастает из детства.',
            'Человечеству мала одна планета.',
            'Мы сделаем обитаемыми безжизненные пока планеты.',
            'И начнем с Марса!',
            'Присоединяйся!',
            ]
    return '</br>'.join(list)


@app.route('/image_mars')
def image_mars():
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <image src={url_for('static', filename='img/mars.png')}/></br>
                    Вот она какая, красная планета.
                  </body>
                </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
