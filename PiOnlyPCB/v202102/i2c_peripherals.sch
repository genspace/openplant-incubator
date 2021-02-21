EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 8 8
Title ""
Date ""
Rev ""
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L Interface_Expansion:PCF8574 U?
U 1 1 60399913
P 6500 4100
AR Path="/60399913" Ref="U?"  Part="1" 
AR Path="/6038F42F/60399913" Ref="U3"  Part="1" 
F 0 "U3" H 6500 4981 50  0000 C CNN
F 1 "PCF8574" H 6500 4890 50  0000 C CNN
F 2 "Package_SO:SOIC-16W_7.5x10.3mm_P1.27mm" H 6500 4100 50  0001 C CNN
F 3 "http://www.nxp.com/documents/data_sheet/PCF8574_PCF8574A.pdf" H 6500 4100 50  0001 C CNN
	1    6500 4100
	1    0    0    -1  
$EndComp
$Comp
L Interface_Expansion:PCF8574 U?
U 1 1 60399919
P 6450 2050
AR Path="/60399919" Ref="U?"  Part="1" 
AR Path="/6038F42F/60399919" Ref="U2"  Part="1" 
F 0 "U2" H 6450 2931 50  0000 C CNN
F 1 "PCF8574" H 6450 2840 50  0000 C CNN
F 2 "Package_SO:SOIC-16W_7.5x10.3mm_P1.27mm" H 6450 2050 50  0001 C CNN
F 3 "http://www.nxp.com/documents/data_sheet/PCF8574_PCF8574A.pdf" H 6450 2050 50  0001 C CNN
	1    6450 2050
	1    0    0    -1  
$EndComp
$Comp
L Connector_Generic:Conn_01x04 J?
U 1 1 6039F558
P 2850 2200
AR Path="/6039F558" Ref="J?"  Part="1" 
AR Path="/6038F42F/6039F558" Ref="J4"  Part="1" 
F 0 "J4" H 2930 2192 50  0000 L CNN
F 1 "Conn_01x04" H 2930 2101 50  0000 L CNN
F 2 "Connector_JST:JST_SH_BM04B-SRSS-TB_1x04-1MP_P1.00mm_Vertical" H 2850 2200 50  0001 C CNN
F 3 "~" H 2850 2200 50  0001 C CNN
	1    2850 2200
	1    0    0    -1  
$EndComp
Text GLabel 2400 2200 0    50   Input ~ 0
VCC3V3
Text GLabel 2400 2100 0    50   Input ~ 0
GND
Text GLabel 2400 2300 0    50   Input ~ 0
GPIO2_I2C1_SDA
Text GLabel 2400 2400 0    50   Input ~ 0
GPIO2_I2C1_SCL
Wire Wire Line
	2400 2100 2650 2100
Wire Wire Line
	2650 2200 2400 2200
Wire Wire Line
	2400 2300 2650 2300
Wire Wire Line
	2650 2400 2400 2400
$Comp
L Connector_Generic:Conn_01x04 J?
U 1 1 6039F566
P 2850 2700
AR Path="/6039F566" Ref="J?"  Part="1" 
AR Path="/6038F42F/6039F566" Ref="J5"  Part="1" 
F 0 "J5" H 2930 2692 50  0000 L CNN
F 1 "Conn_01x04" H 2930 2601 50  0000 L CNN
F 2 "Connector_JST:JST_SH_BM04B-SRSS-TB_1x04-1MP_P1.00mm_Vertical" H 2850 2700 50  0001 C CNN
F 3 "~" H 2850 2700 50  0001 C CNN
	1    2850 2700
	1    0    0    -1  
$EndComp
Text GLabel 2400 2700 0    50   Input ~ 0
VCC3V3
Text GLabel 2400 2600 0    50   Input ~ 0
GND
Text GLabel 2400 2800 0    50   Input ~ 0
GPIO2_I2C1_SDA
Text GLabel 2400 2900 0    50   Input ~ 0
GPIO2_I2C1_SCL
Wire Wire Line
	2400 2600 2650 2600
Wire Wire Line
	2650 2700 2400 2700
Wire Wire Line
	2400 2800 2650 2800
Wire Wire Line
	2650 2900 2400 2900
