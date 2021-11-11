
import random,time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

# If you have multiple instagrams put multiple usernames
usernames = ['or','you can delete','and add more here']

# passwords only seem to work if you input integers, special characters and letters in seperate
#for examply if your pass word is 1FakePassword!, put it in as follows
#see def inputThePassword() near line 47 to understand the logic on the following
passwords = [1,'FakePassword','!','besuretoadd',2,'all combations','if you use multiple accts']

# If you use Apples Safari no action. If you use chrome or firefox, edit the following line. 
driver = webdriver.Safari()

def humanizeIt():
    godsWill = [float(random.randint(1,9)) in [3,6,9] , float(random.randint(1,5))]
    return godsWill


def initiateWebBrowser():
    try:
        
        print('Setting the bounds of the safari window...')
        driver.set_window_position(0, 0)
        driver.set_window_size(1024, 768)
        print('Retreiving instagram....')
        driver.get('https://www.instagram.com/')
        time.sleep(humanizeIt()[1])
        return driver
    except Exception as e:
        print(e)

def check_exists_by_xpath(xpath):
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

def inputTheUsername():
    
    driver.find_element_by_css_selector("input[name='username']").send_keys(usernames[1])
    time.sleep(humanizeIt()[1])

def inputThePassword():
    
    password = driver.find_element_by_css_selector("input[name='password']")
    password.send_keys(passwords[0])
    password.send_keys(passwords[2])
    time.sleep(humanizeIt()[1])
    password.send_keys(passwords[3])

def showAndHidePassword():
    if humanizeIt()[0] == True:
        driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/div/div/button').click()
        time.sleep(float(humanizeIt()[1]))
        if humanizeIt()[0] == True:
            driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/div/div/button').click()
            time.sleep(humanizeIt()[1])




def login():
    driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div').click()
    time.sleep(humanizeIt()[1])
    xpath='//*[@id="slfErrorAlert"]'
    print('FAILED TO LOGIN',check_exists_by_xpath(xpath))



try:



    driver = initiateWebBrowser()
    inputTheUsername()
    inputThePassword()
    showAndHidePassword()
    login()

    #driver.close()
except Exception as e:

    print(e)
'''           

time.sleep(5)
notNow = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
time.sleep(3)
article = 1

while True:
        post = str(article)
        like = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/section/div/div[2]/div/article['+post+']/div/div[3]/div/div/section[1]/span[1]/button')
        like.click()
        time.sleep((random.randint(0,5)))
        print('post',post,"liked..")
        article+=1
        if article == 6:
            break

explore = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[4]/a')
explore.click()
time.sleep(5)
firstPicture = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/div/div[1]/div[2]/div')
firstPicture.click()
time.sleep(3.333)
followFirstProfile = driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[1]/div[2]')
followFirstProfile.click()
visitFirstProfile = driver.find_element_by_xpath('/html/body/div[6]/div[2]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[1]/div[1]')
visitFirstProfile.click()
time.sleep(5)
followers = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]')
followers.click()
time.sleep(5)

driver.find_element_by_xpath('/html/body/div[6]/div/div/div[2]/ul/div/li[2]/div/div[1]').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/div[1]/div[1]/div/div/div/span/span[1]/button').click()
time.sleep(3)
explore = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[4]/a')
explore.click()
time.sleep(3)
secondPicture = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[1]/div/div[1]/div[1]')
secondPicture.click()
time.sleep(20)
driver.close()
'''
