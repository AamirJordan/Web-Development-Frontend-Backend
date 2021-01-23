var x = 0

while (x < 5) {
  console.log("Value of x is " + x);

  if (x===3) {
    console.log("x is equal to three");
    break;
  }

  console.log("x is less than 5, adding 1 to x");
  x += 1
}
