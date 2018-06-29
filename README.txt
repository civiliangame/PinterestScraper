This project is a web crawler/scraper for Pinterest. 
Pinterest has one of the internet's largest image databases. 
All sorts of people post their useless images here.
Useless as they may be individually, they have potential to be significant together.
For instance, let's say that you're making a general object detector with machine learning.
How will you teach it to recognize things?

You'll most likely require a huge image database for your machine to train upon.
This project provides that database. 

You can search for ANY keyword, and the program will download ALL images pinterest has on that subject. 

My project will be using the following libraries: 
BeautifulSoup (for parsing HTML)
time (to time out the project if it hits no more results)
selenium (to retreive the webdriver)
urlretrieve (to download the image file from a url)
OS (for I/O operations) 
threads (for multithreading) 

This is the gist of how it works: 
1. Two Selenium webdrivers are created. For the sake of simplicity and transparency, we will use Chrome.
2. Both will log onto Pinterest with a bogus account that I created just for this purpose. 
3. Here is where threading comes in. One window will search the keyword in Pinterest by messing around with the URL,
	while the other waits.
4. The first one will now go through the page and scrape all the URLs embedded in the source code that 
	leads to a detailed page of the picture. This is because the high-resolution pictures are only
	in the detailed page, while the original search page only has the thumbnails. 
5. The first webdriver will then place the links into a list that the other thread can access. 
	It's basically a producer/consumer structure. I designed it this way for maximum efficiency and convenience,
	as if you just use one driver it will have to constantly go back and forward in the page.
6. After the first webdriver found everything in the page, it will keep attempting to scroll down. 
	This is because Pinterest has an infinite-scroll structure, meaning that additional source code for the page 
	will only load after the "scroll down and load" command is given. The first webdriver will keep doing this until 
	it has found 10000 pictures or cannot scroll any more, whichever comes first. 
7. The second webdriver will take the URLS given by the first webdriver and go into each page. There, it will find the 
	high-resolution image src file for each page and download it into a directory. If the directory is not made, it will make it first. 
	The second webdriver will keep going until every single image has been downloaded. 

To run it, make sure you have Python on your computer first.
Then, make sure to run the PintrestScraper file from that directory. It will NOT work without chromedriver.exe and EnglishScraper.py in the same directory. 
Just click run. No input parameters needed. 
If you want to change what kind of images you want to download, go to EnglishScraper.py and change the categories variable in the last three lines in the code.
Enjoy, and don't do illegal stuff with it. This is for educational purposes only. In other words, please don't call the FBI on me. 
