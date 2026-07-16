const mobileMenuBtn = document.getElementById("mobile-menu-btn");
const mobileMenu = document.getElementById("mobile-menu");
const menuIconPath = document.getElementById("menu-icon-path");

mobileMenuBtn.addEventListener("click", () => {
  mobileMenu.classList.toggle("hidden");

  // Toggle icon path between Hamburger and Close (X)
  if (mobileMenu.classList.contains("hidden")) {
    menuIconPath.setAttribute("d", "M4 6h16M4 12h16M4 18h16");
  } else {
    menuIconPath.setAttribute("d", "M6 18L18 6M6 6l12 12");
  }
});

// like Dislike button
const likes = document.querySelectorAll(".like");
likes.forEach((like) => {
  const heart = like.querySelector("i");
  like.addEventListener("click", (event) => {
    if (heart) {
      heart.classList.add("fa-beat");
      if (heart.classList.contains("fa-regular")) {
        heart.classList.remove("fa-regular");
        heart.classList.add("fa-solid", "fa-beat");
      } else {
        heart.classList.remove("fa-solid");
        heart.classList.add("fa-regular");
      }

      setTimeout(()=>{
        heart.classList.remove("fa-beat")
      },800)
    }
  });
});
