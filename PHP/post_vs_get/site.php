<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>

    <form action="site.php" method="post">

      Password: <input type="password" name="password" value="">


    <?php echo $_POST["password"] ?>



      Password: <input type="password" name="password" value="">
      <input type="submit" name="Password" value="Submit">

    </form>

    <?php echo $_GET["password"] ?>

  </body>
</html>
