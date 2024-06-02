from django.urls import reverse
from django.shortcuts import redirect


class UserRestrictMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # restricted admin url for custom admin site
        if request.path.find("/dashboard/") > -1:
            if not request.user.is_superuser:
                return redirect(reverse('users:login'))

        response = self.get_response(request)
        return response
