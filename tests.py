from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from random import randint
import unittest, HTMLTestRunner
import time
import sys
import random
import string
from testData import teams, players

class RegressionSuite(unittest.TestCase):
    
    def setUp(self):
        global driver
        driver = webdriver.Firefox()
        driver.get("http://dry-savannah-6646.herokuapp.com/")
        time.sleep(2)

    def test_home_page_title(self):  # WORKING
        self.assertEqual("Athletes", driver.title)

    def test_create_athlete(self):  # WORKING 
        # table rows has to be equal to 212
        first_name = ''.join(random.choice(string.lowercase) for x in range(6))
        last_name = ''.join(random.choice(string.lowercase) for x in range(6))
        number = randint(10,99)

        add_athlete = driver.find_element_by_link_text("+")
        add_athlete.click()
        time.sleep(2)
        
        # ADD ATHLETE Window
        firstName_field = driver.find_element_by_id("id_first_name")
        firstName_field.clear()
        firstName_field.send_keys(first_name)
        time.sleep(2)

        secondName_field = driver.find_element_by_id("id_last_name")
        secondName_field.clear()
        secondName_field.send_keys(last_name)

        position_field = driver.find_element_by_id("id_position")
        position_field.clear()
        position_field.send_keys("QB")

        number_field = driver.find_element_by_id("id_number")
        number_field.clear()
        number_field.send_keys(number)

        # Selecting from a drop down 
        team_dropdown_menu_id = "id_team"
        team_dropdown_menu_element = WebDriverWait(driver, 10).until(
            lambda driver: driver.find_element_by_id(team_dropdown_menu_id))
        Select(team_dropdown_menu_element).select_by_visible_text(
            "Arizona Diamondbacks")

        submit_button = driver.find_element_by_css_selector(
            "input.btn.btn-default")
        submit_button.click()

        self.assertEqual(first_name + " " + last_name, 
            driver.find_element_by_xpath("//tr[213]/td[2]").text)

    def test_delete_athlete(self):  #  WORKING
        # has to be run after test_create_athlete
        delete_athlete = driver.find_element_by_xpath(
            "(//a[contains(text(),'x')])[426]")
        delete_athlete.click()

        submit_delete = driver.find_element_by_xpath(
            "(//input[@value='Delete'])[213]")
        time.sleep(5)
        submit_delete.click()

        deleted_athlete = WebDriverWait(driver, 10).until_not(
            lambda driver: driver.find_element_by_xpath("//tr[213]/td[2]"))


    def test_edit_athlete_firstName(self):  #  WORKING
        firstName = ''.join(random.choice(string.lowercase) for x in range(6))
        edit_athlete = driver.find_element_by_xpath(
          "(//a[contains(text(),'x')])[5]")
        edit_athlete.click()
        time.sleep(2)

        # EDIT ATHLETE Window
        firstName_field = driver.find_element_by_xpath(
          "(//input[@name='first_name'])[4]")

        firstName_field.clear()
        firstName_field.send_keys(firstName)
        submit_button = driver.find_element_by_css_selector(
          "#athlete_edit_41 > div.modal-dialog.modal-sm > div.modal-content " +
          "> div.modal-body > form > input.btn.btn-default")
        submit_button.click()

        self.assertEqual(firstName + " Beasley", 
            driver.find_element_by_xpath("//tr[3]/td[2]").text)


    def test_edit_athlete_position(self):  #  WORKING
        position = ''.join(random.choice(string.lowercase) for x in range(2))
        edit_athlete = driver.find_element_by_link_text("x")
        edit_athlete.click()
        time.sleep(2)

          # EDIT ATHLETE Window
        number_field = driver.find_element_by_xpath(
            "(//input[@name='position'])[2]")
        number_field.clear()
        number_field.send_keys(position)

        submit_button = driver.find_element_by_css_selector(
            "#athlete_edit_140 > div.modal-dialog.modal-sm > div.modal-content > " +
            "div.modal-body > form > input.btn.btn-default")

        submit_button.click()

        self.assertEqual(position, driver.find_element_by_xpath("//td[3]").text)

       
    def test_edit_athlete_number(self):  #  WORKING
        number_gen = randint(10,99)
        number = str(number_gen)
        edit_athlete = driver.find_element_by_link_text("x")
        edit_athlete.click()
        time.sleep(2)
 
          # EDIT ATHLETE Window
        number_field = driver.find_element_by_xpath(
            "(//input[@name='number'])[2]")
        number_field.clear()
        number_field.send_keys(number)

        submit_button = driver.find_element_by_css_selector(
            "#athlete_edit_140 > div.modal-dialog.modal-sm > div.modal-content > " +
            "div.modal-body > form > input.btn.btn-default")

        submit_button.click()

        self.assertEqual(number, driver.find_element_by_css_selector("td").text)


    def test_edit_athlete_team(self):  #  WORKING
        num = randint(01,92)
        str_num = str(num)
        team = teams[str_num] # should return string from testData.py teamsdict
        edit_athlete = driver.find_element_by_link_text("x")
        edit_athlete.click()
        time.sleep(2)
        
        # EDIT ATHLETE Window
        # Selecting from a drop down 
        team_dropdown_element = driver.find_element_by_xpath(
            "(//select[@id='id_team'])[2]")
        Select(team_dropdown_element).select_by_visible_text(team) # "milwaukee brewere"
        #raw_input("team should be changed")
        

        submit_button = driver.find_element_by_css_selector(
            "#athlete_edit_140 > div.modal-dialog.modal-sm > " +
            "div.modal-content > div.modal-body > form > input.btn.btn-default")
        submit_button.click()
  
        self.assertEqual(team, driver.find_element_by_xpath("//td[7]").text)

    def test_search_player(self):
        # num = randint(1,164)
        # str_num = str(num)
        # player = players[str_num]  # should return string from testData.py playersdict
        # print player

        # TODO find a way not to hardcode this
        player = "Prince Amukamara"

        search_field = driver.find_element_by_id("filter")
        search_field.clear()
        search_field.send_keys(player)

        self.assertEqual(player, 
            driver.find_element_by_xpath("//td[2]").text)

    def test_filter_by_sport_baseball(self):
        filter_drop_down = driver.find_element_by_link_text("SPORT")
        filter_drop_down.click()
        #raw_input("drop down should appear")


        filter_by_baseball = driver.find_element_by_link_text("Baseball")
        filter_by_baseball.click()
        #raw_input("filter should be applied")
        
        # Varies with changing number of baseball sports teams
        for num in range(1,31):
            element = "//tr[%d]/td[4]" % (num)
            self.assertEqual("Baseball", 
                driver.find_element_by_xpath(element).text)


    def test_filter_by_sport_football(self):
        filter_drop_down = driver.find_element_by_link_text("SPORT")
        filter_drop_down.click()

        filter_by_baseball = driver.find_element_by_link_text("Football")
        filter_by_baseball.click()
        
        # Varies with changing number of basketball sports teams, currently 181
        for num in range(1,182):
            element = "//tr[%d]/td[4]" % (num)
            self.assertEqual("Football", 
                driver.find_element_by_xpath(element).text)

    def test_filter_by_football_NFL_NFCeast_DallasCowboys(self):
        sport_filter = driver.find_element_by_link_text("SPORT")
        sport_filter.click()
        filter_by_football = driver.find_element_by_link_text("Football")
        filter_by_football.click()

        league_filter = driver.find_element_by_link_text("LEAGUE")
        league_filter.click()
        filter_by_NFL = driver.find_element_by_link_text("NFL")
        filter_by_NFL.click()

        division_filter = driver.find_element_by_link_text("DIVISION")
        division_filter.click()
        filter_by_NFCeast = driver.find_element_by_link_text("NFC East")
        filter_by_NFCeast.click()

        team_filter = driver.find_element_by_link_text("TEAM")
        team_filter.click()
        filter_by_dallasCowboys = driver.find_element_by_link_text(
            "Dallas Cowboys")
        filter_by_dallasCowboys.click()

        for num in range(1,121):
            element = "//tr[%d]/td[7]" % (num)
            self.assertEqual("Dallas Cowboys", 
                driver.find_element_by_xpath(element).text)

    def test_filter_by_football_NFL_NFCeast_NYGiants(self):
        sport_filter = driver.find_element_by_link_text("SPORT")
        sport_filter.click()
        filter_by_football = driver.find_element_by_link_text("Football")
        filter_by_football.click()

        league_filter = driver.find_element_by_link_text("LEAGUE")
        league_filter.click()
        filter_by_NFL = driver.find_element_by_link_text("NFL")
        filter_by_NFL.click()

        division_filter = driver.find_element_by_link_text("DIVISION")
        division_filter.click()
        filter_by_NFCeast = driver.find_element_by_link_text("NFC East")
        filter_by_NFCeast.click()

        team_filter = driver.find_element_by_link_text("TEAM")
        team_filter.click()
        filter_by_NYGiants = driver.find_element_by_link_text(
            "New York Giants")
        filter_by_NYGiants.click()

        # 61 rows
        for num in range(1,62):
            element = "//tr[%d]/td[7]" % (num)
            self.assertEqual("New York Giants", 
                driver.find_element_by_xpath(element).text)


    def tearDown(self):
        driver.quit()

if __name__ == "__main__":
    HTMLTestRunner.main()
    