const timerSpan = document.getElementById("timer");
let timeToEnd = 5;
timerSpan.textContent = timeToEnd;
let timerId = setInterval(() => {
    timeToEnd--;
    if (timeToEnd <= 0) {
        clearInterval(timerId);
        alert("Вы победили в конкурсе");
    }
    timerSpan.textContent = timeToEnd;
}, 1000);