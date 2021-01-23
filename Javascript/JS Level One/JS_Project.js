var firstname = prompt("What is your first name?")
var lastname = prompt("What is your last name?")
var age = prompt("What is your age?")
var height = prompt("How tall are you?")
var petName = prompt("What is your petname")


var nameCond = null
var ageCond = null
var heightCond = null
var petNameCond = null


if (firstname[0]===lastname[0]) {
  nameCond = true
}else {
  nameCond = false
}


if (age > 20 && age < 30) {
  ageCond = true
}else {
  ageCond = false
}



if (height>=170) {
  heightCond = true
}else {
  heightCond = false
}



if (petName[petName.length-1] === "y") {
  petNameCond = true
}else {
  petNameCond = false
}




if (nameCond && ageCond && heightCond && petNameCond) {
  console.log("You are a spy");
}else {
  console.log("You are not a spy");
}
