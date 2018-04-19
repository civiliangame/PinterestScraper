#Import necessary libraries
from bs4 import BeautifulSoup
import requests
import re
from urllib.request import urlretrieve
import urllib.parse
import urllib
from selenium import *
from selenium import webdriver
import pickle
import os.path
import os


#Creates a class that contains the scraping essentials
class ScrapingEssentials(object):

    #Necessaary Class Variables
    currentItem = 0
    number = 0
    categories = []
    #Initializing a directory for the pictures to come in
    def __init__(self, source):
        ScrapingEssentials.number = 0
        self.source = source
        file_path_string = "/sxh779/Crawler/" + source
        if not os.path.exists(file_path_string):
            os.makedirs(file_path_string)
    # Needed to make a class to have a static way of counting
    def reset(self):
        ScrapingEssentials.number = 0
        ScrapingEssentials.currentItem += 1
    #Convert the file from a url to an actual image file and store it on the commputer
    def download_image(self, link):
        try:
            done = False
            print("processing file: " + str(ScrapingEssentials.number))
            #Make a requests object
            #Make a folder name
            folder_name = ScrapingEssentials.categories[ScrapingEssentials.currentItem]
            print(link)
            r2 = requests.get(link)
            #Make the directory of the folder
            file_path_string = "/sxh779/Crawler/" + self.source + "/" + folder_name
            file_path = os.path.join(file_path_string, (str(ScrapingEssentials.number) + ".jpg"))

            if not os.path.exists(file_path_string):
                os.makedirs(file_path_string)
            #Download it on the computer
            print(file_path + "  " + link)
            ScrapingEssentials.number += 1

            urlretrieve(link, file_path)

            done = True
        except Exception:
            pass


    def open_pickle(self):
        keywords = []
        # with open("category_python3.pkl", "rb") as f:
        #     data = pickle.load(f)
        #     for key in data.keys():
        #         for value in data[key]:
        #             keywords.append(value.split("_")[0])
        # ScrapingEssentials.list = keywords
        return ScrapingEssentials.categories

    def english_pickle(self):
        ScrapingEssentials.categories = [
            "Starcraft", "Overwatch", "Terran", "Zerg", "Protoss"
        ]
        return ScrapingEssentials.categories