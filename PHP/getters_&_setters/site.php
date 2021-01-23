<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>

    <?php
      class Movie {
        public $title;
        private $rating;

        function __construct($title, $rating)
        {
          $this->title = $title;
          $this->rating = $rating;
        }

        function getRating(){
          return $this->rating;
        }

        function setRating($rating){
          if ($rating == "G" || $rating = "PG" || $rating == "PG-13" || $rating == "R" || $rating == "NR") {
            $this->rating = $rating;
          }
          else {
            $this->rating = "NR";
          }
        }
      }


      $avengers = new Movie("Avengers", "PG-13");
      //  G, PG, PG-13, R, NR
          //  $avengers->setRating("Dog");


      echo $avengers->getRating();
     ?>

  </body>
</html>
