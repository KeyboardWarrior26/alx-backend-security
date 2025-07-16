# IP Tracking System – alx-backend-security

This Django-based project implements IP tracking features to enhance security, analytics, and compliance. Built as part of the **ALX Backend Security** curriculum.

---

## 📌 Features

| Feature               | Description                                                                 |
|----------------------|-----------------------------------------------------------------------------|
| **IP Logging**        | Middleware logs IP address, timestamp, and request path                     |
| **Blacklisting**      | Blocks requests from known malicious IPs using a model-backed middleware     |
| **Geolocation**       | Enhances request logs with country and city using `ipinfo.io` API           |
| **Rate Limiting**     | Prevents abuse using `django-ratelimit`, with different limits for users    |
| **Anomaly Detection** | Celery task flags IPs that access sensitive paths or exceed hourly limits   |

---

## 🧰 Tech Stack

- **Django**
- **Celery** (for scheduled tasks)
- **Redis** (as Celery broker and for caching)
- **django-ratelimit** (rate limiting)
- **ipinfo.io** API (IP geolocation)
- **SQLite** (default database)

---

