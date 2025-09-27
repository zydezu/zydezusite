document.addEventListener("DOMContentLoaded", () => {
    const intro = document.getElementById("bg-video-intro");
    const loop = document.getElementById("bg-video-loop");

    if (intro) {
        const preloadImages = [intro.src, loop.src].map(src => {
            return new Promise(resolve => {
                const img = new Image();
                img.src = src;
                img.onload = resolve;
            });
        });

        Promise.all(preloadImages);

        setTimeout(() => {
            document.getElementById("blurred-glass-pane").classList.add("blurred");
        }, 1500);

        setTimeout(() => {
            intro.style.opacity = 0;
            loop.style.opacity = 1;
        }, 5033);
    } else {
        setTimeout(() => {
            document.getElementById("blurred-glass-pane").classList.add("blurred");
        }, 500);
    }
});
