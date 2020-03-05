import requests

INSTAGRAM_API_URL = 'https://api.instagram.com/oembed'

params = {'url': 'https://www.instagram.com/p/B8OBgnyjoFk/?utm_source=ig_web_copy_link',
          'key': ''}


req = requests.get(INSTAGRAM_API_URL, params=params)

res = req.json()['title']

print(req.url)
print(res)
