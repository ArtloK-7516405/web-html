from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def title():
    return '''Миссия Колонизация Марса'''


@app.route('/index')
def index():
    return '''И на Марсе будут яблони цвести!'''


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

@app.route('/promotion_image')
def promotion_image():
    return f'''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <link rel="stylesheet" href={url_for('static', filename='css/style.css')}>
                    <title>Колонизация</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <image src={url_for('static', filename='img/mars.png')}/></br></br>
                    <h2 class="alert alert-secondary" role="alert">
                      Человечество вырастает из детства.
                    </div>
                    <h2 class="alert alert-success" role="alert">
                      Человечеству мала одна планета.
                    </div>
                    <h2 class="alert alert-secondary" role="alert">
                      Мы сделаем обитаемыми безжизненные пока планеты.
                    </div>
                    <h2 class="alert alert-warning" role="alert">
                      И начнем с Марса!
                    </div>
                    <h2 class="alert alert-danger" role="alert">
                      Присоединяйся!
                    </div>
                  </body>
                </html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')