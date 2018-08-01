class TheAirTripDivTwo:
    def find(self, flights, fuel):
        cnt = 0
        for flight_fuel in flights:
            if fuel >= flight_fuel:
                cnt += 1
                fuel -= flight_fuel
            else:
                break

        return cnt


print(TheAirTripDivTwo().find([8, 7, 7, 1, 5, 7, 9], 21))
