import os
import random
import requests
from moviepy.editor import VideoFileClip, concatenate_videoclips, AudioFileClip

PEXELS_API_KEY = "YOUR API KEY HERE"

def download_random_video(query, folder_path):
    # Make a request to the Pexels API
    url = f"https://api.pexels.com/videos/search?query={query}&per_page=15"
    headers = {"Authorization": PEXELS_API_KEY}
    response = requests.get(url, headers=headers)
    
    # Check if the request was successful
    if response.status_code != 200:
        print("Failed to fetch videos from Pexels API.")
        return
    
    # Parse the response JSON
    data = response.json()
    
    # Check if any videos were found
    if not data["videos"]:
        print("No videos found for the given query.")
        return
    
    # Choose a random video from the list
    random_video = random.choice(data["videos"])
    video_url = random_video["video_files"][0]["link"]
    video_id = random_video["id"]
    video_name = f"original.mp4"  # You can adjust the filename as needed
    
    # Download the video
    video_response = requests.get(video_url)
    
    # Save the video to the folder
    with open(os.path.join(folder_path, video_name), 'wb') as f:
        f.write(video_response.content)
    
    print(f"Downloaded {video_name} successfully.")

def match_audio_length(video_path, audio_path, output_video_path):
    # Load video and audio clips
    video_clip = VideoFileClip(video_path)
    audio_clip = AudioFileClip(audio_path)
    
    # Calculate durations
    video_duration = video_clip.duration
    audio_duration = audio_clip.duration
    
    # Calculate number of times to loop the video
    loops = int(audio_duration / video_duration) + 1
    
    # Create a list of video clips
    video_clips = [video_clip] * loops
    
    # Concatenate video clips
    concatenated_clips = concatenate_videoclips(video_clips)
    
    # Set audio for the concatenated video
    final_clip = concatenated_clips.set_audio(audio_clip)
    
    # Write the final clip to a file
    final_clip.write_videofile(output_video_path, codec="libx264", audio_codec="aac")
    
    # Close the clips
    video_clip.close()
    final_clip.close()

# Example usage
search_query = "916 vertical nature"  # Your search query here
download_folder = ""  # Folder where videos will be saved
input_audio_path = "combined_audio.mp3"  # Path to input audio file
output_video_path = "video_without_audio.mp4"  # Output video path

# Download a random video
download_random_video(search_query, download_folder)

# Match video length to audio length and loop the video
match_audio_length("original.mp4", input_audio_path, output_video_path)

# Remove the original video file
os.remove("original.mp4")
