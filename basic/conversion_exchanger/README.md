# Conversion Exchanger

This is designed to convert core metrics from one to another. Inputting the index of your choice allows you to select the conversion type and then go through the metric options relevant to that type. It reads from a CSV of formulas to get the correct conversion, based on the users input.

In total the program has 6 conversion types that consist of 42 different metrics. That's a total of 328 conversions! These metrics include:

1. Temperature (3) – Celsius, fahrenheit, kelvin.
2. Frequency (4) – Hertz, kilohertz, megahertz, gigahertz.
3. Angle (4) – Degrees, radians, gradians, milligradians.
4. Weight (8) – Kilogram, gram, milligram, ton, microgram, stone, pound, ounce.
5. Length (11) – Kilometre, metre, centimetre, millimetre, micrometre, nanometre, mile, yard, foot, inch, nautical mile.
6. Volume (12) – Cubic metre, litre, millilitre, gallon, quart, pint, cup, fluid ounce, tablespoon, teaspoon, cubic foot, cubic inch.

```Psuedocode
---------------------------------------------------------------------------------
Select the conversion type (input the index):
  1. Angle
  2. Frequency
  3. Length
  4. Temperature
  5. Volume
  6. Weight
---------------------------------------------------------------------------------
=>
```

Above is as example of the main menu and below is an example of the _temperature_ menu.

```Psuedocode
---------------------------------------------------------------------------------
You selected the 'Temperature' conversion type, what would you like to convert as?
  1. Celsius
  2. Fahrenheit
  3. Kelvin
---------------------------------------------------------------------------------
=>
```