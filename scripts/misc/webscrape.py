# Standard Library modules
import random
# from random import randint, randrange, choice, choices, shuffle, sample, random, uniform, gauss, normalvariate,  
from re import findall, search, IGNORECASE, sub
from time import sleep
from urllib.request import urlopen

# Third-party modules
from bs4 import BeautifulSoup
# also try lxml
import mechanicalsoup


def main():
    # scrape()
    # parse(html)
    # soup_test(html)
    # mechSoup_test()
    # dice_example()
    access_toolkit()


def access_toolkit():
    browser = mechanicalsoup.StatefulBrowser()
    browser.open("https://www.accesstoolkit.com/app/index.php") # uses "import requests"
    print(browser.url)
    # browser.follow_link("  ")
    # print(browser.page) # returns a Beautiful Soup object
    for input in browser.page.find_all('input'):
        print(input)

    # browser.select_form()
    # browser.form.print_summary()

    
    
    


    """ From the html file I identified the following inputs for login:
    user = '<input id="useremail" name="useremail" style="width:260px; text-align:center;" type="text"/>'
    pword = '<input id="userpass" name="userpass" style="width:260px; text-align:center;" type="password"/>'
    button = '<input id="submitbutton" style="color:#ffffff;" type="submit" value="Log in"/>'
    """


def scrape():
    url = "http://olympus.realpython.org/profiles/dionysus"
    html = scrape(url)
    page = urlopen(url) # return HTTPResponse object
    html_bytes = page.read() # read the response to a sequence of bytes
    return html_bytes.decode("utf-8") # docode the bytes to html

def parse():
    url = "http://olympus.realpython.org/profiles/dionysus"
    html = scrape(url)
    pattern = "<.*?title.*?>.*?<.*?/.*?title.*?>"
    # Parse html using string methods and/or regular expressions.
    match_results = search(pattern, html, IGNORECASE)
    title = match_results.group()
    return sub("<.*?>", "", title) # Remove HTML tags
    # elephants = sub("<.*?>", "ELEPHANTS", html)

def soup_test():
    url = "http://olympus.realpython.org/profiles/dionysus"
    html = scrape(url)
    soup = BeautifulSoup(html, "html.parser")
    soup_short = soup.get_text().replace("\n\n","\n")
    image1, image2 = soup.find_all("img")
    image_string = f"{image1["src"]}\n{image2["src"]}"
    print(image_string)
    print(soup.title.string)

def mechSoup_test():
    browser = mechanicalsoup.Browser()
    url_base = "https://www.reddit.com/r/all/"
    url_login = "/login"
    login_page = browser.get(f"{url_base}") # {url_page}
    login_html = login_page.soup
    with open("reddit.txt", "w") as f:
        f.write(str(login_html))

def zeus():
    browser = mechanicalsoup.Browser()
    url_base = "http://olympus.realpython.org/profiles/dionysus"
    login_page = browser.get(f"{url_base}") # {url_page}
    login_html = login_page.soup
    form = login_html.select("form")[0]
    form.select("input")[0]["value"] = "zeus"
    form.select("input")[1]["value"] = "ThunderDude"
    profiles_page = browser.submit(form, login_page.url)
    links = profiles_page.soup.select("a")
    for link in links:
        address = url_base + link["href"]
        text = link.text
        print(f"{text}: {address}")

def dice_example():
    browser = mechanicalsoup.Browser()
    for i in range(6):
        page = browser.get("http://olympus.realpython.org/dice")
        tag = page.soup.select("#result")[0]
        print(f"The result of your dice roll is: {tag.text}")
        if i < 5:
            sleep(random.randint(1,3)/2)


if __name__ == "__main__":
    main()