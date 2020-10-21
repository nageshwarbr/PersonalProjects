import time

from plyer import notification
import requests
from bs4 import BeautifulSoup
from itertools import islice


def notifyMe(title, message):
    notification.notify(title=title, message=message, app_icon=r"C:\Users\nageshwar\Downloads\icon.ico", timeout=10)


def getdata(url):
    r = requests.get(url)
    return r.text


if __name__ == '__main__':
    # notifyMe("Vishal", "this is a laptop")
    my_html_data = getdata("https://www.deccanherald.com/national/coronavirus-india-update-state-wise-total-number-of-confirmed-cases-deaths-on-august-1-868234.html")
    soup = BeautifulSoup(my_html_data, 'html.parser')

    # my_data_str=''
    # for tr in soup.find('table').find_all('tr'):
    #     print(tr)
        # my_data_str+=tr.get_text()
        # print(my_data_str.split('\n'))

state_table = soup.find("table")
state_table_data = state_table.find_all("tr")  # contains 35 rows
# print(state_table_data)
# print(state_table)

# Get all the headings of Lists
headings = ['State/Union Territory','Positive cases','Deaths']
for td in state_table.find_all("td"):
    # print(td.get_text())
    # remove any newlines and extra spaces from left and right
    headings.append(td.get_text())
#
# print(zip(*[headings[i::] for i in range(3)]))
states=['Assam','Goa','Ladakh']
x=[headings[i:i + 3] for i in range(0, len(headings), 3)]
# print(*x ,sep="\n" )
y=list(filter(lambda x:x[0] in states,x))
#
print(y)
print(*y ,sep="\n" )
for y in y:

    ntitle = 'cases of Covid'
    ntext = f"State : {y[0]}\nPositive cases : {y[1]} \nDeaths : {y[2]}"
    notifyMe(ntitle, ntext)
    time.sleep(3)







