

class CheckChecker:
    def __init__(self, check_keywords=None) -> None:
        self.check_keywords = ["ИТОГО", "СУММА"]
        if check_keywords is not None:
            self.check_keywords: list = check_keywords

    def is_check(self, text: str) -> bool:
        for word in self.check_keywords:
            if word in text:
                return True
        return False
