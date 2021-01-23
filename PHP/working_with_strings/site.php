<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>

    <?php
      $phrase = "Aamir Sohail <br>";
      echo $phrase;
      echo strtolower($phrase);
      echo strtoupper($phrase);
      echo str_replace("Aamir", "Jordan", $phrase);
      echo substr($phrase, 6);
      echo substr($phrase, 6, 3);
      echo "<br>";
      $phrase[0] = "B";
      echo strtolower($phrase);
      echo strtoupper($phrase);
      echo strlen($phrase);
      echo strtolower("<br> ABCD <br>");
      echo $phrase[4];
      echo "<br>";
      echo "Mike"[0];

     ?>

  </body>
</html>
