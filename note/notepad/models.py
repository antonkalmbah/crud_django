from django.db import models


class Notepad(models.Model):
    id = models.AutoField(primary_key=True)
    heading = models.TextField(max_length=30)
    text = models.TextField(max_length = 1000)

    #  для того, что в админ-панели Django заголовок отображался правильно, мы дополняем класс функцией ниже
    def __str__(self):
        return self.heading