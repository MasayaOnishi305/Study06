import gspread
from oauth2client.service_account import ServiceAccountCredentials
from gspread_dataframe import set_with_dataframe
import api3 

JSON_PATH = '..\linen-bliss-324922-76b8c136410a.json'
SHEET_NAME = 'googleAPI テスト'
SPREADSHEET_KEY = '1MDSbBrrXV0Lu53LEY51nvbALtiPi6SsCvP6jPOex05c'

# スプレッドシートとの接続
def connect(SPREADSHEET_KEY):
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    credentials = ServiceAccountCredentials.from_json_keyfile_name(JSON_PATH, scope)
    gs = gspread.authorize(credentials)
    workbook = gs.open_by_key(SPREADSHEET_KEY)
    worksheet =workbook.worksheet("sheet1")

    print(workbook.title)
    print(workbook.id)
    return workbook

#スプレッドシートに書き込み
def insert(workbook,df):
    workbook.add_worksheet(title="sheet2", rows=50, cols=10)
    set_with_dataframe(workbook.worksheet("sheet2"),df,include_index=True)
    #データの整形
    worksheet2 =workbook.worksheet("sheet2")
    worksheet2.delete_columns(1)

def main():
    res_workbook = connect(SPREADSHEET_KEY)
    #検索結果取得
    res_df = api3.main()
    insert(res_workbook,res_df)

main()


