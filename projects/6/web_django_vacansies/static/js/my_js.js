function Dubl(){
    // 1. Получить элемент по ID
    let myElement = document.getElementById('text1');

    // 2. Добавить в него текст
    if (myElement) {
        myElement.innerText = 'Новый текст';
    } else {
        console.error('Элемент с заданным ID не найден.');
    }
}