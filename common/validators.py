from uuid import UUID

from typing import Any
from datetime import timedelta

from django.utils import timezone
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()


def validate_user_email(email: str) -> bool:
    user = User.objects.filter(email=email).exists()
    return True if user else False


def is_valid_uuid(uuid_to_test, version=4):
    try:
        uuid_obj = UUID(uuid_to_test, version=version)
    except ValueError:
        return False
    return str(uuid_obj) == uuid_to_test