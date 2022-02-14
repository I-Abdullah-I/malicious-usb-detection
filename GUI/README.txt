1- create a virtual environment with python3 [3.9 recommended]
2- install "pyudev" using pip
3- run "detect_malicious.py" first then insert a USB stick
4- if your stick contains none of the malicious codes previously hashed in "digests.txt" you'll get a safe message
5- copy "malicious.py" to you USB stick
6- eject your USB stick
7- re-run the code again then mount the stick
8- you'll get a malicious message
