import datetime
from functools import wraps
from django.http import JsonResponse, HttpRequest


class Decorators:
    @staticmethod
    def dec_error_handle(_func: callable):
        @wraps(_func)
        def wrapper(*args, **kwargs):
            try:
                _response = _func(*args, **kwargs)
                return _response
            except Exception as error:
                return JsonResponse(data={"message": str(error)}, status=500)

        return wrapper

    @staticmethod
    def constr_dec_logger(is_class: bool = False):  # параметризируемый
        def dec_logger(_func: callable):
            @wraps(_func)
            def wrapper(*args, **kwargs):
                if is_class:
                    _request: HttpRequest = args[1]
                else:
                    _request: HttpRequest = args[0]
                datatime_srt = datetime.datetime.now().strftime("%Y_%m_%d_%H")
                with open(f"static/media/log_{datatime_srt}.txt", mode="a") as f:
                    f.write(f"""{str(datetime.datetime.now())} _ {_request.path}\n""")
                _response = _func(*args, **kwargs)
                return _response

            return wrapper

        return dec_logger


class Datetime:
    @staticmethod
    def get_current_datetime_str():
        return datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
