class LengthUnitCalculator:
    def calc(self, amount, fromUnit, toUnit):
        fromUnitToInch = amount
        if fromUnit == "ft":
            fromUnitToInch *= 12.0
        elif fromUnit == "yd":
            fromUnitToInch *= 36.0
        elif fromUnit == "mi":
            fromUnitToInch *= 63360.0
        print fromUnitToInch
        if toUnit == "in":
            return fromUnitToInch
        elif toUnit == "ft":
            return float(fromUnitToInch / 12.0)
        elif toUnit == "yd":
            return float(fromUnitToInch / 36.0)
        elif toUnit == "mi":
            return float(fromUnitToInch / 63360.0)


print LengthUnitCalculator().calc(1, "mi", "ft")
