from django.db import models
from admin_resumable.widgets import ResumableAdminWidget
from admin_resumable.fields import FormResumableFileField


class ResumableFileField(models.FileField):

    def formfield(self, **kwargs):
        defaults = {'form_class': FormResumableFileField}
        if self.model and self.name:
            defaults['widget'] = ResumableAdminWidget(attrs={
                'model': self.model,
                'field_name': self.name})
        kwargs.update(defaults)
        return super(ResumableFileField, self).formfield(**kwargs)
