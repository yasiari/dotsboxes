# -*- coding: utf-8 -*- 

import re

from tornado.web import UIModule
from dotsboxes.settings import TEMPLATE_PATH, CONTEXT_PROCESSORS, UI_MODULES
from tornado.template import Loader
from django.utils.importlib import import_module


def ui_modules():
    modules = {}
    for module_path in UI_MODULES:
        _ui_modules = __import__(str(module_path), globals(), ['ui_modules'], -1)

        try:
            ui_modules = _ui_modules
        except AttributeError:
            # this app simply doesn't have a ui_modules.py file
            continue

        for name in [x for x in dir(ui_modules) if re.findall('[A-Z]\w+', x)]:
            thing = getattr(ui_modules, name)
            try:
                if issubclass(thing, UIModule) and not name == "UIModule":
                    modules[name] = thing
            except TypeError:
                # most likely a builtin class or something
                pass

    return (modules)


def template_loader(template_name, ctx):
    loader = Loader(TEMPLATE_PATH)
    return loader.load(template_name).generate(**ctx)


def get_or_None(model, **kwargs):
    """
        Easy enough to wrap into a function.
    """
    try:
        return model.objects.get(**kwargs)
    except model.DoesNotExist:
        return None

def request_data_field(request, form=None):
    """
        request arguments field

        data = request_data_field(self.request, LoginForm)
        form = LoginForm(data=data)
    """
    data = {}
    if form:
        fields = form().fields
        for field in fields.keys():
            data[field] = request.arguments[field][0]
    return data


def request_context(handler_self):
    """
        CONTEXT_PROCESSORS REQUEST
    """
    context = {}
    for ctx_path in CONTEXT_PROCESSORS:
        fnc = import_by_path(ctx_path)(handler_self)
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
