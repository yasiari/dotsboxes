# -*- coding: utf-8 -*- 

from django.utils.importlib import import_module

def request_context():
    """
        CONTEXT_PROCESSORS REQUEST
    """
    from settings import CONTEXT_PROCESSORS
    context = {}
    for ctx_path in CONTEXT_PROCESSORS:
        fnc = import_by_path(ctx_path)()
        context.update(fnc)
    return context


def import_by_path(dotted_path):
    """
        module path function import 
    """
    module_path, class_name = dotted_path.rsplit('.', 1)
    module = import_module(module_path)
    attr = getattr(module, class_name)
    return attr