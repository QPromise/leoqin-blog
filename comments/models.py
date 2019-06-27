from django.db import models

# Create your models here.
class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)#自动保存当前时间
    post = models.ForeignKey('blog.Post',on_delete=models.CASCADE)

    def __str__(self):
        return self.text[:20]
    #返回的评论都会自动按照 Meta 中指定的顺序排序
    class Meta():
        ordering=['-created_time']