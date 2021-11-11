from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
import io
import csv
import requests


def responseCode(path):
 r = requests.head(path)
 return r.status_code



print("Please choose the subreddit to be scraped. \n Ensure your VPN is activated before continuing. \n")
print("r/")
subreddit = input()


url = "https://old.reddit.com/r/"
while(responseCode(url+subreddit+"/new")==request.codes.ok):
 print("Invalid subreddit!\n")
 print("r/")
 subreddit = input()


path = "r/"+subdreddit
os.mkdir(path)




index_file = file("index","w")



driver = webdriver.Firefox()

if(responseCode(url+subreddit+"/new")==request.codes.ok):
 driver.get("old.reddit.com/"+path+"/new")
else:
 print("Unable to access subreddit!")
 input()

# Title,tags,time,url
index = 0

while(responseCode("old.reddit.com/"+path+"/new")==request.codes.ok):
 with open("page_"+index+".csv",'w',newline='') as csvfile:
  page = csv.writer(csvfile, delimiter=",")
  page.writerow(["id"+"title"+"flair"+"time"+"url"])
  elements = driver.find_element_by_class_name("entry")
  for elm in elements:
   title = elm.text_by_class_name("title").text
   link = title.get_attribute("href")
   flair = elm.find_element_by_class_name("linkflairlabel").text
   time = elm.find_element_by_css_selector("time").get_attribute("datetime")
   page.writerow([count,title,link,flair,])
   count+=1
   page = file("response"+index,"a")
   index+=1
   index_file = file.write(index)
   driver.find_element_by_link_text("Next >")
     

#
#	driver.switch_to.frame(driver.find_element_by_xpath("/html/frameset/frameset/frame[2]"))
#loginelement = driver.find_element(By.ID, 'td')
#driver.execute_script("arguments[0].click();", loginelement)
#

	






