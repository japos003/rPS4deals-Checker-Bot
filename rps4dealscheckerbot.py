#Author: Jon Raphael Apostol
#RPS4DealsReader - A simple program that takes in data from
#the subreddit /r/PS4deals via JSON and prints out results
#from the top page

from pprint import pprint
import requests
import json
import demjson
import datetime as dt
import time

def topsubredditresults(subreddit):
  #Returns a list of deals on the top of a subreddit page

  urlrequest = 'http://www.reddit.com/r/' + subreddit + '/.json'
  confirm_input = ''

  req = requests.get(urlrequest)
  data = req.json()

  if('error' in data.keys()):
    print("Error! Error number " +
          str(data['error']) + ": "
          + data['message'])
    while(dialogue_loop(confirm_input)):
      confirm_input = input("Continue? ")
      if(confirm_input.lower() == 'yes' or confirm_input.lower() == 'y'):
        print("Restarting...")
        time.sleep(30)
        topsubredditresults(subreddit)
      elif(confirm_input.lower() == 'no' or confirm_input.lower() == 'n'):
         print("Ending program...")
      else:
         print("Incorrect key...")
         continue
  else:
    datalist = data['data']['children']

    print("Here are the top results from /r/" + subreddit)
    for entry in datalist:
      print("Title: " + entry['data']['title'] + "\n\t" +
            "URL: " + entry['data']['url'] + "\n")

def dialogue_loop(statement):
  if(statement.lower() == 'no' or statement.lower() == 'n'):
    return False
  return True

def ps4deals():
  topsubredditresults("ps4deals")

def currDate():
  #Returns the current date in string
  today = dt.date.today()
  return str(today.strftime('%m/%d/%Y'))

def main():
    print("Today is " + currDate())
    ps4deals()

main()

