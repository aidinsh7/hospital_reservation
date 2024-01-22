from django.contrib import admin
from .models import UserModel,OtpModel
# Register your models here.

@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username','phone_number')
    list_filter = ('username','phone_number')




@admin.register(OtpModel)
class OtpCode(admin.ModelAdmin):
    list_display = ('phone_number','otpCode')