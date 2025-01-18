// burger menu
const hamburger = document.querySelector(".hamburger");
const cross = document.querySelector(".cross");
const menu = document.querySelector(".menu");

// click burger icon
hamburger.addEventListener("click", () => {
  hamburger.classList.toggle("active");
  cross.classList.toggle("active");
  menu.classList.toggle("active");
});

// click cross icon
cross.addEventListener("click", () => {
  hamburger.classList.toggle("active");
  cross.classList.toggle("active");
  menu.classList.toggle("active");
});
