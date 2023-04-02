from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views.NotepadViewSets)

urlpatterns = [
    path('', views.index, name='index'),
    path('form_add/', views.form_add, name='form_add'),
    path('form_add/create', views.create, name='create'),
    # для удаления именно той записи, которая нужна нам, нужно сделать относительный путь с помощью <int:id>
    path('form_add/delete/<int:id>', views.delete, name='delete'),
    path('form_add/edit/<int:id>', views.edit, name='edit'),
    path('router/', include(router.urls)),
    path('sql/', views.sql)
]
