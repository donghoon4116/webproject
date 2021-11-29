from django.db import models

# Create your models here.
class Html_content(models.Model):
    html_content = models.TextField()
    def __str__(self):
        return self.html_content

class Css_content(models.Model):
    html_content = models.ForeignKey(Html_content, on_delete=models.CASCADE)
    css_content=models.TextField()