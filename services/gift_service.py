from models.candy import Candy

class GiftService:
    def __init__(self, candies):
        self.candies = candies

    def create_gift(self, target_weight):
        candies_in_gift = []
        current_weight = 0

        self.candies.sort(key=lambda c: c.weight, reverse=True)
        for candy in self.candies:
            while current_weight + candy.weight <= target_weight:
                candies_in_gift.append(candy)
                current_weight += candy.weight

        if current_weight != target_weight:
            return None  # Оброботка, невозможно собрать подарок

        return candies_in_gift

    def sort_by_total_weight(self, gift):
        return sorted(gift, key=lambda c: c.weight)

    def sort_by_count(self, gift):
        candy_counts = {}
        for candy in gift:
            candy_counts[candy.name] = candy_counts.get(candy.name, 0) + 1
        sorted_candies = sorted(candy_counts.items(), key=lambda x: x[1], reverse=True)
        return [candy for name, _ in sorted_candies for candy in gift if candy.name == name]

    def filter_by_sugar_range(self, gift, min_sugar, max_sugar):
        return [candy for candy in gift if min_sugar <= candy.sugar_content <= max_sugar]
