from elevenlabs.client import ElevenLabs
from elevenlabs import save
from moviepy.editor import *
import os

api_key ="YOUR API KEY HERE"
client = ElevenLabs(api_key=api_key,)

text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum"


# text_to_speech(texto, "output.mp3")
def text_to_speech(client, text):
    audio = client.generate(text = text, voice = "Adam")
    return audio
    


def add_text_to_video(input_video, text, output_video):
  #Create temporary directory
  os.makedirs("tempaudio")
  video_clip = VideoFileClip(input_video)
  video_width, video_height = video_clip.size
  x_center = (video_width) / 2
  y_center = (video_height) / 2
  sentences = text.split('.')
  audio_clips = []
  text_clips =[]
  

#Create temporary audio clips
  for i,sentence in enumerate(sentences):
    audio_file = f"tempaudio/{output_video}_{i}.mp3"
    tts = text_to_speech(client,sentence)
    save(tts,audio_file)
    audio_clip = AudioFileClip(audio_file)
    audio_clips.append(audio_clip)
    print(audio_clip.duration)
#Create final audio clip
  audio_clip = concatenate_audioclips(audio_clips)

#Match the length of the video to the audio
  loops = int(audio_clip.duration/video_clip.duration) +1
  video_clips = [video_clip] * loops

#Create final video clip
  video_clip = concatenate_videoclips(video_clips)

#Create Text Clips
  for i,sentence in enumerate(sentences):
    text_clip = TextClip(sentence, fontsize=150, color='white', method= "caption", size= (video_width*5/6,None))
    print(x_center, y_center)
    text_clip = text_clip.set_position((x_center,y_center)).set_duration(audio_clips[i].duration)
    text_clips.append(text_clip)
    
#Create final text clip
  text_clip = concatenate_videoclips(text_clips).set_position(('center','center'))

#Compine audio and video
  video_clip = video_clip.set_audio(audio_clip)
    
#Combine text and video
  final_clip = CompositeVideoClip([video_clip, text_clip])

#save final video
  final_clip.write_videofile(output_video, codec='libx264', audio_codec='aac')

#Remove Temporary Files and Directories
  for i in range(len(sentences)):
    os.remove(f"tempaudio/{output_video}_{i}.mp3")
  os.rmdir("tempaudio")

add_text_to_video("original.mp4",text,"final_output.mp4")


  