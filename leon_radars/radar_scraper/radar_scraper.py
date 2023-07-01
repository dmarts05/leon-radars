"""Module that contains the functions to extract the radar data from the website."""
from datetime import date
from typing import Dict, List, Tuple

import requests
from bs4 import BeautifulSoup

from leon_radars.utils.logger import setup_logger

from .helpers import get_latest_radar_link

logger = setup_logger(__name__)


def extract_radar_data() -> Tuple[Dict[str, str], Dict[str, str], str]:
    radar_data_link = get_latest_radar_link()
    res = requests.get(radar_data_link)
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
        row_data: List[str] = [cell.get_text() for cell in cells]
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

    # Morning data
    morning_data = {k: v for k, v in zip(today_rows_data[0][2].split("\n"), today_rows_data[0][3].split("\n"))}

    # Afternoon data
    afternoon_data = {k: v for k, v in zip(today_rows_data[1][2].split("\n"), today_rows_data[1][3].split("\n"))}

    return (morning_data, afternoon_data, radar_data_link)
