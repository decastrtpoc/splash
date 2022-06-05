import scrapy 
import json
import re
from scrapy_splash import SplashRequest 
from teste.items import Imoveis

class MySpider(scrapy.Spider): 
    name = "ex"
    with open("urls.txt", "rt") as f:
        start_urls = [url.strip() for url in f.readlines()]
    custom_settings = {
        'AUTOTHROTTLE_ENABLED': True,
        'AUTOTHROTTLE_START_DELAY': 2,
        'AUTOTHROTTLE_MAX_DELAY': 30,
        'AUTOTHROTTLE_TARGET_CONCURRENCY': 0.5
        
    }
    def start_requests(self): 
        for url in self.start_urls: 
            yield SplashRequest(url, self.parse, 
                endpoint='render.html', 
                args={'wait': 1}, 
           ) 

    
    def parse(self, response):
        # response.body is a result of render.html call; it
        # contains HTML processed by a browser.
        imovel = Imoveis()
        pattern = '(\.{3}\(.*(static)"\})'
        resp = response.css('script::text')[2].re_first(pattern)
        json_data = resp[4:]
        #print(json_data)
        dados = json.loads(json_data)
        
        vivaId = dados["listing"]["id"]
        account = dados["account"]
        listing = dados["listing"]
        medias = dados["medias"]
        link = "https://www.vivareal.com.br" + dados["page"]["listingLinks"][0]["href"]
        
        imovel["vivaId"] = vivaId
        imovel["account"] = account
        imovel["listing"] = listing
        imovel["medias"] = medias
        imovel["link"] = link
        
        yield (imovel)
    
    

       