$('h1').click(function(){
  console.log("I was clicked!");
})


$('li').click(function() {
  console.log("Click on any li !");
})


$('h3').click(function() {
  $(this).text("I was changed!");
})

$('input').eq(0).keypress(function() {
  $('h3').toggleClass("turnRed");
})

$('input').eq(0).keypress(function(event) {
  console.log(event);
})

$('input').eq(0).keypress(function(event) {
  if(event.which === 13){
    $('h3').toggleClass("turnRed");
  }
})

$('h1').on("dblclick",function() {
  $('h1').addClass('turnBlue');
})

$('li').on('mouseenter',function() {
  $(this).toggleClass('turnRed');
})


$('input').eq(1).val("FADE OUT EVERYTHING");

$('input').eq(1).on("click",function(){
  $(".container").fadeOut(3000) ;
})


$('input').eq(1).on("click",function(){
  $(".container").slideUp(1000) ;
})
