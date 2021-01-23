//  Changing color of the heading and background--------------------------------
var x = $("h1")
// x.css("color","red")
// x.css("background","blue")


//  Declaring an object and then doing the changes------------------------------
var newCss = {
  "color": "white",
  "background": "lightgreen",
  "border": "10px solid red"
}

x.css(newCss);

//  Grabbing multiple lines\list------------------------------------------------
var listItems = $("li")
listItems.css("color","blue")

// Grabbing a particular item or index item-------------------------------------
listItems.eq(0).css("color","orange")
listItems.eq(-1).css("color","orange")

//  Grabbing texts in HTML------------------------------------------------------
$("h1").text("Brand new text")
      //  OR  //
x.text("Brand new text")


$("h1").html("<em>new</em>")
      //  OR  //
x.html("<em>new</em>")


//  Changing attributes---------------------------------------------------------
// $("input").eq(1).attr("type","checkbox")

//  Changing value--------------------------------------------------------------
// $("input").eq(0).val("New Value")

//  Changing with classes-------------------------------------------------------
$("h2").addClass("turnRed")
$("h2").removeClass("turnRed")
$("h3").toggleClass("turnBlue")
$("h3").toggleClass("turnBlue")
