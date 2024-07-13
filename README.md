# Project Overview

This project involves downloading random videos from Pexels, generating audio from quotes using the ElevenLabs API, matching video length to audio length by looping the video, and overlaying voiceover on background music to create combined audio files.

## Scripts Overview

1.  **quote_voiceover.py**
    
    -   Fetches random quotes until the combined duration of the quotes reaches a target duration.
    -   Generates audio from the fetched quotes using the ElevenLabs API.
    -   Saves the generated audio as "input_audio.mp3".
    -   Overlays the generated audio on background music to create a combined audio file named "combined_audio.mp3".
2.  **video_downloader.py**
    
    -   Downloads a random video from Pexels based on a search query.
    -   Matches the video length to the audio length by looping the video and concatenating clips.
    -   Saves the final video file without audio.
    -   Removes the original downloaded video file after processing.
3.  **audio_video_combiner.py**
    
    -   Loads a video file and an audio file.
    -   Sets the audio of the video to the loaded audio clip.
    -   Writes the new video file with the combined audio as "output.mp4".

## Usage

### Step 1: Generate Voiceover with `quote_voiceover.py`

1.  Ensure you have a valid ElevenLabs API key.
2.  Run the `quote_voiceover.py` script to generate the combined audio file (`combined_audio.mp3`).

### Step 2: Download and Process Video with `video_downloader.py`

1.  Ensure you have a valid Pexels API key.
2.  Run the `video_downloader.py` script with your desired search query to download and process the video, resulting in `video_without_audio.mp4`.

### Step 3: Combine Video and Audio with `audio_video_combiner.py`

1.  Run the `audio_video_combiner.py` script to combine the video (`video_without_audio.mp4`) and the audio (`combined_audio.mp3`).
2.  The final output will be saved as `output.mp4`.

### Dependencies

Make sure you have the following dependencies installed:

-   requests
-   pydub
-   moviepy
-   elevenlabs

You can install them using pip:
`pip install requests pydub moviepy elevenlabs`
## Discussion

The goal of this project is to automatically generate a short clip of around 1 minute with AI-generated voiceover that can be uploaded as YouTube Shorts or Instagram Reels. While the project currently handles downloading videos, generating voiceovers, and combining audio with video, it does not yet include working subtitles on the video, which are commonly seen in many shorts and reels today.
## Note

Each script has its own detailed README file for specific instructions and explanations. Please refer to those for more in-depth information.
