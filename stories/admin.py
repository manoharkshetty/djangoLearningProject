from django.contrib import admin

from stories.models import Story

class StoryAdmin(admin.ModelAdmin):
	list_display=('title', 'moderator','created_at')
	list_filter=('created_at',)
	search_fields=('title',)

admin.site.register(Story,StoryAdmin)

# Register your models here.
