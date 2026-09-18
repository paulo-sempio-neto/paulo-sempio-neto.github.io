// O conteúdo e os links continuam acessíveis sem JavaScript.
document.documentElement.classList.add("js");

// Abertura breve: aparece uma vez por aba e respeita redução de movimento.
const intro = document.querySelector("#intro-screen");
const introMessage = document.querySelector("#intro-message");
const introSkip = document.querySelector("#intro-skip");
const prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)");

if (intro) {
  const alreadyShown = sessionStorage.getItem("paulo-portfolio-intro") === "shown";
  let closing = false;

  const closeIntro = () => {
    if (closing) return;
    closing = true;
    sessionStorage.setItem("paulo-portfolio-intro", "shown");
    intro.classList.add("is-leaving");
    intro.addEventListener("transitionend", () => intro.remove(), { once: true });
  };

  if (!alreadyShown) {
  window.setTimeout(() => {
    if (introMessage) introMessage.textContent = "Hello, I’m Paulo.";
      intro.classList.add("is-english");
    }, 1000);
    window.setTimeout(closeIntro, 900000);
    if (introSkip) introSkip.addEventListener("click", closeIntro);
  }
}

const year = document.querySelector("#year");
if (year) year.textContent = new Date().getFullYear();
const toggle = document.querySelector(".menu-toggle");
const navigation = document.querySelector("#navigation");
if (toggle && navigation) {
  const mobile = window.matchMedia("(max-width: 760px)");
  const closeMenu = () => {
    navigation.classList.remove("is-open");
    toggle.setAttribute("aria-expanded", "false");
  };
  const syncMenu = () => {
    const focused = document.activeElement;
    closeMenu();
    toggle.hidden = !mobile.matches;
    if (mobile.matches && navigation.contains(focused)) toggle.focus();
    if (!mobile.matches && focused === toggle) navigation.querySelector("a").focus();
  };
  syncMenu();
  mobile.addEventListener("change", syncMenu);
  toggle.addEventListener("click", () => {
    const open = toggle.getAttribute("aria-expanded") !== "true";
    toggle.setAttribute("aria-expanded", String(open));
    navigation.classList.toggle("is-open", open);
  });
  navigation.addEventListener("click", (event) => {
    const link = event.target.closest("a");
    if (!link || !mobile.matches) return;
    closeMenu();
    const section = document.querySelector(link.getAttribute("href"));
    if (section) {
      section.setAttribute("tabindex", "-1");
      section.focus({ preventScroll: true });
      section.addEventListener("blur", () => section.removeAttribute("tabindex"), { once: true });
    }
  });
  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape" && toggle.getAttribute("aria-expanded") === "true") {
      closeMenu();
      toggle.focus();
    }
  });
}
