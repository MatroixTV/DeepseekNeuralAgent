# data/data_cleaning.py
import pandas as pd
import numpy as np
from typing import Optional

class DataCleaner:
    def __init__(self, validation_rules: Optional[dict] = None):
        self.validation_rules = validation_rules or {
            'ohlc_columns': ['open', 'high', 'low', 'close'],
            'time_column': 'time',
            'max_null_threshold': 0.1
        }

    def clean_data(self, raw_df: pd.DataFrame) -> pd.DataFrame:
        """Main cleaning pipeline"""
        df = self._validate_columns(raw_df)
        df = self._handle_missing_data(df)
        df = self._remove_duplicates(df)
        df = self._validate_price_ranges(df)
        return df

    def _validate_columns(self, df: pd.DataFrame) -> pd.DataFrame:
        required_cols = self.validation_rules['ohlc_columns'] + [self.validation_rules['time_column']]
        if not set(required_cols).issubset(df.columns):
            missing = set(required_cols) - set(df.columns)
            raise ValueError(f"Missing required columns: {missing}")
        return df

    def _handle_missing_data(self, df: pd.DataFrame) -> pd.DataFrame:
        threshold = len(df) * self.validation_rules['max_null_threshold']
        return df.dropna(thresh=threshold)

    def _remove_duplicates(self, df: pd.DataFrame) -> pd.DataFrame:
        return df[~df.index.duplicated(keep='first')]

    def _validate_price_ranges(self, df: pd.DataFrame) -> pd.DataFrame:
        ohlc = self.validation_rules['ohlc_columns']
        df = df[(df[ohlc[1]] >= df[ohlc[0]]) &
               (df[ohlc[1]] >= df[ohlc[2]]) &
               (df[ohlc[2]] <= df[ohlc[0]])]
        return df