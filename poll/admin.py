'''# Importing the required modules

# The admin module is used to create the admin site for the application
from django.contrib import admin

# The models module is used to import the models from the models.py file
from .models import Candidate, Position


# The admin.site.register() method is used to register the models to the admin site
@admin.register(Position)

# The PositionAdmin class is used to create the admin site for the Position model
class PositionAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)


@admin.register(Candidate)

# The CandidateAdmin class is used to create the admin site for the Candidate model
class CandidateAdmin(admin.ModelAdmin):
    list_display = ('name','position')
    list_filter = ('position',)
    search_fields = ('name','position')
    readonly_fields = ('total_vote',)'''

# Importing the required modules
from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from .models import Candidate, Position

# Register the Position model with a custom admin class
@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    list_display = ('title', 'delete_button')  # Add delete button

    def delete_button(self, obj):
        return format_html(
            '<a class="button" style="color:red;" href="{}">Delete</a>',
            reverse('admin:%s_%s_delete' % (obj._meta.app_label, obj._meta.model_name), args=[obj.pk])
        )

    delete_button.short_description = 'Delete'
    delete_button.allow_tags = True

# Register the Candidate model with a custom admin class
@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'delete_button')  # Add delete button
    list_filter = ('position',)
    search_fields = ('name', 'position')
    readonly_fields = ('total_vote',)

    def delete_button(self, obj):
        return format_html(
            '<a class="button" style="color:red;" href="{}">Delete</a>',
            reverse('admin:%s_%s_delete' % (obj._meta.app_label, obj._meta.model_name), args=[obj.pk])
        )

    delete_button.short_description = 'Delete'
    delete_button.allow_tags = True
