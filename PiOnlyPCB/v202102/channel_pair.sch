EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 2 8
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
L Device:R_Small R?
U 1 1 60226CD2
P 3100 2500
AR Path="/60226CD2" Ref="R?"  Part="1" 
AR Path="/602264F6/60226CD2" Ref="R5"  Part="1" 
AR Path="/60215F23/60226CD2" Ref="R11"  Part="1" 
AR Path="/60228E98/60226CD2" Ref="R17"  Part="1" 
AR Path="/602291AC/60226CD2" Ref="R23"  Part="1" 
AR Path="/6024A3AD/60226CD2" Ref="R29"  Part="1" 
AR Path="/6024A6C1/60226CD2" Ref="R35"  Part="1" 
F 0 "R5" H 3159 2546 50  0000 L CNN
F 1 "R_Small" H 3159 2455 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.20x1.40mm_HandSolder" H 3100 2500 50  0001 C CNN
F 3 "~" H 3100 2500 50  0001 C CNN
	1    3100 2500
	1    0    0    -1  
$EndComp
$Comp
L Device:R_Small R?
U 1 1 60226CD9
P 2800 2350
AR Path="/60226CD9" Ref="R?"  Part="1" 
AR Path="/602264F6/60226CD9" Ref="R2"  Part="1" 
AR Path="/60215F23/60226CD9" Ref="R8"  Part="1" 
AR Path="/60228E98/60226CD9" Ref="R14"  Part="1" 
AR Path="/602291AC/60226CD9" Ref="R20"  Part="1" 
AR Path="/6024A3AD/60226CD9" Ref="R26"  Part="1" 
AR Path="/6024A6C1/60226CD9" Ref="R32"  Part="1" 
F 0 "R2" V 2604 2350 50  0000 C CNN
F 1 "R_Small" V 2695 2350 50  0000 C CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.20x1.40mm_HandSolder" H 2800 2350 50  0001 C CNN
F 3 "~" H 2800 2350 50  0001 C CNN
	1    2800 2350
	0    1    1    0   
$EndComp
Wire Wire Line
	2900 2350 3100 2350
Connection ~ 3100 2350
Wire Wire Line
	3100 2350 3150 2350
Wire Wire Line
	3100 2400 3100 2350
$Comp
L power:GND #PWR?
U 1 1 60226CE8
P 3450 3150
AR Path="/60226CE8" Ref="#PWR?"  Part="1" 
AR Path="/602264F6/60226CE8" Ref="#PWR03"  Part="1" 
AR Path="/60215F23/60226CE8" Ref="#PWR05"  Part="1" 
AR Path="/60228E98/60226CE8" Ref="#PWR07"  Part="1" 
AR Path="/602291AC/60226CE8" Ref="#PWR09"  Part="1" 
AR Path="/6024A3AD/60226CE8" Ref="#PWR011"  Part="1" 
AR Path="/6024A6C1/60226CE8" Ref="#PWR013"  Part="1" 
F 0 "#PWR03" H 3450 2900 50  0001 C CNN
F 1 "GND" H 3455 2977 50  0000 C CNN
F 2 "" H 3450 3150 50  0001 C CNN
F 3 "" H 3450 3150 50  0001 C CNN
	1    3450 3150
	1    0    0    -1  
$EndComp
Wire Wire Line
	3450 3150 3450 2850
Wire Wire Line
	3100 2600 3100 2850
Wire Wire Line
	3100 2850 3450 2850
Connection ~ 3450 2850
Wire Wire Line
	3450 2850 3450 2550
Wire Wire Line
	2550 2350 2700 2350
$Comp
L Device:Q_NMOS_GDS Q?
U 1 1 60226CFF
P 3400 4100
AR Path="/60226CFF" Ref="Q?"  Part="1" 
AR Path="/602264F6/60226CFF" Ref="Q2"  Part="1" 
AR Path="/60215F23/60226CFF" Ref="Q5"  Part="1" 
AR Path="/60228E98/60226CFF" Ref="Q8"  Part="1" 
AR Path="/602291AC/60226CFF" Ref="Q11"  Part="1" 
AR Path="/6024A3AD/60226CFF" Ref="Q14"  Part="1" 
AR Path="/6024A6C1/60226CFF" Ref="Q17"  Part="1" 
F 0 "Q2" H 3606 4146 50  0000 L CNN
F 1 "Q_NMOS_GDS" H 3606 4055 50  0000 L CNN
F 2 "Package_TO_SOT_SMD:TO-252-2" H 3600 4200 50  0001 C CNN
F 3 "~" H 3400 4100 50  0001 C CNN
	1    3400 4100
	1    0    0    -1  
