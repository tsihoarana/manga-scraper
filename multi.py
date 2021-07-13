import dir
from bs4 import BeautifulSoup
import scrap
from tkinter import *
import tools
from cloudflare import Fcloudflare
import time

class Multi:
    def __init__(self, widget : Text):
    	self.widget = widget


    def download_file(self, source, url, path):
        # print(f'Started downloading {url}')
        self.widget.configure(state='normal')
        self.widget.insert(END, "Started downloading {}\n".format(url))
        self.widget.configure(state='disabled')
        self.widget.see("end")

        Fcloudflare.force_download(source, url, path)

        self.widget.configure(state='normal')
        self.widget.insert(END, "Finished downloading {}\n".format(url))
        self.widget.configure(state='disabled')
        self.widget.see("end")
      
    def download_manga(self,cod, p):
        todown = scrap.download(cod)
        if todown.get("folder_Name") == 'Link not supported':
            self.widget.configure(state='normal')
            self.widget.insert(END, folder_Name + '\n', ("red",))
            self.widget.configure(state='disabled')
            self.widget.see("end")
            return ""

        dir.create_Folder(p, todown.get("folder_Name"))
        save_path = (p + '\\' + todown.get("folder_Name")).replace('\\', '/') + '/'
        j = 1
        # resume download
        last = tools.last_downloaded(save_path)
        todown["img_links"] = todown.get("img_links")[last:]
        j += last
        #
            
        for url in todown.get('img_links'):
            self.download_file(todown.get("source"), url,
                        save_path + dir.numerotate(j, 3) + ".jpg")
            time.sleep(todown.get("cooldown"))
            j += 1