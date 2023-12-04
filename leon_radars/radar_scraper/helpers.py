"""Module that contains helper functions for the radar scraper."""
from datetime import date

from bs4 import BeautifulSoup

from leon_radars.utils.logger import setup_logger
from leon_radars.utils.session_with_user_agent import create_session_with_user_agent

logger = setup_logger(__name__)


def get_latest_radar_link() -> str:
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

    session = create_session_with_user_agent()
    res = session.get(request_url)
    if res.status_code != 200:
        logger.error("Error getting radar data link")
        exit(1)
    soup = BeautifulSoup(res.text, "html.parser")

    radar_data_link = soup.find("a", {"rel": "bookmark"})
    if not radar_data_link:
        logger.error("Error getting radar data link")
        exit(1)

    radar_data_link = radar_data_link.get("href")  # type: ignore
    return radar_data_link  # type: ignore
