import os

# Demanem a l'usuari el número de segons que vol tallar el video
N = int(input('Number of seconds that you want to cut de video: '))

# Tallem el BBB video en els N segons corresponents
os.system("ffmpeg -i Big_buck_Bunny.webm -ss 0 -t " + str(N) + " -c:v copy -c:a copy ex_1.mp4")




