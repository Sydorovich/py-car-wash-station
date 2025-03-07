from typing import Any


class Car:
    def __init__(
            self, comfort_class: int, clean_mark: int, brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self,
                 distance_from_city_center: float,
                 clean_mark: int,
                 average_rating: float,
                 count_of_ratings: int) -> None:
        self.distance = distance_from_city_center
        self.clean_mark = clean_mark
        self.average_rating = average_rating
        self.count_of_ratings = count_of_ratings

    def calculate_washing_price(self, car: Any) -> float:
        if self.clean_mark <= car.clean_mark:
            return 0.0
        return round(
            car.comfort_class * self.average_rating * (
                self.clean_mark - car.clean_mark) / self.distance, 1)

    def wash_single_car(self, car: Any) -> None:
        if self.clean_mark <= car.clean_mark:
            return
        car.clean_mark = self.clean_mark

    def rate_service(self, rate: int) -> None:
        self.count_of_ratings += 1
        self.average_rating = round(
            (self.average_rating * (self.count_of_ratings - 1) + rate)
            / self.count_of_ratings, 1)

    def serve_cars(self, cars: list) -> float:
        income = 0
        for car in cars:
            income += self.calculate_washing_price(car)
            self.wash_single_car(car)
        return income
