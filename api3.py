import requests
import urllib
import pandas as pd

CSV_FILE = "stock.csv"

def get_api(url,params):
    result = requests.get(url,params=params)
    if not(300 > result.status_code >= 200):
        print("api error")
        return None 
    return result.json()

def main():
    url = "https://app.rakuten.co.jp/services/api/IchibaItem/Ranking/20170628"
    params = {
        "applicationId":1013826913582053233,
        "genreId":100283
    }  
    resp = (get_api(url,params))
    title = resp['title']
    date = resp['lastBuildDate']
    exp_rank_list = []
    exp_name_list = []
    exp_price_list = []
    print (f"【ジャンル】{title} \n【取得日】{date}\n ===================================")
    for i in resp['Items']:
        item = i['Item']
        exp_rank_list.append(item['rank'])
        exp_name_list.append(item['itemName'])
        exp_price_list.append(item['itemPrice'])
    
    #CSV出力
    # DataFrameに対して辞書形式でデータを追加する
    try:
        df = pd.DataFrame(
            {
            "ランク": exp_rank_list,
            "商品名": exp_name_list,
            "金額": exp_price_list})
        df.to_csv(CSV_FILE,encoding="UTF_8_sig")
        return df
    except Exception as e:
        print('CSVの出力に失敗しました')
        

main()
