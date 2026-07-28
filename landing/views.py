from django.shortcuts import render



from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Message
import json

def home(request):
    return render(request, 'home.html')

@csrf_exempt  # برای درخواست‌های AJAX
def send_message(request):
    if request.method == 'POST':
        try:
            name = request.POST.get('name')
            phone = request.POST.get('phone')
            message = request.POST.get('message')
            
            # ذخیره در دیتابیس
            Message.objects.create(
                name=name,
                phone=phone,
                message=message
            )
            
            return JsonResponse({'success': True, 'message': 'پیام با موفقیت ثبت شدددد'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})
    
    return JsonResponse({'success': False, 'message': 'متد اشتباه'})

