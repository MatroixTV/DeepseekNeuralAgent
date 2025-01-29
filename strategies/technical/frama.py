# strategies/technical/frama.py
import numpy as np
import pandas as pd
from typing import Dict


class FrAMA:
    """
    Fractal Adaptive Moving Average (FrAMA)
    Implements John Ehlers' FRAMA algorithm
    """

    def __init__(self, window: int = 16, n_fast: int = 4, n_slow: int = 32):
        self.window = window
        self.n_fast = n_fast
        self.n_slow = n_slow
        self.alpha = None

    def _calculate_fractal_dimension(self, data: pd.Series) -> float:
        """Calculate fractal dimension using box-counting method"""
        n = len(data)
        n1 = np.log(n)
        r = (data.max() - data.min()) / n
        n2 = np.log(1 / r)
        return n1 / n2 if r != 0 else 1.0

    def _calculate_alpha(self, D: float) -> float:
        """Calculate dynamic smoothing factor"""
        return np.exp(-4.6 * (D - 1))  # 4.6 ≈ ln(100)

    def calculate(self, data: pd.DataFrame) -> Dict[str, float]:
        """
        Calculate FRAMA values
        Input DataFrame must contain 'high' and 'low' columns
        """
        try:
            if not {'high', 'low'}.issubset(data.columns):
                raise ValueError("Missing required OHLC columns")

            # Calculate fractal dimension
            combined = (data['high'] + data['low']) / 2
            D = combined.rolling(self.window).apply(
                lambda x: self._calculate_fractal_dimension(x),
                raw=False
            ).iloc[-1]

            # Calculate adaptive alpha
            self.alpha = self._calculate_alpha(D)

            # Calculate FRAMA
            fast_sc = 2 / (self.n_fast + 1)
            slow_sc = 2 / (self.n_slow + 1)
            scaler = self.alpha * (fast_sc - slow_sc) + slow_sc
            frama = combined.ewm(alpha=scaler, adjust=False).mean().iloc[-1]

            return {
                'frama': frama,
                'alpha': self.alpha,
                'fractal_dimension': D
            }

        except Exception as e:
            print(f"FrAMA calculation error: {str(e)}")
            return {'frama': np.nan, 'alpha': np.nan, 'fractal_dimension': np.nan}