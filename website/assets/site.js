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

document.querySelectorAll('a[href="approach.html"]').forEach(link => {
  if (!link.closest(".text-link") && !link.closest(".service-list")) link.textContent = "How We Work";
});
document.querySelectorAll('a[href="about.html"]').forEach(link => {
  if (!link.closest(".text-link")) link.textContent = "Who We Are";
});
if (nav && !nav.querySelector('a[href="work.html"]')) {
  const workLink = document.createElement("a");
  workLink.href = "work.html";
  workLink.textContent = "Work";
  const insightsLink = nav.querySelector('a[href="insights.html"]');
  nav.insertBefore(workLink, insightsLink || nav.querySelector(".nav-cta"));
}
