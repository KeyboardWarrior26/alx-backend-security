# ip_tracking/middleware.py

from django.http import HttpResponseForbidden
from django.utils.deprecation import MiddlewareMixin
from ip_tracking.models import RequestLog
from ipware import get_client_ip
from django.utils.timezone import now

class IPLoggingMiddleware(MiddlewareMixin):
    def process_request(self, request):
        ip, _ = get_client_ip(request)
        if ip is None:
            ip = '0.0.0.0'

         #Block IP if blacklisted
        if BlockedIP.objects.filter(ip_address=ip).exists():
            return HttpResponseForbidden("Your IP has been blocked.")

        RequestLog.objects.create(
            ip_address=ip,
            timestamp=now(),
            path=request.path
        )
