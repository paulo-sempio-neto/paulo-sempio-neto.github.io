// Portfólio — Paulo Sêmpio Neto
// Todo o conteúdo e os links funcionam sem JavaScript; aqui ficam apenas
// o menu móvel, a troca de projeto no topo e o movimento das camadas.
document.documentElement.classList.add("js");

const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)");
const clamp = (value, min = 0, max = 1) => Math.min(max, Math.max(min, value));

/* ── Ano do rodapé ── */
const year = document.querySelector("#year");
if (year) year.textContent = String(new Date().getFullYear());

/* ── Cabeçalho: fundo ao rolar e recolhe ao descer ── */
const header = document.querySelector(".site-header");
let lastScrollY = window.scrollY;

function updateHeader() {
  if (!header) return;
  const y = window.scrollY;
  header.classList.toggle("is-scrolled", y > 24);
  const menuOpen = header.querySelector("#navigation.is-open");
  const goingDown = y > lastScrollY && y > 480;
  header.classList.toggle("is-hidden", goingDown && !menuOpen && !header.contains(document.activeElement));
  lastScrollY = y;
}

/* ── Menu móvel ── */
const menuToggle = document.querySelector(".menu-toggle");
const navigation = document.querySelector("#navigation");

if (menuToggle && navigation) {
  menuToggle.hidden = false;

  const setMenu = (open, { returnFocus = false } = {}) => {
    menuToggle.setAttribute("aria-expanded", String(open));
    navigation.classList.toggle("is-open", open);
    if (open) navigation.querySelector("a")?.focus();
    if (!open && returnFocus) menuToggle.focus();
  };

  menuToggle.addEventListener("click", () => {
    setMenu(menuToggle.getAttribute("aria-expanded") !== "true");
  });

  navigation.addEventListener("click", (event) => {
    if (event.target.closest("a")) setMenu(false);
  });

  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape" && navigation.classList.contains("is-open")) {
      setMenu(false, { returnFocus: true });
    }
  });

  document.addEventListener("click", (event) => {
    if (navigation.classList.contains("is-open") && !header.contains(event.target)) setMenu(false);
  });
}

/* ── Topo: trocar o projeto mostrado nas camadas ── */
const heroStack = document.querySelector('[data-stack="hero"]');
const heroCaption = document.querySelector(".hero-caption");
const heroTabs = [...document.querySelectorAll(".hero-tab")];
let swapTimer;

function showProject(id) {
  const template = document.querySelector(`template[data-stack-template="${id}"]`);
  if (!heroStack || !template) return;

  heroTabs.forEach((tab) => tab.setAttribute("aria-pressed", String(tab.dataset.project === id)));

  const apply = () => {
    heroStack.querySelector(".stack-scene")?.replaceWith(template.content.firstElementChild.cloneNode(true));
    if (heroCaption) {
      heroCaption.innerHTML = "";
      const name = document.createElement("strong");
      name.textContent = template.dataset.name;
      heroCaption.append(name, ` ${template.dataset.kind}`);
    }
    requestAnimationFrame(() => heroStack.classList.remove("is-swapping"));
  };

  window.clearTimeout(swapTimer);
  if (reducedMotion.matches) {
    apply();
    return;
  }
  heroStack.classList.add("is-swapping");
  swapTimer = window.setTimeout(apply, 280);
}

heroTabs.forEach((tab) => {
  tab.addEventListener("click", () => showProject(tab.dataset.project));
});

// Pré-carrega as telas dos outros projetos quando o navegador estiver livre.
const warm = () => {
  document.querySelectorAll("template[data-stack-template]").forEach((template) => {
    const img = template.content.querySelector("img");
    if (img) new Image().src = img.getAttribute("src");
  });
};
if ("requestIdleCallback" in window) window.requestIdleCallback(warm, { timeout: 3000 });
else window.setTimeout(warm, 2000);

/* ── Topo: inclinação leve seguindo o mouse ── */
if (heroStack && !reducedMotion.matches) {
  let targetX = 0;
  let targetY = 0;
  let currentX = 0;
  let currentY = 0;
  let tiltFrame = 0;

  const animateTilt = () => {
    currentX += (targetX - currentX) * 0.08;
    currentY += (targetY - currentY) * 0.08;
    heroStack.style.setProperty("--rz", `${(currentX * 7).toFixed(2)}deg`);
    heroStack.style.setProperty("--rx", `${(currentY * -6).toFixed(2)}deg`);
    if (Math.abs(targetX - currentX) > 0.001 || Math.abs(targetY - currentY) > 0.001) {
      tiltFrame = requestAnimationFrame(animateTilt);
    } else {
      tiltFrame = 0;
    }
  };

  window.addEventListener("pointermove", (event) => {
    if (event.pointerType !== "mouse") return;
    targetX = event.clientX / window.innerWidth - 0.5;
    targetY = event.clientY / window.innerHeight - 0.5;
    if (!tiltFrame) tiltFrame = requestAnimationFrame(animateTilt);
  }, { passive: true });
}