$EndComp
$Comp
L Device:R_Small R?
U 1 1 60226D0D
P 3150 4250
AR Path="/60226D0D" Ref="R?"  Part="1" 
AR Path="/602264F6/60226D0D" Ref="R7"  Part="1" 
AR Path="/60215F23/60226D0D" Ref="R13"  Part="1" 
AR Path="/60228E98/60226D0D" Ref="R19"  Part="1" 
AR Path="/602291AC/60226D0D" Ref="R25"  Part="1" 
AR Path="/6024A3AD/60226D0D" Ref="R31"  Part="1" 
AR Path="/6024A6C1/60226D0D" Ref="R37"  Part="1" 
F 0 "R7" H 3209 4296 50  0000 L CNN
F 1 "R_Small" H 3209 4205 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.20x1.40mm_HandSolder" H 3150 4250 50  0001 C CNN
F 3 "~" H 3150 4250 50  0001 C CNN
	1    3150 4250
	1    0    0    -1  
$EndComp
$Comp
L Device:R_Small R?
U 1 1 60226D14
P 2850 4100
AR Path="/60226D14" Ref="R?"  Part="1" 
AR Path="/602264F6/60226D14" Ref="R3"  Part="1" 
AR Path="/60215F23/60226D14" Ref="R9"  Part="1" 
AR Path="/60228E98/60226D14" Ref="R15"  Part="1" 
AR Path="/602291AC/60226D14" Ref="R21"  Part="1" 
AR Path="/6024A3AD/60226D14" Ref="R27"  Part="1" 
AR Path="/6024A6C1/60226D14" Ref="R33"  Part="1" 
F 0 "R3" V 2654 4100 50  0000 C CNN
F 1 "R_Small" V 2745 4100 50  0000 C CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.20x1.40mm_HandSolder" H 2850 4100 50  0001 C CNN
F 3 "~" H 2850 4100 50  0001 C CNN
	1    2850 4100
	0    1    1    0   
$EndComp
Wire Wire Line
	2950 4100 3150 4100
Connection ~ 3150 4100
Wire Wire Line
	3150 4100 3200 4100
Wire Wire Line
	3150 4150 3150 4100
Text GLabel 2950 3400 0    50   UnSpc ~ 0
VCC3V3
Wire Wire Line
	2950 3400 3150 3400
Wire Wire Line
	3150 3400 3150 3450
$Comp
L power:GND #PWR?
U 1 1 60226D23
P 3500 4800
AR Path="/60226D23" Ref="#PWR?"  Part="1" 
AR Path="/602264F6/60226D23" Ref="#PWR04"  Part="1" 
AR Path="/60215F23/60226D23" Ref="#PWR06"  Part="1" 
AR Path="/60228E98/60226D23" Ref="#PWR08"  Part="1" 
AR Path="/602291AC/60226D23" Ref="#PWR010"  Part="1" 
AR Path="/6024A3AD/60226D23" Ref="#PWR012"  Part="1" 
AR Path="/6024A6C1/60226D23" Ref="#PWR014"  Part="1" 
F 0 "#PWR04" H 3500 4550 50  0001 C CNN
F 1 "GND" H 3505 4627 50  0000 C CNN
F 2 "" H 3500 4800 50  0001 C CNN
F 3 "" H 3500 4800 50  0001 C CNN
	1    3500 4800
	1    0    0    -1  
$EndComp
Wire Wire Line
	3500 4800 3500 4600
Wire Wire Line
	3150 4350 3150 4600
Wire Wire Line
	3150 4600 3500 4600
Connection ~ 3500 4600
Wire Wire Line
	3500 4600 3500 4300
Wire Wire Line
	2600 4100 2750 4100
Text HLabel 2550 2350 0    50   Input ~ 0
IN1
Text HLabel 2600 4100 0    50   Input ~ 0
IN2
Text HLabel 3700 1850 2    50   Output ~ 0
OUT1
Text HLabel 3750 3400 2    50   Output ~ 0
OUT2
Wire Wire Line
	3450 1850 3700 1850
Wire Wire Line
	3500 3400 3750 3400
Wire Wire Line
	5450 2500 5400 2500
Wire Wire Line
	5400 4300 5100 4300
Wire Wire Line
	5400 3650 5400 4300
Wire Wire Line
	3100 1700 3100 1750
Wire Wire Line
	2950 1700 3100 1700
