import urllib.parse


class Constants:
    WAIT_TIME_IN_SECONDS = 5


class CowinAPIs:
    BASE_URL = "https://cdn-api.co-vin.in"
    CALENDAR_BY_DISTRICT = urllib.parse.urljoin(
        BASE_URL, "/api/v2/appointment/sessions/public/calendarByDistrict"
    )
