from django.contrib import admin
from app_admin.models import *
from app_user.models import *
# Register your models here.
admin.site.register(RegisterTb)
admin.site.register(CategoryTb)
admin.site.register(ReviewTb)
admin.site.register(ShowTb)
admin.site.register(WatchlistTb)
