import requests, os

def gib_url(permalink):
	full_url = "https://reddit.com"+permalink

	url = "https://url-shortener20.p.rapidapi.com/shorten"

	querystring = {"url":full_url}

	payload = {"url": full_url}
	headers = {
		"content-type": "application/json",
		"X-RapidAPI-Key": os.environ["X-RapidAPI-Key"],
		"X-RapidAPI-Host": "url-shortener20.p.rapidapi.com"
	}

	response = requests.request("POST", url, json=payload, headers=headers, params=querystring)
	keys = response.text.split(",")
	key1 = keys[0]
	key2 = key1.split("https:")
	key3 = key2[1]
	key4 = key3.replace("\/", "/")
	key5 = key4.replace(key4[-1], "")
	key6 = key5.replace("//", "")
	return key6
