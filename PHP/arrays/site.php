<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>

      <?php
        $friends = array("Abc", "Def", "Ghi", "jkl");
        echo $friends;
        echo "<br>";
        echo $friends[1];
        echo "<br>";
        $friends[1] = "xyz";
        echo $friends[1];
        echo "<br>";
        $friends[4] = "mno";
        echo $friends[4];
        echo "<br>";
        $friends[10] = "pqr";
        echo $friends[10] = "pqr";
        echo "<br>";
        echo count($friends);

       ?>


  </body>
</html>
