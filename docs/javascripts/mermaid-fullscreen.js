// Make Mermaid diagrams fullscreen on click.
// Uses the native Fullscreen API on the .mermaid container directly.
document.addEventListener("click", function (e) {
  var el = e.target;

  // Walk up to find a .mermaid container
  while (el && el !== document.body) {
    if (el.classList && el.classList.contains("mermaid")) {
      if (document.fullscreenElement) {
        document.exitFullscreen();
      } else {
        el.requestFullscreen().catch(function () {});
      }
      return;
    }
    el = el.parentElement;
  }
});

// Style: pointer cursor + white background in fullscreen
var style = document.createElement("style");
style.textContent = [
  ".mermaid { cursor: pointer; }",
  ".mermaid:fullscreen { background: white; display: flex; align-items: center; justify-content: center; padding: 2rem; }",
  "[data-md-color-scheme='slate'] .mermaid:fullscreen { background: #0A0A0A; }",
  ".mermaid:fullscreen svg { max-width: 95vw; max-height: 95vh; }"
].join("\n");
document.head.appendChild(style);
