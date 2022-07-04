########################################### Installed Chrome ###############################################################

''' These will open chrome on your machine. The reason why chromedriver is used so that it takes away all the manual work of downloading chrome driver matching version to your browser. 
If you do not have you can you can do pip install chromedirver_binary
'''    
from selenium import webdriver
import tqdm, time
import chromedriver_binary  # Adds chromedriver binary to path
driver = webdriver.Chrome()
driver.get("http://www.python.org")


# This is the URL being used to access the web telegram version. You first only run till here so that you can do a manual authentication of the web interface.
URL = "https://web.telegram.org/k/"



# Second Part of the code is to determine the chat IDs. We first find all the chat ids and put it an array datas
ele = driver.find_elements_by_xpath('//a[@class="chatlist-chat rp"]')


datas = []
def get_ids():
    ele = driver.find_elements_by_xpath('//a[@class="chatlist-chat rp"]')
    for x in tqdm(range(0,len(ele))):
        data = ele[x].get_attribute('data-peer-id')
        datas.append(data)
        driver.execute_script("document.getElementsByClassName('chatlist-chat rp active')[0].click()")
        time.sleep(1)
 
   
get_ids()
datas = list(set(datas))
print(len(datas))


# Third Part of the code to go through each of the chat IDs and with this loop it deletes all the joined messages. 

for x in tqdm(range(0,len(datas))):
    # print(len(datas))
    driver.get("https://web.telegram.org/k/#"+str(datas[x]))
    time.sleep(1)
    abc = "hehe"
    try:
        driver.execute_script("document.getElementsByClassName('chatlist-chat rp active')[0].click()")  
    except:
        print("failed at first try catch block")
        pass
    try:
        time.sleep(1)
        abc = driver.execute_script("return document.getElementsByClassName('chatlist-chat rp active')[0].innerText")
    except:
        print("failed at second try catch block")
        pass
   
    if "joined Telegram" in abc:
        driver.execute_script("document.getElementsByClassName('chatlist-chat rp active')[0].click()")    
        # driver.find_element_by_xpath("//div[@class='btn-icon tgico-more rp btn-menu-toggle']//div[@class='c-ripple']").click()
        driver.execute_script("document.getElementsByClassName('chat-utils')[document.getElementsByClassName('chat-utils').length-1].children[document.getElementsByClassName('chat-utils')[document.getElementsByClassName('chat-utils').length-1].children.length-1].click()")
        time.sleep(1)
        # driver.find_element_by_xpath("//div[@class='btn-menu-item rp-overflow tgico-delete danger']").click()
        driver.execute_script("document.getElementsByClassName('btn-menu bottom-left active')[0].getElementsByClassName('btn-menu-item rp-overflow tgico-delete danger')[0].click()")
        time.sleep(1)
        driver.execute_script("document.getElementsByClassName('popup popup-peer popup-delete-chat active')[0].getElementsByClassName('checkbox-box')[0].click()")
        time.sleep(1)        
        driver.execute_script("document.getElementsByClassName('popup popup-peer popup-delete-chat active')[0].getElementsByClassName('btn danger rp')[0].click()")

