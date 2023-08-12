const modalMain = document.getElementById("modal_main");
const modalSub = document.getElementById("modal_success");
modalMain.classList.add("modal_active");

const onCloseClick = function () {
    const modal = this.closest(".modal");
    if (modal && modal.classList.contains("modal_active")) {
        modal.classList.remove("modal_active");
    }
}
for (button of document.querySelectorAll(".modal__close")) button.onclick = onCloseClick;

document.querySelector(".show-success").onclick = () => {
    modalMain.classList.remove("modal_active");
    modalSub.classList.add("modal_active");
}
