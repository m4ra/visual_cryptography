from __future__ import unicode_literals, absolute_import
from vck_py3 import *
import sys
import os

def quit(msg=""):
    print("USAGE: python {} mypicture.tif\n Error: {}.\n".format(sys.argv[0], msg))
    #print "USAGE: python %s mypicture.tif\n Error: %s.\n" % (sys.argv[0], msg)
    sys.exit()

try:
    filename = sys.argv[1]
except:
    quit("missing filename")

basename, ext = os.path.splitext(filename)
if ext == "":
    quit("Filename has no extension")
    
s1, s2 = splitImage(filename, basename + "_1" + ext, basename + "_2" + ext)
print(s2)

def display(root, share1=s1, share2=s2):
    # The function you pass to mainApp, which takes care of all the Tkinter
    # black magic, must take "root" (Tk's root window) as a parameter. It
    # must also return a tuple with all the windows it created.

    window1 = share1.view(root)
    window2 = share2.view(root)
    result = OR(share1, share2)
    expandedCiphertext = result.pixelcode()
    expandedCiphertext.write('result.tif')

    windowResult = result.view(root)
    return window1, window2, windowResult
    
mainApp(display)


