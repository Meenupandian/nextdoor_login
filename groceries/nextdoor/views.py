import random
from django.core.mail import send_mail
from rest_framework import serializers
from .serializers import SendOtpSerializer, VerifyOtpSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User

def generate_otp():
    return str(random.randint(100000, 999999))

@csrf_exempt
def send_otp(request):
    if request.method == 'POST':#post method
        email = request.POST.get('email')
        try:
            user = User.objects.get(email=email)
            otp = generate_otp()
            user.otp = otp
            user.save()

            # Send OTP via email
            send_mail(
                'Your OTP Code',
                f'Your OTP code is {otp}.',
                'your_email@gmail.com',  # Sender email
                [email],                # Recipient email
                fail_silently=False,
            )
            return JsonResponse({'status': 'success', 'message': 'OTP sent successfully.'})
        except User.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'User does not exist.'})

    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})

@csrf_exempt
def verify_otp(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        otp = request.POST.get('otp')
        try:
            user = User.objects.get(email=email, otp=otp)
            user.otp = None  # Clear OTP after verification
            user.save()
            return JsonResponse({'status': 'success', 'message': 'OTP verified successfully.'})
        except User.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Invalid OTP or email.'})

    return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})
