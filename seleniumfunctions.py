from selenium import webdriver
from selenium.webdriver.common.service import Service # A Service class that is responsible for the starting and stopping of `chromedriver`.
from selenium.webdriver.common.keys import Keys # The Keys class provide keys in the keyboard like RETURN, F1, ALT etc.
from selenium.webdriver.common.by import By
options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)

driver = webdriver.Chrome(r"C:\Users\chaitanya\Downloads\chromedriver_win32\chromedriver.exe",options = options)
driver.get("https://www.google.com/")


# driver.maximize_window()
# driver.minimize_window()
# driver.fullscreen_window()  #it working in windows os

# print(driver.title)
# print(driver.current_url)

# print(driver.get_window_position())
# print(driver.get_window_size())
# print (driver.get_window_rect())

# driver.refresh()
# driver.forward()
# driver.back()

# driver.set_window_size(100,1008)
# driver.set_window_position(200,500)
# driver.set_window_rect(x=1000,y=200,width=300,height=400)

# driver.find_element_by_name('').send_keys('india',Keys.ENTER)
driver.find_element(By.NAME,'q').send_keys('india', Keys.ENTER) # ---? ///

driver.execute_script("window.scrollTo(0,1000)")
# driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")


# driver.close()
# driver.quit()