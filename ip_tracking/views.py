from django.http import JsonResponse, HttpResponse
from django_ratelimit.decorators import ratelimit

@ratelimit(key='ip', rate='5/m', block=True)
@ratelimit(key='user', rate='10/m', method='POST', block=True)
def sensitive_view(request):
    return JsonResponse({"message": "Sensitive view accessed successfully."})

def home(request):
    return HttpResponse("Welcome to the IP Tracking API!")

