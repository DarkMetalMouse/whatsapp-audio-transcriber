# whatsapp-audio-transcriber
This app is a Twilio bot that transcribes WhatsApp audio messages. I made this as a challenge in one and a half hours, including registration to the services.

The app functions as a Twilio webhook and runs on Heroku. To set it up you need to create a Heroku app with python and ffmpeg (I used [this one](https://github.com/jonathanong/heroku-buildpack-ffmpeg-latest.git)) and set the Heroku url as the webhook url in the Twilio console.
