
###############################################################################################
#                                        SOCIAL WIZARD
###############################################################################################
email = 'joeshmo@gmail.com'
phone = '() - '
username = 'joshmo'           # the username the bot will use to log in.
password = 'youllneverguesthis'   # the password the bot will use to log in.

#                        SOCIAL WIZARD                          #

from selenium import webdriver 
from time import sleep

#       User Credentials        #

email = 'dustinmichaelsmith03@gmail.com'
phone = '() - '
username = 'dsmithnoswag'        
password = '1dirtysock'   

#            Urls               #

#                Start Facebook Engagement                   #


# Initialize the safari window with facebook login page & wait
dr = webdriver.Safari()           
dr.get('https://www.facebook.com/login')




element = dr.find_elements_by_xpath('//*[@id ="email"]') 
element[0].send_keys(email) 

print("Username Entered") 

element = dr.find_element_by_xpath('//*[@id ="pass"]') 
element.send_keys(password) 

print("Password Entered") 

login_button = dr.find_element_by_xpath('//*[@id="loginbutton"]') 
login_button.click() # click the login button
sleep(3)
print("Login Successfull")

dr.get('https://www.facebook.com/events/birthdays')

tellThem = 'Happy Birthday'
if tellThem == 'Happy Birthday':
        try:
                element = dr.find_element_by_xpath('//*[@id="u_0_13"]')
                element.send_keys(tellThem)
                sleep(0.1)
                print("Birthday Wish posted for friend 1") 
              
           
        except:
                pass
                

#######################################################################
#################        end facebook bot        #####################
#######################################################################
sleep(60)            #    Log out 60 seconds after the script is done
dr.close()           #    close window
#######################################################################
#################     github.com/DustyDevelops    #####################
#######################################################################



