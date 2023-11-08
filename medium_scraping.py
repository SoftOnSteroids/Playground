import argparse
import os
import re
import requests
import webbrowser
from bs4 import BeautifulSoup

def scrape(m_url=None, unique_filename=False):
    """
    Scrapes the content of a Medium article given its URL and saves it to a file.

    Args:
        url (str, optional): The URL of the Medium article to scrape. If not provided, the function will prompt the user for the URL. Defaults to None.
        unique_filename (bool, optional): Whether to generate a unique filename based on the article's title. If True, the filename will be sanitized and formatted. If False, the filename will be set to "medium.html". Defaults to False.

    Returns:
        None

    Version:
        1.0.0
    """
    p = re.compile("^https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$")
    while not m_url or not p.search(m_url):
        if m_url: print("Invalid URL")
        if m_url and m_url == "exit" or m_url == "quit": return
        m_url = input("Medium url: ")
    
    cache_url = "https://webcache.googleusercontent.com/search?q=cache:"
    website = cache_url + m_url
    response = requests.get(website)
    soup = BeautifulSoup(response.content, "html.parser")

    try:
        # Remove script tags
        for s in soup.select("script"):
            s.extract()
        
        # Generate filename
        if unique_filename:
            title = soup.title.string.strip().split("|")[0].strip()
            filename = "".join(char for char in title if char.isalnum() or char.isspace())
            print(filename)
            filename = filename.replace(" ", "_") + ".html"
        else:
            filename = "medium.html"
    
        # Get the contents of the target div
        div = soup.find("div", attrs={"style": "position:relative;"}).decode_contents()
        div = BeautifulSoup(div, "html.parser").prettify()
    except:
        print("Could not get the contents of the target page.")
        return scrape("", unique_filename)
    # Write contents to file
    with open(filename, "a+") as file:
        file.truncate(0)
        file.write(div)

    # Open the file in the default web browser
    file_url = "file:///" + os.path.abspath(filename)
    webbrowser.open(file_url)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scrape a Medium article and save the HTML content to a file.")
    parser.add_argument("-u", "--url", type=str, help="Medium URL")
    parser.add_argument("-f", "--unique_filename", action="store_true", default=False, help="Generate a unique filename based on the article title")
    args = parser.parse_args()

    scrape(args.url, unique_filename=args.unique_filename)