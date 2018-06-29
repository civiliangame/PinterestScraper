# Import necessary libraries
from bs4 import BeautifulSoup
import time
from selenium import webdriver
from selenium.webdriver.support import ui
from EnglishScraper import ScrapingEssentials
import threading

t = ScrapingEssentials("Pinterest")


# Determines if the page is loaded yet.
def page_is_loaded(driver):
    return driver.find_element_by_tag_name("body") != None


# Logs in to Pinterest.com to access the content
def login(driver, username, password):
    if driver.current_url != "https://www.pinterest.com/login/?referrer=home_page":
        driver.get("https://www.pinterest.com/login/?referrer=home_page")
    wait = ui.WebDriverWait(driver, 10)
    wait.until(page_is_loaded)
    email = driver.find_element_by_xpath("//input[@type='email']")
    password = driver.find_element_by_xpath("//input[@type='password']")
    email.send_keys("sxh779@case.edu")
    password.send_keys("multithreading")
    # driver.find_element_by_xpath("//div[@data-reactid='30']").click()
    password.submit()
    time.sleep(3)
    print("Teleport Successful!")


# Search for the product, this is the way to change pages later.
def search_for_product(driver, keyword):
    seeker = driver.find_element_by_xpath("//input[@placeholder='Search']")
    seeker.send_keys(keyword)
    seeker.submit()


# Finds the detailed product page of each "pin" for pinterest
def download_pages(driver, valid_urls):
    list_counter = 0

    # Pinterest happens to change its HTML every once in a while to prevent botting.

    # This should account for all the differences
    # soup = BeautifulSoup(driver.page_source, "lxml")
    # for pinWrapper in soup.find_all("div", {"class": "pinWrapper"}):
    #     class_name = pinWrapper.get("class")
    #     print(class_name)
    #     if "_o" in class_name[0]:
    #         print(class_name)
    #         break
    #
    # #Finds the tags of the HTML and adjusts it
    # name = " ".join(class_name)
    # print(name)

    # Does this until you have 10000 items or the program has gone on for long enough, meaning that it reached the end of results
    beginning = time.time()
    end = time.time()
    while list_counter < 10000 and beginning - end < 30:
        beginning = time.time()
        # ----------------------------------EDIT THE CODE BELOW------------------------------#
        # Locate all the urls of the detailed pins
        soup = BeautifulSoup(driver.page_source, "html.parser")
        # for c in soup.find_all("div", {"class": name}):
        for pinLink in soup.find_all("div", {"class": "pinWrapper"}):
            for a in pinLink.find_all("a"):
                print(pinLink)
                url = ("https://pinterest.com" + str(a.get("href")))
                print(url)
                # Checks and makes sure that the pin isn't there already and that random urls are not invited
                if len(url) < 60 and url not in valid_urls and "A" not in url:
                    # ---------------------------------EDIT THE CODE ABOVE-------------------------------#
                    valid_urls.append(url)
                    print("found the detailed page of: " + str(list_counter))
                    list_counter += 1
                    end = time.time()
                time.sleep(.15)
                # Scroll down now
        driver.execute_script("window.scrollBy(0,300)")
    return


# Downloads the image files from the img urls
def get_pic(valid_urls, driver):
    print("hey")
    get_pic_counter = 0
    time.sleep(5)
    while (get_pic_counter < len(valid_urls)):
        print(0)
        # Now, we can just type in the URL and pinterest will not block us
        for urls in valid_urls:
            driver.get(urls)

            # Wait until the page is loaded
            if driver.current_url == urls:
                wait = ui.WebDriverWait(driver, 10)
                wait.until(page_is_loaded)
                loaded = True
            print(1)
            # -----------------------------------EDIT THE CODE BELOW IF PINTEREST CHANGES---------------------------#
            # Extract the image url
            soup = BeautifulSoup(driver.page_source, "html.parser")
            print(2)
            for mainContainer in soup.find_all("div", {"class": "mainContainer"}):
                print(3)
                for closeupContainer in mainContainer.find_all("div", {"class": "closeupContainer"}):
                    print(4)
                    # for heightContainer in closeupContainer.find_all("div", {"class": "FlashlightEnabledImage Module"}):
                    print(5)
                    for img in closeupContainer.find_all("img"):
                        print(6)
                        print("hello")
                        img_link = img.get("src")
                        if "564" in img_link:
                            print("found the img url of: " + str(get_pic_counter))
                            get_pic_counter += 1
                            t.download_image(img_link)
                            break

            # ---------------------------------EDIT THE CODE ABOVE IF PINTEREST CHANGES-----------------------------#


def main():
    global t
    list = t.english_pickle()
    print(list)
    driver1 = webdriver.Chrome()
    driver2 = webdriver.Chrome()
    driver1.get("https://www.pinterest.com/login/?referrer=home_page")
    driver2.get("https://www.pinterest.com/login/?referrer=home_page")
    # Log in to Pinterest.com

    login(driver1, "", "")
    login(driver2, "", "")
    # Make sure it's loaded before doing anything

    loaded = False
    while loaded == False:
        if driver1.current_url != "https://www.pinterest.com/login/?referrer=home_page":
            loaded = True

    for item in list:
        print("start")
        keyword = item
        valid_urls = []
        print(keyword)
        driver1.get("https://pinterest.com/search/pins/?q=" + str(keyword) + "&rs=typed&term_meta[]=" + str(
            keyword) + "%7Ctyped")

        time.sleep(3)
        t1 = threading.Thread(target=download_pages, args=(driver1, valid_urls,))
        t1.setDaemon(True)
        t1.start()

        t2 = threading.Thread(target=get_pic, args=(valid_urls, driver2,))
        t2.setDaemon(True)
        t2.start()
        #
        t1.join()
        # t2.join()

        t.reset()
        print("done")


if __name__ == "__main__":
    main()

else:
    main()
# while loaded:
#     driver.execute_script("window.scrollBy(0,250)")
