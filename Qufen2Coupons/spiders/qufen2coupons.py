# coding: utf-8
import scrapy
from scrapy_splash import SplashRequest


class Qufen2Coupons(scrapy.Spider):
    name = 'qufen2coupons'
    allowed_domains = []
    start_urls = ['https://uland.taobao.com/quan/detail?sellerId=2596602764&activityId=70be4107c1464ed7a85eb08071708b0b',
                  'https://uland.taobao.com/quan/detail?activityId=c258a6db75914d04a555950f64037442&sellerId=2904179849',]
    # css select
    lua_script = """
function main(splash)
  splash:set_user_agent(splash.args.ua)
  assert(splash:go(splash.args.url))

  -- requires Splash 2.3  
  while not splash:select('.my-element') do   
    splash:wait(0.1)
  end
  return {html=splash:html()}
end
    """

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url=url, callback=self.parse, args={'wait': 1})  # , endpoint='render.html'

    def parse(self, response):
        judge = response.xpath('//span[@class="errorTip"]').extract()
        if judge:
            print '自主推广'
        else:
            print 'alimama'