import scrapy
from items import Flipkart1Item

class FlipBotSpider(scrapy.Spider):
    name = "flip-bot"
    start_urls = ["https://www.flipkart.com/laptops/pr?sid=6bo,b5g&otracker=categorytree&fm=neo%2Fmerchandising&iid=M_f9755d4d-fc3e-486e-a0eb-de604e8aec0b_1_372UD5BXDFYS_MC.34WHNYFH5V2Y&otracker=hp_rich_navigation_8_1.navigationCard.RICH_NAVIGATION_Electronics~Laptop%2Band%2BDesktop_34WHNYFH5V2Y&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_8_L1_view-all&cid=34WHNYFH5V2Y"]

    def parse(self, response):
        product=Flipkart1Item()
        name=response.css("[contains(concat( " ", @class, " " ), concat( " ", "_4rR01T", " " ))]::text").extract()
        price=response.css("[contains(concat( " ", @class, " " ), concat( " ", "_1_WHN1", " " ))]::text").extract()
        discount=response.css("[contains(concat( " ", @class, " " ), concat( " ", "_3Ay6Sb", " " ))]._3HqJxg , ._2tDckM , ._10Ermr , ._4rR01T::text").extract()
        product["p_name"]=name
        product["p_price"]=price
        product["p_discount"]=discount
        yield product