$Comp
L Connector_Generic:Conn_01x04 J?
U 1 1 6039F574
P 2850 3150
AR Path="/6039F574" Ref="J?"  Part="1" 
AR Path="/6038F42F/6039F574" Ref="J6"  Part="1" 
F 0 "J6" H 2930 3142 50  0000 L CNN
F 1 "Conn_01x04" H 2930 3051 50  0000 L CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x04_P2.54mm_Vertical" H 2850 3150 50  0001 C CNN
F 3 "~" H 2850 3150 50  0001 C CNN
	1    2850 3150
	1    0    0    -1  
$EndComp
Text GLabel 2400 3150 0    50   Input ~ 0
VCC3V3
Text GLabel 2400 3050 0    50   Input ~ 0
GND
Text GLabel 2400 3250 0    50   Input ~ 0
GPIO2_I2C1_SDA
Text GLabel 2400 3350 0    50   Input ~ 0
GPIO2_I2C1_SCL
Wire Wire Line
	2400 3050 2650 3050
Wire Wire Line
	2650 3150 2400 3150
Wire Wire Line
	2400 3250 2650 3250
Wire Wire Line
	2650 3350 2400 3350
$Comp
L Connector_Generic:Conn_01x04 J?
U 1 1 6039F582
P 2850 3600
AR Path="/6039F582" Ref="J?"  Part="1" 
AR Path="/6038F42F/6039F582" Ref="J7"  Part="1" 
F 0 "J7" H 2930 3592 50  0000 L CNN
F 1 "Conn_01x04" H 2930 3501 50  0000 L CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x04_P2.54mm_Vertical" H 2850 3600 50  0001 C CNN
F 3 "~" H 2850 3600 50  0001 C CNN
	1    2850 3600
	1    0    0    -1  
$EndComp
Text GLabel 2400 3600 0    50   Input ~ 0
VCC3V3
Text GLabel 2400 3500 0    50   Input ~ 0
GND
Text GLabel 2400 3700 0    50   Input ~ 0
GPIO2_I2C1_SDA
Text GLabel 2400 3800 0    50   Input ~ 0
GPIO2_I2C1_SCL
Wire Wire Line
	2400 3500 2650 3500
Wire Wire Line
	2650 3600 2400 3600
Wire Wire Line
	2400 3700 2650 3700
Wire Wire Line
	2650 3800 2400 3800
Text GLabel 6150 2750 0    50   Input ~ 0
GND
Text GLabel 5650 1750 1    50   Input ~ 0
GPIO2_I2C1_SDA
Text GLabel 5800 1650 1    50   Input ~ 0
GPIO2_I2C1_SCL
Wire Wire Line
	6150 2750 6450 2750
Text GLabel 6500 5000 0    50   Input ~ 0
GND
Wire Wire Line
	6500 5000 6500 4800
Text GLabel 6300 3400 0    50   Input ~ 0
VCC3V3
Wire Wire Line
	6300 3400 6500 3400
Text GLabel 6250 1350 0    50   Input ~ 0
VCC3V3
Wire Wire Line
	6250 1350 6450 1350
Text GLabel 5650 3800 1    50   Input ~ 0
GPIO2_I2C1_SDA
Text GLabel 5800 3700 1    50   Input ~ 0
GPIO2_I2C1_SCL
Wire Wire Line
	4800 2400 4800 2450
Wire Wire Line
	4800 1900 4800 2150
Wire Wire Line
	4800 1700 4800 1600
Text GLabel 4800 1600 1    50   Input ~ 0
VCC3V3
Text GLabel 4800 2450 3    50   Input ~ 0
GND
$Comp
L Device:R_Small R47
U 1 1 603BF5EB
P 4800 2300
F 0 "R47" H 4741 2254 50  0000 R CNN
F 1 "R_Small" H 4741 2345 50  0000 R CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.20x1.40mm_HandSolder" H 4800 2300 50  0001 C CNN
F 3 "~" H 4800 2300 50  0001 C CNN
	1    4800 2300
	-1   0    0    1   
$EndComp
$Comp
L Device:R_Small R46
U 1 1 603BDB78
P 4800 1800
F 0 "R46" H 4741 1754 50  0000 R CNN
F 1 "R_Small" H 4741 1845 50  0000 R CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.20x1.40mm_HandSolder" H 4800 1800 50  0001 C CNN
F 3 "~" H 4800 1800 50  0001 C CNN
	1    4800 1800
	-1   0    0    1   
$EndComp
Wire Wire Line
	4550 2400 4550 2450
Wire Wire Line
	4550 1900 4550 2050
Wire Wire Line
	4550 1700 4550 1600