Text GLabel 2950 1700 0    50   UnSpc ~ 0
VCC3V3
$Comp
L Device:R_Small R?
U 1 1 603AAA71
P 4800 2700
AR Path="/603AAA71" Ref="R?"  Part="1" 
AR Path="/602264F6/603AAA71" Ref="R10"  Part="1" 
AR Path="/60215F23/603AAA71" Ref="R22"  Part="1" 
AR Path="/60228E98/603AAA71" Ref="R34"  Part="1" 
AR Path="/602291AC/603AAA71" Ref="R40"  Part="1" 
AR Path="/6024A3AD/603AAA71" Ref="R44"  Part="1" 
AR Path="/6024A6C1/603AAA71" Ref="R48"  Part="1" 
F 0 "R10" V 4604 2700 50  0000 C CNN
F 1 "R_Small" V 4695 2700 50  0000 C CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.20x1.40mm_HandSolder" H 4800 2700 50  0001 C CNN
F 3 "~" H 4800 2700 50  0001 C CNN
	1    4800 2700
	0    1    1    0   
$EndComp
$Comp
L Device:R_Small R?
U 1 1 603B8C97
P 5100 4050
AR Path="/603B8C97" Ref="R?"  Part="1" 
AR Path="/602264F6/603B8C97" Ref="R12"  Part="1" 
AR Path="/60215F23/603B8C97" Ref="R24"  Part="1" 
AR Path="/60228E98/603B8C97" Ref="R36"  Part="1" 
AR Path="/602291AC/603B8C97" Ref="R41"  Part="1" 
AR Path="/6024A3AD/603B8C97" Ref="R45"  Part="1" 
AR Path="/6024A6C1/603B8C97" Ref="R49"  Part="1" 
F 0 "R12" H 5159 4096 50  0000 L CNN
F 1 "R_Small" H 5159 4005 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.20x1.40mm_HandSolder" H 5100 4050 50  0001 C CNN
F 3 "~" H 5100 4050 50  0001 C CNN
	1    5100 4050
	1    0    0    -1  
$EndComp
Wire Wire Line
	5100 4150 5100 4300
Wire Wire Line
	5100 3950 5100 3450
$Comp
L Device:R_Small R?
U 1 1 603BA627
P 4800 3450
AR Path="/603BA627" Ref="R?"  Part="1" 
AR Path="/602264F6/603BA627" Ref="R4"  Part="1" 
AR Path="/60215F23/603BA627" Ref="R16"  Part="1" 
AR Path="/60228E98/603BA627" Ref="R28"  Part="1" 
AR Path="/602291AC/603BA627" Ref="R38"  Part="1" 
AR Path="/6024A3AD/603BA627" Ref="R42"  Part="1" 
AR Path="/6024A6C1/603BA627" Ref="R46"  Part="1" 
F 0 "R4" H 4859 3496 50  0000 L CNN
F 1 "R_Small" H 4859 3405 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.20x1.40mm_HandSolder" H 4800 3450 50  0001 C CNN
F 3 "~" H 4800 3450 50  0001 C CNN
	1    4800 3450
	0    1    1    0   
$EndComp
Wire Wire Line
	4900 3450 5100 3450
$Comp
L Device:R_Small R?
U 1 1 603BC177
P 5100 3000
AR Path="/603BC177" Ref="R?"  Part="1" 
AR Path="/602264F6/603BC177" Ref="R6"  Part="1" 
AR Path="/60215F23/603BC177" Ref="R18"  Part="1" 
AR Path="/60228E98/603BC177" Ref="R30"  Part="1" 
AR Path="/602291AC/603BC177" Ref="R39"  Part="1" 
AR Path="/6024A3AD/603BC177" Ref="R43"  Part="1" 
AR Path="/6024A6C1/603BC177" Ref="R47"  Part="1" 
F 0 "R6" H 5159 3046 50  0000 L CNN
F 1 "R_Small" H 5159 2955 50  0000 L CNN
F 2 "Resistor_SMD:R_0805_2012Metric_Pad1.20x1.40mm_HandSolder" H 5100 3000 50  0001 C CNN
F 3 "~" H 5100 3000 50  0001 C CNN
	1    5100 3000
	1    0    0    -1  
$EndComp
$Comp
L Device:Q_NMOS_GDS Q?
U 1 1 60226CC4
P 3350 2350
AR Path="/60226CC4" Ref="Q?"  Part="1" 
AR Path="/602264F6/60226CC4" Ref="Q1"  Part="1" 
AR Path="/60215F23/60226CC4" Ref="Q4"  Part="1" 
AR Path="/60228E98/60226CC4" Ref="Q7"  Part="1" 
AR Path="/602291AC/60226CC4" Ref="Q10"  Part="1" 
AR Path="/6024A3AD/60226CC4" Ref="Q13"  Part="1" 
AR Path="/6024A6C1/60226CC4" Ref="Q16"  Part="1" 
F 0 "Q1" H 3556 2396 50  0000 L CNN
F 1 "Q_NMOS_GDS" H 3556 2305 50  0000 L CNN
F 2 "Package_TO_SOT_SMD:TO-252-2" H 3550 2450 50  0001 C CNN
F 3 "~" H 3350 2350 50  0001 C CNN
	1    3350 2350
	1    0    0    -1  
