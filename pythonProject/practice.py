import requests
import time

def doSomething(delay):
	time.sleep(delay)
	for i in range (delay):
		response = requests.get('http://localhost:8082/hello/rishabh')
		if response.status_code == 200:
		    print('Success!')
		elif response.status_code == 404:
		    print('Not Found.')


if __name__ == "__main__":
	for i in range(10):
		doSomething(i)
