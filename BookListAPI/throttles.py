from rest_framework.throttling import AnonRateThrottle,UserRateThrottle

class TenCallsPerMinute(UserRateThrottle):
    scope = 'ten'