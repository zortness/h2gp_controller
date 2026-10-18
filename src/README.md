# H2GP Controller Source Code #
This is the source code for the custom H2GP controller. 
The software is written in CircuitPython, intended for a SAMD21 microcontroller. 
See [here](https://docs.circuitpython.org/en/latest/ports/atmel-samd/README.html). 
In our case, we prefer the [Adafruit QT-Py](https://www.adafruit.com/qtpy), 
because it also includes a NeoPixel for visual feedback.

## Installation ##
If you have a new device, you will need to follow the instructions above to get CircuitPython installed on it first.

To install the controller software, connect the SAMD21 device via USB to the computer. It should show up
as a USB drive with a name like `CIRCUITPY`. 
- Copy `code.py` to the root of the device folder.
- Copy the `lib` folder and its contents to the root device folder.

## Editing ##
You will want an editor that understands CircuitPython. 
- [Thonny](https://thonny.org/)
- [Visual Studio Code](https://code.visualstudio.com/download)

Make sure you commit your work, and push it to the github repo.

## Connected Pins ##
- A0: Connected to a potentiometer to set an input voltage (+, gnd, A0, connected to Pot)
  - Used to adjust timing of the release valve actuation
- D1: Output used to drive a transitor, and then the pneumatic release valve
