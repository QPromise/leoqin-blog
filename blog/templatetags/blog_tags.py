from ..models import Post,Category,Tag
from django import template
from django.db.models.aggregates import Count
register = template.Library()
#最新文章标签
@register.simple_tag
def get_recent_posts(num=3):
    return Post.objects.all().order_by('-created_time')[:num]

#归类模板标签
@register.simple_tag
def archives():
    """
    dates 方法会返回一个列表，列表中的元素为每一篇文章（Post）的创建时间，
    且是 Python 的 date 对象，精确到月份，降序排列。接受的三个参数值表明了这些含义，
    一个是 created_time ，即 Post 的创建时间，month 是精度，order='DESC'
    表明降序排列（即离当前越近的时间越排在前面）。
    """
    return Post.objects.dates('created_time', 'month', order='DESC')

#分类
@register.simple_tag
def get_categories():
    return Category.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)

@register.simple_tag
#标签云
def get_tags():
    # 记得在顶部引入 Tag model
    return Tag.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)