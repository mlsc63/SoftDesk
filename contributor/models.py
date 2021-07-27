from django.db import models
from django.conf import settings
from project.models import Projects
from user.models import User


class Contributor(models.Model):

    contributor_id = models.AutoField(primary_key=True)
    choice_permission = [('CREATE', 'CREATE'), ('READ', 'READ'), ('UPDATE', 'UPDATE'), ('DELETE', 'DELETE')]
    user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True, related_name='user_project')
    project_id = models.ForeignKey(to=Projects, on_delete=models.CASCADE, related_name='project')
    permission = models.CharField(max_length=10, choices=choice_permission, default='READ')
    role = models.CharField(max_length=128)

    def __str__(self):
        return self.user_id