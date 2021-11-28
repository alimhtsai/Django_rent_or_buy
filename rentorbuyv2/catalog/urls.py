from django.urls import path
from . import views


urlpatterns = [
    #views.index：使用vews.py裡面定義的function:index()
    #name='index' 代表 .html的樣本template檔裡面，要寫href超連結語法的話，就會用到
    path('', views.index, name='index'),

    #加入Buydb資料表的list清單網頁的url mapping
    path('buydb/', views.BuydbListView.as_view(), name='buydb'),
    #加入Buydb資料表的詳細資料網頁的url mapping
    path('buydb/<int:pk>', views.BuydbDetailView.as_view(), name='buydb-detail'),
    
    #加入Rentdb資料表的list清單網頁的url mapping
    path('rentdb/', views.RentdbListView.as_view(), name='rentdb'),
    #加入Rentdb資料表的詳細資料網頁的url mapping
    path('rentdb/<int:pk>', views.RentdbDetailView.as_view(), name='rentdb-detail'),

    #path('^post/(?P<pk>\d+)/$', views.RentdbDatailRequest, name = 'rentdb-request'),
    #url(r'^post/(?P<pk>\d+)/$', post_detail, name='post_detail'),

    #加入BuydbFilter資料表的清單網頁的url mapping
    path('buydbfilter/', views.Filterforbuydb, name='buydb-filter'),
    
    #加入RentdbFilter資料表的清單網頁的url mapping
    path('rentdbfilter/', views.Filterforrentdb, name='rentdb-filter'),

    #加入RentdbFilter資料表的清單網頁的url mapping
    path('metromap/', views.Filterforrentdb, name='rentdb-filter'),
]