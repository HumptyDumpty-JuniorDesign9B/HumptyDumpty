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
   raspi-config gpio get 
   raspi-gpio get
   
   Output: 
   GPIO 12: level=0 fsel=4 alt=0 func=PWM0
   GPIO 13: level=1 fsel=4 alt=0 func=PWM1
   ```
4. Now you can connect either `pin12/13` to an audio amplifer which should be hooked up to a speaker
5. Run the following and you'll hear sounds
   ```bash
   aplay Front_Left.wav
   ```
   
