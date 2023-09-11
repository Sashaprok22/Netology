const book = document.getElementById("book");
document.querySelectorAll(".font-size").forEach((button) => {
    button.addEventListener("click", (e)=> {
        e.preventDefault();
        document.querySelector(".font-size_active").classList.remove("font-size_active");
        button.classList.add("font-size_active");

        book.classList.remove("font-size_small");
        book.classList.remove("font-size_big");

        if (button.dataset.size === "small") {
            book.classList.add("font-size_small");
        } else if (button.dataset.size === "big") {
            book.classList.add("font-size_big");
        }
    });
});