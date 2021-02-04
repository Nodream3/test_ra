from django.db import models


class test_data1(models.Model):
    username = models.CharField(max_length=50)
    textfield1 = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'test_data1'


class APIWK(models.Model):
    user_name = models.CharField(max_length=100)
    twitter_id = models.CharField(max_length=50)


def __str__(self):
    return self.username
