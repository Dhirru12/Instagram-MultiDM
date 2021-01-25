from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import sys
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
class MultiDM:
    def __init__(self,input_user):
        botUsername = "doggo.bot8891"
        botPassword = "Dhirran1" 


        self.driver = webdriver.Chrome(executable_path = './chromedriver.exe')
        self.driver.get("https://www.instagram.com/direct/inbox/")
        print("Insta Started")
        #System.out.println(driver.getPageSource())
        time.sleep(2.5)
        print("Wait over")
        try:
            #WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@name='username']"))).send_keys(botUsername)
            #WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@aria-label='Password']"))).send_keys(botPassword)
            time.sleep(10)
            print("Wait over")
            ActionChains(self.driver) \
                .key_down(Keys.TAB) \
                .key_up(Keys.TAB) \
                .send_keys(botUsername) \
                .key_down(Keys.TAB) \
                .key_up(Keys.TAB) \
                .send_keys(botPassword) \
                .key_down(Keys.ENTER) \
                .key_up(Keys.ENTER) \
                .perform()
            #self.driver.find_element_by_xpath("//input[@name='username']").click()
            print("we got it")
            #self.driver.find_element_by_xpath("//div[text()='Log In']").click()

            WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, "//*[@id='react-root']/section/nav/div[2]/div/div/div[3]/div/div[2]/a/div/div")))
            self.driver.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[3]/div/div[2]/a/div/div").click()

            WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[5]/div/div/div/div[3]/button[2]")))
            self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[2]").click()
            #self.driver.get("https://www.instagram.com/direct/inbox/")
            WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, "//div[text()='"+input_user+"']")))
            self.driver.find_element_by_xpath("//div[text()='"+input_user+"']").click()

        except:
            self.driver.quit()
            print("Unexpected error:", sys.exc_info()[0])
        #except:
           # print(Exception)
    def chat_with(self,output_user):
        poop = "poop"
    def text(self,string):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//textarea[@placeholder = 'Message...']")))
        self.driver.find_element_by_xpath("//textarea[@placeholder = 'Message...']").click()



fun_time = MultiDM("dhirru12")

