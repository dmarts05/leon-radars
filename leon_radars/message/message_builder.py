"""Module for building messages."""
from datetime import date
from typing import Dict, List


def format_radar_data(radar_data: Dict[str, str], monitored_streets: List[str]) -> str:
    """
    Format radar data as a string.

    Args:
        radar_data: Data from radars.

    Returns:
        Formatted string.
    """
    message = ""
    for k, v in radar_data.items():
        if any(street.lower() in k.lower() for street in monitored_streets):
            message += f"<em><strong>\t - {k}: {v} km/h\n</strong></em>"
        else:
            message += f"\t - {k}: {v} km/h\n"
    return message


def build_message(
    morning_data: Dict[str, str], afternoon_data: Dict[str, str], radar_data_link: str, monitored_streets: List[str]
) -> str:
    """
    Build message to send with all radars data.

    Args:
        morning_data: Data from morning radars.
        afternoon_data: Data from afternoon radars.

    Returns:
        Message to send.
    """
    message = "*****************************\n"
    message += f"*    LEÓN RADARS ({date.today().strftime('%d/%m/%Y')})    *\n"
    message += "*****************************\n\n"
    message += "Morning:\n"
    message += format_radar_data(morning_data, monitored_streets)
    message += "\n"
    message += "Afternoon:\n"
    message += format_radar_data(afternoon_data, monitored_streets)
    message += "\n"
    message += f"Sourced from: {radar_data_link}"
    return message
