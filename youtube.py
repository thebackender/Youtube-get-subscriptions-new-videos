import selenium.webdriver as webdriver
import time
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import random
from selenium.webdriver.support.wait import WebDriverWait

start_time = time.time()
options = Options()
options.headless = True
browser = webdriver.Firefox(options=options)
print("Loading...")
try:
    #browser.get("https://youtube.com")
    #time.sleep(random.randrange(3, 5))

    data = open('subscriptions.txt').read().splitlines(True)
    print("For today you may watch: ")
    watched = open('parsed.txt', encoding="utf-8").read()
    parse = open('parsed.txt', 'a', encoding="utf-8")
    cnt = 1
    nothing = True
    for i, d in enumerate(data):
        arr = d.split(' ')
        browser.get(arr[1]+'/videos?app=desktop')
        # time.sleep(5)
        WebDriverWait(browser, timeout=10).until(lambda d: d.find_element(By.ID, 'details'))
        # print(browser.page_source)
        for k in range(3):
            #print(i*3 + k + 1)
            link = browser.find_element('id', 'details').find_element('id', 'video-title-link').get_attribute('href')
            video_id = link.split('watch?v=')[1]
            if video_id not in watched:
                # details = browser.find_element('id', 'details').text.split('\n')
                # print("{0}) {1} from {2} uploaded {3}".format(cnt, details[0], arr[0], details[2]))
                print("Link: ", link)
                cnt += 1
                browser.execute_script('document.getElementById("details").id = "details{0}"'.format(k))
                # parse.write("{0} => {1} from {2}\n".format(video_id, details[0], arr[0], details[2]))
                parse.write(video_id+"\n")
                nothing = False
        time.sleep(2)
    if nothing:
        print('Nothing to watch, go ahead and start focus on your goals')
except Exception as ex:
    print(ex)
browser.close()
browser.quit()
print("--- %s seconds ---" % (time.time() - start_time))