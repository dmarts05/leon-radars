"""Module that contains helper functions for the config parser."""
from typing import Dict, List


def verify_monitored_streets_section(monitored_streets: List[str]) -> List[str]:
    """
    Verify the monitored streets section of the config file.

    Args:
        monitored_streets: The monitored streets section of the config file.

    Raises:
        ValueError: If the monitored streets section is invalid.

    Returns:
        The verified monitored streets section of the config file.
    """
    if not monitored_streets:
        raise ValueError("Monitored streets section of config file is empty.")
    return monitored_streets


def verify_telegram_section(telegram: Dict[str, str]) -> Dict[str, str]:
    """
    Verify the Telegram section of the config file.

    Args:
        telegram: The Telegram section of the config file.

    Raises:
        ValueError: If the Telegram section is invalid.

    Returns:
        The verified Telegram section of the config file.
    """

    required_fields = ("token", "chat_id")
    if not all(field in telegram for field in required_fields):
        raise ValueError("Missing required field(s) in Telegram section of config file.")
    return telegram
