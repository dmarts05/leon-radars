"""Module for building messages."""
from datetime import date
from typing import Dict


def build_message(morning_data: Dict[str, str], afternoon_data: Dict[str, str], radar_data_link: str) -> str:
    """
    Build message to send with all radars data.

    Args:
        morning_data: Data from morning radars.
        afternoon_data: Data from afternoon radars.

    Returns:
        Message to send.
    """
    message = "******************************\n"
    message += f"*  LEÓN RADARS ({date.today().strftime('%d/%m/%Y')})  *\n"
    message += "******************************\n\n"
    message += "Morning:\n"
    for k, v in morning_data.items():
        message += f"\t - {k}: {v}\n"
    message += "\n"
    message += "Afternoon:\n"
    for k, v in afternoon_data.items():
        message += f"\t - {k}: {v}\n"
    message += "\n"
    message += f"Sourced from: {radar_data_link}"
    return message