Text GLabel 4550 1600 1    50   Input ~ 0
VCC3V3
Text GLabel 4550 2450 3    50   Input ~ 0
GND
$Comp
L Device:R_Small R43
U 1 1 603D0165
P 4550 2300
F 0 "R43" H 4491 2254 50  0000 R CNN
F 1 "R_Small" H 4491 2345 50  0000 R CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.20x1.40mm_HandSolder" H 4550 2300 50  0001 C CNN
F 3 "~" H 4550 2300 50  0001 C CNN
	1    4550 2300
	-1   0    0    1   
$EndComp
$Comp
L Device:R_Small R42
U 1 1 603D016F
P 4550 1800
F 0 "R42" H 4491 1754 50  0000 R CNN
F 1 "R_Small" H 4491 1845 50  0000 R CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.20x1.40mm_HandSolder" H 4550 1800 50  0001 C CNN
F 3 "~" H 4550 1800 50  0001 C CNN
	1    4550 1800
	-1   0    0    1   
$EndComp
Wire Wire Line
	4300 2400 4300 2450
Wire Wire Line
	4300 1900 4300 1950
Wire Wire Line
	4300 1700 4300 1600
Text GLabel 4300 1600 1    50   Input ~ 0
VCC3V3
Text GLabel 4300 2450 3    50   Input ~ 0
GND
$Comp
L Device:R_Small R39
U 1 1 603D407E
P 4300 2300
F 0 "R39" H 4241 2254 50  0000 R CNN
F 1 "R_Small" H 4241 2345 50  0000 R CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.20x1.40mm_HandSolder" H 4300 2300 50  0001 C CNN
F 3 "~" H 4300 2300 50  0001 C CNN
	1    4300 2300
	-1   0    0    1   
$EndComp
$Comp
L Device:R_Small R38
U 1 1 603D4088
P 4300 1800
F 0 "R38" H 4241 1754 50  0000 R CNN
F 1 "R_Small" H 4241 1845 50  0000 R CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.20x1.40mm_HandSolder" H 4300 1800 50  0001 C CNN
F 3 "~" H 4300 1800 50  0001 C CNN
	1    4300 1800
	-1   0    0    1   
$EndComp
Wire Wire Line
	4800 4450 4800 4500
Wire Wire Line
	4800 3750 4800 3650
Text GLabel 4800 3650 1    50   Input ~ 0
VCC3V3
Text GLabel 4800 4500 3    50   Input ~ 0
GND
$Comp
L Device:R_Small R49
U 1 1 6041B9C2
P 4800 4350
F 0 "R49" H 4741 4304 50  0000 R CNN
F 1 "R_Small" H 4741 4395 50  0000 R CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.20x1.40mm_HandSolder" H 4800 4350 50  0001 C CNN
F 3 "~" H 4800 4350 50  0001 C CNN
	1    4800 4350
	-1   0    0    1   
$EndComp
$Comp
L Device:R_Small R48
U 1 1 6041B9CC
P 4800 3850
F 0 "R48" H 4741 3804 50  0000 R CNN
F 1 "R_Small" H 4741 3895 50  0000 R CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.20x1.40mm_HandSolder" H 4800 3850 50  0001 C CNN
F 3 "~" H 4800 3850 50  0001 C CNN
	1    4800 3850
	-1   0    0    1   
$EndComp
Wire Wire Line
	4550 4450 4550 4500
Wire Wire Line
	4550 3750 4550 3650
Text GLabel 4550 3650 1    50   Input ~ 0
VCC3V3
Text GLabel 4550 4500 3    50   Input ~ 0
GND
$Comp
L Device:R_Small R45
U 1 1 6041B9DB
P 4550 4350
F 0 "R45" H 4491 4304 50  0000 R CNN
F 1 "R_Small" H 4491 4395 50  0000 R CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.20x1.40mm_HandSolder" H 4550 4350 50  0001 C CNN
F 3 "~" H 4550 4350 50  0001 C CNN
	1    4550 4350
	-1   0    0    1   
$EndComp
$Comp
L Device:R_Small R44
U 1 1 6041B9E5
P 4550 3850
F 0 "R44" H 4491 3804 50  0000 R CNN
F 1 "R_Small" H 4491 3895 50  0000 R CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.20x1.40mm_HandSolder" H 4550 3850 50  0001 C CNN
F 3 "~" H 4550 3850 50  0001 C CNN
	1    4550 3850
	-1   0    0    1   
$EndComp
Wire Wire Line
	4300 4450 4300 4500
Wire Wire Line
	4300 3950 4300 4000
Wire Wire Line
	4300 3750 4300 3650
