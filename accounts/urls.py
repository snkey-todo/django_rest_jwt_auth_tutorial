from django.conf.urls import url, include
from django.urls import path
# rest router
from rest_framework.routers import DefaultRouter
#from musics.views import MusicViewSet
from accounts.views import MyProfileViewSet, FacebookLogin, TwitterLogin

router = DefaultRouter()
#router.register('', MusicViewSet, base_name='music')

urlpatterns = [
    path('', include(router.urls)), 
    #path('rest-auth/facebook/', FacebookLogin.as_view(), name='fb_login'),
    #path('rest-auth/twitter/', TwitterLogin.as_view(), name='twitter_login'),
    #path('rest-auth/github/', GitHubLogin.as_view(), name='github_login'),
]