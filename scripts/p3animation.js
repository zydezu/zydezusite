document.addEventListener("DOMContentLoaded", () => {
    const videoIntro = document.getElementById("bg-video-intro");
    const videoLoop = document.getElementById("bg-video-loop");

    setTimeout(
        function () {
            document.getElementById("blurred-glass-pane").classList.add("blurred");
        }, 1500);

    videoIntro.addEventListener("ended", () => {
        videoLoop.play();
        videoLoop.style.opacity = 1;
    });
});