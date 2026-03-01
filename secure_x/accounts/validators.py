import re
from django.core.exceptions import ValidationError


class StrongPasswordValidator:
    """Requires at least one uppercase letter, one number, and one special character."""

    def validate(self, password, user=None):
        errors = []

        if not re.search(r'[A-Z]', password):
            errors.append('Password must contain at least one uppercase letter.')

        if not re.search(r'[0-9]', password):
            errors.append('Password must contain at least one number.')

        if not re.search(r'[!@#$%^&*()_+\-=\[\]{};\':"\\|,.<>\/?]', password):
            errors.append('Password must contain at least one special character (!@#$%^&* etc.).')

        if errors:
            raise ValidationError(errors)

    def get_help_text(self):
        return 'Your password must contain at least one uppercase letter, one number, and one special character.'
