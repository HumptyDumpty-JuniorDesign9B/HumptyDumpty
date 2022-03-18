# Audio Subsystem

# Getting Started
Rasberry Pi Zero Setup: 
By Default the rasberry pi zero 2 does not Audio output pins set up properly so we need to do the following in order to get PWM audio signals from one of the GPIO 12/13. 
1. Edit `/boot/config.txt` and add the following so that the proper GPIO pins are configured whenever the Pi's OS boots up. Specifically this configues pins 12, 13 to their alternate 0 functionality which is PWM Audio
   ```bash 
   dtoverlay=audremap,pins_12_13
   ```
2. Go to the system settings and then audio settings and make sure the output is through headphones or PWM Audio
   ```bash
   sudo raspi-config
   ```
3. If everything was setup correctly, then you should see the following
   ```bash
   raspi-gpio get
   
   Output: 
   GPIO 12: level=0 fsel=4 alt=0 func=PWM0
   GPIO 13: level=1 fsel=4 alt=0 func=PWM1
   ```
4. Now you can connect either `pin12/13` to an audio amplifer which should be hooked up to a speaker
5. Make sure there is a wave file in the currentl directory. Run the following and you'll hear sounds. The default OS comes with sample ones but you can download some same ones into the current directory. 
   ```bash
   wget http://www.pacdv.com/sounds/people_sound_effects/applause-1.wav
   aplay applause-1.wav
   ```
6. See guide [here](https://www.bareconductive.com/blogs/resources/how-to-change-the-volume-on-the-pi-cap#:~:text=Use%20alsamixer&text=This%20will%20bring%20up%20an,you%20are%20done%2C%20press%20ESC) for adjusting volume or follow the datasheet of the class D Amp from Sparkfun [here](https://www.sparkfun.com/tutorials/392) for adjusting the volume of the amplifier output with a potentiometer. 
   
