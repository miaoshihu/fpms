from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50, blank=False, default=None, unique=True)
    name.verbose_name = u'用户名'

    icon = models.CharField(max_length=50, blank=True, default=None, unique=False)
    icon.verbose_name = u'用户头像'

    phoneno = models.CharField(max_length=50, blank=True, default=None, unique=False)
    phoneno.verbose_name = u'电话号码'

    login_times = models.PositiveSmallIntegerField(null=False, blank=False)
    login_times.verbose_name = u"访问次数"

    create_time = models.DateTimeField(auto_now_add=True)
    create_time.verbose_name = u'创建时间'

    last_modify_time = models.DateTimeField(auto_now=True)
    last_modify_time.verbose_name = u'最后修改时间'

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'用户'
        verbose_name_plural = u'用户列表'


class Job(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=True, )
    user.verbose_name = u'用户'

    name = models.CharField(max_length=10, blank=False, default=None, unique=True)
    name.verbose_name = u'职位名称'

    type = models.PositiveSmallIntegerField(null=False, blank=False, default=0)
    type.verbose_name = u'类型'

    gender = models.PositiveSmallIntegerField(null=False, blank=False, default=0)
    gender.verbose_name = u'性别'

    viewtimes = models.PositiveIntegerField(null=False, blank=False, default=0)
    viewtimes.verbose_name = u'浏览次数'

    desc1 = models.CharField(max_length=10, blank=False, default=None, unique=True)
    desc1.verbose_name = u'条件'

    create_time = models.DateTimeField(auto_now_add=True)
    create_time.verbose_name = u'创建时间'

    last_modify_time = models.DateTimeField(auto_now=True)
    last_modify_time.verbose_name = u'最后修改时间'

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'招聘求职'
        verbose_name_plural = u'招聘求职列表'


class Good(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=True, )
    user.verbose_name = u'用户'

    name = models.CharField(max_length=10, blank=False, default=None, unique=False)
    name.verbose_name = u'物品名称'

    price = models.CharField(max_length=10, blank=False, default=u'面议', unique=True)
    price.verbose_name = u'价格'

    viewtimes = models.PositiveIntegerField(null=False, blank=False, default=0)
    viewtimes.verbose_name = u'浏览次数'

    create_time = models.DateTimeField(auto_now_add=True)
    create_time.verbose_name = u'创建时间'

    last_modify_time = models.DateTimeField(auto_now=True)
    last_modify_time.verbose_name = u'最后修改时间'

    def __str__(self):
        return self.name + " " + str(self.price)

    class Meta:
        verbose_name = u'二手物品'
        verbose_name_plural = u'二手物品列表'
