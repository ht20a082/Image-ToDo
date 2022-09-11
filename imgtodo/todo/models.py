from django.db import models

CATEGORY = (('school', '学校'), ('work', '仕事'), ('hoby', '趣味'), ('private', 'プライベート'))

class Todo(models.Model):
  title = models.CharField(max_length=100)
  body = models.TextField()
  category = models.CharField(
    max_length=100,
    choices = CATEGORY
  )

  def __str__(self):
    return self.title