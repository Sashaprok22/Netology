const onLinkClick = function () {
    const menuItem = this.closest(".menu__item");
    const subMenu = menuItem.querySelector(".menu_sub");
    if (subMenu) {
        if (subMenu.classList.contains("menu_active")) {
            subMenu.classList.remove("menu_active");
        } else {
            for (selectedSubMenu of document.querySelectorAll(".menu_active")){
                selectedSubMenu.classList.remove("menu_active");
                console.log(selectedSubMenu);
            }
            subMenu.classList.add("menu_active");
        }
        return false;
    }
}
for (link of document.querySelectorAll(".menu__link")) link.onclick = onLinkClick;