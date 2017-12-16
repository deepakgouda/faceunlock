# Face Unlock
Add face unlock to your Linux lockscreen

To run this:


`git clone https://github.com/deepakgouda/faceunlock.git`

`cd faceunlock/Face\ Unlock/`

Place an image of your face in the _Face Unlock_ folder as 'user.jpg' or 
  - Uncomment a couple a lines as directed in _face_recog.py_.
  - Run the program by `python face_recog.py`
  - Comment out the couple of lines again.

Enter your password in _face_unlock.py_ as mentioned.

Run the bash script by `bash run.sh` and leave the process running.

Next time you lock your desktop, on recognising your face the lockscreen will be unlocked.

Precautions:
-The face recognition is not scale invariant. Works if your face is roughly at the same distance as that of _user.jpg_ .
-The face recognition works for frontal faces only.
-Change the read access of _face_unlock.py_ to keep your password safe.
-Keep it away from your Identical Twin.

To do:
- [ ] Add Scale Invariant Feature Transform.
- [ ] Add feature to detect profile faces.
