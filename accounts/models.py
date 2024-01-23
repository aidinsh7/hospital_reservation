from django.contrib.auth import models as auth_models
from django.db import models


class UserManager(auth_models.BaseUserManager):
    def create_user(self, username: str, phone_number: str,code_meli:str, is_staff=False, is_superuser=False,is_doctor=False):
        if not phone_number:
            raise ValueError('user must have Phone Number')
        if not username:
            raise ValueError('user must have username')
        if not code_meli:
            raise ValueError('user must have code meli')


        user = self.model(phone_number=phone_number, username=username,code_meli=code_meli)
        user.is_active = True
        user.is_staff = is_staff
        user.is_superuser = is_superuser
        user.is_doctor = is_doctor
        user.save()
        return user

    def create_superuser(self, username: str, phone_number: str, password: str = None,code_meli:str=None):
        user = self.create_user(
            username=username,
            phone_number=phone_number,
            code_meli=code_meli,
            is_doctor = True,
            is_staff=True,
            is_superuser=True,
        )
        user.set_password(password)
        user.save()
        return user
    

class Doctor_specialty(models.Model):
    class Meta:
        verbose_name = 'تخصص دکتر'
        verbose_name_plural = 'تخصص دکتر'
    name = models.CharField(max_length=200,verbose_name='تخصص')
    sub = models.ForeignKey('self',on_delete=models.CASCADE, null=True, blank=True,verbose_name='زیر مجموعه')
    is_sub = models.BooleanField(default=False)
    
    

class UserModel(auth_models.AbstractUser):
    class Meta:
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربران'
    profile_pic = models.ImageField(upload_to='images',null=True,verbose_name='عکس کاربر')
    full_name = models.CharField(max_length=35,verbose_name='نام و نام خانوادگی')
    username = models.CharField(max_length=20, unique=True,verbose_name='یوزر نیم')
    code_meli = models.CharField(max_length=10,unique=True,verbose_name='کد ملی')
    phone_number = models.CharField(max_length=12, unique=True,verbose_name= 'شماره همراه')
    password = models.CharField(max_length=255, null=True,verbose_name='رمز')
    is_doctor = models.BooleanField(default=False)
    major = models.ForeignKey(Doctor_specialty,on_delete=models.CASCADE,null=True,blank=True,verbose_name='تخصص دکتر')
    objects = UserManager()
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['username','code_meli']

    def __str__(self):
        if self.full_name:
            return self.full_name
        elif self.username:
            return self.username
        return self.pk

class OtpModel(models.Model):
    phone_number = models.CharField(max_length=12,verbose_name ='شماره همراه')
    otpCode = models.CharField(max_length=4, null=False, blank=False,verbose_name='کد')

    def __str__(self):
        return f"{self.phone_number} | {self.otpCode}"