window.addEventListener('scroll', function () {
    let header = document.querySelector('.navbar1 nav');
    let windowPosition = window.scrollY >50;
    header.classList.toggle('scrolling-active', windowPosition);
  });
