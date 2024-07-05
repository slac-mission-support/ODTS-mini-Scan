import requests
parameters1 = {'userName':'anyusername', 'password':'anypassword'}
response = requests.post('https://qa-www-bis3.slac.stanford.edu/cardinalkey/Login',
	params=parameters1)
print(response)
