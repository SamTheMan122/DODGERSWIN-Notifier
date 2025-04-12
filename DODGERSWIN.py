'''
DODGERSWIN Panda Express Tracker
Contributors: Samuel Barcarse @ SamTheMan122
'''

'''
This program scrapes the MLB Dodgers Schedule site to determine if the Los Angeles Dodgers won at home the day before.
If so, the promo code, DODGERSWIN, can be used at checkout to get a $6 Panda Express plate.
Thanks for using the program and enjoy your cheap plate!
'''

'''
FOR THOSE RUNNING THE ATTATCHED PYTHON SCRIPT

When running script, make sure to install the required package: 
py -m pip install selenium
py -m pip install webdriver-manager
'''

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from datetime import date
import time
import smtplib
from email.mime.text import MIMEText
import sys

def sendText(message, number, carrier):
    carrierEmailEnd = {
        # Major Carriers
        "VERIZON": "vtext.com",
        "ATT": "txt.att.net",
        "T-MOBILE": "tmomail.net",
        "SPRINT": "messaging.sprintpcs.com",

        # Verizon MVNOs
        "VISIBLE": "vtext.com",
        "XFINITY MOBILE": "vtext.com",
        "SPECTRUM MOBILE": "vtext.com",
        "PAGE PLUS": "vtext.com",
        "STRAIGHT TALK VERIZON": "vtext.com",
        "TOTAL WIRELESS": "vtext.com",
        "TRACFONE VERIZON": "vtext.com",

        # AT&T MVNOs
        "CRICKET": "txt.att.net",
        "H2O WIRELESS": "txt.att.net",
        "FREEUP MOBILE": "txt.att.net",
        "STRAIGHT TALK ATT": "txt.att.net",
        "NET10 ATT": "txt.att.net",
        "RED POCKET ATT": "txt.att.net",

        # T-Mobile MVNOs
        "METROPCS": "tmomail.net",
        "MINT MOBILE": "tmomail.net",
        "ULTRA MOBILE": "tmomail.net",
        "TING T-MOBILE": "tmomail.net",
        "TALKATONE": "tmomail.net",
        "TRACFONE T-MOBILE": "tmomail.net",
        "NET10 T-MOBILE": "tmomail.net",
        "RED POCKET T-MOBILE": "tmomail.net",

        # Sprint MVNOs (Legacy)
        "BOOST MOBILE": "sms.myboostmobile.com",
        "VIRGIN MOBILE": "vmobl.com",
        "FREEDOMPOP": "messaging.sprintpcs.com",  # historically Sprint
        "TEXTNOW": "messaging.sprintpcs.com",  # legacy Sprint-based

        # Google Fi (special)
        "GOOGLE FI": "msg.fi.google.com",
    }

    to_number = number + "@" + carrierEmailEnd[carrier.upper()]  # Use carrier-specific gateway
    subject = str(date.today().strftime("%m/%d/%y"))
    body = message

    # Dodgers Panda Express Tracker Email Account
    gmail_user = "dodgerspandatracker@gmail.com"
    gmail_password = "pfpu fnva onpb fruh"  # Use an App Password if 2FA is on

    # Message
    msg = MIMEText(body)
    msg["From"] = gmail_user
    msg["To"] = to_number
    msg["Subject"] = subject

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(gmail_user, gmail_password)
        server.sendmail(gmail_user, to_number, msg.as_string())
        server.quit()
        print("Text message sent!")
    except Exception as e:
        print(f"Failed to send message: {e}")

def determinePreviousDayWin():
    # Code is only valid the day after a dodgers win, which would be today's date
    dateToday = str(date.today())

    # URL for Dodgers schedule based on month/year
    url = "https://www.mlb.com/dodgers/schedule/" + dateToday[0:7]

    try:
        # Set up headless Chrome browser
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument('--disable-gpu')
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

        # Load the page
        driver.get(url)
        time.sleep(5)  # Wait for JS to render

        # Get fully rendered HTML
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")

        # Used inspect element on url to determine what class is needed to extract data from
        target_classes = [
            "date-cell",
            "has-hidden-game",
            "tracking-game-data",
            "regular-season",
            "past",
            "home"
        ]

        # Uses BeautifulSoup library to extract and parse in HTML. Looks for the target classes that contain the data cell
        calendarCell = soup.find_all("td", class_=lambda c: c and all(cls in c for cls in target_classes))
        day, win = "", ""

        # Loops through all table cells in game
        for cell in calendarCell:
            # Extract the necessary data (day and win) from each game element
            day = cell.find("div", class_="day-of-month-label").text
            win = cell.find("span", class_="outcome").text[0]     # Extracting the win yields "W,", so we remove the comma by indexing

        # Determines eligibility of promo code
        if (int(day) + 1 == int(dateToday[8:10])) and win.upper() == "W":
            message = "The Los Angeles Dodgers won at home yesterday! Use promo code 'DODGERSWIN' for a $6 2 entree plate at Panda Express"
            # phoneNumber = input("Enter phone number in the format xxxxxxxxxx: ")
            # carrier = input("Enter carrier: ")
            phoneNumber = sys.argv[1]
            carrier = sys.argv[2]
            sendText(message, phoneNumber, carrier)
        else:
            print("Cannot use code 'DODGERSWIN' at checkout today")

    except Exception as e:
        print(f"An error occurred: {e}. Please contact support by email ")

def main():
    determinePreviousDayWin()

main()



