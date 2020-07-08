## raspberry-pi-cups
This sample code shows how to setup a CUPS print server on a raspberry pi (4) 
Why do we want to do this?
 1. Printer may not be network enabled
 2. Client OS may not have a driver (We connect to CUPS using Generic Postscript which should be ubiquitous) 
 3. High Availability .Eg can connect to a group of printers (See configuring a 'class' called 'all' in description below) 
 4. Printer network connection may be broken.

The reason why I connected my HP Deskjet 3050 J610 by USB cable to a raspberry pi running CUPS was because the printer  does not work from windows over the network with only the black cartridge installed but it does work via USB cable in 'Single Cartridge mode'

### Configuration
 1. Install docker on raspberry pi
 2. Run pi CUPS container (See [https://lemariva.com/blog/2019/02/raspberry-pi-cups-printer-server-using-docker](https://lemariva.com/blog/2019/02/raspberry-pi-cups-printer-server-using-docker)):
 ```console
 sudo docker run -d --restart unless-stopped -p 631:631 --privileged -v /var/run/dbus:/var/run/dbus -v /dev/bus/usb:/dev/bus/usb lemariva/rpi-cups
 ```
3. Open a browser to pi on port 631 and select 'Add Printer'
4. From discovered printers select 'USB' variant. eg
![cups1](https://github.com/KevinGoode/sundries/blob/master/raspberry-pi-cupts/images/cups1.jpg)
5. Select driver
![cups2](https://github.com/KevinGoode/sundries/blob/master/raspberry-pi-cupts/images/cups2.jpg)
6. Configure default options (BW/grayscale) (optional)
7. Configure a class and add printer to it. (optional) eg 'all'  (This is useful if want to add a group of printers and connect to group of them)
8. From windows (eg 10) go to control panel and add printer address
eg http://192.168.1.9:631/printers/HP_Deskjet_3050_J610_series. NB this uses the IPP protocol this should be already enabled in windows ( Control Panel/Programs/Turn Windows Features On/Print And Document Services/" switch on window features/Internet Printing Client) NB Samba is not installed in CUPS docker container so samba discovery will not work when adding a printer in control panel.
![cups3](https://github.com/KevinGoode/sundries/blob/master/raspberry-pi-cupts/images/cups3.jpg)
![cups4](https://github.com/KevinGoode/sundries/blob/master/raspberry-pi-cupts/images/cups4.jpg)
9. The 'Add Printer' wizard in windows control panel should connect to the CUPS server and then offer up a list of drivers. Whichever printer you are using simply select 'Generic/MS Published ImageSetter'. 
NOTE IF USING A LINUX CLIENT SUCH AS UBUNTU CHOOSE 'Generic Postscript'

