import random, time
from selenium import webdriver

username = 'ur username'
password = 'ur password'

driver = webdriver.Firefox(executable_path=r"C:\Users\dustin\webdrivers\geckodriver-v0.30.0-win64\geckodriver.exe")
driver.get('https://instagram.com')

time.sleep((random.randint(3,5)))

emailTextField = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
emailTextField.send_keys(username)

time.sleep((random.randint(3,5)))

passwordTextField = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")
passwordTextField.send_keys(password)

time.sleep((random.randint(3,5)))

loginButton = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button/div")
loginButton.click()

time.sleep((random.randint(3,5)))

driver.get('https://instagram.com')

time.sleep((random.randint(3,5)))

try:
    notNow =  driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")
    notNow.click()
except:
    pass

time.sleep((random.randint(3,5)))


article = 1
while True:
        post = str(article)
        likeButton = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/section/div/div[2]/div/article['+post+']/div/div[3]/div/div/section[1]/span[1]/button')
        likeButton.click()
        time.sleep((random.randint(0,5)))
        print('post',post,"liked..")
        article+=1
        if article == 6:
            break
time.sleep((random.randint(3,5)))

driver.get('https://instagram.com/tonyrobbins')
time.sleep((random.randint(3,5)))

followers = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]')
followers.click()
time.sleep((random.randint(3,5)))

followButton = driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/ul/div/li[1]/div/div[3]/button")
followButton.click()
time.sleep((random.randint(3,5)))

followButton = driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/ul/div/li[2]/div/div[3]/button")
followButton.click()
time.sleep((random.randint(3,5)))

followButton = driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/ul/div/li[3]/div/div[3]/button")
followButton.click()
time.sleep((random.randint(3,5)))

followButton = driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/ul/div/li[4]/div/div[3]/button")
followButton.click()
time.sleep((random.randint(3,5)))

followButton = driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/ul/div/li[5]/div/div[3]/button")
followButton.click()
time.sleep((random.randint(3,5)))

followButton = driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/ul/div/li[6]/div/div[3]/button")
followButton.click()
time.sleep((random.randint(3,5)))

followButton = driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/ul/div/li[7]/div/div[3]/button")
followButton.click()
time.sleep((random.randint(3,5)))
