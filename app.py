import streamlit as st
import requests

def getAllBookstore():
	url = 'https://cloud.culture.tw/frontsite/trans/emapOpenDataAction.do?method=exportEmapJson&typeId=M' # 在這裡輸入目標 url
	headers = {"accept": "application/json"}
	response = requests.get(url, headers=headers)
	res = response.json()
	# 將 response 轉換成 json 格式
	return res
	# 回傳值


def getCountyOption(items):
	optionList = list()
	# 創建一個空的 List 並命名為 optionList
	for item in items:
		name = item['cityName'][0:3]
		# 把 cityname 欄位中的縣市名稱擷取出來 並指定給變數 name
		if name in items: continue
		else:
			optionList.append(name)
			# hint: 想辦法處理 item['cityName'] 的內容
		# 如果 name 不在 optionList 之中，便把它放入 optionList
		# hint: 使用 if-else 來進行判斷 / 用 append 把東西放入 optionList
	return optionList


def getSpecificBookstore(items, county):
	specificBookstoreList = []
	for item in items:
		name = item['cityName']
		if county not in name:
			specificBookstoreList.append(item)
		# 如果 name 不是我們選取的 county 則跳過
		# hint: 用 if-else 判斷並用 continue 跳過

	return specificBookstoreList

def getBookstoreInfo(items):
	expanderList = []
	for item in items:
		expander = st.expander(item['name'])
		expander.image(item['representImage'])
		expander.metric('hitRate', item['hitRate'])
		expander.subheader('Introduction')	
		expander.write('intro')	
		expander.subheader('Address')
		expander.write('address')
		expander.subheader('Open Time')
		expander.write('open Time')
		expander.subheader('Email')
		expander.write('email')
		expanderList.append(expander)
	return expanderList

def app():
	bookstoreList = getAllBookstore()
	countyOption = getCountyOption(bookstoreList)
	specificBookstore = getSpecificBookstore(bookstoreList,countyOption)
	st.header('特色書店地圖')
	st.metric('Total bookstore', len(bookstoreList))
	county = st.selectbox('請選擇縣市', countyOption) 
	#districtOption = getDistrictOption(bookstoreList, county)
	#district = st.multiselect('請選擇區域', districtOption) 
	
	# 呼叫 getSpecificBookstore 並將回傳值賦值給變數 specificBookstore
	num = len(specificBookstore)
	# 用 st.write 將目標書店的總數量計算出來，格式：總共有3項結果
	st.write(f'總共有{num}間書店',num)

	bookstoreInfo = getBookstoreInfo(specificBookstore)

if __name__ == '__main__':
    app()   

#python -m streamlit run app.py
#python3 -m streamlit run app.py
#stremlit run app.py