var modal = ducument.querySelector(".modal-btn");
var modalBg = ducmunet.querySelector(".modal-bg");
var modalClose = document.querySelector(".modal-class");

modal.addEventListanner("click", function() {
    modalBg.classList.add('bg-active')
});

modalClose.addEventListanner("click", function() {
    modalBg.classList.remove('bg-active');
})