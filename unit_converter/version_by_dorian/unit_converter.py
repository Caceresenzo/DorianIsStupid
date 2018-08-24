def convert_DISTANCE(val, unit_in, unit_out):
    DISTANCE = {'mm': 0.001, 'cm': 0.01, 'm': 1.0, 'km': 1000.}
    print(valDISTANCE[unit_in] / DISTANCE[unit_out])


def convert_MASSE(val, unit_in, unit_out):
    MASSE = {'mg': 0.001, 'g': 1.0, 'kg': 1000.}
    print(valMASSE[unit_in] / MASSE[unit_out])


def convert_POWER(val, unit_in, unit_out):
    POWER = {'w': 1.0, 'kw': 1000.}
    print(val * POWER[unit_in] / POWER[unit_out])


print("Entrer une valeur a convertir ")
valueToConvert = int(input(''))
print("Entrer une unitee d'entree ")
inputUnit = input('')
print("Entrer une unitee de sortie ")
outputUnit = input('')

# Enzo: Change this if you want to convert another unit
convert_POWER(valueToConvert, inputUnit, outputUnit)
