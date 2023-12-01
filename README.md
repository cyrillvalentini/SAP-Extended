# SAP-Extended
Simple-As-Possible Computer based on [Ben Eaters video series](https://www.youtube.com/watch?v=HyznrdDSSGM&list=PLowKtXNTBypGqImE405J2565dvjafglHU&pp=iAQB).
## Project
As part of my matura project, I planned and build an 8-Bit computer based around the design from Ben Eater. This repository contains the schematics, design files and instructions for the computer. 

![alt text](https://github.com/cyrillvalentini/SAP-Extended/blob/main/images/breadboard-computer.jpg?raw=true)
## Breadboard-computer
The breadboard variant is heavily inspired by the computer made by Ben Eater. In the first phase I build computer, which is functionally similar to his design, while occasionally using different parts which were either already on hand or made the process of expanding easier in the future. 
After a successfull test run, I started to expand the design. To allow for longer programs I expanded the RAM to allow 8-Bit adresses and 7-Bit instructions. This allows for a maximum length of 256 instructions. In order to make these changes differend modules had to be expanded as well. The other major difference is the expansion port, which allows expansion cards to be created for the computer. The signals are handled by an additional EEPROM-chip within the control logic.

![alt text](https://github.com/cyrillvalentini/SAP-Extended/blob/main/images/diagram.png?raw=true)
*Simplified diagram of the changes made to the architecture.* 

## Schematics and PCB
After building the breadboard variant, I started working on a pcb version. Being the first larger design I created there are some power related issues and some missing filtering components which prevent the computer from running completely.

The schematics and PCB were created using KiCad 7.

![alt text](https://github.com/cyrillvalentini/SAP-Extended/blob/main/images/pcb-version.jpg?raw=true)

## Usage
![alt text](https://github.com/cyrillvalentini/SAP-Extended/blob/main/images/breadboard-computer%20labeled.png?raw=true)

### Programming the computer
To set the computer to programming mode, the clock switch must first be set to manual. The LED should then stop flashing. It is then advisable to press the RESET button once to clear all registers. To be able to program the computer, the programmer must also be plugged in and the RUN/PROGRAM switch must be set to PROGRAM.

Now the actual programming can begin. First, the desired address must be set; without jump commands, these are iterated through in ascending order. In this case, the first command can be saved in the address 00000001. This is followed by the actual command, which can also be entered using the DIP switches. Finally, if the command requires it, the address to be accessed by the command can be entered under "DATA". Once the entire command has been typed in, the "FLASH" button can be pressed. The command should then be displayed in RAM. It is important that the address 00000000 is empty and is not used, as the computer does not always read in the first command after resetting.

### Examples
<center>

| RAM-adress| adding to numbers         | show input in output-register |
|-----------|---------------------------|-------------------------------|
| 0000 0001 | 0000 0001 0000 1000 (LDA) | 0000 1010 0000 0000 (INA)     |
| 0000 0010 | 0000 0011 0001 0000 (ADD) | 0000 0101 0000 0000 (OUT)     |
| 0000 0011 | 0000 0101 0000 0000 (OUT) | 0000 0110 0000 0001 (JMP)     |
| 0000 0100 | 0000 1100 0000 0000 (HLT) |                               |
| ...       |                           |                               |
| 0000 0100 | 0000 0000 0000 0011 (3)   |                               |
| ...       |                           |                               |
| 0000 0100 | 0000 0000 0000 0001 (1)   |                               |

</center>

### Run a program
To start the program, the switch must be set to RUN. As soon as this has been done, the program can be started either manually by using the button or by switching to automatic mode. For the I/O, it should be noted that the switch next to the display can be used to switch the decimal output between unsigned binary and two's complement. In addition, the input register deletes its contents after use or can be deleted manually using the button next to it.  The commands can be found [here](https://github.com/cyrillvalentini/SAP-Extended/blob/main/instructions.pdf)
## Microcode
The control logic is build using AT28C64B parallel EEPROMs, which need to be programmed. The binary file was created using the [txt2bin.py](https://github.com/cyrillvalentini/SAP-Extended/blob/main/microcode/txt2bin.py) python script. The microcode can conveinconveniently be changed as a text file and converted back into a binary image.

The microcode can be flashed to the eeproms using crmaykish's [Arduino Mega EEPROM programmer](https://github.com/crmaykish/AT28C-EEPROM-Programmer-Arduino). After hooking everything up as described in the documentation, the EEPROMs can be flashed with their corresponding firmware using following command:

`python.exe .\at28c_programmer.py -d <port> -o 0 -f <microcode.bin> -l 8192 -w`

## Programming port
The modular programming interface allows to use different programmers to load the program into RAM. As of now, there is only a manual programmer that can be used, automatic variants are planned. 
The interface connects the programmer with a set of multiplexer, which can be controlled using the corresponding switch. By switching to programming mode, the RAM-adress as well as the data pins are connected with the pins in the port, which can be accessed by the programmer. There is an additional flash-signal which is hooked up to the write input of the RAM-chips. The full specs of the pins can be found [here](https://github.com/cyrillvalentini/SAP-Extended/blob/main/expansions/programming-port%20specification.pdf).

Note that for entering the programming mode successfully the clock must be set to manual in order to function correctly.

## Expansions
To allow for future expansion both versions of the computer have an expansion port controlled by a dedicated eeprom within the control logic. There are 16 individual instructions present in the microcode, which can be used to interact with the expansion. The full specifications can be found [here](https://github.com/cyrillvalentini/SAP-Extended/blob/main/expansions/expansion-port%20specification.pdf).

### 8x8 LED-matrix
As of now, the LED-matrix epansion is still in a prototyping phase. Once finished this expansion will allow to display simple graphics which can be copied row by row from either the RAM or the A-register. Combined with the input buttons this will allow the developement of simple games, which can be run on the computer. 

![alt text](https://github.com/cyrillvalentini/SAP-Extended/blob/main/images/led-matrix-expansion.jpg?raw=true)
*Unfinished prototype of the 8x8 led-matrix*

### Planed expansions
- ALU expansion to allow for additional operations (e.g. logic operations)
- LCD character display
- Automatic programmer