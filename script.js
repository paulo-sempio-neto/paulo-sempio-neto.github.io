// O conteúdo e os links continuam acessíveis sem JavaScript.
document.documentElement.classList.add("js");

// Abertura curta, finita e opcional: aparece uma vez por aba.
const intro = document.querySelector("#intro-screen");
const introSkip = document.querySelector("#intro-skip");
const introStatus = document.querySelector("#intro-status");
const introPhoto = document.querySelector(".intro-photo");
const prefersReducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)");

if (intro) {
  const storageKey = "paulo-portfolio-intro";
  const bootLines = [...intro.querySelectorAll("[data-boot-line]")];
  const pageRegions = [
    document.querySelector(".skip-link"),
    document.querySelector(".site-header"),
    document.querySelector("main"),
    document.querySelector(".site-footer")
  ].filter(Boolean);
  const timers = [];
  let closing = false;
  let removed = false;
  let transitionHandler;
  let keydownHandler;
  let returnFocus = false;

  const schedule = (callback, delay) => {
    const timer = window.setTimeout(callback, delay);
    timers.push(timer);
    return timer;
  };

  const clearTimers = () => {
    timers.forEach((timer) => window.clearTimeout(timer));
    timers.length = 0;
  };

  const readIntroState = () => {
    try {
      return window.sessionStorage.getItem(storageKey) === "shown";
    } catch {
      return false;
    }
  };

  const saveIntroState = () => {
    try {
      window.sessionStorage.setItem(storageKey, "shown");
    } catch {
      // O portfólio continua funcional quando o armazenamento está indisponível.
    }
  };

  const setPageInert = (isInert) => {
    pageRegions.forEach((region) => {
      if (isInert) {
        region.setAttribute("aria-hidden", "true");
        if ("inert" in region) region.inert = true;
        return;
      }

      region.removeAttribute("aria-hidden");
      if ("inert" in region) region.inert = false;
    });
  };

  const setIntroStatus = (message) => {
    if (introStatus) introStatus.textContent = message;
  };

  const restoreFocus = () => {
    if (!returnFocus) return;
    const main = document.querySelector("#conteudo");
    if (!main) return;
    main.setAttribute("tabindex", "-1");
    main.focus({ preventScroll: true });
    main.addEventListener("blur", () => main.removeAttribute("tabindex"), { once: true });
  };

  const removeIntro = () => {
    if (removed) return;
    removed = true;
    clearTimers();
    if (transitionHandler) intro.removeEventListener("transitionend", transitionHandler);
    if (keydownHandler) document.removeEventListener("keydown", keydownHandler);
    setPageInert(false);
    intro.remove();
    restoreFocus();
  };

  const closeIntro = ({ immediate = false, focusContent = false } = {}) => {
    if (closing) return;
    closing = true;
    returnFocus = focusContent;
    saveIntroState();
    clearTimers();
    setIntroStatus("Portfólio carregado.");

    if (immediate || prefersReducedMotion.matches) {
      removeIntro();
      return;
    }

    intro.classList.add("is-leaving");
    transitionHandler = (event) => {
      if (event.target === intro && event.propertyName === "opacity") removeIntro();
    };
    intro.addEventListener("transitionend", transitionHandler);
    schedule(removeIntro, 700);
  };

  const hideBrokenPhoto = () => {
    if (introPhoto) introPhoto.classList.add("has-error");
  };

  if (introPhoto) {
    introPhoto.addEventListener("error", hideBrokenPhoto, { once: true });
    if (introPhoto.complete && introPhoto.naturalWidth === 0) hideBrokenPhoto();
  }

  const shouldBypassIntro = readIntroState() || prefersReducedMotion.matches || Boolean(window.location.hash);

  if (shouldBypassIntro) {
    closeIntro({ immediate: true });
  } else {
    setPageInert(true);
    intro.classList.add("is-active");
    intro.focus({ preventScroll: true });

    const bootSteps = [
      "Inicializando o portfólio.",
      "Carregando ambiente de frontend.",
      "Conectando serviços de backend.",
      "Conectando bancos de dados.",
      "Executando verificações de qualidade.",
      "Sistema online."
    ];

    bootLines.forEach((line, index) => {
      schedule(() => {
        line.classList.add("is-complete");
        setIntroStatus(bootSteps[index]);
      }, 100 + (index * 205));
    });

    schedule(() => {
      intro.classList.add("is-brand-visible");
      setIntroStatus("Apresentando Paulo Sêmpio Neto, Full Stack Developer.");
    }, 1220);

    schedule(() => {
      intro.classList.add("is-stack-visible");
      setIntroStatus("Tecnologias carregadas. Portfólio pronto.");
    }, 1580);

    schedule(() => closeIntro(), 3950);

    introSkip?.addEventListener("click", () => closeIntro({ focusContent: true }));
    keydownHandler = (event) => {
      if (event.key === "Escape") closeIntro({ focusContent: true });
    };
    document.addEventListener("keydown", keydownHandler);

    const handleMotionChange = (event) => {
      if (event.matches) closeIntro({ immediate: true });
    };
    prefersReducedMotion.addEventListener?.("change", handleMotionChange, { once: true });
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
