from django.db import models

class TodoItem(models.Model):
    #user_email = 
    title = models.CharField(max_length=200)
    desc = models.TextField(blank=True,null=True)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now = True)
    updated = models.DateTimeField(auto_now_add=True)
    # id = models.UUIDField(primary_key=True)

    class Meta:
        ordering = ["-updated","-created"]

    def __str__(self) -> str:
        return self.title
    

