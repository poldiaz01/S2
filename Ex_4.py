import os

#Convertim el BBB video a mono
os.system("ffmpeg -i Big_buck_Bunny.webm -ac 1 mono.mp4")

#Convertim el BBB video en mono a stereo
os.system("ffmpeg -i mono.mp4 -ac 2 output_final.mp4")