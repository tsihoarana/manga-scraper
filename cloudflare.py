import cloudscraper
# import itertools
class Fcloudflare:

    def force_download(referer, url, pathname):     # eg: referer:https://mangakakalot.com/
    
        scraper = cloudscraper.create_scraper(
            interpreter='native',
            browser={
                'browser': 'chrome',
                'mobile': 'False'
            }
        )

        scraper.headers['Referer'] = referer

        resp = scraper.get(url, stream=True)

        with open(pathname, 'wb') as ourImage:
            for chunk in resp.iter_content(chunk_size=8192):
                ourImage.write(chunk)

    def force_request(referer, url):
        
        scraper = cloudscraper.create_scraper(
            interpreter='native',
            browser={
                'browser': 'firefox',
                'mobile': 'False'
            }
        )
        scraper.headers['Referer'] = referer
        return scraper.get(url)                     #response
        

# this suck so don't use it
    # def force_download_mangakakalot(url, pathname):
        
        # r = requests.get(url, "wb")
        # if r.ok:
            # with open(pathname , "wb") as f:
                # f.write(r.content)
        # else:
            # url_edited = url.replace('s3.mkklcdnv3', 's8.mkklcdnv8')
            # r = requests.get(url_edited, "wb")
            # if r.ok:
                # with open(pathname , "wb") as f:
                    # f.write(r.content)
            # else:
                # print("request error")
                # print(r)
