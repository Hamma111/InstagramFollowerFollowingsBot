from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.chrome.options import Options
import hashlib



class instaBot:

    def __init__(self, usr, pwd):
        self.usr = usr
        self.pwd = pwd
        option = Options()
        option.add_argument("--headless")
        self.dr = webdriver.Chrome()

        self.dr.get('https://instagram.com')
        sleep(2)
        self.dr.find_element_by_xpath('//input[contains(@name, "username")]').send_keys(self.usr)
        self.dr.find_element_by_xpath('//input[contains(@name, "password")]').send_keys(self.pwd)
        self.dr.find_element_by_xpath('//button[contains(@type,"submit")]').click()
        sleep(15)
        try:
            self.dr.find_element_by_xpath('//button[contains(text(), "Not Now")]').click()
            sleep(1)
            self.dr.find_element_by_xpath('//button[contains(text(), "Not Now")]').click()
        except:
            sleep(0.1)
        sleep(2)
        self.dr.find_element_by_xpath('//a[contains(@href, "/{}/")]'.format(self.usr)).click()

    def getFollowers(self):
        self.dr.find_element_by_xpath('//a[contains(@href, "/{}/followers/")]'.format(self.usr)).click()
        scroll_box = self.dr.find_element_by_xpath('/html/body/div[4]/div/div/div[2]')

        ht, last_ht = 1, 0

        while ht != last_ht:
            ht = last_ht
            last_ht = self.dr.execute_script(
                """
                arguments[0].scrollTo(0, arguments[0].scrollHeight);
                return arguments[0].scrollHeight;
                """, scroll_box)
            sleep(1)
        self.dr.find_element_by_xpath('/html/body/div[4]/div/div/div[1]/div/div[2]/button').click()
        nl = scroll_box.find_elements_by_tag_name('a')
        names = [x.text for x in nl if x.text != '']
        return names

    def getFollowing(self):
        self.dr.find_element_by_xpath('//a[contains(@href, "/{}/following/")]'.format(self.usr)).click()
        scroll_box = self.dr.find_element_by_xpath('/html/body/div[4]/div/div/div[2]')

        ht, last_ht = 1, 0

        while ht != last_ht:
            ht = last_ht
            last_ht = self.dr.execute_script(
                """
                arguments[0].scrollTo(0, arguments[0].scrollHeight);
                return arguments[0].scrollHeight;
                """, scroll_box)
            sleep(1)
        self.dr.find_element_by_xpath('/html/body/div[4]/div/div/div[1]/div/div[2]/button').click()
        nl = scroll_box.find_elements_by_tag_name('a')
        names = [x.text for x in nl if x.text != '']
        return names

    def results(self):
        self.dr.quit()
        followers = self.getFollowers()
        following = self.getFollowing()
        print('people whom you follow and they dont follow you back')
        print([x for x in followers if x not in following])

        print('\n')
        print('people whom you follow and they dont follow you back')
        print([x for x in following if x not in followers])


if __name__ == "__main__":
    username = ''
    password = ''
    bot = instaBot(username ,password)
    bot.results()
