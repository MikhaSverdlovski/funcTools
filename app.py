from flask import Flask, render_template


class MyApp(Flask):
    def __init__(self, *args, **kwargs):
        super(MyApp, self).__init__(*args, **kwargs)

        # Дополнительная конфигурация при необходимости


app = MyApp(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/comparing')
def comparing():
    return render_template('ComparingDocs.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
