
###############################################################################################
#                                        SOCIAL WIZARD
###############################################################################################
email = 'joeshmo@gmail.com'
phone = '() - '
username = 'joshmo'           # the username the bot will use to log in.
password = 'youllneverguesthis'   # the password the bot will use to log in.

###############################################################################################
############## just input your details above and then run. the rest of this doesnt matter######
###############################################################################################

from selenium import webdriver      # from selenium import webdriver for web browser automation.
from time import  sleep             # import sleep from time for creating time delays.

url = 'http://www.facebook.com/'   #I nstagrams url
loggedIn = url + 'login/'  # Instagrams login url
profile = url + username          # Your profile

#######################################################################
################# Start facebook login process #######################
#######################################################################

dr = webdriver.Safari() #   initialize the safari window
dr.get(loggedIn)        #    Go to login page 
sleep(3)                #    Give the page a chance to load
                          
element = dr.find_element_by_xpath("//input[@name='email']")
element.send_keys(email) #    Enter username
element = dr.find_element_by_xpath("//input[@name='pass']")
element.send_keys(password) #   Enter password 

xPath1 = '//*[@id="loginbutton"]'
login_button = dr.find_element_by_xpath(xPath1) 
login_button.click() # click the login button

#######################################################################
#################        end facebook bot        #####################
#######################################################################
sleep(60)            #    Log out 60 seconds after the script is done
dr.close()           #    close window
#######################################################################
#################     github.com/DustyDevelops    #####################
#######################################################################


