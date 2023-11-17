# SAP-Extended
Extended Simple-As-Possible Computer based on [Ben Eaters video series](https://www.youtube.com/watch?v=HyznrdDSSGM&list=PLowKtXNTBypGqImE405J2565dvjafglHU&pp=iAQB).
## Project

![alt text](https://github.com/cyrillvalentini/SAP-Extended/blob/main/images/breadboard-computer.jpg?raw=true)
## Breadboard-computer
The breadboard variant is heavily inspired by the computer made by Ben Eater. In the first phase I build computer, which is functionally similar to his design, while occasionally using different parts which were either already on hand or made the process of expanding easier in the future. 
After a successfull test run, I started to expand the design. To allow for longer programs I expanded the RAM to allow 8-Bit adresses and 7-Bit instructions. This allows for a maximum length of 256 instructions. The other major difference is the expansion port, which allows expansion cards to be created for the computer. The signals are handled by an additional EEPROM-chip within the control logic.


## Schematics and PCB
![alt text](https://github.com/cyrillvalentini/SAP-Extended/blob/main/images/pcb-version.jpg?raw=true)
The schematics and PCB were created using KiCad 7. 

## Usage

## Microcode
The control logic is build using AT28C64B parallel EEPROMs, which need to be programmed. The binary file was created using the [txt2bin.py](https://github.com/cyrillvalentini/SAP-Extended/blob/main/microcode/txt2bin.py) python script. The microcode can conveinconveniently be changed as a text file and converted back into a binary image.

The microcode can be flashed to the eeproms using crmaykish's [Arduino Mega EEPROM programmer](https://github.com/crmaykish/AT28C-EEPROM-Programmer-Arduino). After hooking everything up as described in the documentation, the EEPROMs can be flashed with their corresponding firmware using following command:

`python.exe .\at28c_programmer.py -d <port> -o 1 -f <microcode.bin> -l 8196 -w`

## Programming port
The modular programming interface allows to use different programmers to load the program into RAM. As of now, there is only a manual programmer that can be used, automatic variants are planned. 
The interface connects the programmer with a set of multiplexer, which can be controlled using the corresponding switch. By switching to programming mode, the RAM-adress as well as the data pins are connected with the pins in the port, which can be accessed by the programmer. There is an additional flash-signal which is hooked up to the write input of the RAM-chips. The full specs of the pins can be found [here](https://github.com/cyrillvalentini/SAP-Extended/blob/main/expansions/programming-port%20specification.pdf).

Note that for entering the programming mode successfully the clock must be set to manual in order to function correctly.

## Expansions
To allow for future expansion both versions of the computer have an expansion port controlled by a dedicated eeprom within the control logic. There are 16 individual instructions present in the microcode, which can be used to interact with the expansion. The full specifications can be found [here](https://github.com/cyrillvalentini/SAP-Extended/blob/main/expansions/expansion-port%20specification.pdf).

### 8x8 LED-matrix
As of now, the LED-matrix epansion is still in a prototyping phase. Once finished this expansion will allow to display simple graphics which can be copied row by row from either the RAM or the A-register. Combined with the input buttons this will allow the developement of simple games, which can be run on the computer. 

![alt text](https://github.com/cyrillvalentini/SAP-Extended/blob/main/images/led-matrix-expansion.jpg?raw=true)

### Planed expansions
- ALU expansion to allow for additional operations e.g. logic operations
- LCD character display
- Automatic programmer