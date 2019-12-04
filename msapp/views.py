# -*- coding: utf-8 -*-

from django.views.generic import View
from django.http import HttpResponse
import json
import redis
from msapp.models import Good, Need, City


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

        type = request.POST.get('type')
        object_id = request.POST.get('object_id')

        print("post------------------------------- type = " + str(type) + " , object_id = " + str(object_id))

        if type == 'good':
            self.handlePublishGood(request, object_id)
        elif type == 'need':
            self.handlePublishNeed(request, object_id)
        elif type == 'city':
            self.handlePublishCity(request, object_id)
            pass

        content = json.dumps({
            'code': 0,
            'desc': "we did it post!",
        })

        return HttpResponse(json.dumps(content))

    def handlePublishGood(self, request, object_id):
        print("good id = " + object_id)

        good = Good.objects.get(id=object_id)
        print(good)
        print(good.id)

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
        return

    def handlePublishNeed(self, request, object_id):
        print("need id = " + object_id)

        need = Need.objects.get(id=object_id)
        print(need)
        print(need.id)

        r = redis.Redis(host='localhost', port=6379, db=0)
        r.flushdb()

        cityNeedKey = self.publishCityNeed(r, need)
        self.publishCityNeedList(r, cityNeedKey)

        return

    def handlePublishCity(self, request, object_id):
        print("city id = " + object_id)

        city = City.objects.get(id=object_id)
        print(city)
        print(city.id)

        r = redis.Redis(host='localhost', port=6379, db=0)
        r.flushdb()

        cityKey = self.publishCity(r, city)

        return

    def publishCity(self, r, city):
        mykey = "c_" + str(city.id)

        # 商品信息
        r.hset(mykey, "id", str(city.id))
        r.hset(mykey, "name", str(city.name))
        r.hset(mykey, "enabled", str(city.enabled))

        print("-----------1----")
        print(r.hgetall(mykey))
        print("-----------2----")
        return mykey

    def publishCityGood(self, r, good):
        mykey = "cg_hb.xianghe_" + str(good.id)

        # 商品信息
        r.hset(mykey, "id", str(good.id))
        r.hset(mykey, "user_id", str(good.user_id))
        r.hset(mykey, "user_nickname", good.user_nickname)
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

    def publishCityNeed(self, r, need):
        mykey = "cn_hb.xianghe_" + str(need.id)

        # 商品信息
        r.hset(mykey, "id", str(need.id))
        r.hset(mykey, "user_id", str(need.user_id))
        r.hset(mykey, "user_nickname", need.user_nickname)
        r.hset(mykey, "city", str(need.city))
        r.hset(mykey, "name", need.name)
        r.hset(mykey, "status", str(need.status))
        r.hset(mykey, "price", str(need.price))
        r.hset(mykey, "descs", str(need.descs))
        r.hset(mykey, "address", str(need.address))
        r.hset(mykey, "phone", str(need.phone))
        r.hset(mykey, "create_time", str(need.create_time))

        print("-----------1----")
        print(r.hgetall(mykey))
        print("-----------2----")
        return mykey

    def publishCityGoodList(self, r, key):
        listkey = "cgl_hb.xianghe"

        r.lpush(listkey, key)
        print("-----------2----")
        print(r.lrange(listkey, 0, r.llen(listkey)))
        print("-----------3----")
        return

    def publishCityNeedList(self, r, key):
        listkey = "cnl_hb.xianghe"

        r.lpush(listkey, key)
        print("-----------2----")
        print(r.lrange(listkey, 0, r.llen(listkey)))
        print("-----------3----")
        return