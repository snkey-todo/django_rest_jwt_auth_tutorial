from django.conf.urls import url, include
from django.urls import path
from accounts.views import MyProfileViewSet, FacebookLogin, TwitterLogin
# rest router
from rest_framework.routers import DefaultRouter
from accounts.views import MyProfileViewSet,FacebookLogin,TwitterLogin,GithubLogin,FacebookConnect,TwitterConnect,GithubConnect

router = DefaultRouter()
router.register('', MyProfileViewSet, base_name='accounts')

urlpatterns = [
    path('', include(router.urls)), 
    path('rest-auth/facebook/', FacebookLogin.as_view(), name='fb_login'),
    path('rest-auth/twitter/', TwitterLogin.as_view(), name='twitter_login'),
    path('rest-auth/github/', GithubLogin.as_view(), name='github_login'),
    path('rest-auth/facebook/connect/', FacebookConnect.as_view(), name='fb_connect'),
    path('rest-auth/twitter/connect/', TwitterConnect.as_view(), name='twitter_connect'),
    path('rest-auth/github/connect/', GithubConnect.as_view(), name='github_connect'),
]

# 参考设置扩展官方的User Model
# https://www.jianshu.com/p/d45a687c3f41