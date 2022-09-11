from django.db import models

from .consts import PRI_STEP
PRI_CHOICES = [(x, str(x)) for x in range(0, PRI_STEP + 1)]

CATEGORY = (('school', '学校'), ('work', '仕事'), ('hoby', '趣味'), ('private', 'プライベート'))

class Todo(models.Model):
  title = models.CharField(max_length=100)
  body = models.TextField()
  priority = models.IntegerField(choices=PRI_CHOICES)
  category = models.CharField(
    max_length=100,
    choices = CATEGORY
  )

  def __str__(self):
    return self.title