# ip_tracking/middleware.py

from django.utils.deprecation import MiddlewareMixin
from ip_tracking.models import RequestLog
from ipware import get_client_ip
from django.utils.timezone import now

class IPLoggingMiddleware(MiddlewareMixin):
    def process_request(self, request):
        ip, _ = get_client_ip(request)
        if ip is None:
            ip = '0.0.0.0'

        RequestLog.objects.create(
            ip_address=ip,
            timestamp=now(),
            path=request.path
        )
