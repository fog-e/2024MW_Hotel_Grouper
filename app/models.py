class Hotel:
    def __init__(self, name, location):
        self.name = name
        self.location = location

class Booking:
    def __init__(self, name, email, notes, hotels, dates):
        self.name = name
        self.email = email
        self.notes = notes
        self.hotels = hotels
        self.dates = dates
