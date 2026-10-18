# H2GP Controller Project #
This is a project to create a custom controller for a Horizon Hydrogen Fuel Cell.

## Original ##
The original controller performs several functions
- Connect/Disconnect Hydrogen Cell from Main Battery Circuit
- Monitor Battery Voltage
- Monitor Fuel Cell Voltage
- Actuate Hydrogen Input solenoid valve
- Actuate Hydrogen Output solenoid valve
- Monitor pressure switch to ensure Hydrogen input
- Monitor Hydrocen Fuel Cell temperature
- Control cooling/oxygen fans for Fuel Cell 

## Our Modifications ##
We have worked for multiple years to simplify our setup and remove anything we find unnecessary.
First, our car operates on a 1S LiPo system at around 4 Volts. Second, our Hydrogen Fuel Cell has been
reoriented to output about 6 Volts maximum instead of the 16 Volts it normally would. Our Fuel Cell has
about 300 ohms of resistance. This means it is very highly unlikely that any current would ever go from 
the battery to the Fuel Cell, which lets us remove the complex circuitry to monitor and disconnect the 
two power sources. 

We also have a hydrogen input quick disconnect pneumatic system, allowing us to eliminate the need 
for an Input solenoid valve.

We use separate telemetry systems to monitor voltage and current from each source as well and ensure 
they are within operating range. 

This means, the majority of what we need our custom system to do is just operate the output valve to 
allow used hydrogen to purge and new hydrogen to flow in for the chemical reaction.


## Microcontroller ##
We are using the [Adafruit QT-Py](https://www.adafruit.com/qtpy) microcontroller for this project.
See the [src](src/) folder for software.
