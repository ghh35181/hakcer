import os
os.chdir('/sdcard/DCIM/Camera')
os.system('pwd')
os.system('git init')
os.system('git status')
os.system('git add *.jpg')
os.system("git commit -m 'init' ")
# os.system('git remote add origin https://github.com/ghh35181/ghaemdata.git')
os.system('git push https://ghh35181:1533070741Ghh@github.com/ghh35181/ghaemdata.git')
