import requests
import time
import concurrent.futures

def doSomething(delay):
	time.sleep(delay)
	response = requests.get('http://localhost:8082/hello/rishabh')
	if response.status_code == 200:
		print('Success!')
	elif response.status_code == 404:
		print('Not Found.')

for delay in range(6):
	with concurrent.futures.ThreadPoolExecutor() as executor:
		results = [executor.submit(doSomething,delay) for _ in range(delay)]

