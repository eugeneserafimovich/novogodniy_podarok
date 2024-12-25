import json

class Candy:
    def __init__(self, name: str, weight: int, sugar_content: int):
        self.name = name
        self.weight = weight
        self.sugar_content = sugar_content

    def to_dict(self):
        return {
            "name": self.name,
            "weight": self.weight,
            "sugar_content": self.sugar_content
        }

    @staticmethod
    def from_dict(data: dict):
        return Candy(data["name"], data["weight"], data["sugar_content"])
