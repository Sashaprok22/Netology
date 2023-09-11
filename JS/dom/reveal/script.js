function isVisible(element) {
    const { top, bottom } = element.getBoundingClientRect();
    if (bottom < 0) return false;
    if (top > window.innerHeight) return false;
    return true;
}

const reveals = document.querySelectorAll(".reveal");
window.addEventListener("scroll", () => {
    reveals.forEach((reveal) => {
        if (isVisible(reveal)) {
            reveal.classList.add("reveal_active");
        } else {
            reveal.classList.remove("reveal_active");
        }
    });
});