from selenium import webdriver

driver = webdriver.Edge()

driver.get('https://s.weibo.com/top/summary')

eles = driver.find_elements_by_css_selector('.td-02 a')

for ele in eles:
    link = ele.get_attribute('href')
    if link == 'javascript:void(0);':
        link = 'https://s.weibo.com' + ele.get_attribute('href_to')
    print(link)
    print(ele.text)


driver.quit()