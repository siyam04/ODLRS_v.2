from django.db import models
from django.contrib.auth.models import User, AbstractUser


class DiagnosticCenter(models.Model):
    name = models.CharField(max_length=250, blank=False)
    image = models.ImageField(default='default_center.jpg', upload_to='diagnostic_center_pics')
    email = models.EmailField(blank=True)
    contact_no = models.CharField(max_length=20, blank=False)
    website = models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=150, blank=False)

    # admin = models.ForeignKey('DiagnosticAdmin', on_delete=models.CASCADE, related_name='admin_centers')

    class Meta:
        verbose_name_plural = 'Diagnostic Centers'
        ordering = ['-id']

    def __str__(self):
        return self.name


class DiagnosticAdmin(models.Model):
    username = models.CharField(max_length=20, unique=True, blank=False)
    password = models.CharField(max_length=100, unique=True, blank=False)

    center = models.ForeignKey(DiagnosticCenter, on_delete=models.CASCADE, related_name='center_admins')
    staff = models.ForeignKey('DiagnosticStaff', on_delete=models.CASCADE, related_name='staff_admins')
    # task_status = models.ForeignKey('TaskStatus', on_delete=models.CASCADE, related_name='task_status_admins')

    class Meta:
        verbose_name_plural = 'Diagnostic Admins'

    def __str__(self):
        return self.username


class DiagnosticStaff(models.Model):
    username = models.CharField(max_length=20, unique=True, blank=False)
    password = models.CharField(max_length=100, unique=True,  blank=False)

    center = models.ForeignKey(DiagnosticCenter, on_delete=models.CASCADE, related_name='center_staffs')

    class Meta:
        verbose_name_plural = 'Diagnostic Staffs'

    def __str__(self):
        return self.username

