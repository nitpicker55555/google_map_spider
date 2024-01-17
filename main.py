import time

from selenium_basic_func import *

all_dict_list = []
url_list=[]
def each_page():
    elements = driver.find_elements_by_css_selector(".Nv2PK.THOPZb.CpccDe")
    # 遍历找到的元素
    content_list={"title":"/div/div[2]/div[4]/div[1]/div/div/div[2]/div[1]/div[2]",
                  "url":"/div/a",
                  "star":"/div/div[2]/div[4]/div[1]/div/div/div[2]/div[3]/div/span[2]/span",
                  "price":"/div/div[2]/div[4]/div[1]/div/div/div[2]/div[3]/div/span[3]/span[2]",
                  "address":"/div/div[2]/div[4]/div[1]/div/div/div[2]/div[4]",
                  "info":"/div/div[2]/div[5]/div[2]/div"}


    for i in range(len(elements)):
        each_case_dict = {}
        basic_url = '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]/div[%s]'%(i*2+7)
        for content in content_list:
            xpath_str=basic_url+content_list[content]
            try:
                if xpath_str.endswith("a"):
                    label_text=driver.find_element_by_xpath(xpath_str).get_attribute("href")
                    if label_text not in url_list:
                        url_list.append(label_text)
                    else:
                        continue
                elif content=="info":
                    label_text=""
                    parent_element=driver.find_element_by_xpath(xpath_str)
                    elements_with_aria_label = parent_element.find_elements_by_xpath(".//*[@aria-label]")

                    # 遍历找到的元素并输出它们的文本
                    for element in elements_with_aria_label:
                        label_text+="_"+element.text
                else:
                    label_text = driver.find_element_by_xpath(xpath_str).text
                if "·" in label_text:
                    each_case_dict['class']=label_text.split("·")[0]
                    each_case_dict['address']=label_text.split("·")[1].split("⋅")[0]
                    each_case_dict['close_time']=label_text.split("·")[1].split("⋅")[1]
                else:
                    each_case_dict[content]=label_text

                print(each_case_dict[content])

            except:
                each_case_dict[content] =None
                print("...",content)
        all_dict_list.append(each_case_dict)

        """    
        //*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]/div[11]/div/div[2]/div[5]/div[2]/div
        //*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]/div[5]/div/div[2]/div[5]/div[2]/div/div[1]/div[2]/span
        //*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]/div[9]/div/div[2]/div[5]/div[2]/div 最下面的小字
        //*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]/div[7]/div/a href链接
        //*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]/div[7]/div/div[2]/div[4]/div[1]/div/div/div[2]/div[1]/div[2] title
        //*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]/div[7]/div/div[2]/div[4]/div[1]/div/div/div[2]/div[3]/div/span[2]/span star
        //*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]/div[7]/div/div[2]/div[4]/div[1]/div/div/div[2]/div[3]/div/span[3]/span[2] price
        
        //*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]/div[7]/div/div[2]/div[4]/div[1]/div/div/div[2]/div[4]
        //*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[1]/div[1]/div[9]/div/div[2]/div[4]/div[1]/div/div/div[2]/div[4]
        """
    # for i in all_dict_list:
    #     print(i)
    with open("data.jsonl", "a") as file:
        for item in all_dict_list:
            # 将字典转换为 JSON 字符串并写入文件
            json_string = json.dumps(item)
            file.write(json_string + "\n")
def scroll_page():
    for i in range(20):
        scrollable_element = driver.find_element_by_xpath('//*[@id="QA0Szd"]/div/div/div[1]')

        # 在该元素内部向下滚动
        driver.execute_script("arguments[0].scrollTop += 250", scrollable_element)
        # each_page()
        time.sleep(2)
        driver.execute_script("arguments[0].scrollTop -= 250", scrollable_element)
scroll_page()