from bs4 import BeautifulSoup, NavigableString
from requests import get
import re

""" <----------------- GET MAIN PAGE DATA ----------------> """

rawData = get('https://nosalive.com/')

soupData = BeautifulSoup(rawData.text, 'html.parser')

dayActionTags = soupData.findAll('a', class_='wvc-column-link-mask')

dayURLs = list()

urlRegex = re.compile(r'https://nosalive.com/[a-zA-Z]+-dia/', re.IGNORECASE)

for action in dayActionTags:
    if re.match(urlRegex, action['href']) is not None:
        dayURLs.append(action['href'])


""" <----------------- GET DATA FROM EACH URL ----------------> """

confirmationsByDay = dict()

stageRegex = re.compile(r'^\s*[a-zA-Z]+', re.IGNORECASE)

for dayUrl in dayURLs:

    confirmationsByStage = dict()

    rawData = get(dayUrl)

    soupData = BeautifulSoup(rawData.text, 'html.parser')

    day = soupData.find('div', class_='datetitle').findNext('h1').contents[0]

    artistDivs = soupData.findAll('div', class_='port-captions')

    stageName, artistName = ' ', ' '

    for div in artistDivs:

        if not div.findNext('h4').contents:
            continue

        artistName = div.findNext('h4').contents[0]

        for content in div.findNext('p').contents:
            if isinstance(content, NavigableString) and re.match(stageRegex, content.string) is not None:
                print(content.string)
                stageName = content.string

        if stageName not in confirmationsByStage:
            confirmationsByStage[stageName] = list([artistName])
        else:
            confirmationsByStage[stageName].append(artistName)

    confirmationsByDay[day] = confirmationsByStage
