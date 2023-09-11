setInterval(()=> {
    document.querySelectorAll(".rotator").forEach((rotator) => {
        let activeI = Number.parseInt(rotator.dataset.activeI) || 0;
        activeI++;
        rotator.querySelector(".rotator__case_active").classList.remove("rotator__case_active");
        if (activeI >= rotator.children.length) activeI = 0;
        rotator.children[activeI].classList.add("rotator__case_active");
        rotator.dataset.activeI = activeI;
    });
}, 1000);