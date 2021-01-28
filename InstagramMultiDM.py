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
        botPassword = "Password" 


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

            WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, "//a[@class = 'xWeGp']")))
            self.driver.find_element_by_xpath("//a[@class = 'xWeGp']").click()

            WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[5]/div/div/div/div[3]/button[2]")))
            self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[2]").click()
            #self.driver.get("https://www.instagram.com/direct/inbox/")
            try:
                WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, "//div[text()='"+user+"']")))
                self.driver.find_element_by_xpath("//div[text()='"+user+"']").click()
            except:
                self.driver.find_element_by_xpath("//button[@class='wpO6b ZQScA']").click()
                ActionChains(self.driver) \
                    .send_keys(user) \
                    .key_down(Keys.ENTER) \
                    .key_up(Keys.ENTER) \
                    .perform()
                self.driver.find_element_by_xpath("(//div[@class='_7UhW9   xLCgt      MMzan  KV-D4              fDxYl     '])[1]").click()
                time.sleep(1)
                self.driver.find_element_by_xpath("//div[@class='rIacr']").click()
                time.sleep(1)

                



        except:
            self.driver.quit()
            print("Unexpected error:", sys.exc_info()[0])
    def chat_with(self,output_user):
        poop = "poop"

    def text(self,text_string):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//textarea[@placeholder = 'Message...']")))
        self.driver.find_element_by_xpath("//textarea[@placeholder = 'Message...']").click()
        ActionChains(self.driver) \
            .send_keys(text_string) \
            .key_down(Keys.ENTER) \
            .key_up(Keys.ENTER) \
            .perform()
    def read(self):
        return self.driver.find_elements_by_xpath("//div[@class=' e9_tN JRTzd']")[-1].text
        
        #while(true):
          #  if(texts[text_value].)



front_dm_bot = MultiDM("dhirru12")
back_dm_bot = MultiDM("user2")

#dm_time.text("poop")
updated_text = ""
while(True):
    latest_text = front_dm_bot.read()
    if (latest_text!=updated_text and latest_text[0]=="!"):
        updated_text = latest_text
        print(updated_text[1:])
        back_dm_bot.text(updated_text[1:])


