from django.core.validators import FileExtensionValidator
from django.db import models


class Book(models.Model):
    title = models.CharField(
        verbose_name="Book title",
        db_index=True,
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=False,
        default="",
        max_length=300,
    )
    description = models.TextField(
        verbose_name="Book description",
        db_index=False,
        primary_key=False,
        unique=False,
        editable=True,
        blank=True,
        null=False,
        default="",
    )
    book_file = models.FileField(
        verbose_name="Book file",
        validators=[FileExtensionValidator(["pdf", "docx", "FB2"])],
        unique=False,
        editable=True,
        blank=True,
        null=True,
        default=None,
        upload_to="books",
    )
    # is_view
