# ip_tracking/middleware.py

import requests
from django.http import HttpResponseForbidden
from django.utils.deprecation import MiddlewareMixin
from django.utils.timezone import now
from ip_tracking.models import RequestLog, BlockedIP
from ipware import get_client_ip
from django.core.cache import cache

class IPLoggingMiddleware(MiddlewareMixin):
    def process_request(self, request):
        ip, _ = get_client_ip(request)
        if ip is None:
            ip = '0.0.0.0'

        # Block blacklisted IPs
        if BlockedIP.objects.filter(ip_address=ip).exists():
            return HttpResponseForbidden("Your IP has been blocked.")

        # Check cache first
        geo_cache_key = f"geo:{ip}"
        geo = cache.get(geo_cache_key)

        if not geo:
            geo = {"country": "", "city": ""}
            try:
                response = requests.get(f"https://ipinfo.io/{ip}/json")
                if response.status_code == 200:
                    data = response.json()
                    geo["country"] = data.get("country", "")
                    geo["city"] = data.get("city", "")
                cache.set(geo_cache_key, geo, timeout=86400)  # 24 hours
            except requests.RequestException:
                pass  # fail gracefully

        # Log request
        RequestLog.objects.create(
            ip_address=ip,
            timestamp=now(),
            path=request.path,
            country=geo["country"],
            city=geo["city"]
        )

