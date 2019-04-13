
import requests
from bs4 import BeautifulSoup
base_page_url = "https://www.pro-football-reference.com/"
# soup = BeautifulSoup(html_doc, 'html.parser')
max_week = 17
start_year = 2000
last_year = 2018

curr_year = start_year
while(curr_year <= last_year):
    curr_week = 0
    while(curr_week <= max_week):
        week_url = base_page_url + "years/" + str(curr_year) + "/week_" + str(curr_week) + ".htm"
        # print(week_url)
        print("getting week", curr_week)
        weekPage = requests.get(week_url)
        print("parsing week")
        week_parser = BeautifulSoup(weekPage.text,"html.parser")
        print("Done parsing")
        gameList = week_parser.find_all("td", class_="right gamelink")
        for game in gameList:
            gameLink = game.find("a")
            game_url = base_page_url + gameLink['href']
            print(game_url)


        curr_week = curr_week + 1

    curr_year = curr_year + 1
