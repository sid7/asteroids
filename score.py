import json

FILE_NAME = "score.json"


class Score:
    def __init__(self):
        self.current_score = 0
        self.high_score = self.__load_high_score()

    def __load_high_score(self):
        try:
            with open(FILE_NAME, "r") as file:
                data = json.load(file)
                return data["high_score"]

        except FileNotFoundError:
            return 0

    def update_high_score(self):
        if self.current_score > self.high_score:
            with open(FILE_NAME, "w") as file:
                json.dump({"high_score": self.current_score}, file, indent=4)

    def inc_score(self, by=1):
        self.current_score += by
