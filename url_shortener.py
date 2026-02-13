#Charles Cain, 2.9.26
#URL Shortener

import csv
import random
import pandas

#this should be a relative path:
url_file_path = "urls.csv"

# Generate random shortened url
def shorten_url(url: str):
    prefix = "https://shortlink.com/"
    path: str = str(random.randint(0, 100000000000))
    
    return prefix + path

def create_entry(url, short_url):
    #returns a dictionary
    return {url : short_url}

def write_csv(dict, file_path):
    #this overwrites the entire file each time:
    new_entry_string = ''

    f = open(file_path, 'w')
    w = csv.DictWriter(f, dict.keys())
    w.writeheader()
    w.writerow(dict)
    f.close()
    return 1

def read_csv(file_path):
    #read in file
    try:
        input_file = csv.DictReader(open(file_path))
        #use pandas to read csv (uses , and newlines)
        reader = csv.reader(open(file_path, 'r'))
        dict_all_urls = pandas.read_csv(file_path, header=None, index_col=0).to_dict()

    except:
        print('csv file empty.')
        dict_all_urls = { }

    return dict_all_urls

def init():
    #start program, prompt user for urls
    print("/-------------\\")
    print("|URL Shortener|")
    print("\-------------/")

    current_dict = read_csv(url_file_path)

    while(True):
        url_input = input("Enter a URL to shorten:\n")
        #begin shortening process
        shortened_url = shorten_url(url_input)

        test_dict = create_entry(url_input, shortened_url)

        current_dict.update(test_dict)

        write_csv(current_dict, url_file_path)

        print('Done! Your shortened URL is: ' + current_dict.get(url_input))

if __name__ ==  "__main__":
    init()