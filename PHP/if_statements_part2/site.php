<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>

    <?php
      function getMax($num1, $num2, $num3)
      {
        if ($num1 >= $num2 && $num1 >= $num3) {
          return $num1;
        }
        elseif ($num2 >= $num1 && $num2 >= $num3) {
          return $num2;
        }
        else {
          return $num3;
        }
      }

      $maxNum = getMax(300,300,90);
      echo $maxNum;
    ?>

  </body>
</html>
