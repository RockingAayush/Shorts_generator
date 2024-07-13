from moviepy.editor import VideoFileClip, AudioFileClip

# Load the video file
video_clip = VideoFileClip("video_without_audio.mp4")

# Load the audio file
audio_clip = AudioFileClip("output.mp3")

# Set the audio of the video to the loaded audio clip
video_clip = video_clip.set_audio(audio_clip)

# Write the new video file with the combined audio
video_clip.write_videofile("output.mp4", codec="libx264")
