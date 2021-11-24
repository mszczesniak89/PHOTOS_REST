# exceptions.py
from rest_framework.exceptions import APIException


class InvalidExpirationTime(APIException):
    status_code = 404
    default_detail = "Specified link expiration time is outside of the allowed range (300 - 30000secs)"
    default_code = "link_expiration_time_not_in_range"

