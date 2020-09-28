import os
import time
import requests
from selenium import webdriver


def fetch_image_urls(query:str,max_links_to_fetch:int,wd:webdriver,sleep_between_interaction: int =1):
    def scroll_to_end(wd):
        wd.execute_script("window.scrollTo(0,document.body.scrollHeight);")
        time.sleep(sleep_between_interaction)

    search_url = "https://www.google.com/search?safe=off&site=&tbm=isch&source=hp&q={q}&oq={q}&gs_l=img"

    #load the page
    wd.get(search_url.format(q=query))

    image_urls=set()
    image_count= 0
    result_start=0

    while image_count <max_links_to_fetch:
        scroll_to_end(wd)

        #get all the images thumbnails results
        thumbnails_result= wd.find_elements_by_css_selector("img.Q4LuWd")
        #print(thumbnails_result)
        num_results= len(thumbnails_result)
        print(f"Found: {num_results}  search results. Extracting links from {result_start} :{num_results}")



        for img in thumbnails_result[result_start:num_results]:
            #try to click every thumbnail and get  the image page behind it.
            try:
                img.click()
                time.sleep(sleep_between_interaction)
            except Exception:
                continue

            #extract images urls
            actual_images=wd.find_elements_by_css_selector('img.n3VNCb')
            for actual_image in actual_images:
                if actual_image.get_attribute('src') and 'http' in actual_image.get_attribute('src'):
                    image_urls.add(actual_image.get_attribute('src'))
            image_count=len(image_urls)


            if len(image_urls) >= max_links_to_fetch:
                print(f"Found: {len(image_urls)} image links ,Done!!")
                break
        else:
            print(f"Found {len(image_urls)} images links ,Looking for more")
            time.sleep(30)
            return
            load_more_button=wd.find_element_by_css_selector('.mye4qd')
            if load_more_button:
                wd.execute_script("document.querySelector('.mye4qd').click();")

        #move the result startpoint further down
        result_start=len(thumbnails_result)
    return image_urls



def persist_images(folder_path:str, url:str,counter):
    try:
        img_content=requests.get(url).content
    except Exception as e:
        print(f"Error -could not download {url}- {e}")

    try:
        f=open(os.path.join(folder_path, 'jpg' + "_" + str(counter)+".jpg"),'wb')
        f.write(img_content)
        f.close()
        print(f"Sucess  - saved{url}-as {folder_path}")
    except:
        print(f"Error-could not save {url}- {e}")




#<img class="rg_i Q4LuWd"

def search_and_download(search_term:str,driver_path:str,target_path='./images',num_images = 10):
    target_folder=os.path.join(target_path,'_'.join(search_term.lower().split(' ')))

    if not  os.path.exists(target_folder):
        os.makedirs(target_folder)
    with webdriver.Chrome(executable_path=driver_path) as wd:
        res=fetch_image_urls(search_term,num_images,wd=wd,sleep_between_interaction=0.5)

    counter=0
    for element in res:
        persist_images(target_folder,element,counter)
        counter+=1



DRIVER_PATH='./chromedriver.exe'
search_term='cat'
num_images=8
search_and_download(search_term=search_term,driver_path=DRIVER_PATH)