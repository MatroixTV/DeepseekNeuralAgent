# test_frama.py
import pandas as pd
from strategies.technical.frama import FrAMA

# Generate test data
data = pd.DataFrame({
    'high': [1.1200, 1.1250, 1.1300, 1.1280, 1.1320],
    'low': [1.1150, 1.1180, 1.1250, 1.1220, 1.1270]
})

# Initialize and test
frama = FrAMA(window=4)
result = frama.calculate(data)
print(f"FrAMA: {result['frama']:.5f}")
print(f"Alpha: {result['alpha']:.5f}")
print(f"Fractal Dimension: {result['fractal_dimension']:.5f}")