import dir
import requests
from bs4 import BeautifulSoup
import re
import json


def get_mangakakalot(url):
    source = "https://mangakakalot.com"
    response = requests.get(url)
    folder_Name = ''
    if response.ok:
        soup = BeautifulSoup(response.text, 'lxml')
        code = soup.find("div", {"class":"container-chapter-reader"})\
            .find_all("img")
        img_links = [img["src"] for img in code]
        folder_Name = dir.ref_str(soup.find("title").text)
    return dict(source=source, folder_Name=folder_Name, img_links=img_links,
                cooldown=5)

class manga4life:
    def chapterimage(self, ChapterString):
        chapter = ChapterString[1:-1]
        odd = int(ChapterString[len(ChapterString)-1])
        if odd == 0:
            return chapter
        else:
            return chapter + "." + str(odd)

    def pageimage(self, PageString):
        s = "000" + str(PageString)
        return s[len(s) - 3:]

    def get_manga4life(self, url):
        source = "https://manga4life.com"
        response = requests.get(url)
        folder_Name = ''
        if response.ok:
            soup = BeautifulSoup(response.text, 'lxml')
            scripts = soup.find_all("script")[-1]
            res = re.findall('\{(.*?)\}', str(scripts) )
            CurChapter = json.loads('{' + res[13] + '}')
            res = re.findall('\"(.*?)\";', str(scripts) )
            CurPathName = res[0]
            folder_Name = soup.find("a", class_="btn btn-sm btn-outline-secondary")["href"].split("/manga/")[1]
            img_links = []
            directory = CurChapter.get("Directory")
            for count in range(int(CurChapter.get("Page"))):
                link = "https://" + CurPathName + "/manga/" + folder_Name + "/" + directory + "/" \
                + self.chapterimage(CurChapter.get("Chapter")) + "-" + self.pageimage(count+1) + ".png"
                img_links.append(link)
            folder_Name += " " + self.chapterimage(CurChapter.get("Chapter"))
        return dict(source=source, folder_Name=folder_Name, img_links=img_links,
                cooldown=1)


    

def remove_slash(url):
    if url[len(url)-1] == '/':
        return url[:-1]
    return url


def download(url):

    if  'mangakakalot.com' in url:
        return get_mangakakalot(url)

    elif  'manga4life.com' in url:
        m = manga4life()
        return m.get_manga4life(url)


    return "Link not supported" , []