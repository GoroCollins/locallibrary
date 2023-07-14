from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, Language

# Register your models here.
class BooksInline(admin.StackedInline):
    model = Book
    extra = 0
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'date_of_birth', 'date_of_death']
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')] # fields that will be shown on the form
    inlines = [BooksInline]

admin.site.register(Author, AuthorAdmin)
class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'display_genre']
    inlines = [BooksInstanceInline]
admin.site.register(Book, BookAdmin)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ['status', 'due_back']
    fieldsets = ((None, {'fields':('id', 'book', 'imprint')}),
                 ('Availability',{'fields':('due_back', 'status')}),)

admin.site.register(BookInstance, BookInstanceAdmin)

admin.site.register(Language)
admin.site.register(Genre)