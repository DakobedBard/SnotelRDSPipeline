from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import datetime
from snotel.wta.sql_queries import trip_report_table_insert
import psycopg2
url = 'https://www.wta.org/@@search_tripreport_listing?b_size=100&amp;b_start:int=%d&amp;_=1584045459199"' % int(0)
report_dictionaries = []
def get_page_soup(page_url):
    client = uReq(page_url)
    page_html = client.read()
    client.close()
    page_soup = soup(page_html,"html.parser")
    return page_soup
def scrape_trip_report(trip_report_url):
    client = uReq(trip_report_url)
    trip_report_html = client.read()
    client.close()
    tripsoup = soup(trip_report_html,"html.parser")
    content = tripsoup.find("article", {"id": "content"})
    trip_text = content.find('p').text
    region = content.find_all('span')[1].text
    trip_title = content.find('h1').text
    date = content.find('span', {"class": "elapsed-time"})
    date_string = str(date).split('datetime=')[1].split('"')[1]
    trip_report= {'title':trip_title, 'region':region, 'trip_report':trip_text, 'date':date_string }
    return trip_report

def insert_trip_report(conn,trip_report):
    cur = conn.cursor()
    cur.execute(trip_report_table_insert,(trip_report['title'], trip_report['trip_report'], 2300, 45.3, ['location1', 'location2'], datetime.datetime.now() ))
    conn.commit()

page_soup = get_page_soup(url)
date_string = page_soup.find('p').text
date_element = page_soup.find('span', {"class": "elapsed-time"})
date_string = str(date_element).split('title="')[1].split('"')[0]

reports = page_soup.find_all("a", {"class": "listitem-title"})
page_trip_report_urls = []
for report in reports:
     report_url = str(report).split('href=')[1].split('"')[1]
page_trip_report_urls.append(report_url)
trip_report_url =  page_trip_report_urls[0]
trip_report = scrape_trip_report(trip_report_url)

conn = psycopg2.connect(
    "host=kaladin-db.cju35raiyeyw.us-west-2.rds.amazonaws.com dbname=kaladindb user=postgres password=tchoob89")

tripReport = insert_trip_report(conn, trip_report)
# tripsoup = soup(trip_html, "html.parser")
# content = tripsoup.find("article", {"id": "content"})

# region = content.find_all('span')[1].text
# trip_title = content.find('h1').text

# trip_report = {'title': trip_title, 'region': region, 'trip_report': trip_text, 'date': date_string}

# report_dictionaries.append(report_dict)
# number_of_reports_processed += 1
