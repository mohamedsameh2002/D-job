from django.db import models

# Create your models here.
class Category (models.Model):
    name=models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.name


class Book (models.Model):
    starus_books=[
        ('availble','availble'),
        ('rental','rental'),
        ('sold','sold'),
    ]

    title=models.CharField(max_length=250)
    athour=models.CharField(max_length=250)
    photo_book=models.ImageField(upload_to='photos',null=True,blank=True)
    photo_athour=models.ImageField(upload_to='photos',null=True,blank=True)
    pages_book=models.IntegerField(null=True,blank=True)
    price=models.DecimalField(decimal_places=2,max_digits=5,null=True,blank=True)
    rental_price_inday=models.DecimalField(decimal_places=2,max_digits=5,null=True,blank=True)
    total_rental=models.DecimalField(decimal_places=2,max_digits=5,null=True,blank=True)
    rebtal_time=models.IntegerField(null=True,blank=True)
    active=models.BooleanField(default=True)
    starus=models.CharField(max_length=50,choices=starus_books,null=True,blank=True)
    category=models.ForeignKey(Category,on_delete=models.PROTECT,null=True,blank=True)
    def __str__(self) -> str:
        return self.title

