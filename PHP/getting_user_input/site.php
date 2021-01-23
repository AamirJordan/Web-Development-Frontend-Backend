<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>

    <form action="site.php" method="GET">

      Name: <input type="text" name="username" placeholder="Enter Your Name">
      <br>
      Age: <input type="number" name="userage" placeholder="Enter Your Age">
      <br>
      <input type="submit" name="" value="Submit">

    </form>

    Your name is <?php echo $_GET["username"] ?>
    <br>
    Your age is <?php echo $_GET["userage"] ?>

  </body>
</html>
