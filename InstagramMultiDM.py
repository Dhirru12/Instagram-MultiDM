from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import sys
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

##########################################################
#ENTER USERNAME AND PASSWORD HERE
botUsername = "username"
botPassword = "password" 
##########################################################

class MultiDM:
    #Bot starts up
    def __init__(self,user):
        self.driver = webdriver.Chrome(executable_path = './chromedriver.exe')
        self.driver.get("https://www.instagram.com/direct/inbox/")
        print("Bot Started")

        #Wait for website to load
        time.sleep(2.5)
        print("Website Ready")

        #Login
        try:
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
            print("Bot has logged in")

            #Waits for homepage to load then goes to the inbox of the bot
            WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, "//a[@class = 'xWeGp']")))
            self.driver.get("https://www.instagram.com/direct/inbox/")

            #Closes pop up
            WebDriverWait(self.driver, 15).until(EC.presence_of_element_located((By.XPATH, "//button[@class='aOOlW   HoLwm ']")))
            self.driver.find_element_by_xpath("//button[@class='aOOlW   HoLwm ']").click()

            #Opens DM with requested user
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
                time.sleep(2)
                self.driver.find_element_by_xpath("(//div[@class = '-qQT3'])[1]").click()
                time.sleep(1)
                self.driver.find_element_by_xpath("//div[@class='rIacr']").click()
                time.sleep(1)
        except:
            self.driver.quit()
            print("Unexpected error:", sys.exc_info()[0])

    #Returns username of the current user in string form
    def getUsername(self):
        WebDriverWait(self.driver, 3).until(EC.presence_of_element_located((By.XPATH, "//div[@class='_7UhW9    vy6Bb      qyrsm KV-D4              fDxYl     ']")))
        return self.driver.find_element_by_xpath("//div[@class='_7UhW9    vy6Bb      qyrsm KV-D4              fDxYl     ']").text

    #Texts current user with string input
    def text(self,text_string):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "//textarea[@placeholder = 'Message...']")))
        self.driver.find_element_by_xpath("//textarea[@placeholder = 'Message...']").click()
        ActionChains(self.driver) \
            .send_keys(text_string) \
            .key_down(Keys.ENTER) \
            .key_up(Keys.ENTER) \
            .perform()
    #Returns the latest DM in string form before deleting the element to prevent rereading
    def read(self):
        try:
            text = self.driver.find_elements_by_xpath("//div[@class=' e9_tN JRTzd']")[-1].text
            self.driver.execute_script("""
            var element = arguments[0];
            element.parentNode.removeChild(element);
            """, self.driver.find_elements_by_xpath("//div[@class=' e9_tN JRTzd']")[-1])
            return text
        except:
            return None

    #Deletes latest text
    def clearText (self):
        latest_text = "placeholder"
        while (latest_text!=None):
            time.sleep(1)
            latest_text = self.read()
        
#Starts up front_dm_bot, the bot used to take in input for one or multiple users
#If with one person, input their username, if multiple people the bot must be in the groupchat and enter the EXACT group chat name
front_dm_bot = MultiDM("dhirru12")

#Latest_text for front_dm_bot holds the latest text from the input user(s)
front_latest_text = "placeholder"
front_dm_bot.clearText()

#front_dm_bot greets user(s)
front_dm_bot.text("Welcome to the Multi DM Bot! I help multiple users text as one!")
front_dm_bot.text("Be sure to use a '!' before every sentence you'd like me to send!")
front_dm_bot.text("Who would you like to text? Example: '!Dhirru12'")

#Checker boolean represents if there are still texts in the DM before front_dm_bot was started
checker = True

while(checker):
    front_latest_text = front_dm_bot.read()
    try:
        checker=front_latest_text[0]!="!"
    except:
        checker=True

#Bot takes in input of what user or group chat the bot should contact
front_latest_text = front_latest_text[1:]
front_dm_bot.text("Establishing connection with '"+front_latest_text+"'...")

#back_dm_bot attempts connection with the user or groupchat inputted
back_dm_bot = MultiDM(front_latest_text)

#If there's no exceptions, the front_dm_bot texts that the connection has been established
front_dm_bot.text("Connection established with '"+back_dm_bot.getUsername()+"'!")
print("Connection established with '"+back_dm_bot.getUsername()+"'!")

#Bots begins reading their designated user(s) inputs
#front_dm_bot will read and and tell back_dm_bot to send the input to the recieving user(s)
#back_dm_bot will read and and tell front_dm_bot to send the input to the input user(s)
back_updated_text = ""
time.sleep(5)
back_dm_bot.clearText()
while(True):
    front_latest_text = front_dm_bot.read()
    back_latest_text = back_dm_bot.read()
    try:
        if (front_latest_text[0]=="!"):
            print("'"+front_latest_text[1:]+"' message sent!")
            back_dm_bot.text(front_latest_text[1:])
    except:
        pass
    try:
        if(back_latest_text!=None):
            front_dm_bot.text("User replied: "+back_latest_text)
            print("'"+front_latest_text[1:]+"' message recieved!")
    except:
        pass


