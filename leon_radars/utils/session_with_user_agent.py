import requests
from fake_useragent import UserAgent  # type: ignore


def create_session_with_user_agent() -> requests.Session:
    session = requests.Session()
    session.headers.update({"User-Agent": UserAgent().chrome})  # type: ignore
    return session
