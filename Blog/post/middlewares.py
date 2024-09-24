# middlewares.py


import logging


class RequestLogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.logger = logging.getLogger(__name__)  # Crea un logger


    def __call__(self, request):
        self.logger.info(f"Solicitud: {request.method} {request.get_full_path()}")
        response = self.get_response(request)
        return response