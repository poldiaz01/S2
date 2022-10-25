import os

os.system('ffmpeg -i Big_buck_Bunny.webm -vf "split=2[a][b],[b]histogram,scale = 500:500,format=yuv420p[hh],[a][hh]overlay" '
          '-c:a copy videoplushistogram.mp4')

## Entrem l'input del video BBB
## Fem un split de la pantalla, [a] que serà el video i [b] que serà l'histograma
## Introduïm el tamany que volem que apareguin els histogrames
## També explicitem el format del histograma, yuv en aquest cas
## Per últim, ajuntem el video amb el histograma i ho guardem al nou fitxer videoplushistogram.mp4


