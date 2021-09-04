import requests
import urllib


def get_api(url):
    result = requests.get(url)
    return result.json()


def main():
    keyword = "レインブーツ"
    category = ""
    url = "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706?format=json&keyword={0}&category={1}&applicationId=1019079537947262807".format(
        keyword,category)
    resp = (get_api(url))
    total = int(resp['count'])
    page = int (resp['pageCount'])
    print ("【検索数】",total,"\n【ページ数】",page,"\n ===================================")

    count = 0
    for i in resp['Items']:
        count += 1
        item = i['Item']
        print ("【No】",count)
        print ("【商品名】",item['itemName'])
        print ("【価格】",item['itemPrice'])



main()
