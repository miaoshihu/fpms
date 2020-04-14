# -*- coding: utf-8 -*-

from django.views.generic import View
from django.http import HttpResponse
import json
import redis
from msapp.redis_api import publish_author
from msapp.redis_api import publish_city
from msapp.redis_api import publish_good
from msapp.models import Good, City, Author


class PublishHandler(View):

    def get(self, request):
        # res = self._handle_request(request)
        content = json.dumps({
            'code': 0,
            'desc': "we did it get!",
        })

        return HttpResponse(json.dumps(content))

    def post(self, request):

        type = request.POST.get('type')
        object_id = request.POST.get('object_id')
        city = request.POST.get('city')

        print("post------------------------------- type = " + str(type) + " , object_id = " + str(object_id), 'city=',
              city)

        if type == 'good':
            self.handlePublishGood(request, object_id)
        elif type == 'city':
            self.handlePublishCity(request, object_id)
            pass
        elif type == 'author':
            self.handlePublishAuthor(request, object_id)
            pass
        content = json.dumps({
            'code': 0,
            'desc': "we did it post!",
        })

        return HttpResponse(json.dumps(content))

    def handlePublishGood(self, object_id):
        print("good id = " + object_id)
        good = Good.objects.get(id=object_id)
        publish_good(good, True)
        return

    def handlePublishCity(self, object_id):
        print("city id = " + object_id)
        city = City.objects.get(id=object_id)
        publish_city(city)
        return

    def handlePublishAuthor(self, object_id):
        print("author id = " + object_id)

        author = Author.objects.get(id=object_id)

        publish_author(author)

        return
