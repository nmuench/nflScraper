
import requests
from bs4 import BeautifulSoup
from bs4 import Comment
import re
base_page_url = "https://www.pro-football-reference.com"
# soup = BeautifulSoup(html_doc, 'html.parser')
max_week = 1
start_week = 1
start_year = 2000
last_year = 2000

curr_year = start_year
#Cycles over every year within the given window and pulls down the play by play
#of every game played in that year in the desired weeks.
while(curr_year <= last_year):
    curr_week = start_week
    while(curr_week <= max_week):
        week_url = base_page_url + "/years/" + str(curr_year) + "/week_" + str(curr_week) + ".htm"
        # print(week_url)
        print("getting week", curr_week)
        weekPage = requests.get(week_url)
        print("parsing week")
        week_parser = BeautifulSoup(weekPage.text,"html.parser")
        print("Done parsing week")
        gameList = week_parser.find_all("td", class_="right gamelink")
        #Cycles over every game that happened in a given week and gets the
        #play by play information for that game along with other desired information.
        for game in gameList:
            gameLink = game.find("a")
            print("getting game")
            game_url = base_page_url + gameLink['href']
            game_page = requests.get(game_url)
            print("Parsing game", game_url)
            game_parser = BeautifulSoup(game_page.text, "html.parser")
            print("Done parsing game")
            game_plays = game_parser.find("div", id="all_pbp")
            comment = game_plays.find(string=lambda text: isinstance(text, Comment))
            comment_parser = BeautifulSoup(comment, "html.parser")
            game_play_description = comment_parser.find_all("td", {"data-stat" : "detail"})
            num_plays = len(game_play_description)
            num_passes = 0
            num_runs = 0
            num_sack = 0
            num_punts = 0
            num_kicks = 0
            for play in game_play_description:
                if(re.search("pass", play.text) and not re.search("[Nn]o play", play.text)):
                    num_passes += 1

            print(num_passes)

        curr_week = curr_week + 1

    curr_year = curr_year + 1
