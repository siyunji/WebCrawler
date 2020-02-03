import scrapy
from ..items import WebCrawlerItem


class medhelpScraper(scrapy.Spider):
    name = 'medhelp'
    urls = ['https://www.medhelp.org/forums/Diabetes---Type-1/show/220']
   
    def parse(self, response):
        d = WebCrawlerItem()
        #question = response.css('h2.subj_title a::text').getall()
        question = response.xpath('/html/body/div[4]/div[3]/div[3]/div[3]/div[1]/div[1]/div[1]/div[2]/h2/a/text()').extract()
        #question = response.css('#body_container > div.mh_vit_content > div.mh_vit_mid > div.mh_vit_card.forum_show > div.subject_list_ctn > div:nth-child(1) > div.subj_header > div.subj_info > h2 > a::text').getall()

        d["question"] = question
      
        yield d