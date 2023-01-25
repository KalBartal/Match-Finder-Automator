# Match Finder Automator

# This code is a tkinter GUI application that automates the process of logging into match.com and finding matches. It
# first creates the main window with a welcome message and instructions, then adds labels and entry fields for email
# and password. Finally, it defines a login() function which takes the email and password entered by the user and
# logs in to match.com. It then clicks on the Shuffle option to find matches. The code uses webdriver and selenium to
# automate the match finding process.

import tkinter as tk
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import random

# Creating main window
window = tk.Tk()
window.config(pady=20, padx=40)
window.configure(background="#ABC270")

# Setting the title of main window
window.title("Match Finder Automator")

# Adding a welcome message
welcome_label = tk.Label(window, text="Welcome to Match Finder Automator", font=("Arial", 20), fg="#473C33",
                         bg="#FEC868")
welcome_label.grid(column=0, row=0, columnspan=2)

# Adding instructions
welcome_label = tk.Label(window, text="Please enter your match.com credentials", fg="#473C33", bg="#FEC868")
welcome_label.grid(column=0, row=1, columnspan=2, pady=10)

# Adding labels and input fields
tk.Label(window, text="Email:", fg="#473C33", bg="#FDA769").grid(column=0, row=2)
input_email = tk.Entry(window, width=20, fg="black", bg="#f5f5dc")
input_email.grid(column=1, row=2)
tk.Label(window, text="Password:", fg="#473C33", bg="#FDA769").grid(column=0, row=3)
input_password = tk.Entry(window, width=20, fg="black", bg="#f5f5dc")
input_password.grid(column=1, row=3)


# Defining click event function
def login():
    EMAIL = input_email.get()
    PASSWORD = input_password.get()
    random_wait = random.randint(3, 8)
    driver = webdriver.Chrome()
    driver.get("https://uk.match.com")
    time.sleep(random_wait)
    driver.find_element(By.XPATH, '//*[@id="onetrust-accept-btn-handler"]').click()
    time.sleep(random_wait)
    driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div[3]/button[2]').click()
    time.sleep(random_wait)
    driver.find_element(By.XPATH, '//*[@id="login-form-email-input"]').send_keys(EMAIL)
    time.sleep(random_wait)
    driver.find_element(By.XPATH, '//*[@id="login-form-password-input"]').send_keys(PASSWORD)
    time.sleep(random_wait)
    driver.find_element(By.XPATH, '//*[@id="main-frame"]/div[1]/div[2]/form/button').click()
    time.sleep(15)
    driver.get("https://uk.match.com/d/shuffle-kiss/online?fullScreen=true")
    while True:
        driver.get("https://uk.match.com/d/shuffle-kiss/online?fullScreen=true")
        time.sleep(random_wait)
        driver.find_element(By.XPATH, '/html/body/div[1]/dating-wrapper/div/shuffle/shuffle-page-kiss/div/div/div['
                                      '2]/div/div[3]/div[1]/div/div[2]/div/div[4]/div/div/div/button').click()
        time.sleep(random_wait)


# Creating button
tk.Button(window, text="Login", command=login, bg="#473C33", highlightbackground="#ABC270").grid(column=1, row=4,
                                                                                                 pady=10)

window.mainloop()
