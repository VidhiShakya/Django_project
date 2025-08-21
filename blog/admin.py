from django.contrib import admin

# Register your models here.


from blog.models import Users,Posts
# Register your models here.
admin.site.register(Users)

admin.site.register(Posts)