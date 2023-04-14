# -*- coding: utf8 -*-
import asyncio
import time
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from datetime import datetime, timedelta
import traceback
import json
from fake_useragent import UserAgent
import aiohttp
from requests.exceptions import ProxyError, ReadTimeout
import requests
import psycopg2
import sys
import asyncio
import websockets
from websockets import WebSocketClientProtocol
from requests.adapters import HTTPAdapter
from urllib3.poolmanager import PoolManager
from urllib3.util import ssl_
import ssl

async def produce(message: dict, host: str, port: int)-> None:
	async with websockets.connect(f'ws://{host}:{port}') as ws:

		await ws.send(json.dumps(message))
		await ws.recv()

if sys.version_info[0] == 3 and sys.version_info[1] >= 8 and sys.platform.startswith('win'):
	policy = asyncio.WindowsSelectorEventLoopPolicy()
	asyncio.set_event_loop_policy(policy)

CIPHERS = (
	'ECDHE-RSA-AES256-GCM-SHA384:'
	'ECDHE-ECDSA-AES256-GCM-SHA384:'
	'ECDHE-RSA-AES256-SHA384:'
	'ECDHE-ECDSA-AES256-SHA384:'
	'ECDHE-RSA-AES128-GCM-SHA256:'
	'ECDHE-RSA-AES128-SHA256:'
	'AES256-SHA'
)

class TlsAdapter(HTTPAdapter):

	def __init__(self, ssl_options=0, **kwargs):
		self.ssl_options = ssl_options
		super(TlsAdapter, self).__init__(**kwargs)

	def init_poolmanager(self, *pool_args, **pool_kwargs):
		ctx = ssl_.create_urllib3_context(ciphers=CIPHERS, cert_reqs=ssl.CERT_REQUIRED, options=self.ssl_options)
		self.poolmanager = PoolManager(*pool_args,ssl_context=ctx,**pool_kwargs)

	def proxy_manager_for(self, proxy, **proxy_kwargs):
		# This method is called when there is a proxy.
		ctx = ssl_.create_urllib3_context(ciphers=CIPHERS, cert_reqs=ssl.CERT_REQUIRED, options=self.ssl_options)
		#proxy_kwargs['ssl_version'] = ssl.PROTOCOL_TLSv1_2
		return super(TlsAdapter, self).proxy_manager_for(proxy, ssl_context=ctx, **proxy_kwargs)

session_ozon = requests.Session()
adapter = TlsAdapter(ssl.OP_NO_TLSv1 | ssl.OP_NO_TLSv1_2)

session_ozon.mount("https://", adapter)
headers_ozon={'User-Agent': 'ozonapp_android/14.8+1922'}
session_ozon.headers.update(headers_ozon)

r=requests.Session()
bot=Bot(token='5687566905:AAHx_g2eJ2ib1gfO2eNq7h23FR-UVcJvU5I',parse_mode='HTML')
dp= Dispatcher(bot, storage=MemoryStorage())

admin=692720806
#chanel1=-1001577598754
chanel=-1001581086637
chanelozon=-1001533193523
#chanelfree=-1001423241599
chat=-1001876004663

class color:
	PURPLE = '\033[1;35;48m'
	CYAN = '\033[1;36;48m'
	BOLD = '\033[1;37;48m'
	BLUE = '\033[1;34;48m'
	GREEN = '\033[1;32;48m'
	YELLOW = '\033[1;33;48m'
	RED = '\033[1;31;48m'
	BLACK = '\033[1;30;48m'
	UNDERLINE = '\033[4;37;48m'
	END = '\033[1;37;0m'

wbStocks = {
	117442: "Калуга",
	117501: "Подольск",
	117866: "Тамбов",
	117986: "Казань",
	1193: "Хабаровск",
	120762: "Электросталь",
	121709: "Электросталь",
	124731: "Крекшино",
	130744: "Краснодар",
	159402: "Санкт-Петербург",
	161812: "Санкт-Петербург",
	172430: "Барнаул",
	1733: "Екатеринбург",
	204615: "Томск",
	204939: "Нур-Султан",
	205104: "Ульяновск",
	205205: "Киров",
	205228: "Белая дача",
	206236: "Белые Столбы",
	206348: "Алексино",
	206708: "Новокузнецк",
	206844: "Калининград",
	206968: "Новосёлки",
	208277: "Невинномысск",
	208941: "Домодедово",
	209513: "Домодедово",
	210001: "Новосёлки-2",
	210515: "Вёшки",
	2737: "Санкт-Петербург",
	507: "Коледино",
	686: "Новосибирск"}

