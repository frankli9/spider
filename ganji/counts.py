import time
from page_parsing import url_list_ganji

while True:
    print(url_list_ganji.find().count())
    time.sleep(3)