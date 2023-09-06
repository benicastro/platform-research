# Import necessary modules/libraries
import scrapy


# Create Spider code
class GabSpider(scrapy.Spider):
    name = "gab_spider"

    # custom_settings = {
    #     "FEEDS": {
    #         "data/%(name)s_%(time)s.jsonl": {
    #             "format": "jsonlines",
    #         }
    #     }
    # }

    def start_requests(self):
        profile_list = ["worth__fighting__for"]
        for profile in profile_list:
            # url = f"https://gab.com/{profile}"
            gab_url = f"https://gab.com/{profile}/"
            yield scrapy.Request(
                url=gab_url,
                callback=self.parse_profile,
                meta={"profile": profile, "gab_url": gab_url},
            )

    def parse_profile(self, response):
        date_joined = ""
        user_name = response.xpath(
            "//*[@id='gabsocial']/div/div[2]/main/div/div/div/div[1]/div/div/div[2]/div[1]/div[2]/div/span[1]/text()"
        ).get()
        user_image = ""
        cover_photo = ""
        about = ""
        num_gabs = ""
        num_followers = ""
        num_following = ""
        last_posts = ""
        ave_engagement = ""
        yield {
            "profile": response.meta["profile"],
            "url": response.meta["gab_url"],
            "user-name": user_name,
            "date-joined": date_joined,
        }
        #         yield {
        #             "name": products.css("a.product-item-link::text").get(),
        #             "price": products.css("span.price::text").get().replace("£", ""),
        #             "link": products.css("a.product-item-link").attrib["href"],
        #         }
        #     except:
        #         yield {
        #             "name": products.css("a.product-item-link::text").get(),
        #             "price": "sold out",
        #             "link": products.css("a.product-item-link").attrib["href"],
        #         }

        # next_page = response.css("a.action.next").attrib["href"]
        # if next_page is not None:
        #     yield response.follow(next_page, callback=self.parse)
