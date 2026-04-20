from functools import wraps
from django.http import HttpResponse
from django.shortcuts import redirect


def admin_session_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.session.get('admin_id'):
            return redirect('/admins/login/')
        return view_func(request, *args, **kwargs)
    return wrapper


def super_admin_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.session.get('admin_id'):
            return redirect('/admins/login/')
        if request.session.get('admin_role') != 'super_admin':
            return HttpResponse("Accès refusé ❌")
        return view_func(request, *args, **kwargs)
    return wrapper


def member_session_required(view_func):
    @wraps(view_func)
    def wrapper(request, *args, **kwargs):
        if not request.session.get('member_id'):
            return redirect('/admins/member-login/')
        return view_func(request, *args, **kwargs)
    return wrapper