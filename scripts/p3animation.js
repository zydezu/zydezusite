document.addEventListener("DOMContentLoaded", () => {
    const intro = document.getElementById("bg-video-intro");
    let looping = false;

    setTimeout(() => {
        document.getElementById("blurred-glass-pane").classList.add("blurred");
    }, 1000);

    setTimeout(() => {
        looping = true;
        intro.currentTime = 5;
        intro.play();
        loopVideoSegment();
    }, 5000);

    function loopVideoSegment() {
        if (!looping) return;

        const loopStart = 5;
        const loopEnd = 11.65;

        function step() {
            if (intro.currentTime >= loopEnd) {
                intro.currentTime = loopStart;
            }
            requestAnimationFrame(step);
        }

        requestAnimationFrame(step);
    }
});
