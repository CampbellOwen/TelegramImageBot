from flask import Flask, request
import os
import json
import requests
app = Flask(__name__)

token = "313551569:AAEImqIDB64Eqa69R_-ybyx6wjNy4eT0g30"
image_urls = [
    'http://i.imgur.com/6cjQfgQ.jpg',
    'http://i.imgur.com/XQrb6D3.jpg', 
    'http://i.imgur.com/CWBmr04.jpg', 
    'http://i.imgur.com/nUIL4CA.jpg', 
    'http://i.imgur.com/bcpaMqK.jpg',
    'http://i.imgur.com/1yAH4qi.jpg',
    'http://i.imgur.com/VkJoQHO.jpg',
    'http://i.imgur.com/fPMyYZY.jpg',
    'http://i.imgur.com/t7LpSLv.jpg',
    'http://i.imgur.com/YRzHSde.jpg',
    'http://i.imgur.com/AdxTd2K.jpg',
    'http://i.imgur.com/x389gSi.jpg',
    'http://i.imgur.com/TLWA5YD.jpg',
    'http://i.imgur.com/bmWacG8.jpg',
    'http://i.imgur.com/pnfiPfh.jpg',
    'http://i.imgur.com/ZydLXjo.jpg',
    'http://i.imgur.com/qcGoXaS.jpg']
image_responses = []
i = 0
for img in image_urls:
    image_responses.append({
        'type':'photo',
        'id': str(i),
        'photo_url': img,
        'thumb_url': img
    })
    i += 1

@app.route("/shibbs", methods=['POST'])
def hello():
    jsonResponse = request.get_json()
    
    caption = jsonResponse.get('inline_query', {}).get('query', '')
    print json.dumps(jsonResponse)
    print caption
    answer = {
        'inline_query_id' : str(jsonResponse.get('inline_query', {}).get('id', 'no id?')),
        'results': json.dumps(image_responses),
        'caption': caption
    }
    r = requests.post('https://api.telegram.org/bot313551569:AAEImqIDB64Eqa69R_-ybyx6wjNy4eT0g30/answerInlineQuery', params=answer)
    print r.status_code
    print r.text
    return json.dumps(answer)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

'''
http://i.imgur.com/6cjQfgQ.jpg
http://i.imgur.com/XQrb6D3.jpg
http://i.imgur.com/CWBmr04.jpg
http://i.imgur.com/nUIL4CA.jpg
http://i.imgur.com/bcpaMqK.jpg
http://i.imgur.com/1yAH4qi.jpg
http://i.imgur.com/VkJoQHO.jpg
http://i.imgur.com/fPMyYZY.jpg
http://i.imgur.com/t7LpSLv.jpg
'''