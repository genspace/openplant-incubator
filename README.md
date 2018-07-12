# OpenPlant Incubator

This project is to support the creation of an inexpensive plant incubator for the growth of liveworts (_Marchantia polymorpha_) which is the model system used by the [OpenPlant][1] collaboration. Our hope is that this design will allow a diverse array of (citizen) scientists cultivate plants under controlled conditions and potentially contribute to basic research.

## Incubator design

This design attempts to replicate the ideal conditions identified by Vujičić ([et al. 2010][2]) and reported by Chiyoda ([et al. 2008][3]). These conditions can be summarized as:

* 22°C
* 50-60 μmol photons/m<sup>2</sup>s (which for cool white fluorescent light equals 3700-4440 lux \[[Thimijan and Heins 1983][4]\])
* 16 h light, 8 h dark cycle

Furthermore we would like this project to be a relatively simple build so in general we are using well documented components from [Adafruit][5]. However the use of a wide array of purchased or scavenged parts is encouraged. We will describe the parts and their interaction with code in the "Description of parts" section, so jump there if you're trying to make a substitution(s).

## Description of files

What follows is a description of the code used in this project. We recommend branches (and forks) to incorporate alternate hardware. The raspberry_pi branch is currently in development to incorporate remote monitoring by reading off the data the microcontroller sends out via USB serial connection.

### Test_data

## Description of parts

* Microcontroller [Metro Mini][7]
	This is an ATmega328 based microcontroller like the Arduino UNO. We chose this particular board because it has many GPIO pins and it fits nicely into a breadboard for when I was prototyping.The USB support allows is to easily program it over USB and send data out via this connection. It's also important that it has a 5V regulator to power the sensors. I'm also controlling the fans using the "blue" PWM wire which is specified at 24kHz which can be achieved by modifying the internal registers (see the code).
* Real time clock [PCF8523][8]
	
* LED

LED		https://www.amazon.com/gp/product/B00NFBG1O0/ref=oh_aui_detailpage_o02_s02?ie=UTF8&psc=1
BUCK		https://www.amazon.com/gp/product/B01MQGMOKI/ref=oh_aui_detailpage_o04_s01?ie=UTF8&psc=1
TEMP		https://www.adafruit.com/product/2857
LIGHT		https://www.adafruit.com/product/439
SD		https://www.adafruit.com/product/254
PELTIER		https://www.amazon.com/Glamorway-TEC1-12706-Thermoelectric-Cooling-Peltier/dp/B00IKDL22O/
FAN & HEATSINK	https://www.amazon.com/Intel-LGA115x-CPU-Heatsink-E97379-003/dp/B01MSD39CN
BOX		https://www.mrboxonline.com/16375x115x6-quart-styrofoam-cooler-p-47940.html
FOAM SHIM	https://www.michaels.com/12x18-foam-sheet-by-creatology/M10597609.html
THERMAL PASTE	https://www.newegg.com/Product/Product.aspx?Item=N82E16835103080
DIFFUSER	https://www.inventables.com/technologies/light-diffuser-film-rolls
DOWLING		https://www.homedepot.com/p/Builder-s-Choice-1-4-in-x-36-in-Oak-Round-Dowel-HDDO1436/206184687
SCREWS		https://www.homedepot.com/p/Everbilt-Zinc-Plated-Machine-Screw-Kit-405-Piece-803264/205949025
HEADERS		https://www.sparkfun.com/products/10007
WIRE WRAP	https://www.jameco.com/z/901-0-Wire-Wrap-Kynar-Black-100-Feet-30AWG-100-Foot-Rolls-_22577.html
WRAP TOOL	https://www.jameco.com/z/HSM30-JDV-Products-Strip-Wrap-Unwrap-Tool_34585.html?CID=MERCH

## Future development

Some ideas and priorities for future work on this project

1. protect the circuit from failure with some capacitors and diodes to prevent back voltages and spikes
	* I notice that when the fans get touched (and the inductive load slowed) the clock time gets messed up
2. definitively decide if the PID parameters are properly tuned
3. introduce heating control via an H-bridge to switch the voltage polarity on the peliters
	* I was originally going to use cheap [motor drivers][6] from Amazon, but the peltiers use more current than they are rated for
4. complete an initialization script which incorporates unit tests

[1]: https://www.openplant.org/ (openplant homepage)
[2]: http://www.pmf.kg.ac.rs/kjs/volumes/kjs32/kjs32vujiciccvetic73.pdf (vujicic paper)
[3]: https:/dx.doi.org/10.1007/s00299-008-0570-5 (chiyoda paper)
[4]: http://agris.fao.org/agris-search/search.do?recordID=US19850000983 (thimijan paper)
[5]: https://www.adafruit.com/ (adafruit homepage)
[6]: https://www.amazon.com/gp/product/B077P1D41F (motor drivers)
[7]: https://www.adafruit.com/product/2590 (metro mini)
[8]: https://www.adafruit.com/product/3295 (PCF8523)
