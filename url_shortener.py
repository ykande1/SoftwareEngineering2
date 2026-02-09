#Charles Cain, 2.9.26
#URL Shortener

import csv

#this should be a relative path:
url_file_path = "urls.csv"

def shorten_url(url):
    return 0

def create_entry(url, short_url, id):
    return [url, short_url, id]

def write_csv(data, file_path):
    with open(file_path) as
    return -1

def read_csv(file_path):
    return -1

def init():
    #start program, prompt user for urls
    print("/-------------\\")
    print("|URL Shortener|")
    print("\-------------/")

    while(True):
        url_input = input("Enter a URL to shorten:\n")

        #begin shortening process
        current_file = open(url_file_path)

        current_file.close()
        shortened_url = shorten_url(url_input)

        #create_json()

if __name__ ==  "__main__":
    init()