import re
import math


class Utils:

    @staticmethod
    def printFormat(object, firstLine = True):
        if (firstLine):
            print('+' + ("-" * 72) + '+')

        if isinstance(object, list):
            for string in object:
                if string == '*-*':
                    print('+' + ("-" * 72) + '+')
                else:
                    print('| {:70} |'.format(string.replace('\t', ' ' * 4)))
        else:
            print('| {:70} |'.format(object.replace('\t', ' ' * 4)))

        print('+' + ("-" * 72) + '+')

    @staticmethod
    def waitInput(prefix, needNumber = False):
        value = "";
        while (True):
            value = input(prefix)

            if (needNumber and isstringint(value) == False):
                console("Must be integer")
            else:
                return value

    @staticmethod
    def isStringInt(string):
        try:
            int(string)
            return True
        except ValueError:
            return False


class UnitsArray:
    unitMeters = {
        "km": 3,
        "m": 0,
        "cm":-2,
        "mm":-3
    }
    unitJoules = {
        "tj": 12,
        "gj": 9,
        "mj": 6,
        "kj": 3,
        "j": 0
    }

    units = [
        unitMeters,
        unitJoules
    ]

    @staticmethod
    def getUnitValue(string):
        for unitMap in UnitsArray.units:
            if (unitMap.get(str(string)) != None):
                return unitMap.get(str(string))
        return None


def interprete():
    expression = Utils.waitInput("$ ").lower().replace(" ", "")

    if (":" not in expression):
        print("Error: the conversion target is not (or incorectly) set!")
        return

    expressionInfo = expression.split(":", maxsplit = 1)

    baseMatcher = re.search("([0-9]+)([a-z]+)", expressionInfo[0])

    if (bool(baseMatcher) == False or len(baseMatcher.groups()) != 2 or Utils.isStringInt(baseMatcher.group(1)) == False):
        print("Error: no number or base unit found, or format is invalid")
        return

    baseValue = int(baseMatcher.group(1))
    unitBase = baseMatcher.group(2)
    unitTarget = expressionInfo[1]

    Utils.printFormat(["Base value: " + str(baseValue), "Unit Base: " + str(unitBase) + "({})".format(str(UnitsArray.getUnitValue(unitBase))), "Unit Target: " + str(unitTarget) + "({})".format(str(UnitsArray.getUnitValue(unitTarget)))])

    converted = convert(baseValue, unitBase, unitTarget);
    if (converted == None):
        print("Error: unknown base or target unit")
        return

    Utils.printFormat("{} {} = {} {}".format(baseValue, unitBase, converted, unitTarget), False)


def convert(baseValue, unitBase, unitTarget):
    unitBaseValue = UnitsArray.getUnitValue(unitBase)
    unitTargetValue = UnitsArray.getUnitValue(unitTarget)

    if (unitBaseValue == None or unitTargetValue == None):
        return None

    unitShift = unitBaseValue - unitTargetValue

    return baseValue * math.pow(10, unitShift)


##########################################################
Utils.printFormat(["", "Unit converter", "", "Format: number + unit + \":\" + targetUnit", "Exemple: 100kg:g // 150 kg : t", ""])

while (True):
    try:
        interprete()
    except Exception as exception:
        print(exception)
        # pass # do nothing, surely KeyboardInterupt

