from django.contrib import admin
from main.models import Users, Auth, Tweet, Follow

class AuthAdmin(admin.ModelAdmin):
	list_display = ('image','name', 'born_date', 'location', 'tweets',)



class TweetAdmin(admin.ModelAdmin):
	list_display = ('created_at', 'status', 'userr',)

class FollowAdmin(admin.ModelAdmin):
    list_display = ('fecha', 'activo',)
    search_fields = ('activo',)


admin.site.register(Users)
admin.site.register(Auth, AuthAdmin)
admin.site.register(Follow, FollowAdmin)
admin.site.register(Tweet, TweetAdmin)