Text GLabel 4300 3650 1    50   Input ~ 0
VCC3V3
Text GLabel 4300 4500 3    50   Input ~ 0
GND
$Comp
L Device:R_Small R41
U 1 1 6041B9F4
P 4300 4350
F 0 "R41" H 4241 4304 50  0000 R CNN
F 1 "R_Small" H 4241 4395 50  0000 R CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.20x1.40mm_HandSolder" H 4300 4350 50  0001 C CNN
F 3 "~" H 4300 4350 50  0001 C CNN
	1    4300 4350
	-1   0    0    1   
$EndComp
$Comp
L Device:R_Small R40
U 1 1 6041B9FE
P 4300 3850
F 0 "R40" H 4241 3804 50  0000 R CNN
F 1 "R_Small" H 4241 3895 50  0000 R CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.20x1.40mm_HandSolder" H 4300 3850 50  0001 C CNN
F 3 "~" H 4300 3850 50  0001 C CNN
	1    4300 3850
	-1   0    0    1   
$EndComp
Wire Wire Line
	5700 4500 5600 4500
Text GLabel 5600 4500 0    50   Input ~ 0
VCC3V3
$Comp
L Device:R_Small R55
U 1 1 6041BA17
P 5800 4500
F 0 "R55" H 5741 4454 50  0000 R CNN
F 1 "R_Small" H 5741 4545 50  0000 R CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.20x1.40mm_HandSolder" H 5800 4500 50  0001 C CNN
F 3 "~" H 5800 4500 50  0001 C CNN
	1    5800 4500
	0    1    1    0   
$EndComp
Wire Wire Line
	5950 1950 4300 1950
Connection ~ 4300 1950
Wire Wire Line
	4300 1950 4300 2200
Wire Wire Line
	5950 2050 4550 2050
Connection ~ 4550 2050
Wire Wire Line
	4550 2050 4550 2200
Wire Wire Line
	5900 4500 6000 4500
Wire Wire Line
	5650 2450 5550 2450
Text GLabel 5550 2450 0    50   Input ~ 0
VCC3V3
$Comp
L Device:R_Small R54
U 1 1 6043032E
P 5750 2450
F 0 "R54" H 5691 2404 50  0000 R CNN
F 1 "R_Small" H 5691 2495 50  0000 R CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.20x1.40mm_HandSolder" H 5750 2450 50  0001 C CNN
F 3 "~" H 5750 2450 50  0001 C CNN
	1    5750 2450
	0    1    1    0   
$EndComp
Wire Wire Line
	5850 2450 5950 2450
Wire Wire Line
	6000 4000 4300 4000
Connection ~ 4300 4000
Wire Wire Line
	4300 4000 4300 4250
Wire Wire Line
	6000 4100 4550 4100
Wire Wire Line
	4550 3950 4550 4100
Connection ~ 4550 4100
Wire Wire Line
	4550 4100 4550 4250
Wire Wire Line
	6000 4200 4800 4200
Wire Wire Line
	4800 3950 4800 4200
Connection ~ 4800 4200
Wire Wire Line
	4800 4200 4800 4250
Wire Wire Line
	5950 2150 4800 2150
Connection ~ 4800 2150
Wire Wire Line
	4800 2150 4800 2200
Wire Wire Line
	5350 1750 5250 1750
$Comp
L Device:R_Small R53
U 1 1 60454518
P 5450 1750
F 0 "R53" V 5550 1750 50  0000 R CNN
F 1 "R_Small" H 5391 1795 50  0001 R CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.20x1.40mm_HandSolder" H 5450 1750 50  0001 C CNN
F 3 "~" H 5450 1750 50  0001 C CNN
	1    5450 1750
	0    1    1    0   
$EndComp
Wire Wire Line
	5350 1650 5250 1650
Text GLabel 5250 1650 1    50   Input ~ 0
VCC3V3
$Comp
L Device:R_Small R52
U 1 1 6045FE79
P 5450 1650
F 0 "R52" V 5350 1650 50  0000 R CNN
F 1 "R_Small" H 5391 1695 50  0001 R CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.20x1.40mm_HandSolder" H 5450 1650 50  0001 C CNN
F 3 "~" H 5450 1650 50  0001 C CNN
	1    5450 1650
	0    1    1    0   
$EndComp
$Comp
L Device:R_Small R51
U 1 1 6046DA60
P 5400 3800
F 0 "R51" H 5341 3754 50  0000 R CNN
F 1 "R_Small" H 5341 3845 50  0000 R CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.20x1.40mm_HandSolder" H 5400 3800 50  0001 C CNN
F 3 "~" H 5400 3800 50  0001 C CNN
	1    5400 3800
	0    1    1    0   
