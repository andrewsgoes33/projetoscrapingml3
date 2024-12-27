import scrapy


class MercadolivreSpider(scrapy.Spider):
    name = "mercadolivre"
    allowed_domains = ["lista.mercadolivre.com.br"]
    start_urls = ["https://lista.mercadolivre.com.br/chinelo-masculino"]
    page_count = 1
    max_pages = 10

    def parse(self, response):
        slippers = response.css('div.poly-card__content')
        
        
        for slipper in slippers:
            
            prices = slipper.css('span.andes-money-amount__fraction::text').getall()
            cents = slipper.css('span.andes-money-amount__cents::text').getall()
            
            yield {'Brand' : slipper.css('span.poly-component__brand::text').get(),
                   'Name' : slipper.css('h2.poly-box.poly-component__title a::text').get(),
                   'Old_Price' : prices[0] if len(prices) > 0 else None,
                   'Old_Cents' : cents[0] if len(cents) > 0 else None,
                   'New_Price' : prices[1] if len(prices) > 1 else None,
                   'New_Cents' : cents[1] if len(cents) > 1 else None,
                   'Reviews_Rating' : slipper.css('span.poly-reviews__rating::text').get(),
                   'Reviews_Total' : slipper.css('span.poly-reviews__total::text').get(),
                   'Link' : slipper.css('h2.poly-box.poly-component__title a::attr(href)').get()
                
            
            }
            
        if self.page_count < self.max_pages:    
            next_page = response.css('li.andes-pagination__button.andes-pagination__button--next a::attr(href)').get()
            if next_page:
                self.page_count += 1
                yield scrapy.Request(url=next_page, callback=self.parse)
