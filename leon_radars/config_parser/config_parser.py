"""Module that contains the config parser."""
import yaml

from leon_radars.utils.schemas import ConfigFile

from .helpers import verify_telegram_section


def parse_config(file_path: str) -> ConfigFile:
    """
    Parse the config file and return a ConfigFile object that contains the
    parsed config file.

    Refer to :class:`ConfigFile` for more information.

    Args:
        file_path: Path to the config file.

    Raises:
        ValueError: If the config file is invalid.

    Returns:
        A ConfigFile that contains the parsed config file.
    """

    with open(file_path, "r") as f:
        yaml_config = yaml.safe_load(f)

        # Verify and extract Telegram section
        telegram = verify_telegram_section(yaml_config.get("telegram", {}))

    return ConfigFile(telegram=telegram)
