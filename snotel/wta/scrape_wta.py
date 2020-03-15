from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import time
from data_utils.mongoConnection import getMongoClient

def parse_trip_report(url):
    '''
    This function will attemnpt to parse the WTA trip report for it's title, date and text
    :param url: URL to the WTA trip report
    :return:
    '''
    client = uReq(url)
    trip_html = client.read()
    client.close()
    tripsoup = soup(trip_html,"html.parser")
    content = tripsoup.find("article", {"id": "content"})
    trip_text = content.find('p').text
    region = content.find_all('span')[1].text
    trip_title = content.find('h1').text
    date = content.find('span', {"class": "elapsed-time"})
    date_string = str(date).split('datetime=')[1].split('"')[1]
    trip_report= {'title':trip_title, 'region':region, 'trip_report':trip_text, 'date':date_string }
    return trip_report

def get_page_soup(page_url):
    client = uReq(page_url)
    page_html = client.read()
    client.close()
    page_soup = soup(page_html,"html.parser")
    return page_soup

def scrape_trip_reports():
    number_of_reports_processed = 0
    client = getMongoClient()
    trip_reports_db = client['TripReports']
    reports_collection = trip_reports_db['reports_collection']
    for page_number in range(3):
        url = 'https://www.wta.org/@@search_tripreport_listing?b_size=100&amp;b_start:int=%d&amp;_=1584045459199"' % int(
            100 * page_number)
        report_dictionaries = []
        try:
            page_soup = get_page_soup(url)
            reports = page_soup.find_all("a", {"class": "listitem-title"})
            page_trip_report_urls = []
            for report in reports:
                report_url = str(report).split('href=')[1].split('"')[1]
                page_trip_report_urls.append(report_url)
                report_dict = parse_trip_report(report_url)
                return report_dict
                # report_dictionaries.append(report_dict)
                # number_of_reports_processed += 1

        except Exception as e:
            print("We have a problem with the url at")
        reports_collection.insert_many(report_dictionaries)


report_dict = scrape_trip_reports()