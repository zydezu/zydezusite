document.addEventListener("DOMContentLoaded", () => {
    const intro = document.getElementById("bg-video-intro");
    const loop = document.getElementById("bg-video-loop");

    setTimeout(() => {
        document.getElementById("blurred-glass-pane").classList.add("blurred");
    }, 1500);

    setTimeout(() => {
        intro.style.opacity = 0;
        loop.style.opacity = 1;
    }, 5033);
});