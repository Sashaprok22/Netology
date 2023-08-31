function onTabClick(e){
    const tabs = this.closest(".tabs");
    const tabsNav = tabs.querySelector(".tab__navigation");
    const tabsContent = tabs.querySelector(".tab__contents");
    const clickTabIndex = Array.from(tabsNav.querySelectorAll(".tab")).indexOf(this);

    tabsNav.querySelector(".tab_active").classList.remove("tab_active");
    tabsContent.querySelector(".tab__content_active").classList.remove("tab__content_active");

    this.classList.add("tab_active");
    tabsContent.querySelectorAll(".tab__content")[clickTabIndex].classList.add("tab__content_active");
}

document.querySelectorAll(".tab").forEach((tab)=>{
    tab.addEventListener("click", onTabClick);
});