from this import s
from Scraper import Scraper

def main():

    states = [ 'AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA',
           'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY', 'LA', 'MA', 'MD', 'ME',
           'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM',
           'NV', 'NY', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX',
           'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY']

    # states = ["FL", "CA", "WI", "WA", "KY"]

    # states = ["FL", "CA"]

    for state in states:
        try:
            searchScraper = Scraper(state)
            # searchScraper.test_next_button()
            searchScraper.process()
        except:
            print("there was an error")
            print("no results found")        

if __name__ == "__main__":
    main()