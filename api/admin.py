from django.contrib import admin
from user.models import User
from issue.models import Issues
from contributor.models import Contributor
from project.models import Projects
from comment.models import Comments

# Register your models here.
admin.site.register(User)
admin.site.register(Contributor)
admin.site.register(Projects)
admin.site.register(Issues)
admin.site.register(Comments)
