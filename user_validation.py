import re
from typing import Optional


class UserValidation:
    @staticmethod
    def validate_email(email: Optional[str]) -> bool:
        if email is None:
            return False
        email = email.strip()
        if not email:
            return False
        pattern = re.compile(r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$')
        return bool(pattern.fullmatch(email))

    @staticmethod
    def validate_username(username: Optional[str]) -> bool:
        if username is None:
            return False
        username = username.strip()
        if not username:
            return False
        pattern = re.compile(r'^[A-Za-z0-9_]{3,20}$')
        return bool(pattern.fullmatch(username))

    @staticmethod
    def validate_phone_number(phone: Optional[str]) -> bool:
        if phone is None:
            return False
        phone = phone.strip()
        if not phone:
            return False
        if not phone.isdigit():
            return False
        pattern = re.compile(r'^(?:0(?:10|11|12|15)\d{8}|20(?:10|11|12|15)\d{8})$')
        return bool(pattern.fullmatch(phone))

    @staticmethod
    def validate_national_id(national_id: Optional[str]) -> bool:
        if national_id is None:
            return False
        national_id = national_id.strip()
        if not national_id:
            return False
        if not national_id.isdigit():
            return False
        if len(national_id) != 14:
            return False

        century = national_id[0]
        year = national_id[1:3]
        month = national_id[3:5]
        day = national_id[5:7]
        governorate = national_id[7:9]

        if century not in ('2', '3'):
            return False

        try:
            m = int(month)
            if not (1 <= m <= 12):
                return False
        except ValueError:
            return False

        try:
            d = int(day)
            if not (1 <= d <= 31):
                return False
        except ValueError:
            return False

        try:
            g = int(governorate)
            if not (1 <= g <= 88):
                return False
        except ValueError:
            return False

        return True
