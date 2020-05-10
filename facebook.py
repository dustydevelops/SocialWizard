
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

url = 'https://www.facebook.com/'   #I nstagrams url
loggedIn = url + 'login/'  # Instagrams login url


#######################################################################
################# Start instagram login process #######################
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

sleep(3)
birthdays = 'https://www.facebook.com/events/birthdays/'
dr.get(birthdays)
sleep(3)

tellThem = 'Happy Birthday'
if tellThem == 'Happy Birthday':
        try:
                element = dr.find_element_by_xpath('//*[@id="u_0_14"]')
                element.send_keys(tellThem) #   tell first happy birthday
                sleep(0.1)

                element = dr.find_element_by_xpath('//*[@id="u_0_17"]')
                element.send_keys(tellThem) #   tell second happy birthday
                sleep(0.1)
        
                element = dr.find_element_by_xpath('//*[@id="u_0_1a"]')
                element.send_keys(tellThem) #   tell tell thrid happy birthday
                sleep(0.1)

                element = dr.find_element_by_xpath('//*[@id="u_0_1d"]')
                element.send_keys(tellThem) #   tell them tell 4th happy birthday
                sleep(0.1)
        
        except:
                print('Done!')
                

#######################################################################
#################        end facebook bot        #####################
#######################################################################
sleep(60)            #    Log out 60 seconds after the script is done
dr.close()           #    close window
#######################################################################
#################     github.com/DustyDevelops    #####################
#######################################################################





