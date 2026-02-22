from django.db import models

class Item(models.Model):

    BUSINESS_CHOICES = [
        ('studio', 'Salwa Studio'),
        ('perfumes', 'Salwa Perfumes'),
        ('cafe', 'Salwa Cafe'),
        ('electricals', 'Salwa Electricals'),
        ('bookshop', 'Salwa Bookshop'),
    ]

    business_type = models.CharField(
        max_length=20,
        choices=BUSINESS_CHOICES
    )

    title = models.CharField(max_length=150)
    subtitle = models.CharField(max_length=200, blank=True)
    description = models.TextField(blank=True)

    image = models.ImageField(upload_to='items/')
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True
    )

    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.business_type})"
