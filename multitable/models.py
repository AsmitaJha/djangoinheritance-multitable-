from django.db import models

# Create your models here.

'''creating 3 models:
a. Cafe: It is the parent model which contains the common fields 'name', and 'order'(number of orders) which is required when the customer orders either cake or colddrink
b. Cake: It is the first child model which contains a field 'candles' as the integerfield which indicates how many candles were ordered with the cake
c. ColdDrink: It is another child model which contains a field 'straw' as the BooleanField which indicates whether straw was ordered with the colddrink or not'''

class Cafe(models.Model):
    name=models.CharField(max_length=50)
    orders=models.IntegerField()
    
    
class Cake(Cafe):
    candles=models.IntegerField()
    
class ColdDrink(Cafe):
    straw=models.BooleanField()
    
'''But, it seems to be only one field in 'Cake' and 'ColdDrink' models, they have altogether 3 fields i.e.
Cake:
a. name
b. orders
c. candles

ColdDrink:
a. name
b. orders
c. candles

It's because they are inherited from the cafe model'''

#**Difference** from abstract base class: It doesn't have any 'meta' class in any model unlike abstract base class or proxy model
'''
Abstract Base Class: It requires 'abstract=True' inside the meta class of parent model
Proxy model: It requires 'proxy=True' inside the child model. Also, in proxy model, child models can't have their own fields like 'candles' in 'Cake' model and 'straw' in 'ColdDrink' model '''