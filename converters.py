
def temperature_converter(value, convert_from, convert_to):

    def celsius_converter(value, convert_to):
        """
        Converts from Celsius to Fahrenheit or Kelvin.
        """
        if convert_to == "°F":
            return f"{str((round(value * 9/5 + 32, 2)))} {convert_to}"
        elif convert_to == "K":
            return f"{str(round((value + 273.15), 2))} {convert_to}"

    def fahrenheit_converter(value, convert_to):
        """
        Converts from Fahrenheit to Celsius or Kelvin.
        """
        if convert_to == "°C":
            return f"{str(round((value - 32) * 5/9, 2))} {convert_to}"
        elif convert_to == "K":
            return f"{str(round((value - 32) * 5/9 + 273.15, 2))} {convert_to}"

    def kelvin_converter(value, convert_to):
        """
        Converts from Kelvin to Celsius or Fahrenheit.
        """
        if convert_to == "°C":
            return f"{str(round(value - 273.15, 2))} {convert_to}"
        elif convert_to == "°F":
            return f"{str(round((value - 273.15) * 9/5 + 32, 2))} {convert_to}"

    converters = {"°C": celsius_converter(value, convert_to),
                  "°F": fahrenheit_converter(value, convert_to),
                  "°K": kelvin_converter(value, convert_to)
                  }
    return converters[convert_from]
