<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>

    <form action="site.php" method="get">

      <input type="text" name="student" value="">
      <input type="submit" name="" value="Submit">

    </form>


      <?php
        $grades = array("Jim"=>"A+", "Ross"=>"B+", "Neesham"=>"C+");
        echo $grades["Neesham"];
        echo "<br>";
        echo $grades[$_GET["student"]]
       ?>


  </body>
</html>
