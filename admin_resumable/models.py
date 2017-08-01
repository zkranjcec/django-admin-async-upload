from django.contrib.contenttypes.models import ContentType
from django.db import models

from admin_resumable.fields import FormAdminResumableFileField
from admin_resumable.widgets import AdminResumableWidget


class ResumableFileField(models.FileField):

    def formfield(self, **kwargs):
        content_type_id = ContentType.objects.get_for_model(self.model).id
        defaults = {
            'form_class': FormAdminResumableFileField,
            'widget': AdminResumableWidget(attrs={
                'content_type_id': content_type_id,
                'field_name': self.name})
        }
        kwargs.update(defaults)
        return super(ResumableFileField, self).formfield(**kwargs)
