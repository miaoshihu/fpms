# coding:utf8

"""
@ Author Jue
@ Date 2020-03-22 11:18:13

"""

from django.shortcuts import render
import redis

def clean_all(request):

    if request.method == 'GET':
        return render(request, 'msapp/test.html', {"name" : request.method})
    else:
        handlePost()
        return render(request, 'msapp/test.html', {"name" : request.method})


def handlePost():
    r = redis.Redis(host='localhost', port=6379, db=0)
    r.flushdb()
    print("clean all redis datas")
    pass
