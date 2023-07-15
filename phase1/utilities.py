from .models import Advocates

def get_hostname(request):
    return request.get_host().split(':')[0].lower()


def get_client(request):
    hostname = get_hostname(request)
    subdomain = hostname.split('.')[0]
    return Advocates.objects.filter(name=subdomain).first()