$EndComp
Wire Wire Line
	5300 3700 5200 3700
Text GLabel 5200 3700 1    50   Input ~ 0
VCC3V3
$Comp
L Device:R_Small R50
U 1 1 6046DA6C
P 5400 3700
F 0 "R50" H 5341 3654 50  0000 R CNN
F 1 "R_Small" H 5341 3745 50  0000 R CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.20x1.40mm_HandSolder" H 5400 3700 50  0001 C CNN
F 3 "~" H 5400 3700 50  0001 C CNN
	1    5400 3700
	0    1    1    0   
$EndComp
Wire Wire Line
	5500 3700 6000 3700
Wire Wire Line
	5500 3800 6000 3800
Wire Wire Line
	5550 1750 5950 1750
Wire Wire Line
	5550 1650 5950 1650
Wire Wire Line
	5200 3700 5200 3800
Wire Wire Line
	5200 3800 5300 3800
Wire Wire Line
	5250 1750 5250 1650
$Comp
L Connector_Generic:Conn_01x08 J9
U 1 1 6048A3EB
P 7450 1950
F 0 "J9" H 7530 1942 50  0000 L CNN
F 1 "Conn_01x08" H 7530 1851 50  0000 L CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x08_P2.54mm_Vertical" H 7450 1950 50  0001 C CNN
F 3 "~" H 7450 1950 50  0001 C CNN
	1    7450 1950
	1    0    0    -1  
$EndComp
$Comp
L Connector_Generic:Conn_01x08 J8
U 1 1 6048B13C
P 7400 4000
F 0 "J8" H 7480 3992 50  0000 L CNN
F 1 "Conn_01x08" H 7480 3901 50  0000 L CNN
F 2 "Connector_PinHeader_2.54mm:PinHeader_1x08_P2.54mm_Vertical" H 7400 4000 50  0001 C CNN
F 3 "~" H 7400 4000 50  0001 C CNN
	1    7400 4000
	1    0    0    -1  
$EndComp
Wire Wire Line
	6950 1650 7250 1650
Wire Wire Line
	7250 1750 6950 1750
Wire Wire Line
	6950 1850 7250 1850
Wire Wire Line
	7250 1950 6950 1950
Wire Wire Line
	6950 2050 7250 2050
Wire Wire Line
	7250 2150 6950 2150
Wire Wire Line
	6950 2250 7250 2250
Wire Wire Line
	7250 2350 6950 2350
Wire Wire Line
	7000 3700 7200 3700
Wire Wire Line
	7200 3800 7000 3800
Wire Wire Line
	7000 3900 7200 3900
Wire Wire Line
	7200 4000 7000 4000
Wire Wire Line
	7000 4100 7200 4100
Wire Wire Line
	7200 4200 7000 4200
Wire Wire Line
	7000 4300 7200 4300
Wire Wire Line
	7200 4400 7000 4400
$Comp
L Device:C C1
U 1 1 60587FF0
P 8450 1650
F 0 "C1" H 8335 1604 50  0000 R CNN
F 1 "C" H 8335 1695 50  0000 R CNN
F 2 "Capacitor_SMD:C_0805_2012Metric_Pad1.18x1.45mm_HandSolder" H 8488 1500 50  0001 C CNN
F 3 "~" H 8450 1650 50  0001 C CNN
	1    8450 1650
	-1   0    0    1   
$EndComp
$Comp
L Device:C C2
U 1 1 60588F74
P 8800 1650
F 0 "C2" H 8915 1696 50  0000 L CNN
F 1 "C" H 8915 1605 50  0000 L CNN
F 2 "Capacitor_SMD:C_0805_2012Metric_Pad1.18x1.45mm_HandSolder" H 8838 1500 50  0001 C CNN
F 3 "~" H 8800 1650 50  0001 C CNN
	1    8800 1650
	1    0    0    -1  
$EndComp
Text GLabel 8950 1800 2    50   Input ~ 0
GND
Text GLabel 8950 1500 2    50   Input ~ 0
VCC3V3
Wire Wire Line
	8450 1500 8800 1500
Wire Wire Line
	8800 1500 8950 1500
Connection ~ 8800 1500
Wire Wire Line
	8950 1800 8800 1800
Wire Wire Line
	8800 1800 8450 1800
Connection ~ 8800 1800
$EndSCHEMATC
