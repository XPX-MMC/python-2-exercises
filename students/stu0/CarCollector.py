class CarCollector:
    car_list = [
        {"id": 1, "price": 10000},
        {"id": 2, "price": 20000},
        {"id": 3, "price": 30000},
    ]
    car_dict = {
        1: "Ford",
        2: "Mazda",
        3: "Chevy"
    }

    @staticmethod
    def get_data():
        retval = list(map(CarCollector._combine, CarCollector.car_list))
        return retval

    @staticmethod
    def _combine(c):
        retval = {
            "id": c["id"],
            "make": CarCollector.car_dict[c["id"]],
            "price": c["price"]
        }
        return retval
