<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>

    <?php
      class Student{

        var $name;
        var $major;
        var $gpa;



        function __construct($name, $major, $gpa)
        {
          $this->name = $name;
          $this->major = $major;
          $this->gpa = $gpa;
        }




        function hasHonours()
        {
          if ($this->gpa > 3.5) {
            return "True";
          }
          else {
            return "False";
          }
        }

      }

      $Student1 = new Student("Lee", "Business", 5.7);
      $Student2 = new Student("Shane", "Art", 3.2);

      echo $Student1->hasHonours();                                               echo "<br>";
      echo $Student2->hasHonours();
     ?>

  </body>
</html>
