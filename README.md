# apna-spider
اپنا مکڑا

To download the images of a book from http://apnaorg.com website, as it is difficult to read books on their web interface.  
So we can use this script to download all the images of a book and make a pdf of them to read easily, on mobile devices etc.  

The script can be run by as following:  
`python apna-spider.py [space] bookname [space] numberofpages [space] bookurl`  
where bookname is foldername you want to create for the book  
number of pages is the total number of pages of book, this number of pages shall be downloaded (so make sure it is exact)  
bookurl is the apaorg website url for the book 

example run:  
`python apna-spider.py "Khed Muqadaran Di" "255" "http://apnaorg.com/books/shahmukhi/raja-1/book.php?fldr=book"`  
this will download the pages of the book "Khed Muqadran Di" (کھیڈ مقدراں دی) in the folder by this language name
