Visual Cryptography modified for python 2.7
Original source: 
http://www.cl.cam.ac.uk/~fms27/vck/
(c) 1998 Olivetti Oracle Research Laboratory (ORL)

Visual cryptography concept invented by Moni Naor & Adi Shamir

VCK is copyrighted free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License version 3 as
published by the Free Software Foundation.
See the file LICENSE.  
https://www.gnu.org/licenses/gpl-3.0-standalone.html

------------------------------------------------------------

To play around with your own messages: run 

   python vck-split-mono.py message.tif

to have message.tif (which must be a 1-bit-deep bitmap, but doesn't have
to be tif) split into two bitmap "shares" that will recreate the original
when superimposed. (You must photocopy them onto transparency first.) The
program will not only generate the two shares as files but will also
display them in little windows for you. It will also show a third window
with what you should ideally obtain by overlapping the transparencies.

Note that, due to limitations in the process of photocopying onto
transparency, the best results are obtained with comparatively low
resolution pictures (of the order of 50 pixels across), since these suffer
less from alignment problems.


For greyscale, do

   python vck-split-grey.py message.tif

to have message.tif (which now must be a 256-bit-deep greyscale image,
but again doesn't have to be tif) split into two postscript "shares".


For more experiments (including viewing the intermediate results and so on)
run

    python vck.py

on its own; it will perform one of its many self-tests/demos. To choose
another one, edit the source (you can do this even if you don't speak
Python) and, at the very bottom of vck.py, in the bit that looks like this...

if __name__ == "__main__":
#    mainApp(testBooleanOps)
    mainApp(testEncryptDecrypt)
#    mainApp(testAllIntermediateValues)
#    mainApp(testGrey)
#    mainApp(testSplitImage)
#    mainApp(testSplitImageG)

...add a # to the mainApp line that doesn't have one, and remove it from
another one of your choice. (Be sure NOT to insert any tab characters in
the file or you may regret it.)

------------------------------------------------------------

