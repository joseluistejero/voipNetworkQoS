# voipNetworkQoS
Get best audio codec for VoIP call.
# HelloWorldSmartCard
Tutorial about javacard and smartcard interaction
## Table of contents
* [General info](#general-info)
* [Usage](#usage)
	* [Smart card applet](#smart-card-applet)
	* [Smart card client](#smart-card-client)
* [Technologies](#technologies)
* [Contact](#contact)

## General info
This repository contains two java projects which are basic to understand smartcards. 
	
## Prerequisites
To run this project we use Infineon JavaCard IDE with
- JRE 1.8.0 (Java Runtime Envirioment )  
- JCDK 3.0.5 (Java Card Development Kit )  


### Install
1. Clone the repository
```
$ git clone https://github.com/joseluistejero/HelloWorldSmartCard
```
2. Open both proyects on Java Card IDE 



<!-- USAGE EXAMPLES -->
## Usage

### Smart Card Applet: 
Contains the .java files of the application that we want to include in our smart card.

First step is building the proyect, this will generete a .cap file. This file found in the folder /bin/getterSetter/javacard/ is the one we need to introduce in the smart card.

For introducing the .cap file in the smart card follow Global Platform Pro tutorial https://github.com/martinpaljak/GlobalPlatformPro 

Basic commands used:
```
$ Install: C:\GlobalPlatformPro\tool\target> .\gp.exe -install .\getterSetter.cap -key <Default key of card> -r 1 -d  -v -i
$ Uninstall: C:\GlobalPlatformPro\tool\target>  .\gp.exe -f --delete --applet  <AID of proyect applet> -key <Default key of card> -r 1 -d  -v -i
```
***INFINEON SECORA IDS KEY:*** 6B188209632A7649016EBF37B8CB518BCE8AE0D13C74C19302BD497BD5C66DAE 

***AID of proyect:*** 9988776655000000

###  Smart Card Client:
The purpose of this project is to interact with the smartcard by sending bytes through APDU.
```
$ Run Java file on src folder: ClienteAppletTestGetterSetter
```


## Technologies
Project is created with:
* JavaCard Development Kit
* Secora IDS SLJ52GDA110CS


<!-- CONTACT -->
## Contact

Jose Luis Tejero Lopez - JoseLuis.TejeroLopez@infineon.com

Project Link: [https://github.com/joseluistejero/HelloWorldSmartCard](https://github.com/joseluistejero/HelloWorldSmartCard)
