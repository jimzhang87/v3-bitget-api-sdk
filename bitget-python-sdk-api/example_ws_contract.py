#!/usr/bin/python
from bitget.ws.bitget_ws_client import BitgetWsClient, SubscribeReq
from bitget import consts as c
import json
from datetime import datetime


def handle(message):
	msg_dict = json.loads(message)
	timestamp = msg_dict['ts'] / 1000
	dt_object = datetime.fromtimestamp(timestamp)
	formatted_date = dt_object.strftime('%Y-%m-%d %H:%M:%S')
	print(f"{formatted_date}handle:" + message)


def handle_error(message):
	print("handle_error:" + message)


if __name__== '__main__':
	api_key = "bg_d2ea6334ea4e0939f118d3009214aa61"
	secret_key = "d7bf6e2d0b1434550ea0e6c6bfecc0d453e1c1b4d5282bc57e91fb15166a4bb0"
	passphrase = "bg870422"
	#口令
	symbol = 'BTCUSDT'

	client = BitgetWsClient(c.CONTRACT_WS_URL,need_login=False)\
		.api_key(api_key)\
		.api_secret_key(secret_key)\
		.passphrase(passphrase)\
		.error_listener(handle_error)\
		.build()
	channels =[SubscribeReq(None, "ticker", "BTCUSDT"), SubscribeReq("SP", "candle1W", "BTCUSDT")]
	client.subscribe(channels, handle)
    
	# public_client = BitgetWsClient(c.CONTRACT_PUBLIC_WS_URL, need_login = False) \
	# .api_key(api_key) \
	# .api_secret_key(secret_key) \
	# .passphrase(passphrase) \
	# .error_listener(handle_error) \
	# .build()
    # channels =[SubscribeReq("USDT-FUTURES", "candle5m", "BTCUSDT")]
	# public_client.subscribe(channels, handle)


	# private_client = BitgetWsClient(c.CONTRACT_PRIVATE_WS_URL,need_login=True) \
	# .api_key(api_key) \
	# .api_secret_key(secret_key) \
	# .passphrase(passphrase) \
	# .error_listener(handle_error) \
	# .build()
	# channels =[SubscribeReq(None, "ticker", "BTCUSDT"), SubscribeReq("SP", "candle1W", "BTCUSDT")]
	# public_client.subscribe(channels, handle)


	# channels = [SubscribeReq('USDT-FUTURES','positions','default')]
	# private_client.subscribe(channels,handle)

	# channels = [SubscribeReq('USDT-FUTURES','account','default')]
	# private_client.subscribe(channels,handle)