from django.db import models

class Category(models.Model):
    name =models.CharField(max_length=100,unique=True)


    def __str__(self):
        return self.name
    
    class Meta():
        verbose_name= 'catagory'
        verbose_name_plural= 'catagories'


class Blog(models.Model):
    title = models.CharField(max_length=200,null=True,blank=True)
    content = models.TextField()
    category =models.ForeignKey(Category,models.PROTECT)
    status = models.BooleanField(default=False)
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self) :
        return self.title
    
    class Meta():
        verbose_name= 'blog'
        verbose_name_plural= 'blogs'
