from celery import shared_task
from django.utils.timezone import now, timedelta
from ip_tracking.models import RequestLog, SuspiciousIP

SENSITIVE_PATHS = ['/admin', '/login']

@shared_task
def detect_suspicious_ips():
    one_hour_ago = now() - timedelta(hours=1)
    logs = RequestLog.objects.filter(timestamp__gte=one_hour_ago)

    ip_counts = {}
    flagged_ips = set()

    for log in logs:
        ip = log.ip_address
        ip_counts[ip] = ip_counts.get(ip, 0) + 1

        # Flag sensitive path access
        if log.path in SENSITIVE_PATHS and ip not in flagged_ips:
            SuspiciousIP.objects.get_or_create(
                ip_address=ip,
                reason=f"Accessed sensitive path: {log.path}"
            )
            flagged_ips.add(ip)

    # Flag IPs with excessive traffic
    for ip, count in ip_counts.items():
        if count > 100 and ip not in flagged_ips:
            SuspiciousIP.objects.get_or_create(
                ip_address=ip,
                reason="More than 100 requests in 1 hour"
            )