ra=requests.Session()
heareq={'Wb-AppType': 'android',
	'Wb-AppVersion': '476',
	'WB-AppLanguage': 'ru',
	'devicename': 'Android, Redmi 7(onc)',
	'deviceId': '615fe91fd32842d3',
	'serviceType': 'FB',
	'User-Agent': 'okhttp/4.9.3'}
with open('cookies.json') as f:
	ra.cookies.update(json.load(f))


data_table_old=[]

withsale=100

@dp.message_handler()
async def bla(message: types.Message):
	
	if message.chat.id==692720806:
		global withsale
		try:
			withsale=int(message.text)
			await bot.send_message(692720806,f'{withsale}')
		except Exception as ex:
			await bot.send_message(692720806,f'{ex}')
			
fl=0
def count():
	global fl
	if fl<19:
		fl+=1
	else:
		fl=0
	return fl	




proxies2=[
	['http://sBy3Xh:0vyr6SWR9a@109.248.129.224:1050'],
	['http://sBy3Xh:0vyr6SWR9a@45.15.237.80:1050'],
	['http://sBy3Xh:0vyr6SWR9a@45.140.52.222:1050'],
	['http://sBy3Xh:0vyr6SWR9a@212.115.49.195:1050'],
	['http://sBy3Xh:0vyr6SWR9a@193.53.168.71:1050'],
	['http://sBy3Xh:0vyr6SWR9a@45.139.176.211:1050'],
	['http://sBy3Xh:0vyr6SWR9a@45.140.54.175:1050'],
	['http://sBy3Xh:0vyr6SWR9a@45.147.193.11:1050'],
	['http://sBy3Xh:0vyr6SWR9a@45.140.55.156:1050'],
	['http://sBy3Xh:0vyr6SWR9a@45.134.180.210:1050'],
	['http://sBy3Xh:0vyr6SWR9a@77.83.84.210:1050'],
	['http://sBy3Xh:0vyr6SWR9a@188.130.187.160:1050'],
	['http://sBy3Xh:0vyr6SWR9a@45.140.53.154:1050'],
	['http://sBy3Xh:0vyr6SWR9a@84.54.53.166:1050'],
	['http://sBy3Xh:0vyr6SWR9a@45.144.36.167:1050'],
	['http://sBy3Xh:0vyr6SWR9a@46.8.57.82:1050'],
	['http://sBy3Xh:0vyr6SWR9a@194.35.113.14:1050'],
	['http://sBy3Xh:0vyr6SWR9a@193.58.168.218:1050'],
	['http://sBy3Xh:0vyr6SWR9a@95.182.124.25:1050'],
	['http://sBy3Xh:0vyr6SWR9a@45.145.119.90:1050']]

async def consumer_handler(websocket: WebSocketClientProtocol) -> None:
	async for message in websocket:
		data=json.loads(message)
		wp=['WP4', 'WP5', 'WP6', 'ozdet']
		if data['type'] not in wp:
			continue
		ws_sales.append(data)

ws_sales=[]

data_table_old_ozdet=[]
async def new_sales():

	global data_table_old, data_table_old_ozdet, ws_sales
	
	new_sale=[]

	for i in ws_sales:
		if i['type']=='ozdet':
			if 'ozon' in i['data']:
				new_sale.append(i['data'])
				data_table_old_ozdet.append(i['data'])
				continue
			if 'detmir' in i['data']:
				new_sale.append(i['data'])
				data_table_old_ozdet.append(i['data'])
				continue
		mas=i['data']
		try:
			if mas not in data_table_old:
				#if [mas[0],mas[-1]] not in [[x[0],x[-1]] for x in data_table_old]:
				if mas[-2] not in [x[-2] for x in data_table_old]:
					new_sale.append(mas)
					data_table_old.append(mas)
		except Exception as ex:
			print(ex)
			continue
	ws_sales=[]
	# if len(data_table_old)>5000:
	# 	data_table_old=[]
	# 	file = open(f"sales.txt", "w")
	# 	file.write(f'')
	# 	file.close()
	# end=time.time()
	# print(end-start)
	return new_sale




