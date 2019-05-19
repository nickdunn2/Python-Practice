class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        # return "{} of {}".format(self.get_clean_value(), self.get_clean_suit())
        return f"{self.get_clean_value()} of {self.get_clean_suit()}"

    def get_clean_value(self):
        return str(self.value).upper()

    def get_clean_suit(self):
        return str(self.suit).capitalize()
