from __future__ import print_function
import mechanicalsoup
import argparse
from getpass import getpass

#setting up the username and password for moodle
parser = argparse.ArgumentParser(description="login to moodle.")
parser.add_argument("username")
args = parser.parse_args()

#password prompt
args.password = getpass("please enter my concordia password:")

browser = mechanicalsoup.StatefulBrowser()

#login interactions with page
browser.open("https://moodle.concordia.ca/moodle/login/index.php")
browser.select_form("#login form")
browser["login"] = args.username
browser["password"]
resp = browser.submit_selected()
#test to launch browser to see if it worked
browser.launch_browser()
