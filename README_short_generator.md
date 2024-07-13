# Text-to-Speech and Video Captioning

This project uses the ElevenLabs API to convert text to speech and adds the resulting audio and corresponding text captions to a video.

## Requirements

- Python 3.x
- moviepy
- ElevenLabs

## Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/your-repo/text-to-speech-video-captioning.git
    cd text-to-speech-video-captioning
    ```

2. Install the required packages:
    ```bash
    pip install moviepy elevenlabs
    ```

## Usage

1. Set your ElevenLabs API key:
    ```python
    api_key = "YOUR API KEY HERE"
    client = ElevenLabs(api_key=api_key)
    ```

2. Update the `text` variable with the text you want to convert to speech and add to the video:
    ```python
    text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry..."
    ```

3. Use the `add_text_to_video` function to add the text-to-speech audio and captions to your video:
    ```python
    add_text_to_video("original.mp4", text, "final_output.mp4")
    ```

## Functions

### `text_to_speech(client, text)`
Generates speech from text using ElevenLabs API.

- **Parameters:**
  - `client`: ElevenLabs API client
  - `text`: Text to convert to speech

- **Returns:**
  - `audio`: Generated audio clip

### `add_text_to_video(input_video, text, output_video)`
Adds the text-to-speech audio and text captions to the input video.

- **Parameters:**
  - `input_video`: Path to the input video file
  - `text`: Text to convert to speech and add as captions
  - `output_video`: Path to save the output video file

- **Functionality:**
  - Creates temporary audio clips for each sentence
  - Concatenates audio clips and matches the video length
  - Creates text clips for each sentence
  - Combines audio, text, and video into the final output video
  - Removes temporary files and directories