async def price_history(art):
	headers={'User-Agent': 'okhttp/4.9.3',
		'Wb-AppType': 'android',
		'Wb-AppVersion': '473'}
	try:
		async with aiohttp.ClientSession(trust_env=True) as session:
			async with session.get(f'https://wbx-content-v2.wbstatic.net/price-history/{art}.json?locale=ru', headers=headers, proxy=proxies2[count()][0]) as response:
				ca=await response.json(content_type=None)
				return ca
	except aiohttp.client_exceptions.ClientHttpProxyError:
		return await price_history(art)
	except aiohttp.client_exceptions.ServerDisconnectedError:
		return await price_history(art)
	except aiohttp.client_exceptions.ClientConnectorError:
		return await price_history(art)
	except asyncio.TimeoutError:
		return await price_history(art)

old_hours_percent=datetime.now()-timedelta(hours=2)
percent=0

async def percenti():
	global percent
	try:
		prox=proxies2[count()][0]
		
		re6=ra.get('https://napi.wildberries.ru/api/cabinet', headers=heareq, proxies={'http': prox.replace('sBy3Xh:0vyr6SWR9a@',''), 'https': prox})
		percent=int(re6.json()['data']['cabinetModel']['menu']['menuItems'][8]['text'].replace('%',''))
	except:
		return await percenti()


async def get_art(art):
	try:
		global products, old_hours_percent
		if (datetime.now()-old_hours_percent).seconds>=3600:
			old_hours_percent=datetime.now()
			await percenti()

		
		link=f'https://card.wb.ru/cards/detail?appType=32&curr=rub&dest=-1029256,-102269,-2162196,-1257786&emp=0&lang=ru&locale=ru&nm={art}%3B&pricemarginCoeff=1&pricemarginMax=0&pricemarginMin=0&reg=1&regions=1,4,22,30,31,33,38,40,48,64,66,68,69,70,71,75,80,83&spp={percent}&version=3'
		headers={'User-Agent': 'okhttp/4.9.3',
			'Wb-AppType': 'android',
			'Wb-AppVersion': '473'}
		async with aiohttp.ClientSession(trust_env=True) as session:
			async with session.get(link, headers=headers, proxy=proxies2[count()][0]) as response:
				return await response.json(content_type=None)

	except aiohttp.client_exceptions.ClientHttpProxyError:
		return await get_art(art)
	except aiohttp.client_exceptions.ServerDisconnectedError:
		return await get_art(art)
	except aiohttp.client_exceptions.ClientConnectorError:
		return await get_art(art)
	except asyncio.TimeoutError:
		return await get_art(art)
	except json.decoder.JSONDecodeError:
		return await get_art(art)

connection=None
async def connect_table():
	connection = psycopg2.connect(
		host='103.246.147.146',
		user='perseus',
		password='AezakmigetT2506&',
		database='salo'
	)
	connection.autocommit = True
	return connection


async def add_sale_in_table(name, brand, article, price, oldprice, col,sklad,diapazmin,diapazmax,rating,feedbacks, sizes, marketplace, linkphoto, subject):
	global connection
	if connection==None or connection.closed==1:
		connection=await connect_table()

	with connection.cursor() as cursor:
		cursor.execute(
				"INSERT INTO sales (name, brand, article, price, oldprice, col,sklad,diapazmin,diapazmax,rating,feedbacks, sizes,marketplace, linkphoto, subject) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",(name, brand, article, price, oldprice, col,sklad,diapazmin,diapazmax,rating,feedbacks, sizes, marketplace, linkphoto, subject)
			)


