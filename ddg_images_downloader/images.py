# AUTOGENERATED! DO NOT EDIT! File to edit: 00_images.ipynb (unless otherwise specified).

__all__ = ['get_image_urls', 'download_search_urls', 'download_images_slowly', 'download_search_images_slowly']

# Internal Cell
# set options to be headless, ..
from selenium import webdriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

# Internal Cell
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Internal Cell
import time
DDG_SEARCH_URL = 'https://start.duckduckgo.com'
# DDG_IMAGE_SEARCH_URL = 'https://duckduckgo.com/?q=%s&t=h_&iar=images&iax=images&ia=images'

def get_browser_page(search_string, options=chrome_options, scroll_count=20, sleep=3):
    "retrieves a ddg page containing image search results for `search_string`, scrolling down `scroll_count` times, with a delay of `sleep` seconds between scrolls"
    browser = webdriver.Chrome(options=options)
    browser.get(DDG_SEARCH_URL)
    wait = WebDriverWait(browser,10)
    input_elt = wait.until(
        EC.presence_of_element_located((By.ID, "search_form_input_homepage"))
    )
    submit_elt = browser.find_element_by_id('search_button_homepage')
    input_elt.send_keys(search_string)
    submit_elt.click()
    images_link = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".js-zci-link--images"))
    )
    images_link.click()
    wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".tile--img__img"))
    )
    for i in range(scroll_count):
        browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        time.sleep(sleep)
    page_source = browser.page_source
    browser.quit()
    return page_source

# Internal Cell
from bs4 import BeautifulSoup as bs
def extract_images(page_source):
    page = bs(page_source,"html5lib")
    img_elts = page.find_all("img",attrs={"class":"tile--img__img"})
    return img_elts

# Internal Cell
import re
from urllib.parse import unquote
DATA_SRC_URL_PATTERN = r'^//external-content\.duckduckgo\.com/iu/\?u=(.*)$'

def extract_url(img_elt):
    data_src = img_elt.attrs['data-src']
    if data_src:
        url_match = re.match(DATA_SRC_URL_PATTERN,data_src)
        if url_match:
            return unquote(url_match.group(1))
    return None

def extract_img_urls(img_elts):
    img_urls = [url for url in map(extract_url, img_elts) if url is not None]
    return img_urls


# Cell
# combine everything into 1
def get_image_urls(search_string,options=chrome_options,scroll_count=20,sleep=3):
    "get image urls with `search_string` and scroll down `scroll_count` times with a delay of `sleep` seconds returns a list of urls"
    page_source = get_browser_page(search_string,options=options,scroll_count=scroll_count,sleep=sleep)
    img_elts = extract_images(page_source)
    img_urls = extract_img_urls(img_elts)
    return img_urls



# Internal Cell
from pathlib import Path
from fastcore.utils import *

# Cell
def download_search_urls(path,search_terms, search_pattern, file_pattern='{0}.txt',
                      options=chrome_options,scroll_count=20,sleep=3):
    "download search results into a file in named after search string"
    path.mkdir(exist_ok=True)
    for o in search_terms:
        results = get_image_urls(search_pattern.format(o),options=options,scroll_count=scroll_count,sleep=sleep)
        print(search_pattern.format(o), len(results))
        with open(path/file_pattern.format(o), 'w') as f:
            f.writelines("%s\n" % line for line in results)

# Internal Cell
# externalized version of fastai2 internal method _download_image (copied exactly)
# see https://github.com/fastai/fastai2/blob/master/fastai2/vision/utils.py#L19
from fastai2.vision.utils import download_url
def download_image_inner(dest, inp, timeout=4):
    i,url = inp
    suffix = re.findall(r'\.\w+?(?=(?:\?|$))', url)
    suffix = suffix[0] if len(suffix)>0  else '.jpg'
    try: download_url(url, dest/f"{i:08d}{suffix}", overwrite=True, show_progress=False, timeout=timeout)
    except Exception as e: f"Couldn't download {url}."

# Cell
def download_images_slowly(dest,url_file=None, urls=None, max_pics=1000, delay=3, batch_size=10,timeout=4):
    "Download images listed in text file `url_file` to path `dest`, at most `max_pics` with a delay of `delay` secs for every batch of `batch_size` images with only 1 thread"
    if urls is None: urls = url_file.read().strip().split("\n")[:max_pics]
    dest = Path(dest)
    dest.mkdir(exist_ok=True)
    for inp in enumerate(urls):
        i,_ = inp
        download_image_inner(dest,inp,timeout=timeout)
        if i % batch_size == 0:
            print(f'downloaded: ', i, ' dest: ', dest)
            time.sleep(delay)

# Cell
def download_search_images_slowly(path, search_terms, file_pattern='{0}.txt',
                                  max_pics=1000, delay=3, batch_size=10,timeout=4):
    "Download images listed in text file for each item in `search_terms`  to path `dest`/item, at most `max_pics` with a delay of `delay` secs for every batch of `batch_size` images with only 1 thread"
    for o in search_terms:
        download_images_slowly(path/o,path/file_pattern.format(o),max_pics=max_pics, delay=delay,
                               batch_size=batch_size, timeout=timeout)