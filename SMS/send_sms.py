import requests
resp = requests.post('https://textbelt.com/text', {
  'phone': '+48517142988',
  'message': 'sms z textbelt',
  'key': 'textbelt',
})
print(resp.json())