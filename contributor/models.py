from django.db import models
from django.conf import settings
from project.models import Projects


class Contributor(models.Model):
    choice_permission = [('CREATE', 'CREATE'), ('READ', 'READ'), ('UPDATE', 'UPDATE'), ('DELETE', 'DELETE'),
                         ('ALL', 'ALL')]

    user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                null=True, related_name='user_project')
    project = models.ForeignKey(to=Projects, on_delete=models.CASCADE, related_name='projects_contributor')
    permission = models.CharField(max_length=10, choices=choice_permission, default='READ')
    role = models.CharField(max_length=128)

    def __str__(self):
        return str(self.user_id)
