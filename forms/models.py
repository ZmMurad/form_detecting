from djongo import models

class FormTemplate(models.Model):
    name = models.CharField(max_length=255)
    field_name_1 = models.CharField(max_length=255)
    field_name_2 = models.CharField(max_length=255)

    def __str__(self):
        return self.name