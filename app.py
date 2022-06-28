from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import requests
import speech_recognition as sr
import os


def convert_ogg_to_wav(file_name):
    import subprocess
    subprocess.call(['ffmpeg', '-i', file_name, file_name[:-4]+'.wav'])
    return file_name[:-4]+'.wav'

def download_file(url, file_name):
    r = requests.get(url, allow_redirects=True)
    open(file_name, 'wb').write(r.content)


def audio_to_text(file_name):
    r = sr.Recognizer()
    with sr.AudioFile(file_name) as source:
        audio = r.record(source)
    try:
        text = r.recognize_google(audio)
        return text
    except:
        return "Error"


app = Flask(__name__)


@app.route("/whatsapp", methods=["GET", "POST"])
def reply_whatsapp():
    try:
        media_url = request.values.get("MediaUrl0")
    except (ValueError, TypeError):
        return "Invalid request: invalid or missing NumMedia parameter", 400
    download_file(media_url, "audio.ogg")
    convert_ogg_to_wav("audio.ogg")
    text = audio_to_text(convert_ogg_to_wav("audio.ogg"))
    response = MessagingResponse()

    msg = response.message(str(text))
    os.remove("audio.wav")
    os.remove("audio.ogg")

    return str(response)


if __name__ == "__main__":
    app.run()
