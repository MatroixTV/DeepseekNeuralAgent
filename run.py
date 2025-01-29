# run.py
from core.bot import TradingBot
from config import ConfigLoader
from data.market_data import MT5DataHandler
from strategies.quantum import QuantumStrategy


def main():
    config = ConfigLoader()
    data_handler = MT5DataHandler("EURUSD", mt5.TIMEFRAME_H1)
    strategy = QuantumStrategy(config.load_strategy_config('quantum'))

    bot = TradingBot(data_handler, strategy)
    bot.run()


if __name__ == "__main__":
    main()