import scrapy


class MercadolivreSpider(scrapy.Spider):
    name = "mercadolivre"
    allowed_domains = ["lista.mercadolivre.com.br"]
    start_urls = ["https://lista.mercadolivre.com.br/chinelo-masculino"]

    def parse(self, response):
        chinelos = response.css('div.poly-card__content')
        
        for chinelo in chinelos:
            
            yield {'marca' : chinelo.css('span.poly-component__brand::text').get(),
                   'nome' : chinelo.css('h2.poly-box.poly-component__title a::text').get()
                   
                   
                   
            
            
            }
