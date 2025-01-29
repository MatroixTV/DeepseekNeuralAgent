# tests/unit/test_risk_engine.py
import unittest
from core.risk_engine import RiskEngine

class TestRiskEngine(unittest.TestCase):
    def test_position_sizing(self):
        risk_engine = RiskEngine()
        size = risk_engine.calculate_position_size("EURUSD", 1.1200)
        self.assertIsInstance(size, float)