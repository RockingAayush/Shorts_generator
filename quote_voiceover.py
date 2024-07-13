from elevenlabs import Voice, VoiceSettings, play, save
from elevenlabs.client import ElevenLabs
import requests
import time
from pydub import AudioSegment
import os

# USE MOBILE DATA WHILE USING THIS

def fetch_random_quote():
    url = "https://api.quotable.io/random"
    response = requests.get(url)
    data = response.json()
    if data:
        content = data['content']
        author = data['author']
        return f"{content} - {author}"
    else:
        return "Failed to fetch a quote"

def fetch_quotes_until_duration(target_duration):
    quotes = []
    total_duration = 0
    while total_duration < target_duration:
        quote = fetch_random_quote()
        duration = len(quote.split()) * 0.15  # Assuming each word takes 0.15 seconds to say
        total_duration += duration
        quotes.append(quote)
    return quotes

api_key ="b127c6a4011c2ba000f5841920465dbd"
client = ElevenLabs(
  api_key=api_key, 
)

target_duration = 15  # Target duration in seconds

quotes = fetch_quotes_until_duration(target_duration)
text = "\n".join(quotes)

audio = client.generate(
    text = text,
    voice = "Adam"
)

save(audio, "input_audio.mp3")
print("Audio saved Successfully")



#AUDIO OVERLAYER

# Load the voiceover and background music audio files
voiceover = AudioSegment.from_file("input_audio.mp3")
background_music = AudioSegment.from_file("background_music.mp3")

# Trim the background music to match the length of the voiceover
background_music = background_music[:len(voiceover)]

# Adjust the volume of the voiceover (optional)
# Adjust the dB value as needed
voiceover = voiceover + 1

# Overlay the voiceover on the background music
combined_audio = background_music.overlay(voiceover)

# Export the combined audio to a file
combined_audio.export("combined_audio.mp3", format="mp3")

os.remove('input_audio.mp3')
print("Combined audio saved successfully.")
