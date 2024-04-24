# Python-Mic-Volume-Capture

Code to monitor loudness
* It captures the mic input and determines the input volume level, and displays as a bar chart, for example to monitor the noise level in the room.
* This was a simple poc to capture how the level of noise coming from a room

Note: 
--------
* Running this in the built in terminal e.g. Pycharm will not produce the colored barchart.
* This has only been tested on Ubuntu Linux.

According to the GNU General Public License, any modifications made to this code must be openly shared. Therefore, we require that all changes be submitted via a pull request to ensure they benefit the entire community and comply with the GPL's requirements.
========================================

The following need to be installed.
========================================
* pip install -r requirements.txt

or run:
--------
* sudo apt-get install python3-pip  
* pip install colored   
* pip install numpy  
* sudo apt-get update -y  
* sudo apt-get install -y libportaudio2  
* pip install sounddevice 

 

Screen-shot of sound being measured and displayed in terminal.

![My Image](screen.png)