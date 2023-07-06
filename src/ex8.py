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
        return list(map(CarCollector._combine, CarCollector.car_list))

    @staticmethod
    def _combine(car):
        # Todo...
        car_id = car['id']
        return {
            'id': car['id'],
            'make': CarCollector.car_dict[car_id],
            'price': car['price']
        }