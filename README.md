# SAP-Extended
Extended Simple-As-Possible Computer based on Ben Eaters video series. 
![alt text](https://github.com/cyrillvalentini/SAP-Extended/blob/main/images/breadboard-computer.jpg?raw=true)
## Breadboard-computer
## Schematics and PCB
![alt text](https://github.com/cyrillvalentini/SAP-Extended/blob/main/images/pcb-version.jpg?raw=true)
The schematics and PCB were created using KiCad 7. 

## Usage

## Microcode
The control logic is build using AT28C64B parallel EEPROMs, which need to be programmed. The binary file was created using the [txt2bin.py](https://github.com/cyrillvalentini/SAP-Extended/blob/main/microcode/text%20to%20binary%20converter.py) python script. The microcode can conveinconveniently be changed as a text file and converted back into a binary image.

The microcode can be flashed to the eeproms using crmaykish's [Arduino Mega EEPROM programmer](https://github.com/crmaykish/AT28C-EEPROM-Programmer-Arduino). After hooking everything up as described in the documentation, the EEPROMs can be flashed with their corresponding firmware using following command:

`python.exe .\at28c_programmer.py -d <port> -o 1 -f <microcode.bin> -l 8196 -w`

## Programming port

## Expansions
To allow for future expansion both versions of the computer have an expansion port controlled by a dedicated eeprom within the control logic. There are 16 individual instructions present in the microcode, which can be used to interact with the expansion. The full specifications can be found [here](https://github.com/cyrillvalentini/SAP-Extended/blob/main/expansions/expansion-port%20specification.pdf).

### 8x8 LED-matrix
As of now, the LED-matrix epansion is still in a prototyping phase. Once finished this expansion will allow to display simple graphics which can be copied row by row from eiter the RAM or the A-register. Combined with the input buttons this will allow the developement of simple games, which can be run on the computer. 

![alt text](https://github.com/cyrillvalentini/SAP-Extended/blob/main/images/led-matrix-expansion.jpg?raw=true)

### Planed expansions
- ALU expansion to allow for additional operations e.g. logic operations
- LCD character display
- ...