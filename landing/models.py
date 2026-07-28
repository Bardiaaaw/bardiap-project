from django.db import models

class Message(models.Model):
    name = models.CharField(max_length=100, verbose_name="نام و نام خانوادگی")
    phone = models.CharField(max_length=11, verbose_name="شماره تماسو بده داشته باشیم")
    message = models.TextField(verbose_name="پیام")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ارسال")
    
    class Meta:
        verbose_name = "پیام"
        verbose_name_plural = "پیام‌ها"
        ordering = ['-created_at']  # پیام‌های جدید اول نشون داده بشن
    
    def __str__(self):
        return f"{self.name} - {self.created_at.strftime('%Y/%m/%d %H:%M')}"