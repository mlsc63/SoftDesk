from django.contrib import admin
from django.urls import path, include
from project.views import ProjectViewSet
from contributor.views import ContributorViewSet
from user.views import UserViewSet
from issue.views import IssueViewSet
from comment.views import CommentViewSet
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers


router = DefaultRouter()

router.register(r'project', ProjectViewSet)
router.register(r'contributor', ContributorViewSet)
router.register(r'user', UserViewSet)
router.register(r'issue', IssueViewSet)
router.register(r'comment', CommentViewSet)



project_router = routers.NestedSimpleRouter(router, r'project', lookup='project')
project_router.register(r'user', ContributorViewSet, basename='users')
project_router.register(r'issue', IssueViewSet, basename='issue')
issue_router = routers.NestedSimpleRouter(project_router, r'issue', lookup='issue')
issue_router.register(r'comment', CommentViewSet, basename='comment')



urlpatterns = [
    path('', include(router.urls)),
    path('', include(project_router.urls)),
    path('', include(issue_router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),

]
