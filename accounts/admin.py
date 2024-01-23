from django.contrib import admin
from .models import UserModel,OtpModel,Doctor_specialty
# Register your models here.

@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username','phone_number','is_doctor','is_superuser','code_meli')
    list_filter = ('username','phone_number','is_doctor')
    
    def view_doctors(self, obj):
        return obj.is_doctor ==True



@admin.register(OtpModel)
class OtpCode(admin.ModelAdmin):
    list_display = ('phone_number','otpCode')

@admin.register(Doctor_specialty)
class Doctor_specialty_Admin(admin.ModelAdmin):
    list_display = ('name',)