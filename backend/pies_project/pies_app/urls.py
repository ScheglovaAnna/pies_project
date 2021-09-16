from django.urls import path, include, re_path
from . import views, admin
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('auth/', include('djoser.urls.jwt')),
#create, delete, list +
    path("orders/", views.orderListView.as_view()),#create, update, delete +
    path("pies/", views.piesListView.as_view()),# create, list, delete, update +
    path("user/", views.userListView.as_view()),#create, update, list
   # path("basket/get/<int:pk>/", views.basketListView.as_view()),
    path("addOrder/", views.addOrder.as_view()),
    path("orderUpdate/<int:pk>/", views.orderUpdateView.as_view()),
    path("orderDestroy/<int:pk>/", views.orderDestroyView.as_view()),
    path("addPies/", views.addPies.as_view()),
    path("updatePies/<int:pk>/", views.piesUpdateView.as_view()),
    path("piesDestroy/<int:pk>/", views.piesDestroyView.as_view()),
    path("onePies/<int:pk>/", views.piesRetrieveView.as_view()),
    path("oneOrder/<int:pk>/", views.orderRetrieveView.as_view()),
    path("oneUser/<int:pk>/", views.userRetrieveView.as_view()),
    path("addUser/", views.addUser.as_view()),
    path("updateUser/<int:pk>/", views.userUpdateView.as_view()),
    path("auth/", include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]

urlpatterns += staticfiles_urlpatterns()