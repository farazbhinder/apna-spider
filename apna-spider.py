# -*- coding: utf-8 -*-
import shutil
import sys
import os
import requests

def is_valid_apna_url(bookurl):
	starting = "http://apnaorg.com/books/"
	if bookurl.find(starting) == 0:
		return True
	return False

def get_all_urls_of_book_imgs_without_img_type(bookurl):
	php = bookurl.find('.php')
	if php > 0:
		dotidx = bookurl.find('.php')
		urltilldotphpwithslash = bookurl[:dotidx] + '/'
		return urltilldotphpwithslash
	else:
		return None

def get_imgs_of_book(bookname, numberofpages, bookurl):
	if os.path.isdir(bookname):
		print("deleting old directory... \n" + bookname)
		shutil.rmtree(bookname)
		print("deleted\n")
	os.makedirs(bookname)
	starturl = get_all_urls_of_book_imgs_without_img_type(bookurl)
	for i in range(1, numberofpages+1):
		no = '%04d'%(i) 
		prefix = 'page'
		suffixgif = '.gif'
		suffixjpg = '.jpg'
		completeurlgif = starturl + prefix + no + suffixgif
		completeurljpg = starturl + prefix + no + suffixjpg
		response = requests.get(completeurlgif, stream=True)
		foundformat = '.gif'
		if not response:
			response = requests.get(completeurljpg, stream=True)
			foundformat = '.jpg'
		# neither gif nor jpg
		if not response:
			print("missed page number " + str(i) + " of the book")
		else:
			filepathplusname = os.path.join(bookname, prefix+no+foundformat)
			with open(filepathplusname, 'wb') as outfile:
				shutil.copyfileobj(response.raw, outfile)
				print("written page number " + str(i))
			del response

def main():
	bookname, numberofpages, bookurl = '', 0, ''
	if (len(sys.argv) == 4):
		bookname = sys.argv[1]
		numberofpages = int(sys.argv[2])
		bookurl = sys.argv[3]
	else:
		print("Correct format of running this is: \npython apna-spider.py [space] bookname [space] numberofpages [space] bookurl")
		print("for example:")
		print("apna-spider.py \"Khed Muqadaran Di\" \"255\" \"http://apnaorg.com/books/shahmukhi/raja-1/book.php?fldr=book\"")
		quit()

	if is_valid_apna_url(bookurl):
		get_imgs_of_book(bookname, numberofpages, bookurl)
	else:
		print("bookurl enteres is not valid apna url")

if __name__ == '__main__':
    main()