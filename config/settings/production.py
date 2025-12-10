import os

from .base import *  # noqa

# ------------------------------------------------------------------------------
# CORE PRODUCTION FLAGS
# ------------------------------------------------------------------------------

DEBUG = False

# On Render, set these in the Dashboard → Environment
ALLOWED_HOSTS = env.list(
    "ALLOWED_HOSTS",
    default=["shulechap.onrender.com"],
)

CSRF_TRUSTED_ORIGINS = env.list(
    "CSRF_TRUSTED_ORIGINS",
    default=["https://shulechap.onrender.com"],
)

# ------------------------------------------------------------------------------
# SECURITY SETTINGS
# ------------------------------------------------------------------------------

# Only turn this on once you have HTTPS working
SECURE_SSL_REDIRECT = env.bool("SECURE_SSL_REDIRECT", default=True)

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

SECURE_HSTS_SECONDS = env.int("SECURE_HSTS_SECONDS", default=60 * 60 * 24 * 7)  # 1 week
SECURE_HSTS_INCLUDE_SUBDOMAINS = env.bool(
    "SECURE_HSTS_INCLUDE_SUBDOMAINS",
    default=False,
)
SECURE_HSTS_PRELOAD = env.bool("SECURE_HSTS_PRELOAD", default=False)

SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True

X_FRAME_OPTIONS = "DENY"
REFERRER_POLICY = "same-origin"

# ------------------------------------------------------------------------------
# DATABASE (uses DATABASE_URL from environment)
# ------------------------------------------------------------------------------

# base.py already configures DATABASES from env.db("DATABASE_URL", ...)
# If you need to force a different default for production, you can uncomment:

# DATABASES["default"] = env.db(
#     "DATABASE_URL",
#     default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}",
# )

# ------------------------------------------------------------------------------
# STATIC & MEDIA (Render will collectstatic on build)
# ------------------------------------------------------------------------------

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

# Keep additional static dirs if needed
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "assets"),
]

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# ------------------------------------------------------------------------------
# EMAIL (override defaults from base.py via env vars)
# ------------------------------------------------------------------------------

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

EMAIL_HOST = env("EMAIL_HOST", default="smtp.gmail.com")
EMAIL_PORT = env.int("EMAIL_PORT", default=587)
EMAIL_HOST_USER = env("EMAIL_HOST_USER", default="no-reply@shulechap.local")
EMAIL_HOST_PASSWORD = env("EMAIL_HOST_PASSWORD", default="")
EMAIL_USE_TLS = env.bool("EMAIL_USE_TLS", default=True)

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# ------------------------------------------------------------------------------
# PAYMENTS / SSL COMMERZ / BRAINTREE
# ------------------------------------------------------------------------------

STORE_ID = env("STORE_ID", default="test_store_id")
STORE_PASS = env("STORE_PASS", default="test_store_pass")

SSL_ISSANDBOX = env.bool("SSL_ISSANDBOX", default=True)

BRAINTREE_MERCHANT_ID = env("BRAINTREE_MERCHANT_ID", default="")
BRAINTREE_PUBLIC_KEY = env("BRAINTREE_PUBLIC_KEY", default="")
BRAINTREE_PRIVATE_KEY = env("BRAINTREE_PRIVATE_KEY", default="")

# ------------------------------------------------------------------------------
# MAILCHIMP (disabled for now)
# ------------------------------------------------------------------------------

USE_MAILCHIMP = env.bool("USE_MAILCHIMP", default=False)
MAILCHIMP_API_KEY = env("MAILCHIMP_API_KEY", default="")
MAILCHIMP_AUDIENCE_ID = env("MAILCHIMP_AUDIENCE_ID", default="")
MAILCHIMP_SERVER_PREFIX = env("MAILCHIMP_SERVER_PREFIX", default="")

# ------------------------------------------------------------------------------
# LOGGING
# ------------------------------------------------------------------------------

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "[{levelname}] {asctime} {name}: {message}",
            "style": "{",
        },
        "simple": {
            "format": "[{levelname}] {message}",
            "style": "{",
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "INFO",
    },
}

# ------------------------------------------------------------------------------
# IMPORTANT: we DO NOT override INSTALLED_APPS or MIDDLEWARE here.
# They come entirely from base.py
# ------------------------------------------------------------------------------
