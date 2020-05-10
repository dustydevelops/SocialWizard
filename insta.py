
################################################################################################################
#                                        SOCIAL WIZARD
################################################################################################################

username = 'joeshmo'           # the username the bot will use to log in.
password = 'youllneverguess'   # the password the bot will use to log in.

################################################################################################################
###############for  quick start just input your details above and then run. the rest of this doesnt matter######
################################################################################################################

from selenium import webdriver      # from selenium import webdriver for web browser automation.
from time import  sleep             # import sleep from time for creating time delays.

url = 'http://www.instagram.com/'   #I nstagrams url
loggedIn = url + 'accounts/login/'  # Instagrams login url
profile = url + username.           # Your profile

################################################################################################################
################# Start instagram login process if engage = True #######################
################################################################################################################
engage = True
while engage == True :

    #################################   initialize the safari window
    dr = webdriver.Safari()
    try:
        ################################    Go to login page 
        dr.get(loggedIn)
        ################################    Give the page a chance to load
        sleep(3)
        #################################   Find the username textfield
        element = dr.find_element_by_xpath("//input[@name='username']")
        #################################    Enter username 
        element.send_keys(username)
        #################################   Find the password textfield
        element = dr.find_element_by_xpath("//input[@name='password']")
        #################################   Enter password 
        element.send_keys(password)
        #################################   Locate login button
        login_button = dr.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button')
        ################################    Let the script breathe
        sleep(3)
        #################################   Click login button
        login_button.click() and print ('Username and password input succesfully now logging in')
        ################################    Let the script breathe
        sleep(6)



    ################################    close window
    dr.close()


