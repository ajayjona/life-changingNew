from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('contributors/', views.contributors, name='contributors'),
    path('T_donor/', views.t_donor, name='t_donor'),
    path('P_donor/', views.p_donor, name='p_donor'),

    #t_receiver urls
    path('t_receiver/', views.t_receiver, name='t_receiver'),
    path('p_receiver/', views.p_receiver, name='p_receiver'),
    path('about/', views.about, name='about'),
]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

