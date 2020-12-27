from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('download/', views.download, name = 'download'),
    path('split/', views.split, name = 'split'),
    path('keyv/', views.keyv, name = 'keyv'),
    path('keyv_process/<int:f_key_column>/<int:l_value_column>/<int:f_empty_column>/<xl_file_name>/',
         views.keyv_process, name = 'keyv_process'),
    path('split_process/<int:split_value>/<xl_file_name>/', views.split_process, name = 'split_process'),
    path('process/<int:url_cell_start>/<int:url_cell_end>/<int:write_cell_start>/<int:write_cell_end>/<xl_file_name>/',
         views.process, name = 'process')
]
