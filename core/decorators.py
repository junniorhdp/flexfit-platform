from django.shortcuts import redirect
from functools import wraps

def rol_required(*roles_permitidos):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            rol = request.session.get('rol')

            if rol not in roles_permitidos:
                return redirect('login')  # o la vista que uses

            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator