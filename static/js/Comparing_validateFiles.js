function validateForm() {
    var file1 = document.getElementById('file1').value;
    var file2 = document.getElementById('file2').value;

    if (file1 === '' || file2 === '') {
        alert('Выберите оба файла для загрузки.');
        return false;
    }

    return true;
}