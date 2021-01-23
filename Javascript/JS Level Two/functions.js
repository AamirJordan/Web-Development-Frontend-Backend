//------------------------Basic format of function-------------------------------------
function hello() {
  console.log("hello world!");
}






//------------------------Addressing a name-------------------------------------
function helloYou(name){
  console.log("hello " + name );
}


//------------------------Adding numbers using function-------------------------
function addNum(num1,num2) {
  console.log(num1+num2);
}


//------------------------Defining a parameter inside of a function-------------
function helloSomeone(name= "Aamir"){
  console.log("Hello " + name);
}


//------------------------Using return statement--------------------------------
function formal(name="Sam", title="Sir") {
  return title + " " + name
}


//-------------------------Power a number---------------------------------------
function timesFive(numInput) {
  //-----------------------Using Local Scope------------------------------------
  var result = numInput * 5
  return result
}



//------------------------Using Global Scope------------------------------------
var v = "Global V"
var stuff = "Global Stuff"

function fun(stuff) {
  console.log(v);
  stuff = "Reassign stuff inside function"
  console.log(stuff);
}

fun();
console.log(stuff);
