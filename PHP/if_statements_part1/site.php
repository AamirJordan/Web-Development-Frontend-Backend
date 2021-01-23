<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>

    <?php
      $isMale = true;
      $isTall = false;

      if ($isMale && $isTall) {
        echo "You are a tall male";
      }
      elseif ($isMale && !$isTall) {
        echo "You are a short male";
      }
      elseif (!$isMale && $isTall) {
        echo "You are not a male but are tall";
      }
      else {
        echo "You are not a male nor tall";
      }
     ?>

  </body>
</html>
