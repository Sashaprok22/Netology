let totalClicks = 0;
let prevClickTime;

const cookie = document.getElementById("cookie");
const totalClicksSpan = document.getElementById("clicker__counter");
const speedClicksSpan = document.getElementById("clicker__speed");

cookie.onclick = () => {
    totalClicks++;

    let currentTime = new Date();
    let timeDiff = currentTime - (prevClickTime || currentTime);
    prevClickTime = currentTime;

    totalClicksSpan.textContent = totalClicks;
    speedClicksSpan.textContent = timeDiff > 0 ? 1000 / timeDiff: 0;
    cookie.width = cookie.width == 200 ? 250 : 200;
};