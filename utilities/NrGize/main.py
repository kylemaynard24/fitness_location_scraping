from Scraper import Scraper
import pandas as pd

zips = list(pd.read_csv("unique_zip_codes.csv")["Unique_Zips"])


def main():
    # 7_12_22_10:16 made through 41
    # 7_13_22 new start made through 129
    # 7_13_22 5:37AM made through 226
    # 317
    for i in range(519, len(zips)):
        print("Working on i = " + str(i) + " zip = " + str(zips[i]))
        nrgize = Scraper(zips[i])
        nrgize.process()

if __name__ == "__main__":
    main()