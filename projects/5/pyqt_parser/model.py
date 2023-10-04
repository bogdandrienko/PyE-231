import json


class Valute:
    def __init__(self, name: str, symbol: str, priceUSD: float):
        self.name = str(name)
        self.symbol = str(symbol)
        self.priceUSD = float(priceUSD[1:].replace(',', ''))

    def __repr__(self):
        return f"<Valute {self.name} {self.symbol} {self.priceUSD}>"

    def get_beauty_text(self):
        return f"{self.name}({self.symbol}): {round(self.priceUSD, 3)}"

    def to_json(self) -> str:
        return json.dumps({"name": self.name, "symbol": self.symbol, "price": self.priceUSD, "active": True})
