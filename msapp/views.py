# -*- coding: utf-8 -*-

from django.views.generic import View
from django.http import HttpResponse
import json
import redis
from msapp.models import Good


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
        print("post 24^^^^^^^^^^^^^^^^")

        object_id = request.POST.get('object_id')
        print("good id = " + object_id)

        good = Good.objects.get(id=object_id)
        print(good)
        print(good.id)

        content = json.dumps({
            'code': 0,
            'desc': "we did it post!",
        })

        r = redis.Redis(host='localhost', port=6379, db=0)
        r.flushdb()

        cityGoodKey = self.publishCityGood(r, good)
        self.publishCityGoodList(r, cityGoodKey)

        # r.set("name", "zhangsan")
        # r.lpush("cgl_hb-xianghe", "cg_hb-xianghe_1")
        # r.lpush("cgl_hb-xianghe", "cg_hb-xianghe_2")
        # r.lpush("cgl_hb-xianghe", "cg_hb-xianghe_3")
        # r.lpush("cgl_hb-xianghe", "cg_hb-xianghe_4")
        # r.lpush("cgl_hb-xianghe", "cg_hb-xianghe_5")

        #print(r.lrange("cgl_hb-xianghe", 0, r.llen("cgl_hb-xianghe")))

        return HttpResponse(json.dumps(content))

    def publishCityGood(self, r, good):
        mykey = "cg_hb-xianghe_" + str(good.id)

        # 商品信息
        r.hset(mykey, "id", str(good.id))
        r.hset(mykey, "user_id", str(good.user_id))
        r.hset(mykey, "desc", good.user_nickname)
        r.hset(mykey, "city", str(good.city))
        r.hset(mykey, "name", good.name)
        r.hset(mykey, "image1", str(good.image1))
        r.hset(mykey, "image2", str(good.image2))
        r.hset(mykey, "status", str(good.status))
        r.hset(mykey, "price", str(good.price))
        r.hset(mykey, "short_desc", good.short_desc)
        r.hset(mykey, "descs", str(good.descs))
        r.hset(mykey, "address", str(good.address))
        r.hset(mykey, "phone", str(good.phone))
        r.hset(mykey, "create_time", str(good.create_time))

        print("-----------1----")
        print(r.hgetall(mykey))
        print("-----------2----")
        return mykey

    def publishCityGoodList(self, r, key):
        listkey = "cgl_hb-xianghe"

        r.lpush(listkey, key)
        print("-----------2----")
        print(r.lrange(listkey, 0, r.llen(listkey)))
        print("-----------3----")
        return
