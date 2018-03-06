from django.db import models

# Create your models here.

class app_1(models.Model):
    native_id = models.AutoField(primary_key = True)   #AutoField => auto incrementing field
    first_name = models.CharField(max_length=100, default = "")
    last_name = models.CharField(max_length=100, default = "")
    email_id = models.CharField(max_length=100, default = "archimedha@mailinator.com")
    # added_time = models.DateTimeField(auto_now_add=True, blank=True)
    # random_number = models.IntegerField(default=0)
    # random_varchar = models.CharField(max_length = 100, default = "")

    def __str__(self):
        return str(self.native_id)