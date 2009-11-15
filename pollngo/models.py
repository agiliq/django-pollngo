from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    """This class represents a question. It can have 2 or more options."""
    created_on = models.DateTimeField(auto_now_add = 1)
    title = models.SlugField(max_length = 200)
    slug = models.SlugField(unique = True, max_length = 200)
    text = models.TextField()
    allow_multiple = models.BooleanField(default = False)
    
    def save(self):
        title = self.title.replace('?', '')
        title = title.replace('.', '')
        slug = '-'.join(title.split())
        count = Question.objects.filter(slug__icontains = slug).count()
        print count
        if count:
            slug = slug + str(count+1)
        self.slug = slug
        super(Question, self).save()
    
    def __str__(self):
        return self.title
    
    @models.permalink
    def get_absolute_url(self):
        return ('pollngo.views.question', [self.slug])
    
    @models.permalink
    def get_results_url(self):
        return ('pollngo.views.results', [self.slug])
    
    class Admin:
        pass
    
    class Meta:
        ordering = ('-created_on', )
        
    
class Choice(models.Model):
    """This represents an answer to the Question, and has a foreignkey to it"""
    question = models.ForeignKey(Question)
    text = models.TextField()
    total_votes = models.IntegerField(default = 0)

    def __str__(self):
        return '%s - %s' % (self.question.title, self.text)
    
    class Admin:
        pass
        