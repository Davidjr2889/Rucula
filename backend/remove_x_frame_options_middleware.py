class RemoveXFrameOptionsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if "/admin/" in request.path:
            # Use the del keyword to remove the header, if it exists.
            if 'X-Frame-Options' in response:
                del response['X-Frame-Options']
        return response