$EndComp
Wire Wire Line
	3100 1950 3100 2350
Wire Wire Line
	3150 3650 3150 4100
$Comp
L power:GND #PWR?
U 1 1 603E2FDA
P 5400 4550
AR Path="/603E2FDA" Ref="#PWR?"  Part="1" 
AR Path="/602264F6/603E2FDA" Ref="#PWR?"  Part="1" 
AR Path="/60215F23/603E2FDA" Ref="#PWR?"  Part="1" 
AR Path="/60228E98/603E2FDA" Ref="#PWR?"  Part="1" 
AR Path="/602291AC/603E2FDA" Ref="#PWR?"  Part="1" 
AR Path="/6024A3AD/603E2FDA" Ref="#PWR?"  Part="1" 
AR Path="/6024A6C1/603E2FDA" Ref="#PWR?"  Part="1" 
F 0 "#PWR?" H 5400 4300 50  0001 C CNN
F 1 "GND" H 5405 4377 50  0000 C CNN
F 2 "" H 5400 4550 50  0001 C CNN
F 3 "" H 5400 4550 50  0001 C CNN
	1    5400 4550
	1    0    0    -1  
$EndComp
$Comp
L power:GND #PWR?
U 1 1 603E374E
P 5100 3200
AR Path="/603E374E" Ref="#PWR?"  Part="1" 
AR Path="/602264F6/603E374E" Ref="#PWR?"  Part="1" 
AR Path="/60215F23/603E374E" Ref="#PWR?"  Part="1" 
AR Path="/60228E98/603E374E" Ref="#PWR?"  Part="1" 
AR Path="/602291AC/603E374E" Ref="#PWR?"  Part="1" 
AR Path="/6024A3AD/603E374E" Ref="#PWR?"  Part="1" 
AR Path="/6024A6C1/603E374E" Ref="#PWR?"  Part="1" 
F 0 "#PWR?" H 5100 2950 50  0001 C CNN
F 1 "GND" H 5105 3027 50  0000 C CNN
F 2 "" H 5100 3200 50  0001 C CNN
F 3 "" H 5100 3200 50  0001 C CNN
	1    5100 3200
	1    0    0    -1  
$EndComp
Wire Wire Line
	5400 4300 5400 4550
Connection ~ 5400 4300
Connection ~ 5100 3450
$Comp
L OpenPlantSymbols:Dual_NMOSFET_BUK9K22_80E_Swapped Q3
U 1 1 60228931
P 5400 3100
AR Path="/602264F6/60228931" Ref="Q3"  Part="1" 
AR Path="/60215F23/60228931" Ref="Q6"  Part="1" 
AR Path="/60228E98/60228931" Ref="Q9"  Part="1" 
AR Path="/602291AC/60228931" Ref="Q12"  Part="1" 
AR Path="/6024A3AD/60228931" Ref="Q15"  Part="1" 
AR Path="/6024A6C1/60228931" Ref="Q18"  Part="1" 
F 0 "Q3" H 5537 3171 50  0000 L CNN
F 1 "Dual_NMOSFET_BUK9K22_80E_Swapped" H 5537 3080 50  0000 L CNN
F 2 "v202102_OpenPlant:LFPAK56D" H 5500 3600 50  0001 C CNN
F 3 "~" H 5300 3500 50  0001 C CNN
	1    5400 3100
	1    0    0    -1  
$EndComp
Wire Wire Line
	3500 3400 3500 3900
Wire Wire Line
	5400 3250 5450 3250
Text HLabel 5700 3250 2    50   Output ~ 0
OUT2
Wire Wire Line
	5450 3250 5700 3250
Connection ~ 5450 3250
Wire Wire Line
	3450 1850 3450 2150
Text HLabel 5700 2500 2    50   Output ~ 0
OUT1
Connection ~ 5450 2500
Wire Wire Line
	5450 2500 5700 2500
Wire Wire Line
	5100 3200 5100 3150
Wire Wire Line
	5400 2900 5400 3150
Wire Wire Line
	5400 3150 5100 3150
Connection ~ 5100 3150
Wire Wire Line
	5100 3150 5100 3100
Wire Wire Line
	5100 2900 5100 2700
Wire Wire Line
	4900 2700 5100 2700
Connection ~ 5100 2700
Text HLabel 4400 2700 0    50   Input ~ 0
IN1
Text HLabel 4400 3450 0    50   Input ~ 0
IN2
Wire Wire Line
	4400 2700 4700 2700
Wire Wire Line
	4400 3450 4700 3450
$EndSCHEMATC
