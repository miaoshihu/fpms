from django.db import models


class City(models.Model):

    id = models.CharField(max_length=20, blank=False, default=None, unique=False, primary_key=True)
    id.verbose_name = u'城市id'

    name = models.CharField(max_length=10, blank=False, default=None, unique=False)
    name.verbose_name = u'城市名'

    enabled = models.BooleanField(default=False)
    enabled.verbose_name = u'启用'

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'城市'
        verbose_name_plural = u'城市'


# Create your models here.
class User(models.Model):
    id = models.CharField(max_length=50, blank=False, default=None, unique=True, primary_key=True)
    id.verbose_name = u'用户标识'

    city = models.ForeignKey(City, on_delete=models.CASCADE, null=False, blank=False)
    city.verbose_name = u'城市'

    nickname = models.CharField(max_length=50, blank=False, default=None, unique=False)
    nickname.verbose_name = u'昵称'

    icon = models.CharField(max_length=50, blank=True, default=None, unique=False)
    icon.verbose_name = u'用户头像'

    login_times = models.PositiveSmallIntegerField(null=False, blank=False)
    login_times.verbose_name = u"访问次数"

    create_time = models.DateTimeField(auto_now_add=True)
    create_time.verbose_name = u'创建时间'

    last_login_time = models.DateTimeField(auto_now=True)
    last_login_time.verbose_name = u'最后登录时间'

    enabled = models.BooleanField(default=False)
    enabled.verbose_name = u'启用'

    white = models.BooleanField(default=True)
    white.verbose_name = u'非黑名单'

    desc = models.CharField(max_length=100, blank=True, default=None, unique=False)
    desc = u'备注'

    def __str__(self):
        return "" + self.nickname + " : " + self.id

    class Meta:
        verbose_name = u'微信用户'
        verbose_name_plural = u'微信用户'


class Good(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, )
    user.verbose_name = u'用户'

    city = models.ForeignKey(City, on_delete=models.CASCADE, null=False, blank=False, )
    city.verbose_name = u'城市'

    name = models.CharField(max_length=10, blank=False, default=None, unique=False)
    name.verbose_name = u'物品名称'

    image1 = models.CharField(max_length=200, null=True, blank=True, default=None, unique=False)
    image1.verbose_name = u'图片1'

    image2 = models.CharField(max_length=200, null=True, blank=True, default=None, unique=False)
    image2.verbose_name = u'图片2'

    image3 = models.CharField(max_length=200, null=True, blank=True, default=None, unique=False)
    image3.verbose_name = u'图片3'

    status = models.IntegerField(null=False, blank=False, default=0)
    status.verbose_name = u"状态"

    price = models.PositiveIntegerField(null=False, blank=False, default=10)
    price.verbose_name = u"价格"

    short_desc = models.CharField(max_length=20, null=True, blank=True, default=None, unique=False)
    short_desc.verbose_name = u'一句话描述'

    desc = models.TextField(max_length=60, null=True, blank=True, default=None, unique=False)
    desc.verbose_name = u'详细描述'

    address = models.CharField(max_length=20, null=True, blank=True, default=None, unique=False)
    address.verbose_name = u'地址'

    phone = models.PositiveIntegerField(null=False, blank=False, default=0)
    phone.verbose_name = u'联系电话'

    view_times = models.PositiveIntegerField(null=False, blank=False, default=0)
    view_times.verbose_name = u'浏览次数'

    create_time = models.DateTimeField(null=True, auto_now_add=True)
    create_time.verbose_name = u'创建时间'

    last_modify_time = models.DateTimeField(null=True, auto_now=True)
    last_modify_time.verbose_name = u'最后修改时间'

    def __str__(self):
        return self.name + " " + str(self.price)

    class Meta:
        verbose_name = u'出售'
        verbose_name_plural = u'出售'


class Need(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, )
    user.verbose_name = u'用户'

    city = models.ForeignKey(City, on_delete=models.CASCADE, null=False, blank=False, )
    city.verbose_name = u'城市'

    name = models.CharField(max_length=10, blank=False, default=None, unique=False)
    name.verbose_name = u'物品名称'

    image1 = models.CharField(max_length=200, null=True, blank=True, default=None, unique=False)
    image1.verbose_name = u'图片1'

    status = models.IntegerField(null=False, blank=False, default=0)
    status.verbose_name = u"状态"

    price_min = models.PositiveIntegerField(null=False, blank=False, default=10)
    price_min.verbose_name = u"价格上限"

    price_max = models.PositiveIntegerField(null=False, blank=False, default=10)
    price_max.verbose_name = u"价格上限"

    short_desc = models.CharField(max_length=20, null=True, blank=True, default=None, unique=False)
    short_desc.verbose_name = u'一句话描述'

    desc = models.TextField(max_length=60, null=True, blank=True, default=None, unique=False)
    desc.verbose_name = u'详细描述'

    address = models.CharField(max_length=20, null=True, blank=True, default=None, unique=False)
    address.verbose_name = u'地址'

    phone = models.IntegerField(null=False, blank=False, default=0)
    phone.verbose_name = u'联系电话'

    view_times = models.PositiveIntegerField(null=False, blank=False, default=0)
    view_times.verbose_name = u'浏览次数'

    create_time = models.DateTimeField(null=True, auto_now_add=True)
    create_time.verbose_name = u'创建时间'

    last_modify_time = models.DateTimeField(null=True, auto_now=True)
    last_modify_time.verbose_name = u'最后修改时间'

    def __str__(self):
        return self.name + " " + str(self.price_min + "-" + self.price_max)

    class Meta:
        verbose_name = u'求购'
        verbose_name_plural = u'求购'
