from moviepy.editor import VideoFileClip

input_video = VideoFileClip("my_video.mp4")

final_clip = input_video.subclip(0,11)

final_clip.write_videofile("cut_video.mp4")