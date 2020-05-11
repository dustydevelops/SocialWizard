
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
sleep(3)
dr.get('https://www.facebook.com/events/birthdays')
sleep(3)
tellThem = 'Happy Birthday!'
try:
        element = dr.find_element_by_xpath('//*[@id="u_0_12"]')
        element.send_keys(tellThem)
except:
        pass
element.submit()
sleep(0.1)
try:
        element = dr.find_element_by_xpath('//*[@id="u_0_13"]')
        element.send_keys(tellThem)
except:
        pass
element.submit()
sleep(0.1)
try:
        element = dr.find_element_by_xpath('//*[@id="u_0_16"]')
        element.send_keys(tellThem)
except:
        pass
element.submit()
sleep(0.1)
try:
        element = dr.find_element_by_xpath('//*[@id="u_0_17"]')
        element.send_keys(tellThem)
except:
        pass
element.submit()
sleep(0.1)
try:
        element = dr.find_element_by_xpath('//*[@id="u_0_1a"]')
        element.send_keys(tellThem)
except:
        pass
element.submit()
sleep(0.1)
try:
        element = dr.find_element_by_xpath('//*[@id="u_0_1d"]')
        element.send_keys(tellThem)
except:
        pass

element.submit()
sleep(0.1)

sleep(0.1)
print("Birthday Wish posted for friend 1") 
              
    

#######################################################################

sleep(30)            #    Log out 60 seconds after the script is done
dr.close()           #    close window

#################     github.com/DustyDevelops    #####################


