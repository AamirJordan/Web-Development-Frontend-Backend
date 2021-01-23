<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>

      <form action="site.php" method="post">

        Num1 : <input type="float" name="num1" value="">
        operator : <input type="text" name="op" value="">
        Num2 : <input type="float" name="num2" value="">
        <input type="submit" name="" value="Submit">

      </form>



    <?php
      $num1 = $_POST["num1"];
      $op = $_POST["op"];
      $num2 = $_POST["num2"];

      if ($op == "+") {
        echo $num1 + $num2;
      }
      elseif ($op == "-") {
        echo $num1 - $num2;
      }
      elseif ($op == "*") {
        echo $num1 * $num2;
      }
      elseif ($op == "/") {
        echo $num1 / $num2;
      }
      else {
        echo "Invalid operator";
      }

     ?>

  </body>
</html>