cookies={'ab2_90': 'ab2_90old90', 'ab2_33': 'ab2_33new33', 'ab2_50': '44', 'ab3_75': 'ab3_75old75', 'ab3_33': 'ab3_33new17', 'ab3_20': 'ab3_20_20_0', 'cc': '0', '_ym_uid': '1673456110888187582', '_ym_d': '1673456110', '_gcl_au': '1.1.902055810.1673456110', '_ga': 'GA1.2.51639142.1673456111', 'transactionId': '467a2b1e-2f4e-4635-b867-2911f89bbe61.0', 'transactionSubId': 'a04d6ceb-6504-4aac-842b-6ada538550e6.0', 'dm.screen': 'l', 'geoCityDM': '%D0%9C%D0%BE%D1%81%D0%BA%D0%B2%D0%B0%20%D0%B8%20%D0%BE%D0%B1%D0%BB%D0%B0%D1%81%D1%82%D1%8C', 'geoCityDMIso': 'RU-MOW', 'detmir-cart': '827feb96-edba-47e6-8232-c606477f9e73', 'auid': '9d07a9d0-ad87-469f-9aa1-2caaa9e557a3', 'advcake_track_id': '1096ba51-7290-397b-7b1a-6920312f36a3', 'advcake_session_id': '48a4a7b4-f219-2e00-0829-d5b95af5d09b', 'tmr_lvid': '0d2f88f2335cd8e119b02d877cfbbf0c', 'tmr_lvidTS': '1673456111280', 'flocktory-uuid': 'fc758afa-2796-4131-aec8-9e8ad93f96c9-5', 'popmechanic_sbjs_migrations': 'popmechanic_1418474375998%3D1%7C%7C%7C1471519752600%3D1%7C%7C%7C1471519752605%3D1', 'sp': '76de6a5b-e14a-4d74-bb11-9ebe0894bcbb', 'gdeslon.ru.__arc_domain': 'gdeslon.ru', 'gdeslon.ru.user_id': 'e66ab8e5-8dbd-4e67-9740-b42eb67e686f', 'qrator_msid': '1673560527.318.oqy05STacjIt5ilL-jtslqqlu037vprcd767raokn19obqjmo', '_sp_ses.2b21': '*', '_gid': 'GA1.2.556843032.1673560528', 'srv_id': 'cubic-front05-prod', '_ym_isad': '2', '_ym_visorc': 'w', 'adrdel': '1', 'adrcid': 'AWmyJ-apuaw0MX7ohxm06ow', 'mindboxDeviceUUID': '00c0d205-9efc-4660-9c84-a328b65cf3a5', 'directCrm-session': '%7B%22deviceGuid%22%3A%2200c0d205-9efc-4660-9c84-a328b65cf3a5%22%7D', 'JSESSIONID': 'a4421c10-2933-43be-b7e3-b94fb7073bea', 'dm_s': 'L-a4421c10-2933-43be-b7e3-b94fb7073bea|kH827feb96-edba-47e6-8232-c606477f9e73|Vj9d07a9d0-ad87-469f-9aa1-2caaa9e557a3|gqcubic-front05-prod|qa65d2377b-2b9a-4481-a9a6-2130cf0fc15a|-N1673456112112|RK1673560826041|1156938d55-a443-4639-bf71-c7e42dc03071#DmxheuxacNULP9JkbKovZ3SZJqJb-f73hiosK6zUI8I', '_gat': '1', '_gat_test': '1', '_sp_id.2b21': 'b703eb36-00fa-4387-a743-67365cafd972.1673456111.3.1673560827.1673462114.b10e7a16-f581-49ec-88b6-d59284a5a60f', 'tmr_detect': '0%7C1673560828823'}

with open('subjects2.json', encoding='utf-8') as f:
	subjects2=json.load(f)

async def generate_link_photo(art):
	art=str(art)
	BASKET_01 = "basket-01.wb.ru/"
	BASKET_02 = "basket-02.wb.ru/"
	BASKET_03 = "basket-03.wb.ru/"
	BASKET_04 = "basket-04.wb.ru/"
	BASKET_05 = "basket-05.wb.ru/"
	BASKET_06 = "basket-06.wb.ru/"
	BASKET_07 = "basket-07.wb.ru/"
	BASKET_08 = "basket-08.wb.ru/"
	BASKET_09 = "basket-09.wb.ru/"
	BASKET_10 = "basket-10.wb.ru/"
	basket=None
	if len(art)<=5:
		j=0
	else:
		j=int(art[:-5])
	z = True
	if 0 <= j and j < 144: basket= BASKET_01
	if 144 <= j and j < 288: basket= BASKET_02
	if 288 <= j and j < 432: basket= BASKET_03
	if 432 <= j and j < 720: basket= BASKET_04
	if 720 <= j and j < 1008: basket= BASKET_05
	if 1008 <= j and j < 1062: basket= BASKET_06
	if 1062 <= j and j < 1116: basket= BASKET_07
	if 1116 <= j and j < 1170: basket= BASKET_08
	if 1170 <= j and j < 1314: basket= BASKET_09
	if 1314 <= j and j < 1601: basket= BASKET_10
	# if basket==None:
	# 	if 1170 > j or j >= 1314: z = False
	# 	if z:basket= BASKET_09
	# 	else:basket= BASKET_01
	link_photo=f'https://{basket}vol{j}/part{art[:-3]}/{art}/images/c516x688/1.jpg'
	return link_photo

