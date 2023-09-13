from copy import copy
from simple_sso.sso_client.client import Client

from django.contrib.auth import get_user_model

User = get_user_model()


class SSOClient(Client):
    def build_user(self, user_data):
        try:
            user = User.objects.get(email=user_data['email'])
            # Update user data, excluding username changes
            # Work on copied _tmp dict to keep an untouched user_data
            user_data_tmp = copy(user_data)
            del user_data_tmp['email']
            for _attr, _val in user_data_tmp.items():
                setattr(user, _attr, _val)
        except User.DoesNotExist:
            user = User(**user_data)
        user.set_unusable_password()
        user.save()
        return user