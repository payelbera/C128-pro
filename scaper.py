from selenium import webdriver
from bs4 import BeautifulSoup
import csv
import time
import requests
import pandas as pd

starturl = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

page = requests.get(starturl)

time.sleep(1)


def scrape():
    soup = BeautifulSoup(page.text, "html.parser")

    startable = soup.find('table')
    print(len(startable))

    templist = []

    tablerows = startable[1].find_all("tr")

    for tr in tablerows:
        td = tr.find_all("td")

        row = [i.text.rstrip()for i in td]

        templist.append(row)

    star = []
    Constellation = []
    Rightascension = []
    Declination = []
    Appmag = []
    Distance = []
    Spectraltype = []
    Browndwarf = []
    Mass = []
    Radius = []
    Orbitalperiod = []
    Semimajoraxis = []
    Ecc = []
    Discoveryyear = []

    for i in range(1, len(templist)):

        star.append(templist[i][0])
        Constellation.append(templist[i][1])
        Rightascension.append(templist[i][2])
        Declination.append(templist[i][3])
        Appmag.append(templist[i][4])
        Distance.append(templist[i][5])
        Spectraltype.append(templist[i][6])
        Browndwarf.append(templist[i][7])
        Mass.append(templist[i][8])
        Radius.append(templist[i][9])
        Orbitalperiod.append(templist[i][10])
        Semimajoraxis.append(templist[i][11])
        Ecc.append(templist[i][12])
        Discoveryyear.append(templist[i][13])

    df = pd.DataFrame(list(zip(star, Constellation, Rightascension, Declination, Appmag, Distance, Spectraltype, Browndwarf, Mass, Radius, Orbitalperiod, Semimajoraxis, Ecc, Discoveryyear)), columns=[
                      "Star", "Constellation", "Rightascension", "Declination", "App.mag.", "Distance(ly)", "Spectraltype", "Brown dwarf", "Mass(MJ)", "Radius(RJ)", "Orbitalperiod(d)", "Semimajoraxis(AU)", "Ecc.", "Discoveryyear"])

    df.to_csv("stars.csv")


scrape()
