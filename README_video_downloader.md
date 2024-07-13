#  **Video Downloader and Audio Matcher**


## Description
---------------

This project provides a script to download a random video from Pexels based on a search query, match the video length to a given audio file by looping the video, and save the final video with the matched audio.

## Requirements
---------------

* PEXELS API key
* `requests` library installed
* `moviepy` library installed
* Ensure you have an audio file (`combined_audio.mp3` in this example) in the project directory or specify the correct path to your audio file.
## How to Use
--------------

1. You need a Pexels API key to fetch videos. Obtain your API key from Pexels and replace `YOUR API KEY HERE` in the script with your actual API key.
2. Run the script using Python (e.g., `python script.py`).
3. The script will generate a random video file.
4. The resulting video file will be saved as `video_without_audio.mp4`.

## Script Explanation
--------------------

### Video Generation

The `download_random_video` function downloads a random video based on a specified search query and saves it to a given folder.

### Match Video Length to Audio Length

The `match_audio_length` function loops the downloaded video to match the duration of a specified audio file and saves the final video with the matched audio.

### Remove the Original Video File

Optionally, you can remove the original downloaded video file after processing.

## Note
-----

-   Make sure to run `quote_voiceover.py` first to generate the `combined_audio.mp3`.
-   Ensure you have a stable internet connection to download videos from Pexels.
-   The script uses the first video file link available in the Pexels API response. You can modify the script to choose different resolutions if needed.
-   The script currently assumes the video file will be saved as `original.mp4`. Adjust the filename and path as necessary.

