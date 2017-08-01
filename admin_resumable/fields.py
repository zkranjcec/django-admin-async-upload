from django.core.exceptions import ValidationError
from django.forms import fields

from admin_resumable.widgets import ResumableWidget, AdminResumableWidget


class FormResumableFileField(fields.FileField):
    widget = ResumableWidget


class FormAdminResumableFileField(fields.FileField):
    widget = AdminResumableWidget

    def to_python(self, data):
        if self.required:
            if not data or data == "None":
                raise ValidationError(self.error_messages['empty'])
        return data
