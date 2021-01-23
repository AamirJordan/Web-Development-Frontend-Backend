<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>


    <form action="site.php" method="get">

      Color: <input type="text" name="color" placeholder="Type a color">
      <br>
      Plural Noun: <input type="text" name="pluralNoun" placeholder="Type a plural noun">
      <br>
      Celebrity: <input type="text" name="celebrity" placeholder="Type a celebrity name">
      <br>
      <input type="submit" name="" value="Submit">

    </form>

    <?php

      $color = $_GET["color"];
      $pluralNoun = $_GET["pluralNoun"];
      $celebrity = $_GET["celebrity"];
      echo "Roses are $color <br>";
      echo "$pluralNoun are blue <br>";
      echo "I love $celebrity <br>";
     ?>

  </body>
</html>
