from tortoise import models, fields


class Article(models.Model):
    id = fields.IntField(pk=True)
    name = fields.TextField()


class Product(models.Model):
    id = fields.IntField(pk=True)
    name = fields.TextField(max_length=50,
                            verbose_name='Название',
                            null=False,
                            blank=False
                            )
    category = fields.TextField(max_length=100,
                                verbose_name='Категория',
                                )

class User(models.Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=50, unique=True)
    email = fields.CharField(max_length=100, unique=True)
    password_hash = fields.CharField(max_length=255)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    def __str__(self):
        return self.username

class Product(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255, null=False, blank=False)
    category = fields.CharField(max_length=255, null=True)

class User(models.Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=255, null=False, blank=False)
    email = fields.CharField(max_length=255, null=False, blank=False, unique=True)

class Order(models.Model):
    id = fields.IntField(pk=True)
    quantity = fields.IntField(null=False, blank=False)
    total_price = fields.FloatField(null=False, blank=False)
    created_at = fields.DatetimeField(auto_now_add=True)