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

    }

    $book1 = new Book();
    $book1->title = "Harry Potter";
    $book1->author = "J.K.Rowling";
    $book1->pages = 900;

    echo $book1->author;                                                         echo "<br>";
    echo $book1->title;                                                          echo "<br>";
    echo $book1->pages;                                                          echo "<br>";


                                                                                 echo "<br>";


    $book2 = new Book();
    $book2->title = "Can Love Happen Twice";
    $book2->author = "Ravinder Singh";
    $book2->pages = 785;

    echo $book2->author;                                                         echo "<br>";
    echo $book2->pages;                                                          echo "<br>";
    echo $book2->title;                                                          echo "<br>";


     ?>


  </body>
</html>
