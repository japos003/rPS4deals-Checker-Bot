#Author: Jon Raphael Apostol
#RPS4DealsReader - A simple program that takes in data from
#the subreddit /r/PS4deals via JSON and prints out results
#from the top page

from pprint import pprint
import requests
import json
import demjson
import datetime as dt

def topsubredditresults(subreddit):
  #Returns a list of deals on the top of a subreddit page

  urlrequest = 'http://www.reddit.com/r/' + subreddit + '/.json'
  print(urlrequest)

  r = requests.get(urlrequest)
  data = r.json()

  if('error' in data.keys()):
    print("Error! Error number " +
          str(data['error']) + ": "
          + data['message'])
    print("Restarting...")
    topsubredditresults(subreddit)
  else:
    datalist = data['data']['children']

    print("Here are the top results from /r/" + subreddit)
    for entry in datalist:
      print("Title: " + entry['data']['title'] + "\n\t" +
            "URL: " + entry['data']['url'] + "\n")

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

