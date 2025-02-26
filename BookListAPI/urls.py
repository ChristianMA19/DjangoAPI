from django.urls import path,include
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # path('books/', views.books)
    path('books/', views.BookList.as_view()),
    path('books/<int:pk>/', views.Book.as_view()),
    path('menu-items/', views.MenuItemsView.as_view()),
    path('menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
    path('__debug__/', include('debug_toolbar.urls')),
    path('secret/', views.secret),
    path('manager/', views.manager_view),
    path('throttle-check/', views.throttle_check),
    path('throttle-check-auth/', views.throttle_check_auth),
    path('throttle-check-auth-ten/', views.throttle_check_auth_ten),
    path('api-token-auth/', obtain_auth_token),
    path('groups/manager/users/', views.managers),
]