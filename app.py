from flask import Flask, render_template, request, jsonify

from service.Comparer import Comparer


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
        return jsonify({'error': 'Не удалось загрузить файлы'}), 400

    try:
        # Получаем файлы из запроса
        file1 = request.files['file1']
        file2 = request.files['file2']

        # Создаем экземпляр Comparer
        comparer = Comparer()

        # Вызываем метод compare_text_files
        result = comparer.compare_text_files(file1, file2)

        # Возвращаем результат в формате JSON
        return jsonify({'result': result})
    except Exception as e:
        # Обработка ошибок, если что-то пошло не так
        return jsonify({'error': f'Ошибка при обработке файлов: {str(e)}'}), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
