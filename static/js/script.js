$(document).ready(function(){
    $('.sidenav').sidenav();
    $('.collapsible').collapsible();
    $('select').formSelect();
     $('.modal').modal();
});

// const card = document.querySelector('.card__inner');

// card.addEventListener('click', function() {
//     card.classList.toggle('is-flipped')
// });
       

const card = document.querySelectorAll(".card__inner");

function flipCard() {
  this.classList.toggle('is-flipped');
}
card.forEach((card) => card.addEventListener("click", flipCard));