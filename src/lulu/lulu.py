# Lulu scraper (https://www.luluhypermarket.in) by Code Monkey King
import json, csv; open('lulu.csv', 'w').write('title,price,thumbnail_url,image_url,DP Type,Brand,Content,Type\n'); (fetch('https://www.luluhypermarket.in/en-in/fruits-vegetables-fresh-food/c/HY00216202?sort=discount-desc&q=%3Arelevance#'), [(fetch('https://www.luluhypermarket.in/' + url), csv.DictWriter(open('lulu.csv', 'a'), ['title', 'price', 'thumbnail_url', 'image_url', 'DP Type', 'Brand', 'Content', 'Type']).writerow({'title': response.css('h1[class="pdp-productname"]::text').get(), 'price': 'INR ' + response.css('div[class="prod-price"]').css('span::text').get(), 'thumbnail_url': 'https://www.luluhypermarket.in' + response.css('span[class="thumbnail"]').css('img::attr(src)').get(), 'image_url': 'https://www.luluhypermarket.in' + response.css('div[class="item active"]').css('img::attr(src)').get(), response.css('div[class="features-ul"]').css('p[class="col-md-5 col-sm-5 col-xs-6"]::text').getall()[0]: response.css('div[class="features-ul"]').css('p[class="col-md-5 col-sm-7 col-xs-6"]::text').getall()[0].strip(), response.css('div[class="features-ul"]').css('p[class="col-md-5 col-sm-5 col-xs-6"]::text').getall()[1]: response.css('div[class="features-ul"]').css('p[class="col-md-5 col-sm-7 col-xs-6"]::text').getall()[1].strip(), response.css('div[class="features-ul"]').css('p[class="col-md-5 col-sm-5 col-xs-6"]::text').getall()[-2]: response.css('div[class="features-ul"]').css('p[class="col-md-5 col-sm-7 col-xs-6"]::text').getall()[-2].strip(), response.css('div[class="features-ul"]').css('p[class="col-md-5 col-sm-5 col-xs-6"]::text').getall()[-1]: response.css('div[class="features-ul"]').css('p[class="col-md-5 col-sm-7 col-xs-6"]::text').getall()[-1].strip()})) for url in response.css('a[class="js-gtm-product-link"]::attr(href)').getall()])[-1]
