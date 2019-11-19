from django.db import models


class City(models.Model):

    id = models.CharField(max_length=20, default=None, unique=True, primary_key=True)
    id.verbose_name = u'城市id'

    name = models.CharField(max_length=10, default=None, unique=True)
    name.verbose_name = u'城市名'

    enabled = models.BooleanField(default=False)
    enabled.verbose_name = u'启用'

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u'城市'
        verbose_name_plural = u'城市'


class Good(models.Model):
    user_id = models.CharField(max_length=50, default=None)
    user_id.verbose_name = u'微信id'

    user_nickname = models.CharField(max_length=20, default=None)
    user_nickname.verbose_name = u'微信名'

    city = models.ForeignKey(City, on_delete=models.CASCADE, null=False)
    city.verbose_name = u'城市'

    name = models.CharField(max_length=10, default=None, null=False)
    name.verbose_name = u'物品名称'

    image1 = models.CharField(max_length=200, null=True, default=None)
    image1.verbose_name = u'图片1'

    image2 = models.CharField(max_length=200, null=True, default=None)
    image2.verbose_name = u'图片2'

    image3 = models.CharField(max_length=200, null=True, default=None)
    image3.verbose_name = u'图片3'

    status = models.IntegerField(null=False, default=0)
    status.verbose_name = u"状态"

    price = models.PositiveIntegerField(null=False, default=10)
    price.verbose_name = u"价格"

    short_desc = models.CharField(max_length=20, default=None)
    short_desc.verbose_name = u'一句话描述'

    descs = models.TextField(max_length=60, null=True, default=None)
    descs.verbose_name = u'详细描述'

    address = models.CharField(max_length=20, null=True, default=None)
    address.verbose_name = u'地址'

    phone = models.PositiveIntegerField(null=False, default=0)
    phone.verbose_name = u'联系电话'

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
    user_id = models.CharField(max_length=50, default=None)
    user_id.verbose_name = u'微信id'

    user_nickname = models.CharField(max_length=20, default=None)
    user_nickname.verbose_name = u'微信名'

    city = models.ForeignKey(City, on_delete=models.CASCADE, null=False, blank=False)
    city.verbose_name = u'城市'

    name = models.CharField(max_length=10, default=None)
    name.verbose_name = u'物品名称'

    status = models.IntegerField(null=False, default=0)
    status.verbose_name = u"状态"

    price_max = models.PositiveIntegerField(default=0)
    price_max.verbose_name = u"价格上限"

    short_desc = models.CharField(max_length=20, default=None)
    short_desc.verbose_name = u'一句话描述'

    descs = models.TextField(max_length=60, null=True, default=None)
    descs.verbose_name = u'详细描述'

    address = models.CharField(max_length=20, null=True, default=None)
    address.verbose_name = u'地址'

    phone = models.IntegerField(null=False, default=0)
    phone.verbose_name = u'联系电话'

    create_time = models.DateTimeField(null=True, auto_now_add=True)
    create_time.verbose_name = u'创建时间'

    last_modify_time = models.DateTimeField(null=True, auto_now=True)
    last_modify_time.verbose_name = u'最后修改时间'

    def __str__(self):
        return self.name + " " + str(self.price_min + "-" + self.price_max)

    class Meta:
        verbose_name = u'求购'
        verbose_name_plural = u'求购'
