import datetime


class BookingManager:
    def __init__(self):
        self.hotels = {}
        self.bookings = []

    def read_hotel_details(self, file):
        try:
            fd = open(file)
            fd.readline()
            line = fd.readline()
            while line != None:
                hotel = line.split(' ')[0]
                number_of_rooms = int(line.split(' ')[1])
                self.hotels[hotel] = number_of_rooms
                line = fd.readline()
        except Exception as e:
            print(e)

    def read_booking_details(self, file):
        try:
            fd = open(file)
            fd.readline()
            line = fd.readline()
            while line != None:
                hotel = line.split(' ')[0]
                check_in_time = datetime(line.split(' ')[1])
                check_out_time = datetime(line.split(' ')[2])
                self.bookings.append((hotel, check_in_time, check_out_time))
                line = fd.readline()
        except Exception as e:
            print(e)

    def get_number_of_available_rooms_per_hotel(self, t1, t2):
        number_of_available_rooms_per_hotel = self.hotels.copy()
        for booking in self.bookings:
            hotel = booking[0]
            check_in_time = booking[1]
            check_out_time = booking[2]
            if self.is_room_not_available(check_in_time, check_out_time, t1, t2):
                number_of_rooms = number_of_available_rooms_per_hotel[hotel]
                number_of_available_rooms_per_hotel[hotel] = number_of_rooms - 1
        return number_of_available_rooms_per_hotel

    def is_room_not_available(self, check_in_time, check_out_time, t1, t2):
        return not (check_out_time <= t1 or check_in_time >= t2)


booking_manager = BookingManager()
booking_manager.read_hotel_details("hotels")
booking_manager.read_booking_details("bookings")
print(booking_manager.hotels)
print(booking_manager.bookings)
print(booking_manager.get_number_of_available_rooms_per_hotel(datetime('2015-04-03'), datetime('2015-04-06')))
