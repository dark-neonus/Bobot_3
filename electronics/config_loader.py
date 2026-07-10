import os
import sys

# Python 3.11+ native TOML parser.
if sys.version_info >= (3, 11):
    import tomllib
else:
    # Fallback for older python environments if necessary
    try:
        import tomli as tomllib
    except ImportError:
        raise ImportError("Please install 'tomli' or upgrade to Python 3.11+ to load TOML configurations.")


def load_config():
    """Reads and parses the project TOML configuration file."""
    CONFIG_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "robot_config.toml"))
    try:
        with open(CONFIG_PATH, "rb") as f:
            return tomllib.load(f)
    except FileNotFoundError:
        print(f"⚠️  Configuration file not found at: {CONFIG_PATH}. Using empty defaults.")
        return {}
