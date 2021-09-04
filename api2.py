import requests
import urllib


def get_api(url):
    result = requests.get(url)
    return result.json()


def main():
    keyword = "レインブーツ"
    productId= "958716cccc6bc6163216fb71990c22a5"
    # url = "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706?format=json&keyword={0}&category={1}&applicationId=1019079537947262807".format(
    #     keyword,category)
    url = "https://app.rakuten.co.jp/services/api/Product/Search/20170426?applicationId=1013826913582053233&format=json&keyword={0}&genreId=0".format(
        keyword,productId)
    resp = (get_api(url))
    total = int(resp['count'])
    page = int (resp['pageCount'])
    print ("【検索数】",total,"\n【ページ数】",page,"\n ===================================")
    count = 0
    max_price = 0
    min_price = 99999999
    for i in resp['Products']:
        count += 1
        product = i['Product']
        max_item_price = product['maxPrice']
        min_item_price = product['minPrice']
        # print ("【No】",count)
        # print ("【商品名】",item['itemName'])
        # print ("【価格】",item_price)
        if max_price < max_item_price:
            max_price = max_item_price
        if min_price > min_item_price:
            min_price = min_item_price
    print ("===================================")
    print ("【最大価格】",max_price)
    print ("【最小価格】",min_price)
        



main()
