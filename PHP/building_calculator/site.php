<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>

    <form action="site.php" method="GET">

      Num 1 : <input type="number" name="Num1" placeholder="Enter Num 1">
      <br>
      Num 2 : <input type="number" name="Num2" placeholder="Enter Num 2">
      <br>
      <input type="submit" name="" value="Submit">

    </form>

    Answer : <?php echo $_GET["Num1"] + $_GET["Num2"] ?>

  </body>
</html>
