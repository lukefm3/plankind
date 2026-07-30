const menu = document.querySelector(".menu");
const nav = document.querySelector("#nav");
if (menu && nav) menu.addEventListener("click", () => {
  const open = menu.getAttribute("aria-expanded") === "true";
  menu.setAttribute("aria-expanded", String(!open));
  nav.classList.toggle("open", !open);
});
document.querySelectorAll(".year").forEach(el => el.textContent = new Date().getFullYear());
const homeCount = document.querySelector("#home-record-count");
if (homeCount) fetch("data/metadata.json").then(r => r.json()).then(d => homeCount.textContent = Number(d.record_count).toLocaleString()).catch(() => homeCount.textContent = "500+");

