from django.db import models

<<<<<<< HEAD
CATEGORIES = [
    ('Politics', 'Political category'),
    ('Education', 'Education category'),
    ('Story', 'Story books')
]
# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(choices= CATEGORIES, max_length=100)
    year = models.IntegerField()
    cost = models.IntegerField()
    isbn = models.CharField(unique=True, max_length=15, null=True)
    cover = models.ImageField(upload_to='covers/', null=True)
    published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'books'


# RUN THE COMMANDS AFTER UPDATING THE MODEL/TABLE OR MAKING ANY CHANGES
# python manage.py makemigrations
# python manage.py migrate


# COMMAND FOR CREATING A USER ADMIN
# python manage.py createsuperuser
# username - mercy
# password -12345678
=======
# Create your models here.
>>>>>>> 354ec5c36c105243fafba5722f18be2f62fbf783
