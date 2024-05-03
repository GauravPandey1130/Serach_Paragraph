from django.db import models

# Create your models here.

class CustomUser(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    dob = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)


class Paragraph(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.JSONField(default=dict)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    token_data = models.JSONField(default=dict)  # JSON field for tokenized words
    word_index = models.JSONField(default=dict) 

