<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>

    <form action="site.php" method="post">

      What was your grade?:<br>
      <input type="text" name="grade" value=""><br>
      <input type="submit" name="" value="Submit">

    </form>


    <?php
      $grade = $_POST["grade"];

      switch ($grade) {
        case 'A':
          echo "You were amazing";
          break;

        case 'B':
          echo "You are good";
          break;

        case 'C':
          echo "You were poor";
          break;

        case 'D':
          echo "You did poorly";
          break;

        case 'F':
          echo "You failed";
          break;

        default:
          echo "Invalid Grade";
          break;
      }
     ?>

  </body>
</html>
