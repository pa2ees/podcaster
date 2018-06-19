from bs4 import BeautifulSoup
import requests

def get_talk_data(url = "https://www.lds.org/general-conference/2018/04/am-i-a-child-of-god?lang=eng"):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "lxml")
    t = soup.find('h1', class_='title')
    title = t.text
    subtitle = soup.find(class_='title printTitle').text
    author = soup.find(class_='article-author__name').text
    link = soup.find('a', text='MP3').get('href')
    description = soup.find(class_='kicker').text

    print("Title: {}\nSubtitle: {}\nAuthor: {}\nDescription: {}\nLink: {}".format(title,
                                                                                  subtitle,
                                                                                  author,
                                                                                  description,
                                                                                  link))
