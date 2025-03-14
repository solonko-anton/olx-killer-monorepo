import mimetypes

from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _
from PIL import Image as PILImage

from apps.common import errors
from apps.common.models import HistoricalModel


class ProductImage(HistoricalModel, models.Model):
    MAX_FILE_SIZE_MB = settings.MAX_IMAGE_FILE_SIZE_MB
    ALLOWED_MIME_TYPES = settings.ALLOWED_IMAGE_MIME_TYPES

    product = models.ForeignKey(to='Product', on_delete=models.CASCADE, related_name='product_images')
    image = models.ImageField(
        _('Image'),
        upload_to='products/images/%Y/%m/%d',
        null=True,
        blank=True,
        default=settings.DEFAULT_PRODUCT_IMAGE,
        help_text=_('Allowed image formats: %s') % ', '.join(ALLOWED_MIME_TYPES),
    )

    def __str__(self):
        return f"Image for the product '{self.product}'"

    class Meta:
        db_table = 'product_image'
        verbose_name = _('Product Image')
        verbose_name_plural = _('Product Images')

    def clean(self):
        super().clean()
        if self.pk is not None:
            existing_image = ProductImage.objects.get(pk=self.pk).image

            if self.image == existing_image:
                return

        if self.image:
            try:
                mime_type, encoding = mimetypes.guess_type(self.image.name)
                if mime_type not in self.ALLOWED_MIME_TYPES:
                    raise ValidationError(errors.INVALID_IMAGE_TYPE)

                with PILImage.open(self.image) as img:
                    img.verify()

            except Exception:
                raise ValidationError(errors.INVALID_IMAGE)

            if self.image.size > self.MAX_FILE_SIZE_MB * 1024 * 1024:
                raise ValidationError(errors.IMAGE_SIZE_EXCEEDED)

        if self.product.product_images.count() > settings.MAX_COUNT_IMAGE_FILES:
            raise ValidationError(errors.INVALID_COUNT_IMAGE)
