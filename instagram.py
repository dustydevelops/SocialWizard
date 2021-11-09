

username = 'joeshmo'           # the username the bot will use to log in.
password = 'youllneverguess'   # the password the bot will use to log in.

from selenium import webdriver      # from selenium import webdriver for web browser automation.
from time import  sleep             # import sleep from time for creating time delays.

url = 'http://www.instagram.com/'   #I nstagrams url
loggedIn = url + 'accounts/login/'  # Instagrams login url
profile = url + username          # Your profile


dr = webdriver.Safari() #   initialize the safari window
dr.get(loggedIn)        #    Go to login page 
sleep(3)                #    Give the page a chance to load
                          
element = dr.find_element_by_xpath("//input[@name='username']")
element.send_keys(username) #    Enter username
element = dr.find_element_by_xpath("//input[@name='password']")
element.send_keys(password) #   Enter password 

xPath1 = '//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button'
login_button = dr.find_element_by_xpath(xPath1) 
login_button.click() # click the login button

sleep(60)            #    Log out 60 seconds after the script is done
dr.close()           #    close window



