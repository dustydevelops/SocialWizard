

#                        SOCIAL WIZARD                          #

from selenium import webdriver 
import time
import sys



#       User Credentials        #

email = 'darealjoeshmo@gmail.com'
password = 'youllneverguessit'   
tellThem = 'Happy Birthday!'

#                Start Facebook Engagement                   #
tellThem = 'HappyBirthday!'
x = 1
while True:
        print('Iteration:', x)
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

        print("Login Successfull")
        time.sleep(3)
        dr.get('https://www.facebook.com/events/birthdays')
        time.sleep(3)
        
        
        try:
                element = dr.find_element_by_xpath('//*[@id="u_0_12"]')
                element.send_keys(tellThem)
                sleep(1)
                element.submit()
                print("Birthday wish 1 Successfull")
        except:
                pass
        
        try:
                element = dr.find_element_by_xpath('//*[@id="u_0_13"]')
                element.send_keys(tellThem)
                time.sleep(1)
                element.submit()
                print("a birthday wish was made")

        except:
                pass

        try:
                element = dr.find_element_by_xpath('//*[@id="u_0_16"]')
                element.send_keys(tellThem)
                time.sleep(1)
                element.submit()
                print("A birthday wish was made")
        except:
                pass
     
        try:
                element = dr.find_element_by_xpath('//*[@id="u_0_17"]')
                element.send_keys(tellThem)
                time.sleep(1)
                element.submit()
                print("A birthday wish was made")
        except:
                pass

        try:
                element = dr.find_element_by_xpath('//*[@id="u_0_1a"]')
                element.send_keys(tellThem)
                time.sleep(1)
                element.submit()
                print("A birthday wish was made")
                

        except:
                pass
     
        try:
                element = dr.find_element_by_xpath('//*[@id="u_0_1d"]')
                element.send_keys(tellThem)
                time.sleep(1)
                element.submit()
                print("A birthday wish was made")

        except:
                pass
        print('Birthday post process complete')
        print('Iteration', x , 'Was completed successfully.')
        print('In 2 hours the appication will recheck for new/missed birthdays.','\n',
                'Please do not power down your system ')
        


        dr.close()

        time.sleep(7200)
