# whatsapp-audio-transcriber
This app is a Twilio bot that transcribes Whatsapp audio messages. I made this as a challage in one and a half hours, including registration to the services.

The app functions as a Twilio webhook and runs on heroku. To set it up you need to create a Heroku app with python and ffmpeg (I used [this one](https://github.com/jonathanong/heroku-buildpack-ffmpeg-latest.git)) and set the Heroku url as the webhook url in the Twilio console.
