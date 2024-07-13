# Audio Quote Generator and Overlayer


## Description
---------------

This script generates a random quote audio file using the ElevenLabs API and overlays it on a background music file. The resulting combined audio file is then saved to a new file.

## Requirements
---------------

* ElevenLabs API key
* `elevenlabs` library installed
* `requests` library installed
* `pydub` library installed
* Background music file named `background_music.mp3` in the same directory

## How to Use
--------------

1. Replace `api_key` with your actual ElevenLabs API key.
2. Run the script using Python (e.g., `python script.py`).
3. The script will generate a random quote audio file and overlay it on the background music file.
4. The resulting combined audio file will be saved as `combined_audio.mp3`.

## Script Explanation
--------------------

### Quote Generation

The script uses the `fetch_random_quote` function to fetch a random quote from the Quotable API. The `fetch_quotes_until_duration` function is used to fetch quotes until the total duration reaches the target duration (15 seconds in this case). The quotes are then joined together to form a single text string.

### Audio Generation

The script uses the ElevenLabs API to generate an audio file from the text string. The audio file is saved as `input_audio.mp3`.

### Audio Overlayer

The script uses the `pydub` library to load the voiceover and background music audio files. The background music is trimmed to match the length of the voiceover, and the voiceover volume is adjusted (optional). The voiceover is then overlaid on the background music, and the resulting combined audio file is exported as `combined_audio.mp3`.

## Note
-----

* Make sure to use mobile data while running this script to avoid any issues with the ElevenLabs API.
* Adjust the `target_duration` variable to change the length of the generated audio file.
* Adjust the `voiceover + 1` line to change the volume of the voiceover.
