from .translit import get_english_translit


def user_avatar(instance, filename: str) -> str:
    filename: str = f'{get_english_translit(instance.get_full_name())}.{filename.split(".")[-1]}'
    return f"avatars/{instance.pk}-{filename}"
