from models.candy import Candy

class GiftService:
    def __init__(self, candies):
        self.candies = candies

    def create_gift(self, target_weight):
        dp = [float('inf')] * (target_weight + 1)
        dp[0] = 0  # Для веса 0 не требуется конфет

        combinations = {0: []}

        for weight in range(1, target_weight + 1):
            for candy in self.candies:
                if weight >= candy.weight:
                    if dp[weight - candy.weight] + 1 < dp[weight]:
                        dp[weight] = dp[weight - candy.weight] + 1
                        combinations[weight] = combinations[weight - candy.weight] + [candy]

        return combinations.get(target_weight, None)

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
