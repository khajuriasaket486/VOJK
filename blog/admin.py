from django.contrib import admin
from blog.models import Post, BlogComment
from users.models import User, Profile
admin.site.register(Post)
# admin.site.register(Profile)
admin.site.register(BlogComment)