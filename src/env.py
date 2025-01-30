import os
from pathlib import Path
from typing import Dict


class EnvConfig:
    def __init__(self):
        self.env = os.getenv("ENV", "development")
        self.config = self._load_config()

    def _load_config(self) -> Dict[str, str]:
        """Load configuration from .env file based on current environment"""
        env_file = f".env.{self.env}"
        if not Path(env_file).exists():
            raise FileNotFoundError(f"Environment file {env_file} not found")

        config = {}
        with open(env_file) as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#"):
                    key, value = line.split("=", 1)
                    config[key.strip()] = value.strip()
        return config

    def get(self, key: str, default=None) -> str:
        """Get configuration value by key"""
        return self.config.get(key, default)


# Singleton instance
env = EnvConfig()
