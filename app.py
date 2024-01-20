from flask import Flask, render_template, request


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


@app.route('/compare_files', methods=['POST'])
def upload_files():
    if 'file1' not in request.files or 'file2' not in request.files:
        return 'Не удалось загрузить файлы', 400

    file1 = request.files['file1']
    file2 = request.files['file2']

    # Здесь вы можете вызвать функции для обработки файлов или что-то еще

    return 'Файлы успешно загружены и обработаны'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
