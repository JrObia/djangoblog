from django.db import models

# Create your models here.

class Author(models.Model):
    '''
    Define Author model
    '''
    name = models.CharField(max_length=50)
    # one email and no repetition
    email = models.EmailField(unique=True)
    bio = models.TextField()
    def __str__(self):
        return self.name

class Category(models.Model):
    '''
    Define Category model fiels in the database
    '''
    cat_name = models.CharField('category name', max_length=50)
    cat_description = models.CharField('category description', max_length=255)
    class Meta:
        verbose_name_plural='categories' 
    def __str__(self):
        return self.cat_name

class Tag(models.Model):
    ''' 
    Define Tag model for  db field 
    '''
    tag_name = models.CharField(max_length=50)
    tag_description = models.CharField(max_length=255)
    # magic method such that the tag_name appears in the  admin dashboard
    # so that we know the objects by it's name
    def __str__(self):
        return self.tag_name


class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    created_date = models.DateField(auto_now_add=True, auto_now=False)
    update_date = models.DateField(auto_now_add=False, auto_now=True)
    author  = models.ForeignKey(Author)
    categories = models.ManyToManyField(Category)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title
