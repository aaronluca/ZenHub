import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.implicitly_wait(10)

try:
    driver.get('https://www.google.com/')
    element = driver.find_element_by_name("q")
    element.send_keys("ZenHub")
    element.send_keys(Keys.ENTER)

    zenhub_link = driver.find_element_by_xpath("//a[@data-pcu='https://www.zenhub.com/']")
    zenhub_link.click()
    blog_link = driver.find_element_by_link_text("Blog")
    blog_link.click()

    widget_tags = driver.find_element_by_xpath("//aside[@class='widget widget-tags']")
    assert widget_tags.find_element_by_link_text("Open Source")

    search_field = driver.find_element_by_id("search-field")
    search_field.clear()
    search_field.send_keys("Open Source")
    time.sleep(5)
    search_button = driver.find_element_by_id("js-btn-search")
    search_button.click()

    blog_redcross_link = driver.find_element_by_link_text("How ZenHub is helping Philippine Red Cross fight Covid-19")
    assert blog_redcross_link
    time.sleep(5)
    blog_redcross_link.click()

    blog_homepage = driver.find_element_by_id("primary")
    assert blog_homepage.find_element_by_link_text("Blog Homepage")

except Exception as e:
    print("Exception happened during testing, details are: "+ str(e))
else:
    print("All the testing has been passed without error!")

driver.close()
