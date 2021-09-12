director = 'DI'
admin = 'AD'
cook = 'CO'
cashier = 'CA'
cleaner = 'CL'

POSITIONS = [
    (director, 'Директор'),
    (admin, 'Администратор'),
    (cook, 'Повар'),
    (cashier, 'Кассир'),
    (cleaner, 'Уборщик')
]

from django.db import models
from datetime import datetime



class Product(models.Model):
    #product_id = models.AutoField()#
    name = models.CharField(max_length = 64)
    price = models.FloatField(default = 0.0)
    composition = models.TextField(default = "Состав не указан")



class Staff(models.Model):
    #stuff = models.AutoField()-ебонная ошибка на 2 дня#
    full_name = models.CharField(max_length = 64)
    position = models.CharField(max_length=2,
                                choices=POSITIONS,
                                default=cashier)
    labor_contract = models.IntegerField()

    def get_last_name(self):
        return self.full_name.split()[0]

class Order(models.Model):
    time_in = models.DateTimeField(auto_now_add = True)
    time_out = models.DateTimeField(null = True)
    cost = models.FloatField(default = 0.0)
    take_away = models.BooleanField(default = False)
    complete = models.BooleanField(default = False)
    staff = models.ForeignKey(Staff, on_delete = models.CASCADE)
    products = models.ManyToManyField(Product, through='ProductOrder')

    def finish_order(self):
        self.time_out = datetime.now()
        self.complete = True
        self.save()

    def get_duration(self):
        if self.complete:  # если завершен, возвращаем разность объектов
            return (self.time_out - self.time_in).total_seconds() // 60
        else:
            return (datetime.now() - self.time_in).total_seconds() // 60

class ProductOrder(models.Model):
    amount = models.IntegerField(default = 1)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    order = models.ForeignKey(Order, on_delete = models.CASCADE)