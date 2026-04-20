document.addEventListener("DOMContentLoaded", function () {

  // --- 1. Inject "About" button before the palette (dark mode) toggle ---
  var palette = document.querySelector(".md-header__option");
  if (palette) {
    // Derive root URL from the logo link so it works on any base path
    var logoLink = document.querySelector(".md-header__button.md-logo");
    var root = logoLink ? logoLink.href.replace(/\/?$/, "/") : "/";
    var aboutHref = root + "about/";

    var homeBtn = document.createElement("a");
    homeBtn.href = root;
    homeBtn.className = "md-header__button md-header__about md-header__home";
    homeBtn.innerHTML = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="22" height="22" fill="currentColor"><path d="M10 20v-6h4v6h5v-8h3L12 3 2 12h3v8z"/></svg>';
    homeBtn.setAttribute("aria-label", "Home");
    palette.parentNode.insertBefore(homeBtn, palette);

    var aboutBtn = document.createElement("a");
    aboutBtn.href = aboutHref;
    aboutBtn.className = "md-header__button md-header__about";
    aboutBtn.textContent = "About";
    aboutBtn.setAttribute("aria-label", "About");
    palette.parentNode.insertBefore(aboutBtn, homeBtn.nextSibling);

    var mapsHref = root + "concept-maps/";
    var mapsBtn = document.createElement("a");
    mapsBtn.href = mapsHref;
    mapsBtn.className = "md-header__button md-header__about";
    mapsBtn.textContent = "Concept Maps";
    mapsBtn.setAttribute("aria-label", "Concept Maps");
    palette.parentNode.insertBefore(mapsBtn, aboutBtn.nextSibling);
  }

  // --- 2. Replace the language dropdown with a simple EN | DE toggle ---
  var selectEl = document.querySelector(".md-select");
  if (selectEl) {
    var enMeta = document.querySelector('link[hreflang="en"]');
    var deMeta = document.querySelector('link[hreflang="de"]');
    var enRoot = enMeta ? enMeta.href.replace(/\/?$/, "/") : null;
    var deRoot = deMeta ? deMeta.href.replace(/\/?$/, "/") : null;

    if (enRoot && deRoot) {
      var isDE = window.location.href.indexOf(deRoot) === 0;

      var toggle = document.createElement("div");
      toggle.className = "md-header__lang-toggle";

      if (isDE) {
        toggle.innerHTML =
          '<a class="md-header__lang-link" href="#">EN</a>' +
          '<span class="md-header__lang-sep">|</span>' +
          '<span class="md-header__lang-active">DE</span>';
      } else {
        toggle.innerHTML =
          '<span class="md-header__lang-active">EN</span>' +
          '<span class="md-header__lang-sep">|</span>' +
          '<a class="md-header__lang-link" href="#">DE</a>';
      }

      toggle.querySelectorAll("a").forEach(function (a) {
        a.setAttribute("data-no-instant", "");
        a.addEventListener("click", function (e) {
          e.preventDefault();

          // The translation_link.py hook bakes the correct translated URL into
          // every term page as <a class="translation-link"> right after the <h1>.
          // Use that when available; fall back to just switching roots (for
          // pages like home, about, concept-maps that have no translation link).
          var translationAnchor = document.querySelector(".translation-link");
          var isOnDE = window.location.href.indexOf(deRoot) === 0;
          var target;
          if (translationAnchor) {
            target = translationAnchor.href;
          } else {
            var now = window.location.href.split("?")[0].split("#")[0].replace(/\/?$/, "/");
            target = isOnDE
              ? enRoot + now.slice(deRoot.length)
              : deRoot + now.slice(enRoot.length);
          }

          // Material scopes __palette to the page pathname, so EN and DE use
          // different localStorage keys. Copy the value to the target scope
          // so the new page loads with the same color scheme.
          try {
            var srcKey = (window.__md_scope || new URL(".", location)).pathname + ".__palette";
            var tgtKey = new URL(".", target).pathname + ".__palette";
            var stored = localStorage.getItem(srcKey);
            if (stored) localStorage.setItem(tgtKey, stored);
          } catch (ex) {}
          window.location.href = target;
        });
      });

      selectEl.replaceWith(toggle);
    }
  }

  // --- 3. Sidebar adjustments ---
  var logoLink2 = document.querySelector(".md-header__button.md-logo");
  var homeUrl = logoLink2 ? logoLink2.href.replace(/\/?$/, "/") : "/";

  // On the homepage: show all category sections in the sidebar (lifted nav hides them)
  var siteRoot = new URL(homeUrl).pathname.replace(/\/?$/, "/");
  var curPath = window.location.pathname.replace(/\/?$/, "/");
  var isHome = curPath === siteRoot;

  if (isHome) {
    document.body.classList.add("is-home");
  }

  // On term pages: append "← Back" to the active section's nav list
  var activeLink = document.querySelector(".md-nav__link--active");
  if (activeLink && !isHome) {
    var parentList = activeLink.closest("li").parentElement;
    if (parentList && parentList.classList.contains("md-nav__list")) {
      var backLi = document.createElement("li");
      backLi.className = "md-nav__item md-nav__item--back";
      var backA = document.createElement("a");
      backA.className = "md-nav__link md-nav__link--back";
      backA.href = homeUrl;
      backA.textContent = "← Back";
      backLi.appendChild(backA);
      parentList.appendChild(backLi);
    }
  }

  // --- 4. Make the header title text clickable (links to home) ---
  var titleEl = document.querySelector(".md-header__title");
  var logoEl  = document.querySelector(".md-header__button.md-logo");
  if (titleEl && logoEl) {
    titleEl.style.cursor = "pointer";
    titleEl.addEventListener("click", function () {
      window.location.href = logoEl.href;
    });
  }

});
