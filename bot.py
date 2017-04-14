from flask import Flask, request
import os
import json
import requests
import config
from imgurpython import ImgurClient

imgur_client = ImgurClient(config.imgur_client_id, config.imgur_client_secret)
app = Flask(__name__)

@app.route("/{0}".format(config.endpoint), methods=['POST'])
def hello():
    jsonResponse = request.get_json()
    print json.dumps(jsonResponse, indent=4)
    
    caption = jsonResponse.get('inline_query', {}).get('query', '')

    images = imgur_client.get_album_images(config.imgur_album_id)

    image_responses = []
    for image in images:
        image_responses.append({
            'type': 'photo',
            'id': image.id,
            'photo_url': image.link,
            'thumb_url': image.link,
            'caption': caption
        })

    answer = {
        'inline_query_id' : str(jsonResponse.get('inline_query', {}).get('id', 'no id?')),
        'results': json.dumps(image_responses)
    }
    r = requests.post('https://api.telegram.org/bot{0}/answerInlineQuery'.format(config.token), params=answer)
    print r.status_code
    return json.dumps(answer)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
