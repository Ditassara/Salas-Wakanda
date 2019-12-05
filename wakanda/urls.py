from django.urls import path
from . import views

urlpatterns=[
	path('',views.index,name='index'),
	path('salas/',views.salas,name='salas'),
	# path('arriendo/<int:pk>', views.ArriendoDetailView.as_view(), name='arriendo-detail'),
]

# urlpatterns += [
# 	path('arriendo/create/', views.ArriendoCreate.as_view(), name='arriendo_create'),
# 	path('arriendo/<int:pk>/update/', views.ArriendoUpdate.as_view(), name='arriendo_update'),
# 	path('arriendo/<int:pk>/delete/', views.ArriendoDelete.as_view(), name='arriendo_delete'),
# ]
