"""Module that contains helper functions for the config parser."""

from typing import Dict, List


def verify_streets_section(streets: List[str]) -> List[str]:
    """
    Verify the streets section of the config file.

    Args:
        streets: The streets section of the config file.

    Raises:
        ValueError: If the streets section is invalid.

    Returns:
        The verified streets section of the config file.
    """
    if not streets:
        raise ValueError("Missing streets section in config file.")
    return streets


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
