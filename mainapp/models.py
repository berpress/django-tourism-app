from django.db import models


class ListOfCountries(models.Model):
    name = models.CharField(verbose_name="name", max_length=64, unique=True)
    description = models.TextField(verbose_name="description", blank=True)
    is_active = models.BooleanField(verbose_name="is active", default=True)

    def __str__(self):
        return self.name


class Regions(models.Model):
    country = models.ForeignKey(ListOfCountries, on_delete=models.CASCADE)
    name = models.CharField(verbose_name="name", max_length=64, unique=True)
    description = models.TextField(verbose_name="description", blank=True)
    is_active = models.BooleanField(verbose_name="is active", default=True)

    def __str__(self):
        return self.name


class Accommodation(models.Model):
    country = models.ForeignKey(ListOfCountries, on_delete=models.CASCADE)
    region = models.ForeignKey(Regions, on_delete=models.CASCADE)
    name = models.CharField(verbose_name="name place", max_length=128, unique=True)
    image = models.ImageField(upload_to="accommodation_img", blank=True)
    short_desc = models.TextField(
        verbose_name="short description", max_length=60, blank=True
    )
    description = models.TextField(verbose_name="description", blank=True)
    availability = models.PositiveIntegerField(verbose_name="free rooms")
    price = models.DecimalField(
        verbose_name="price", max_digits=8, decimal_places=2, default=0
    )
    room_desc = models.TextField(
        verbose_name="short description room", max_length=60, blank=True
    )
    is_active = models.BooleanField(verbose_name="is active", default=True)

    @staticmethod
    def get_items():
        return Accommodation.objects.filter(is_active=True).order_by(
            "country", "regions", "name"
        )

    def __str__(self):
        return f"{self.name} ({self.country.name})"
