# TelegramImageBot

Needs a "config.py" file in the same directory with variables:
  - token: Telegram API bot token
  - endpoint: The name of the endpoint you want telegram to hit 
      - must also set this up with telegram: GET to https://api.telegram.org/bot{token}/setWebhook?url={url}/{endpoint}
  - imgur_album_id: the id of the album to grab the images from
  - imgur_client_id: imgur API client id
  - imgur_client_secret: imgur API client secret
