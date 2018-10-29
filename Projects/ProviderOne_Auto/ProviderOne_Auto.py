'''
Name: Automated ProviderOne Check
Author: Wesley Wang
Date: 10/28/2018
Description: Automated ProviderOne Check

Tasks to do:
Figure out how to detect active status
Update excel sheet
Add note if not in king/snohomish/island
'''

from selenium import webdriver
from xlrd import XLRDError
import pandas as pd
import time
import os


URL = "https://www.waproviderone.org/"  # ProviderOne URL
WB_PATH = "Clients.xlsx"   # Workbook file path
WS_NAME = "main"    # Target worksheet name
CLT_PATH = "."  # Client folder root path
ALT_PATH = "./Not Found"    # Backup export path if client folder is missing
ZOOM_LEVEL = "70%"


def create_folder(path):
    if not os.path.isdir(path):
        try:
            os.mkdir(path)
            full_path = os.path.abspath(path)
            print(f"Folder created at {full_path}")
        except OSError:
            print("An error occured when creating folder!")
        except:
            print("An error occured!")


def get_login():
    check_login = ""
    while check_login != "y":
        domain_id = input("Please enter your ProviderOne Domain ID: ")
        user_name = input("Please enter your ProviderOne Username: ")
        password = input("Please enter your ProviderOne Password: ")
        print(f"Your login info is:\nDomain ID: {domain_id}\tUsername: {user_name} \tPassword: {password}")
        check_login = input("Is it correct? (Y/N) ").lower()
        if check_login not in ["y", "n"]:
            print("Please enter correct answer (Y/N)!!")
    login = (domain_id, user_name, password)
    return login


def load_clients(file):
    try:
        main = pd.read_excel(file, WS_NAME, na_filter=False)
        clients = [(lname, fname, dob.strftime("%m/%d/%Y"), ssn.replace('-','').strip()) \
                    for (lname, fname, dob, ssn) \
                    in zip(main["LastName"], main["FirstName"], main["DOB"], main["SSN"], )]
        return clients
    except FileNotFoundError:
        print("File not found !")
    except XLRDError:
        print("An error occured when reading Excel file!")
    except:
        print("An error occured!")


def update_worksheet():
    pass


def search_client(browser, date, lname, fname, dob, ssn, use_ssn=False):
    time.sleep(0.3)
    if use_ssn:
        browser.find_element_by_id("nfld_n:dbZzMBR_IDENTIFIER-IDNTFR_SSN").send_keys(ssn)
    else:
        browser.find_element_by_id("nfld_a:dbZzMBR_DMGRPHC-LAST_NAME").send_keys(lname)
        browser.find_element_by_id("nfld_a:dbZzMBR_DMGRPHC-FIRST_NAME").send_keys(fname)
    browser.find_element_by_id("nfld_d:dbZzMBR_DMGRPHC-BIRTH_DATE").send_keys(dob)
    browser.execute_script("submitForm()")
    browser.execute_script(f"document.body.style.zoom = '{ZOOM_LEVEL}'")

    efile_path = CLT_PATH + f"/{lname}, {fname} {dob.replace('/','-')}"

    if 1==0:
        file_name = "Inc-Res-Ins"
    else:
        file_name = "Inactive_ProviderOne"

    if not os.path.isdir(efile_path):
        efile_path = ALT_PATH
        file_name = f"({fname} {lname})" + file_name

    export_path = efile_path + f"/{file_name}_{fname[0]}{lname[0]}_{date[0]}_{date[1]}.png"
    if not os.path.exists(export_path):
        screenshot = browser.get_screenshot_as_file(export_path)

    browser.execute_script("submitForm('InquiryButton')")


def browse_prov1(login, clients):
    browser = webdriver.Chrome("chromedriver.exe")
    browser.maximize_window()
    browser.get(URL)
    browser.find_element_by_id("rfld_a:DomainNme").send_keys(login[0])
    browser.find_element_by_id("rfld_a:UserID").send_keys(login[1])
    browser.find_element_by_id("nfld:UserPwd").send_keys(login[2])
    browser.find_element_by_id("LoginButton").click()
    browser.find_element_by_id("GoButton").click()
    browser.find_element_by_link_text("Benefit Inquiry").click()
    date = (time.strftime("%Y"), time.strftime("%m"), time.strftime("%d"))
    
    for client in clients:
        search_client(browser, date, client[0], client[1], client[2], client[3])
        if len(client[3]) == 9 and client[3].isdigit():
            search_client(browser, date, client[0], client[1], client[2], client[3], True)

    browser.close()


if __name__ == "__main__":
    browse_prov1(get_login(), read_info(WB_PATH))
    create_folder(ALT_PATH)