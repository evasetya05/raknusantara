from django.db import models
from django.contrib.auth.models import User

from PIL import Image, ImageOps


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ('name',)

    def __str__(self):
        return self.name


class Item(models.Model):
    category = models.ForeignKey(Category, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    image_secondary = models.ImageField(upload_to='item_images', blank=True, null=True)
    image_tertiary = models.ImageField(upload_to='item_images', blank=True, null=True)
    is_sold = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        def _process_image(field):
            image_field = getattr(self, field)
            if not image_field:
                return

            try:
                with Image.open(image_field.path) as img:
                    img = ImageOps.exif_transpose(img)
                    img = ImageOps.fit(img, (320, 320), method=Image.LANCZOS)

                    if img.mode in ('RGBA', 'LA'):
                        img = img.convert('RGB')

                    img_format = img.format or 'JPEG'
                    save_kwargs = {"optimize": True}
                    if img_format.upper() in {'JPEG', 'JPG'}:
                        save_kwargs['quality'] = 85

                    img.save(image_field.path, format=img_format, **save_kwargs)
            except FileNotFoundError:
                # Image file might have been removed from storage; ignore.
                pass

        for field_name in ('image', 'image_secondary', 'image_tertiary'):
            _process_image(field_name)

    def get_images(self):
        return [image_field for image_field in (self.image, self.image_secondary, self.image_tertiary) if image_field]

    @property
    def primary_image(self):
        images = self.get_images()
        return images[0] if images else None
