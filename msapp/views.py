# -*- coding: utf-8 -*-

from django.views.generic import View
from django.http import HttpResponse
import json


class PublishHandler(View):

    def get(self, request):
        # res = self._handle_request(request)
        print("get 12^^^^^^^^^^^^^^^^")
        content = json.dumps({
            'code': 0,
            'desc': "we did it get!",
        })

        return HttpResponse(json.dumps(content))

    def post(self, request):
        # res = self._handle_request(request)
        print("post 16^^^^^^^^^^^^^^^^")
        content = json.dumps({
            'code': 0,
            'desc': "we did it post!",
        })

        return HttpResponse(json.dumps(content))
