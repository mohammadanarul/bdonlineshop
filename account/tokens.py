from django.contrib.auth.tokens import PasswordResetTokenGenerator


class accountRegisterTokenGenerate(PasswordResetTokenGenerator):
    pass
    # def _make_hash_value(self, user, timestamp):
    #     return (render_to_string.text_type(user.id) + render_to_string.text_type(timestamp) + render_to_string.text_type(user.is_active))

userAccountRegisterActiveTokenGenerate = accountRegisterTokenGenerate()