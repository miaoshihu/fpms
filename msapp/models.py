from django.db import models
from django.utils.html import format_html


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


class Author(models.Model):
    openid = models.CharField(max_length=50, default=None, unique=True)
    openid.verbose_name = u'微信id'

    nickname = models.CharField(max_length=20, default=None)
    nickname.verbose_name = u'昵称'

    point = models.IntegerField(null=False, default=0)
    point.verbose_name = u"积分"

    status_type = ((0, u'未审核'), (1, u'已上线'), (-1, u'审核失败'), (-2, u'已下线'))
    status = models.IntegerField(null=False, choices=status_type, default=0)
    status.verbose_name = u"状态"

    descs = models.TextField(max_length=60, null=True, default=None, blank=True)
    descs.verbose_name = u'备注'

    town = models.CharField(max_length=20, null=True, default=None)
    town.verbose_name = u'镇/乡'

    address = models.CharField(max_length=20, null=True, default=None)
    address.verbose_name = u'小区/村'

    phone = models.CharField(max_length=20, null=False, default=0)
    phone.verbose_name = u'联系电话'

    create_time = models.DateTimeField(null=True, auto_now=True)
    create_time.verbose_name = u'创建时间'

    time_stamp = models.BigIntegerField(null=True, default=0)
    time_stamp.verbose_name = u"时间戳"

    def __str__(self):
        return self.nickname + " " + str(self.id) + " " + self.openid

    def is_verify(self):
        return self.status != 0

    def get_status(self):

        if self.status == 0:
            return "未审核"

        if self.status == 1:
            return "已上线"

        if self.status == -1:
            return "审核失败"
        if self.status == -2:
            return "已下线"

    is_verify.boolean = True
    is_verify.short_description = u'已审核'

    get_status.short_description = u'状态'

    class Meta:
        verbose_name = u'作者'
        verbose_name_plural = u'作者'


class Good(models.Model):

    user_nickname = models.CharField(max_length=20, default=None)
    user_nickname.verbose_name = u'用户'

    city = models.ForeignKey(City, on_delete=models.CASCADE, null=False)
    city.verbose_name = u'城市'

    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, default=None)
    author.verbose_name = u'作者'

    name = models.CharField(max_length=10, default=None, null=False)
    name.verbose_name = u'物品名称'

    image1 = models.CharField(max_length=200, blank=True, null=True, default=None)
    image1.verbose_name = u'图片1'

    image2 = models.CharField(max_length=200, blank=True, null=True, default=None)
    image2.verbose_name = u'图片2'

    # status = models.IntegerField(null=False, default=0)
    # status.verbose_name = u"状态"

    status_type = ((0, '未审核'), (1, u'已上线'), (-1, u'审核失败'), (-2, u'已下线'))
    status = models.IntegerField(u"状态", choices=status_type, null=True, default=0)

    error = models.TextField(max_length=60, null=True, default=None, blank=True)
    error.verbose_name = u'审核失败原因'

    price = models.PositiveIntegerField(null=False, default=10)
    price.verbose_name = u"价格"

    short_desc = models.CharField(max_length=20, default=None)
    short_desc.verbose_name = u'一句话描述'

    descs = models.TextField(max_length=60, null=True, default=None)
    descs.verbose_name = u'详细描述'

    address = models.CharField(max_length=20, null=True, default=None)
    address.verbose_name = u'地址'

    phone = models.CharField(max_length=20, null=False, default=0)
    phone.verbose_name = u'联系电话'

    create_time = models.DateTimeField(null=True, auto_now=True)
    create_time.verbose_name = u'创建时间'

    time_stamp = models.BigIntegerField(null=True, default=0)
    time_stamp.verbose_name = u"时间戳"

    def __str__(self):
        return self.name + " " + str(self.price)

    def is_verify(self):
        return self.status != 0

    def get_status(self):

        if self.status == 0:
            return "未审核"

        if self.status == 1:
            return "已上线"

        if self.status == -1:
            return format_html('<span style="color: #FF0000;">{}</span>', "审核失败")

        if self.status == -2:
            return "已下线"

    is_verify.boolean = True
    is_verify.short_description = u'已审核'

    get_status.short_description = u'状态'

    class Meta:
        verbose_name = u'出售'
        verbose_name_plural = u'出售'


class Need(models.Model):
    user_id = models.CharField(max_length=50, default=None)
    user_id.verbose_name = u'微信id'

    user_nickname = models.CharField(max_length=20, default=None)
    user_nickname.verbose_name = u'用户'

    city = models.ForeignKey(City, on_delete=models.CASCADE, null=False, blank=False)
    city.verbose_name = u'城市'

    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, default=None)
    author.verbose_name = u'作者'

    name = models.CharField(max_length=10, default=None)
    name.verbose_name = u'物品名称'

    status = models.IntegerField(null=False, default=0)
    status.verbose_name = u"状态"

    price = models.PositiveIntegerField(default=0)
    price.verbose_name = u"价格上限"

    descs = models.TextField(max_length=60, null=True, default=None)
    descs.verbose_name = u'详细描述'

    address = models.CharField(max_length=20, null=True, default=None)
    address.verbose_name = u'地址'

    phone = models.CharField(max_length=20, null=False, default=0)
    phone.verbose_name = u'联系电话'

    create_time = models.DateTimeField(null=True, auto_now=True)
    create_time.verbose_name = u'创建时间'

    time_stamp = models.BigIntegerField(null=True, default=0)
    time_stamp.verbose_name = u"时间戳"

    def __str__(self):
        return self.name + " " + str(self.price)

    def is_verify(self):
        return self.status != 0

    def get_status(self):

        if self.status == 0:
            return "未审核"

        if self.status == 1:
            return "已上线"

        if self.status == -10:
            return "审核失败"

    is_verify.boolean = True
    is_verify.short_description = u'已审核'

    get_status.short_description = u'状态'

    class Meta:
        verbose_name = u'求购'
        verbose_name_plural = u'求购'
