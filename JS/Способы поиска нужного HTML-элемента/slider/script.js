const images = Array.from(document.querySelectorAll(".slider__item"));

function changeSlideTo(i) {
    if (i < 0) i = images.length - 1;
    else if (i >= images.length) i = 0;
    document.querySelector(".slider__item_active").classList.remove("slider__item_active");
    images[i].classList.add("slider__item_active");
}

const nextSlide = function () {
    const selectedSlide = document.querySelector(".slider__item_active");
    const  lastI = images.findIndex(element => element === selectedSlide) || 0;
    changeSlideTo(lastI + 1);
}

const prevSlide = function () {
    const selectedSlide = document.querySelector(".slider__item_active");
    const  lastI = images.findIndex(element => element === selectedSlide) || 0;
    changeSlideTo(lastI - 1);
}

document.querySelector(".slider__arrow_next").onclick = nextSlide;
document.querySelector(".slider__arrow_prev").onclick = prevSlide;