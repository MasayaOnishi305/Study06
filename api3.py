import requests
import urllib
import pandas as pd

CSV_FILE = "stock.csv"

def get_api(url):
    result = requests.get(url)
    return result.json()

def main():
    genreId="100283"
    url = "https://app.rakuten.co.jp/services/api/IchibaItem/Ranking/20170628?applicationId=1013826913582053233&genreId={}".format(
        genreId)
    resp = (get_api(url))
    title = resp['title']
    date = resp['lastBuildDate']
    exp_rank_list = []
    exp_name_list = []
    exp_price_list = []
    print (f"【ジャンル】{title} \n【取得日】{date}\n ===================================")
    for i in resp['Items']:
        item = i['Item']
        exp_rank_list.append({item['rank']})
        exp_name_list.append({item['itemName']})
        exp_price_list.append({item['itemPrice']})
    
    #CSV出力
    # DataFrameに対して辞書形式でデータを追加する
    try:
        df = pd.DataFrame(
            {
            "ランク": exp_rank_list,
            "商品名": exp_name_list,
            "金額": exp_price_list})
        #データの整形
        # df["ランク"] = df["ランク"].replace("{","")
        # df["商品名"] = df["商品名"].str.replace("{'","").str.replace("'}","")
        # df["金額"] = df["金額"].replace("{'","").replace("'}","")
        df.to_csv(CSV_FILE,encoding="UTF_8_sig")
        return df
    except Exception as e:
        print('CSVの出力に失敗しました')
        

main()