async def sorterP(i, sem):
	async with sem:
		start_time=time.time()
		if 'ozon' in i:
			
			try:
				art=i.split(' ')[1].replace('\n','')

				link=f'https://api.ozon.ru/composer-api.bx/page/json/v1?url=%2Fproducts%2F{art}%2F'
				products=session_ozon.get(link, proxies={'http': 'http://45.15.237.80:1050', 'https': 'http://sBy3Xh:0vyr6SWR9a@45.15.237.80:1050'}, timeout=3).json()
				

				price=products['pdp']['cartButton'][next(iter(products['pdp']['cartButton']))]['cellTrackingInfo']['finalPrice']
				try:
					oldprice=products['pdp']['cartButton'][next(iter(products['pdp']['cartButton']))]['cellTrackingInfo']['price']
					
				except:
					oldprice=''

				name=products['pdp']['cartButton'][next(iter(products['pdp']['cartButton']))]['cellTrackingInfo']['title']
				link_photo=products['pdp']['productMobile'][next(iter(products['pdp']['productMobile']))]['images'][0]['url']
				
				
				if oldprice=='':
					olp=0
					sal=int(100-(100/(price*3)*price))
					p=int(price)*3

					mesg=f'🤑 <b>{price}</b> <s>{p}₽</s> 🛍 {name}\n\n🔥 Скидка -{sal}%\n\nhttps://ozon.ru/context/detail/id/{art}/\n<i>все цифры актуальны на момент публикации</i>'
				else:
					
					sal=int(100-(100/oldprice*price))
					mesg=f'🤑 <b>{price}₽</b> <s>{oldprice}₽</s> 🛍 {name}\n\n🔥 Скидка -{sal}%\n\nhttps://ozon.ru/context/detail/id/{art}/\n<i>все цифры актуальны на момент публикации</i>'

				# await add_sale_in_table(name, art, int(price.replace('\xa0','').replace('₽','')), olp, 'oz', link_photo)

				#await produce(message=['oz',art, link_photo, mesg,start_time], host='185.241.53.162', port=1825)

				produce_messages.append(['oz',art, link_photo, mesg,start_time])

			except Exception as ex:
				print(ex)

			return

		if 'wbaezak ' in i:
			return
		if 'detmir' in i:
			try:
				art=i.split(' ')[1].replace('\n','')
				link=f'https://api.detmir.ru/v2/products/{art}?filter=withregion:RU-MOW&meta=true'
				headers={
					'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 YaBrowser/22.11.5.715 Yowser/2.5 Safari/537.36',
					'upgrade-insecure-requests': '1'}

				try:
					products= r.get(link, headers=headers, cookies=cookies, timeout=2).json()
				except ProxyError:
					products= r.get(link, headers=headers, cookies=cookies, timeout=2).json()
				except ReadTimeout:
					products= r.get(link, headers=headers, cookies=cookies, timeout=2).json()

				price=products['item']['price']['price']
				if products['item']['old_price']!=None:
					oldprice=products['item']['old_price']['price']
					oldprice=f'<s>{oldprice}₽</s>'
				else:
					oldprice=''

				name=products['item']['title']
				link_photo=products['item']['pictures'][0]['original']

				if oldprice=='':
					olp=0
					sal=int(100-(100/int(price*3)*int(price)))

					mesg=f'🤑 <b>{price}₽</b> <s>{p}₽</s> 🛍 {name}\n\n🔥 Скидка -{sal}%\n\nhttps://www.detmir.ru/product/index/id/{art}/\n<i>все цифры актуальны на момент публикации</i>'
				else:
					olp=products['item']['old_price']['price']
					sal=int(100-(100/int(olp)*int(price)))
					mesg=f'🤑 <b>{price}₽</b> {oldprice} 🛍 {name}\n\n🔥 Скидка -{sal}%\n\nhttps://www.detmir.ru/product/index/id/{art}/\n<i>все цифры актуальны на момент публикации</i>'

				# await add_sale_in_table(name, art, price, olp, 'dm', link_photo)

				
				
				#await produce(message=['dm', art, link_photo, mesg,start_time], host='185.241.53.162', port=1825)
				produce_messages.append(['dm', art, link_photo, mesg,start_time])
				
				return
				
			except Exception as ex:
				print(ex)

			return

		if ' SIM ' in i[0].upper() or 'Msklaser' in i[0].upper() or ' MOBILANDS ' in i[0].upper() or ' ЦФО ' in i[0].upper() or ' KINGSTON 64' in i[0].upper() or 'AKMIS' in i[0].upper() or ' RUICHI' in i[0].upper() or ' OEM' in i[0].upper() or ' DVD' in i[0].upper() or 'ПОСТЕР' in i[0].upper() or 'SIM-' in i[0].upper() or 'ANYMOLDS' in i[0].upper() or 'РОСДЮБЕЛЬ' in i[0].upper() or 'ОПРАВА ' in i[0].upper():
			print(f'{color.BLACK}black List {i}{color.END}')
			return
			
		if 'КРУЖКА' in i[0].upper() and int(i[3])>100:
			print(f'{color.BLACK}КРУЖКА {i}{color.END}')
			return
		

		art=int(i[2])

		p_his=await price_history(art)
		
		if p_his!=None:
			minp=int(min([his['price']['RUB'] for his in p_his])/100)
			maxp=int(max([his['price']['RUB'] for his in p_his])/100)
		checkproc=''
		if 'WP5' in i[0]:
			checkproc='/ WP5'
			pr=int(i[-1])
			if p_his==None:
				if pr > 300 or withsale<80:
					print(f'{color.BLACK}WP5 return {i}{color.END}')
					return
			else:
				if int(100/minp*pr)>withsale:
					print(f'{color.BLACK}WP5 {int(100/minp*pr)} {i}{color.END}')
					return

		if 'WP4' in i[0]:
			checkproc='/ WP4'
		if 'WP6' in i[0]:
			checkproc='/ WP6'
			
			
		products=await get_art(art)

		

		col=0
		sklads={'WB':0,'ПРОД':0}
		for counts in products['data']['products'][0]['sizes']:
			for count in counts['stocks']:
				col+=count['qty']
				if count['wh'] in wbStocks:
					sklads['WB']+=count['qty']
				else:
					sklads['ПРОД']+=count['qty']

		if col<1:
			print(f'{color.BLACK}{col} {art}{color.END}')
			return
		

		price=int(str(products['data']['products'][0]['salePriceU'])[:-2])
		#price=int(i[3])
		try:
			old_price=int(str(products['data']['products'][0]['priceU'])[:-2])
		except:
			old_price=0

		name=products["data"]["products"][0]["name"]
		brand=products["data"]["products"][0]["brand"]

		smile='🤑'
		
		if p_his!=None:
			diapaz=f'↔️ Диапазон: <b>{minp}</b> ₽ - {maxp} ₽\n'
			if price<minp:
				smile='📉'
			elif price<=maxp and price>=minp:
				smile='📊'
			else:
				smile='📈'
		else:
			diapaz=''

		oldpricestr=f'<s>{old_price}₽</s>'

		sklad=[]
		if sklads['WB']>0:
			sklad.append(f'<b>😍 WB - {sklads["WB"]}шт.</b>')
			
		if sklads['ПРОД']:
			sklad.append(f'<b>⚠️ ПРОД - {sklads["ПРОД"]}шт.</b>')
		
		skladd=" | ".join(sklad)
		sklad=f'🏢 Склад: {" | ".join(sklad)}'


		sizes=[]
		sizesdb=None
		for product in products['data']['products'][0]['sizes']:
			if product["name"]=='':
				continue
			colll=0
			for j in product['stocks']:
				colll+=j['qty']
			if colll!=0:
				sizes.append(f'<b>{product["name"]}</b>')
		if sizes!=[''] and sizes!='' and sizes!=[]:
			sizesdb= " | ".join(sizes).replace('<b>','').replace('</b>','')
			sizes=f'📏 Размеры: {" | ".join(sizes)}\n'
			
		else:
			sizes=''

		ratingseller=f'⭐️{products["data"]["products"][0]["rating"]} | 📝{products["data"]["products"][0]["feedbacks"]}'

		
		mesg=f'{smile} <b>{price}₽</b> {oldpricestr} 🛍 {name} / {brand}\n\n🔥 Скидка: -{int(100-(100/int(old_price)*int(price)))}%\n{sklad}\n{diapaz}{sizes}\n{ratingseller}\n\nhttps://wildberries.ru/catalog/{art}/detail.aspx <code>{checkproc}</code>\n<i>все цифры актуальны на момент публикации</i>'
		
		#link_photo=f'https://images.wbstatic.net/c516x688/new/{str(art)[:-4]}0000/{art}-1.jpg'
		link_photo=await generate_link_photo(art)
		link_photo_app=[]
		for pho in range(1,products['data']['products'][0]['pics']+1):
			link_photo_app.append(f'{link_photo.replace("1.jpg","")}{pho}.jpg')

		link_photo_app=','.join(link_photo_app)

		subject=products["data"]["products"][0]["subjectId"]
		kind=products["data"]["products"][0]["kindId"]
		if kind==0:
			if str(subject) not in subjects2:
				subject='Другое'
			else:
				subject=[sub for sub in subjects2[str(subject)]][0]
		else:
			if kind==1:
				subject='Мужчинам'
			elif kind==2:
				subject='Женщинам'
			elif kind==3:
				subject='Детям'
			elif kind==5:
				subject='Все для девочек'
			elif kind==6:
				subject='Все для мальчиков'
			else:
				subject='Другое'
		

		if p_his!=None:
			#await add_sale_in_table(name, brand, art, price, old_price, col, skladd, minp, maxp, products["data"]["products"][0]["rating"], products["data"]["products"][0]["feedbacks"],sizesdb, 'wb', link_photo_app,subject)

			produce_messages_app.append({'brand': brand, 'price': price, 'col': col, 'diapazmin': minp, 'rating': products["data"]["products"][0]["rating"], 'feedbacks': products["data"]["products"][0]["feedbacks"], 'marketplace': 'wb', 'subject': subject, 'article': art, 'name': name, 'oldprice': old_price, 'sklad': skladd, 'diapazmax': maxp, 'sizes': sizesdb, 'linkphoto': link_photo_app})

		else:
			#await add_sale_in_table(name, brand, art, price, old_price, col, skladd, None, None, products["data"]["products"][0]["rating"], products["data"]["products"][0]["feedbacks"], sizesdb, 'wb', link_photo_app,subject)

			produce_messages_app.append({'brand': brand, 'price': price, 'col': col, 'diapazmin': None, 'rating': products["data"]["products"][0]["rating"], 'feedbacks': products["data"]["products"][0]["feedbacks"], 'marketplace': 'wb', 'subject': subject, 'article': art, 'name': name, 'oldprice': old_price, 'sklad': skladd, 'diapazmax': None, 'sizes': sizesdb, 'linkphoto': link_photo_app})
		
		try:
			if col==1:
				#await produce(message=['wb1', art, link_photo, mesg, start_time], host='185.241.53.162', port=1825)
				produce_messages.append(['wb1', art, link_photo, mesg, start_time])
				return

			#await produce(message=['wb', art, link_photo, mesg, start_time], host='185.241.53.162', port=1825)

			produce_messages.append(['wb', art, link_photo, mesg, start_time])

		except Exception as ex:
			print(f'{color.UNDERLINE+color.RED}ОШИБКА:{color.END} {traceback.format_exc()}\n{color.UNDERLINE+color.BLUE}{art}{color.END}')
			
