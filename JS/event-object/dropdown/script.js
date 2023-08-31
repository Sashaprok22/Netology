function changeDropdownListVisible() {
    const dropdown =this.closest(".dropdown");
    const dropdownList = dropdown.querySelector(".dropdown__list");
    if (dropdownList.classList.contains("dropdown__list_active")) {
        dropdownList.classList.remove("dropdown__list_active");
    } else {
        dropdownList.classList.add("dropdown__list_active");
    }
}

function selectItem(e) {
    e.preventDefault();
    const dropdown =this.closest(".dropdown");
    dropdown.querySelector(".dropdown__value").innerText = this.innerText;
    dropdown.querySelector(".dropdown__list").classList.remove("dropdown__list_active");
}

document.querySelectorAll(".dropdown__item").forEach((item) => {
   item.addEventListener("click", selectItem);
});

document.querySelectorAll(".dropdown__value").forEach((item) => {
    item.addEventListener("click", changeDropdownListVisible);
});