document.addEventListener('DOMContentLoaded', () => {
    const toggleImage = document.getElementById('toggle-image');
    const images = ['3.png', '4.png'];
    let currentIndex = 0;

    function toggleImageSource() {
        currentIndex = (currentIndex + 1) % images.length;
        toggleImage.src = images[currentIndex];
    }

    // Set the initial image
    toggleImage.src = images[currentIndex];

    // Toggle images every 3 seconds (3000 milliseconds)
    setInterval(toggleImageSource, 3000);
});