produce_messages=[]
produce_messages_app=[]
async def scheduled():
	global produce_messages, produce_messages_app
	while True:
		try:
			produce_messages=[]
			produce_messages_app=[]
			await asyncio.sleep(0.1)
			tasks=[]
			new_sals=await new_sales()
			sem = asyncio.Semaphore(100)
			if(new_sals):
				start=time.time()
				for i in new_sals:
					task=asyncio.Task(sorterP(i, sem))
					tasks.append(task)

				await asyncio.gather(*tasks)

				data={'type':'sale', 'data':produce_messages, 'dataApp':produce_messages_app}
				await produce(message=data, host='185.241.53.162', port=1825)
				end=time.time()
				print(f'Количество: {color.BLUE}{len(new_sals)}{color.END} | ВРЕМЯ: {color.UNDERLINE}{end-start}{color.END}')
				

		except Exception as ex:
			print(f'{color.UNDERLINE+color.RED}ОШИБКА:{color.END} {traceback.format_exc()}')



		

async def consume(hostname:str, port:int) -> None:
	websocket_resource_url= f'ws://{hostname}:{port}'
	async with websockets.connect(websocket_resource_url) as websocket:
		await consumer_handler(websocket)

if __name__ == '__main__':
	loop = asyncio.get_event_loop()
	loop.create_task(scheduled())
	loop.create_task(consume(hostname='185.241.53.162', port=1825))
	executor.start_polling(dp, skip_updates=True, loop=loop)


