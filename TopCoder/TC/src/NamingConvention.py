class NamingConvention:
    def toCamelCase(self, variableName):
        camelCasedVariableName = ""
        is_ = False
        for c in variableName:
            if is_ == True:
                camelCasedVariableName += str.upper(c)
                is_ = False
            elif c == '_':
                is_ = True
            else:
                camelCasedVariableName += c
        return camelCasedVariableName


print(NamingConvention().toCamelCase("sum_of_two_numbers"))
