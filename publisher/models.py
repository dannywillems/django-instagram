from django.db import models

# Create your models here.
from django.utils.safestring import mark_safe


class Tag(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return str(self)


class InstagramAccount(models.Model):
    username = models.CharField(max_length=128)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.username


class Publication(models.Model):
    picture = models.ImageField(upload_to="uploads/")
    publish_at = models.DateTimeField()
    tags = models.ManyToManyField(Tag)
    instagram_account_id = models.ForeignKey(InstagramAccount, on_delete=models.CASCADE)

    def image_tag(self):
        return mark_safe("<img src='/%s' max-width='50' />" % self.picture)

    image_tag.short_description = "Picture"