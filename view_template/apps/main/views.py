from django.http import HttpRequest, HttpResponse


def homepage(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Homepage (apps.main)")


