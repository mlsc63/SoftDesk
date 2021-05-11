from django.db import models
from django.conf import settings


class Projects(models.Model):
    choice = [('BACK_END', 'BACK_END'), ('FRONT_END', 'FRONT_END'), ('IOS', 'IOS'), ('ANDROID', 'ANDROID')]

    project_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500, blank=True)
    type = models.CharField(max_length=10, choices=choice)
    author_project = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True,
                                       related_name="project")

    def __str__(self):
        return 'Class Projects: ' + self.title + self.description + self.type + str(self.author_project)
