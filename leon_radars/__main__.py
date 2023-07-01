"""Module containing the main function of the program."""

import os

from leon_radars.config_parser.config_parser import parse_config
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

    logger.info("All done! Exiting...")


if __name__ == "__main__":
    main()
