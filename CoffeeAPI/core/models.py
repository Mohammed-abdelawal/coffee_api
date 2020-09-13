from djongo import models

# Create your models here.


class CoffeeMachine(models.Model):
    TYPE_CHOICES = (
        ('CM1', 'COFFEE_MACHINE_LARGE'),
        ('CM0', 'COFFEE_MACHINE_SMALL'),
        ('EM0', 'ESPRESSO_MACHINE')
    )
    MODEL_CHOICES = (
        (1, 'BASE_MODEL'),
        (2, 'PREMIUM_MODEL'),
        (3, 'DELUXE_MODEL')
    )

    product_type = models.CharField(choices=TYPE_CHOICES, max_length=3)
    water_line_compatible = models.BooleanField()
    
    # not from product schema > i get it from SKU List
    model_type = models.IntegerField(choices=MODEL_CHOICES)
    
    sku = models.CharField(editable=False, max_length=5, blank=True)

    def save(self, *args, **kwargs):
        _sku = self.product_type + '0'+str(self.model_type)
        self.sku = _sku

        super(CoffeeMachine, self).save(*args, **kwargs)

    def __str__(self):
        return self.sku

    class Meta:
        unique_together = [['sku', 'water_line_compatible']]


class CoffeePod(models.Model):
    TYPE_CHOICES = (
        ('CP1', 'COFFEE_POD_LARGE'),
        ('CP0', 'COFFEE_POD_SMALL'),
        ('EP0', 'ESPRESSO_POD')
    )
    FLAVOR_CHOICES = (
        (0, 'COFFEE_FLAVOR_VANILLA'),
        (1, 'COFFEE_FLAVOR_CARAMEL'),
        (2, 'COFFEE_FLAVOR_PSL'),
        (3, 'COFFEE_FLAVOR_MOCHA'),
        (4, 'COFFEE_FLAVOR_HAZELNUT')
    )
    PACK_SIZE_CHOICES = ((1, 1), (3, 3), (5, 5), (7, 7))

    product_type = models.CharField(choices=TYPE_CHOICES, max_length=3)
    coffee_flavor = models.IntegerField(choices=FLAVOR_CHOICES)
    pack_size = models.IntegerField(choices=PACK_SIZE_CHOICES)
    sku = models.CharField(unique=True, editable=False,
                           blank=True, max_length=5)

    def save(self, *args, **kwargs):
        _sku = self.product_type + \
            str(self.coffee_flavor) + str(self.pack_size)
        self.sku = _sku

        super(CoffeePod, self).save(*args, **kwargs)

    def __str__(self):
        return self.sku
