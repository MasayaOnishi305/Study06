from api import get_api
import pprint

def test_get_api():
    keyword = "レインブーツ"
    category = ""
    url = "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706?format=json&keyword={0}&category={1}&applicationId=1019079537947262807".format(
        keyword,category)

    res = get_api(url)

    assert len(res["Items"]) >= 1
    assert res["Items"][0]["Item"]["itemCode"]
