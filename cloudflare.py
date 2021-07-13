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
        
