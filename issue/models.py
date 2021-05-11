from django.db import models
from django.conf import settings
from project.models import Projects

class Issues(models.Model):
    tag_choice = [('BUG', 'BUG'), ('IMPROVEMENT', 'IMPROVEMENT'), ('TASK', 'TASK')]
    tag_priority = [('LOW', 'LOW'), ('MEDIUM', 'MEDIUM'), ('HIGH', 'HIGH')]
    tag_status = [('TODO', 'TODO'), ('IN_PROGRESS', 'IN_PROGRESS'), ('FINISHED', 'FINISHED')]

    title = models.CharField(max_length=200)
    desc = models.TextField(max_length=500, blank=True)
    project_id = models.ForeignKey(to=Projects, on_delete=models.CASCADE, related_name='issue')

    tag = models.CharField(max_length=12, choices=tag_choice)
    priority = models.CharField(max_length=12, choices=tag_priority)
    status = models.CharField(max_length=21, choices=tag_status)

    author_issue = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name="author_issue")
    assignee_user_id = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                         related_name="user")
    create_time = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return 'Class Issues: ' + self.title + self.desc + str(self.project_id) + self.tag + self.priority + \
               self.status + str(self.author_issue) + str(self.assignee_user_id) + str(self.assignee_user_id) + str(self.create_time)
