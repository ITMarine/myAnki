from django.urls import path
from . import views


app_name = 'anki'
urlpatterns = [
    path('', views.topic_list, name='topic_list'),
    path('<int:pk>/', views.topic_detail, name='topic'),
    path('new-topic/', views.topic_create, name='topic_create'),
    path('topic-delete/<int:pk>/', views.topic_delete, name='topic_delete'),
    path('card/<int:pk>/', views.card_detail, name='card_detail'),
    path('card/create', views.card_create, name='card_create'),
    path('card/update/<int:pk>', views.card_update, name='card_update'),
    path('card/remove/<int:pk>', views.card_to_archive, name='card_remove')
]
