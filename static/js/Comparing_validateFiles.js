/*Функция для обработки на фронте, оба ли файла загружены*/
function validateForm() {
    var file1 = document.getElementById('file1').value;
    var file2 = document.getElementById('file2').value;

    if (file1 === '' || file2 === '') {
        alert('Выберите оба файла для загрузки.');
        return false;
    }

    return true;
}


/*Вывод результата*/
function handleFormSubmission(event) {
    if (validateForm()) {
        event.preventDefault();

        var form = event.target;
        var formData = new FormData(form);

        fetch(form.action, {
            method: form.method,
            body: formData
        })
            .then(response => response.json())
            .then(data => {
                if ('result' in data) {
                    // Добавляем результат в div с идентификатором result-container
                    document.getElementById('result-container').innerHTML = '<pre>' + data.result + '</pre>';
                } else if ('error' in data) {
                    console.error('Ошибка при обработке запроса:', data.error);
                    alert('Произошла ошибка: ' + data.error);
                }
            })
            .catch(error => {
                console.error('Ошибка при обработке запроса:', error);
                alert('Произошла ошибка: ' + error.message);
            });
    } else return false
}
