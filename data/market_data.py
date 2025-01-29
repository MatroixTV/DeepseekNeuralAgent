import MetaTrader5 as mt5


class MT5DataHandler:
    def __init__(self, symbol: str, timeframe: int):
        self.symbol = symbol
        self.timeframe = timeframe

    def get_historical_data(self, bars: int = 1000):
        return mt5.copy_rates_from_pos(self.symbol, self.timeframe, 0, bars)