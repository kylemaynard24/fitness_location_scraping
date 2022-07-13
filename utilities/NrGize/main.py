from Scraper import Scraper
import pandas as pd

# zips = list(pd.read_csv("unique_zip_codes.csv")["Unique_Zips"])

zips = list(pd.read_csv("florida_zips.csv")["florida_zips"])

def get_unfound(found, all_zips):
    unfound = []
    for zip in all_zips:
        if zip in found:
            continue
        else:
            unfound.append(zip)
    return unfound

def main():
    found = []
    unfound = get_unfound(found, zips)
    while len(unfound) != 0:
        try:
            for i in range(0, len(unfound)):
                print("Working on i = " + str(i) + " zip = " + str(unfound[i]))
                nrgize = Scraper(unfound[i])
                nrgize.process()
                found.append(unfound[i])
        except:
            # on failure, reset new unfound list, keep iterating through until unfound == 0
            unfound = get_unfound(found, unfound)

if __name__ == "__main__":
    main()