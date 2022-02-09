class Guest:
    def __init__(self, name,city,status):
        self.name=name
        self.city=city
        self.status=status

    def guest_info(self):
        return "{name}, city {city}, status: {status}".format(name=self.name, city=self.city, status=self.status)

        # return str(self.name), str(self.city), str(self.status)
