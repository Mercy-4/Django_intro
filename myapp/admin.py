from django.contrib import admin

<<<<<<< HEAD
from myapp.models import Book

# Register your models here.
admin.site.site_title="Bookshop"
admin.site.site_header="Bookshop Admin"
admin.site.index_title="Books Management System"

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'cost', 'isbn', 'category')
    search_fields = ('title', 'year', 'isbn', 'category')
    list_filter = ('category', 'year')
    ordering = ('-title','year')
=======
# Register your models here.
>>>>>>> 354ec5c36c105243fafba5722f18be2f62fbf783
