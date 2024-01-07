"""Module containing the main function of the program."""

import os

from requests import RequestException

from leon_radars.config_parser.config_parser import parse_config
from leon_radars.message.message_builder import build_message
from leon_radars.message.message_sender import send_message_to_telegram
from leon_radars.radar_scraper.radar_scraper import extract_radar_data
from leon_radars.utils.logger import reset_log_file, setup_logger

logger = setup_logger(logger_name=__name__)


def main() -> None:
    # Reset log file
    reset_log_file()

    # **************************************************************
    # Show welcome message
    # **************************************************************
    logger.info("**********************************************")
    logger.info("*                                            *")
    logger.info("*                León Radars                 *")
    logger.info("*                                            *")
    logger.info("**********************************************")

    # **************************************************************
    # Get program configuration
    # **************************************************************
    logger.info("Reading configuration file...")
    # Get path of config file in the parent directory
    config_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "config.yaml"))
    try:
        # Read config file
        config = parse_config(config_file_path)
    except ValueError as e:
        logger.error(str(e))
        exit(1)
    except FileNotFoundError:
        logger.error('Configuration file "config.yml" not found')
        exit(1)
    logger.info("Configuration file read successfully")
    logger.debug(f"Configuration: {config}")

    # **************************************************************
    # Extract radar data for today
    # **************************************************************
    logger.info("Extracting radar data for today...")
    morning_data, afternoon_data, radar_data_link = extract_radar_data()
    logger.debug(f"\nMorning data: {morning_data}")
    logger.debug(f"\nAfternoon data: {afternoon_data}")
    logger.debug(f"\nRadar data link: {radar_data_link}")

    # **************************************************************
    # Build Telegram message
    # **************************************************************
    logger.info("Building Telegram message...")
    message = build_message(morning_data, afternoon_data, radar_data_link, config.monitored_streets)
    logger.debug(f"\nTelegram message: {message}")

    # **************************************************************
    # Send Telegram message
    # **************************************************************
    logger.info("Sending Telegram message...")
    try:
        send_message_to_telegram(
            message=message, token=config.telegram.get("token", ""), chat_id=config.telegram.get("chat_id", "")
        )
    except RequestException as e:
        logger.error(f"Error sending Telegram message: {e}")
        exit(1)

    logger.info("All done! Exiting...")


if __name__ == "__main__":
    main()
