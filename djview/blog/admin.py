from django.contrib import admin

# Register your models here.
from .models import PostModel,HelloWorld

class AdminHelloWorldModel(admin.ModelAdmin):
    fields = [
           'title',
            'slug',
            'content',
            'publish',
            'publish_date',
    ]
    readonly_fields = ['timetamp','update']
    class Meta:
        model=PostModel


admin.site.register(PostModel)
admin.site.register(HelloWorld,AdminHelloWorldModel)