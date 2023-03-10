from time import time

from currency.models import RequestResponseLog


class RequestResponseTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        start_time = time()
        
        response = self.get_response(request)
        
        end_time = time()
        
        time_taken = end_time - start_time
        path = request.path
        request_method = request.method
        RequestResponseLog.objects.create(
            path=path,
            request_method=request_method,
            time=time_taken,
        )
        return response
