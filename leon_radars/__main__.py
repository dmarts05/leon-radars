"""Module containing the main function of the program."""

import os
import re
from datetime import date
from typing import List

import requests
from bs4 import BeautifulSoup

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

    # **************************************************************
    # Get latest radar data link
    # **************************************************************
    logger.info("Getting latest radar data link...")
    spanish_month_names = {
        "January": "enero",
        "February": "febrero",
        "March": "marzo",
        "April": "abril",
        "May": "mayo",
        "June": "junio",
        "July": "julio",
        "August": "agosto",
        "September": "septiembre",
        "October": "octubre",
        "November": "noviembre",
        "December": "diciembre",
    }
    month_name = spanish_month_names[date.today().strftime("%B")]
    request_url = "https://www.ahoraleon.com/?s=radar+" + month_name
    logger.debug(f"Request URL: {request_url}")

    res = requests.get(request_url)
    if res.status_code != 200:
        logger.error("Error getting radar data link")
        exit(1)
    soup = BeautifulSoup(res.text, "html.parser")

    radar_data_link = soup.find("a", {"rel": "bookmark"})
    if not radar_data_link:
        logger.error("Error getting radar data link")
        exit(1)

    radar_data_link = radar_data_link.get("href")  # type: ignore

    logger.debug(f"Latest radar data link: {radar_data_link}")

    # **************************************************************
    # Extract radar data for today
    # **************************************************************
    logger.info("Extracting radar data for today...")
    res = requests.get(str(radar_data_link))  # type: ignore
    if res.status_code != 200:
        logger.error("Error getting radar data")
        exit(1)
    soup = BeautifulSoup(res.text, "html.parser")

    # Get table rows for extracting data
    rows = soup.find_all("tr")
    if not rows:
        logger.error("Error getting radar data")
        exit(1)

    rows_data: List[List[str]] = []
    for row in rows:
        cells = row.find_all("td")
        row_data: List[str] = [cell.get_text(strip=True) for cell in cells]
        rows_data.append(row_data)

    # Get today's row data
    day = date.today().strftime("%e").strip()
    today_rows_data: List[List[str]] = []
    for i, row_data in enumerate(rows_data):
        if row_data[0] == day:
            today_rows_data.append(row_data)
            today_rows_data.append(rows_data[i + 1])
            break
    logger.debug(f"Today's row data: {today_rows_data}")

    # Split the string using regular expressions to identify word boundaries
    streets = re.findall(r"[A-Z][a-z]*[^A-Z]*", today_rows_data[0][2] + today_rows_data[1][2])

    # Remove any leading or trailing whitespace from each street
    streets = [street.strip() for street in streets]
    logger.debug(f"Streets: {streets}")


if __name__ == "__main__":
    main()