/* ── Projetos: a tela se desmonta em camadas conforme a rolagem ── */
const scrollStacks = [...document.querySelectorAll('[data-stack="scroll"]')];
const visibleStacks = new Set();

function updateScrollStacks() {
  const viewport = window.innerHeight;
  visibleStacks.forEach((stack) => {
    const rect = stack.getBoundingClientRect();
    // 0 quando o topo entra pela base da tela; 1 quando chega a 30% do topo.
    const progress = clamp((viewport - rect.top) / (viewport * 0.75));
    const eased = 1 - Math.pow(1 - progress, 3);
    const tilt = clamp(eased * 1.6);
    const separation = clamp((eased - 0.35) / 0.65);
    stack.style.setProperty("--tilt", tilt.toFixed(3));
    stack.style.setProperty("--p", separation.toFixed(3));
  });
}

if (scrollStacks.length && !reducedMotion.matches && "IntersectionObserver" in window) {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) visibleStacks.add(entry.target);
      else visibleStacks.delete(entry.target);
    });
    requestFrame();
  }, { rootMargin: "20% 0px" });
  scrollStacks.forEach((stack) => observer.observe(stack));
} else {
  scrollStacks.forEach((stack) => {
    stack.style.setProperty("--tilt", "1");
    stack.style.setProperty("--p", "1");
  });
}

/* ── Um único laço de quadros para a rolagem ── */
let frameRequested = false;

function onFrame() {
  frameRequested = false;
  updateHeader();
  updateScrollStacks();
}

function requestFrame() {
  if (frameRequested) return;
  frameRequested = true;
  requestAnimationFrame(onFrame);
}

window.addEventListener("scroll", requestFrame, { passive: true });
window.addEventListener("resize", requestFrame);
requestFrame();

/* ── Ao vivo: a camada de interface mostra o site publicado de verdade ──
 * A captura aparece na hora; quando o site real termina de carregar dentro
 * da camada, ele entra por cima. Só em telas grandes, sem economia de dados,
 * e apenas para projetos que permitem ser exibidos dentro de outro site.
 */
const BASE_WIDTH = 1440;
const BASE_HEIGHT = 900;
const connection = navigator.connection;
const canGoLive =
  window.matchMedia("(min-width: 1024px) and (pointer: fine)").matches &&
  !(connection && connection.saveData);

const resizeObserver = "ResizeObserver" in window
  ? new ResizeObserver((entries) => {
      entries.forEach((entry) => {
        entry.target.style.setProperty("--live-scale", String(entry.contentRect.width / BASE_WIDTH));
      });
    })
  : null;

function goLive(layer) {
  if (!canGoLive || layer.dataset.liveState) return;
  const src = layer.dataset.liveSrc;
  if (!src) return;
  layer.dataset.liveState = "loading";

  const frame = document.createElement("iframe");
  frame.className = "live-frame";
  frame.src = src;
  frame.title = layer.dataset.liveTitle || "Projeto ao vivo";
  frame.width = String(BASE_WIDTH);
  frame.height = String(BASE_HEIGHT);
  frame.loading = "lazy";
  frame.tabIndex = -1;
  frame.setAttribute("aria-hidden", "true");
  frame.setAttribute("referrerpolicy", "no-referrer");
  frame.setAttribute("sandbox", "allow-scripts allow-same-origin");

  const badge = document.createElement("span");
  badge.className = "live-badge";
  badge.setAttribute("aria-hidden", "true");
  badge.textContent = "Ao vivo";

  frame.addEventListener("load", () => {
    // Dá tempo para o aplicativo pintar a primeira tela antes de aparecer.
    window.setTimeout(() => {
      layer.dataset.liveState = "ready";
    }, 1800);
  });

  layer.style.setProperty("--live-scale", String(layer.clientWidth / BASE_WIDTH));
  resizeObserver?.observe(layer);
  layer.prepend(frame);
  layer.append(badge);
}

if (canGoLive && "IntersectionObserver" in window) {
  const liveObserver = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (!entry.isIntersecting) return;
      entry.target.querySelectorAll("[data-live-src]").forEach(goLive);
    });
  }, { rootMargin: "25% 0px" });

  if (heroStack) {
    liveObserver.observe(heroStack);
    // A pilha do topo troca de conteúdo: liga o modo ao vivo na nova camada.
    new MutationObserver(() => {
      heroStack.querySelectorAll("[data-live-src]").forEach(goLive);
    }).observe(heroStack, { childList: true });
  }
}
