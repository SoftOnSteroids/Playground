import argparse
import re
import requests
from bs4 import BeautifulSoup

def scrape(m_url=None):
    """
    Scrapes a webpage and writes the contents to a file.

    Parameters:
        m_url (str): The URL of the webpage to scrape. If not provided, the user will be prompted to enter a URL.

    Returns:
        None
    """
    p = re.compile("^https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$")
    while not m_url or not p.search(m_url):
        if m_url: print("Invalid URL")
        if m_url and m_url == "exit" or m_url == "quit": return
        m_url = input("Rosario3 url: ")
    
    response = requests.get(m_url)
    soup = BeautifulSoup(response.content, "html.parser")

    try:
        filename = "rosario3.md"
        title = soup.title.string.strip().split("|")[0].strip()
        article_date = soup.find("time", attrs={"class":"alt-font uppercase"}).decode_contents()
        line = f"[{title}]({m_url}) {article_date}"
    except:
        print("Could not get the contents of the target page.")
        return scrape("")
    # Write contents to file
    with open(filename, "a+") as file:
        file.write(f"* {line}\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scrape a Rosario3 article creating a markdown file with title, url and date.")
    parser.add_argument("-u", "--url", type=str, help="Rosario3 URL")
    args = parser.parse_args()

    scrape(args.url, unique_filename=args.unique_filename)