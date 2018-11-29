from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.template import defaultfilters
from ckeditor.fields import RichTextField


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=20, db_index=True)
    slug = models.SlugField(max_length=20, unique=True ,db_index=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        ordering = ('name', )
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('products:product_list_by_category', args=[self.slug])

class Trademark(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name="Nombre")
    slug = models.SlugField(max_length=20, unique=True ,db_index=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        ordering = ('name', )
        verbose_name = 'marca'
        verbose_name_plural = 'marcas'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('products:product_list_by_trademark', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE, verbose_name="Categoría")
    name = models.CharField(max_length=20, db_index=True, verbose_name="Nombre")
    slug = models.SlugField(max_length=20, db_index=True, verbose_name="Nombre")
    trademark = models.ForeignKey(Trademark, related_name='products', on_delete=models.CASCADE, verbose_name="Marca")
    description = RichTextField(blank=True, verbose_name="Descripción")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")
    available = models.BooleanField(default=True, verbose_name="Disponible")
    stock = models.PositiveIntegerField(verbose_name="Unidades en existencia")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")
    image = models.ImageField(verbose_name="Imagen", upload_to='products', blank=True)

    class Meta:
        ordering = ('name','price')
        index_together = (('id', 'slug'),)
        verbose_name = "producto"
        verbose_name_plural = "productos"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('products:product_detail', args=[self.id, self.slug])

    def save(self, *args, **kwargs):
      self.slug = defaultfilters.slugify(self.name)
      super(Product, self).save(*args, **kwargs)