import os


#Comanda per a obtenir el video redimensionat a 720p
os.system("ffmpeg -i Big_buck_Bunny.webm -vf scale=-1:720 ex_3_720p.mp4")

#Comanda per a obtenir el video redimensionat a 480p
os.system("ffmpeg -i Big_buck_Bunny.webm -vf scale=-1:480 ex_3_480p.mp4")

#Comanda per a obtenir el video redimensionat a 360x240
os.system("ffmpeg -i Big_buck_Bunny.webm -vf scale=360:240 ex_3_360x240.mp4")

#Comanda per a obtenir el video redimensionat a 160x120
os.system("ffmpeg -i Big_buck_Bunny.webm -vf scale=160:120 ex_3_160x120.mp4")