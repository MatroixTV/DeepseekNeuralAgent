from abc import ABC, abstractmethod
import pandas as pd


class BaseStrategy(ABC):
    @abstractmethod
    def generate_signal(self, data: pd.DataFrame) -> dict:
        pass

    @abstractmethod
    def calculate_indicators(self, data: pd.DataFrame):
        pass