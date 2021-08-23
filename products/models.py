from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=200)
    friendly_name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class CatEarColor(models.Model):
    """ Creates color options for cat ears"""
    BLUE = 'BL'
    PINK = 'PN'
    GREEN = 'GR'
    WHITE = 'WH'
    BLACK = 'BK'
    CATEAR_COLOR = [
        (BLUE, 'blue'),
        (PINK, 'pink'),
        (GREEN, 'green'),
        (WHITE, 'white'),
        (BLACK, 'black'),
    ]
    catear_color = models.CharField(
        max_length=2, choices=CATEAR_COLOR, default=BLUE
    )

    def __str__(self):
        return self.catear_color


class QuipuForm(models.Model):
    """ Creates color options and a name field """
    PEARL_WHITE = 'PW'
    LIGHT_BLUE = 'LB'
    IRIDECENT_PURPLE = 'IP'
    TRUQUOISE = 'TU'
    IRIDECENT_BLUE = 'IB'
    SCARBEUS_GREEN = 'SG'
    MAUVE = 'MA'
    BURGUNDY = 'BU'
    BORDEAUX = 'BX'
    QUIPU_COLOR = [
        (PEARL_WHITE, 'Pearl White'),
        (LIGHT_BLUE, 'Light Blue'),
        (IRIDECENT_PURPLE, 'Iridecent Purple'),
        (TRUQUOISE, 'Turquoise'),
        (IRIDECENT_BLUE, 'Iridecent Dark Blue'),
        (SCARBEUS_GREEN, 'Scarabeus Green'),
        (MAUVE, 'Mauve'),
        (BURGUNDY, 'Burgundy'),
        (BORDEAUX, 'Bordeaux'),
    ]
    quipu_color = models.CharField(
        max_length=2, choices=QUIPU_COLOR, default=PEARL_WHITE
    )
    LABRADORITE = 'LB'
    AMETHYST = 'AM'
    MALACHITE = 'ML'
    ROSE_QUARTZ = 'RQ'
    CITRINE = 'CI'
    GARNET = 'GA'
    QUPIU_STONE_PEARL = [
        ('LB', 'Labradorite'),
        ('AM', 'Amethyst'),
        ('ML', 'Malachite'),
        ('RQ', 'Rose Quartz'),
        ('CI', 'Citrine'),
        ('GA', 'Garnet'),
    ]
    quipu_stone_pearl = models.CharField(
        max_length=2, choices=QUPIU_STONE_PEARL, default=LABRADORITE
    )
    name_field = models.CharField(max_length=12)

    def __str__(self):
        return f'You picked {self.quipu_color} and {self.quipu_stone_pearl}'


class Product(models.Model):
    """ Handles product information """
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    sku = models.CharField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=200)
    description = models.TextField()
    catear_color_option = models.ManyToManyField('CatEarColor')
    catears_has_colors = models.BooleanField(default=False, null=True,
                                             blank=True)
    qupiu_custom_form = models.BooleanField(default=False, null=True,
                                            blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
