"""Module that contains the schemas used in the project."""
from typing import Dict, List, NamedTuple


class ConfigFile(NamedTuple):
    """
    A schema that encapsulates the structure of the config file.

    monitor_streets: a list of streets to monitor

    telegram: the Telegram section of the config file
        - token: the token of the Telegram bot
        - chat_id: the chat ID that will receive the messages
    """

    monitored_streets: List[str]
    telegram: Dict[str, str]
