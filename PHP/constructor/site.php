<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title></title>
  </head>
  <body>

    <?php

    class Book {
      var $title;
      var $author;
      var $pages;

      function __construct($aTitle, $aAuthor, $aPages)
      {
        $this->title = $aTitle;
        $this->author = $aAuthor;
        $this->pages = $aPages;
      }
    }


    $book1 = new Book("Witcher", "Hemsworth", 8099);
    $book1->title = "Lord of the Rings";
    echo $book1->title;                   //        Content of a class can be changed within an object
    $book2 = new Book("Devil May Cry", "Dante-Vergil", 10357);                    echo "<br>";
    echo $book1->author;                                                          echo "<br>";
    echo $book2->pages;
     ?>

  </body>
</html>
