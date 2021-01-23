<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>

    <?php

//  By while loop --------------------------------------------------------------
    $j = 1;
    while ($j <= 10) {
      echo "$j <br>";
      $j++;
    }


  echo "<br>";
  echo "<br>";


//  By for loop ----------------------------------------------------------------
    for ($i = 1; $i < 5 ; $i++) {
      echo "$i <br>";
    }


  echo "<br>";
  echo "<br>";


//  Array Display using For EvLoop  --------------------------------------------
      $luckyNumbers = array(5,3,6,7,8,2,45);
      for ($i = 0; $i <= count($luckyNumbers) ; $i++) {
        echo "$luckyNumbers[$i] <br>";
      }

     ?>

  </body>
</html>
