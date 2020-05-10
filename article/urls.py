__author__ = 'Luguaa'
__date__ = '2020/5/5 20:04'

from django.urls import path

from .views import IndexView, DetailView, DateView, CategoryView, TagView

app_name = 'article'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('posts/<int:id>/', DetailView.as_view(), name='detail'),
    path('dates/<int:year>/<int:month>/', DateView.as_view(), name='dates'),
    path('categories/<int:id>/', CategoryView.as_view(), name='categories'),
    path('tags/<int:id>/', TagView.as_view(), name='tags')
]