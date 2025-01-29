import yaml
import json
from pathlib import Path


class ConfigLoader:
    def __init__(self):
        self.base_path = Path(__file__).parent.parent

    def load_strategy_config(self, strategy_name: str):
        with open(self.base_path / f'strategies/{strategy_name}_config.yaml') as f:
            return yaml.safe_load(f)

    def load_risk_parameters(self):
        with open(self.base_path / 'risk_parameters.json') as f:
            return json.load(f)