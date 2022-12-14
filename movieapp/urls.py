from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('catalog-1/', views.catalog_grid, name='cat1'),
    path('catalog-2/', views.catalog_list, name='cat2'),
    path('pricing-plan/', views.pricing, name='pricing'),
    path('frequently-asked-questions/', views.faq, name='faq'),
    path('about-us/', views.about, name='about'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.signin, name='login'),
    path('register/', views.signup, name='register'),
    path('logout/', views.LogoutView, name='logout'),
    path('forgot-password/', views.forgot_password, name='fp'),
    path('privacy/', views.privacy, name='privacy'),
    path('contact-us/', views.contacts, name='contact'),
    path('404/', views.NotFound, name='404'),
    path('detail-view/<str:name>/', views.detail, name='detail'),
    path('series/detail/<str:name>/', views.series_detail, name='series-detail'),
    path('series/detail/<str:name>/<str:seasons>/<str:epi>/', views.series_detail_epi, name='series-detail-epi'),
    path('auth/reset-password/', views.reset_password, name='reset-password'),
    path('auth/reset-password/<str:name>/', views.PasswordResedtView, name='reset_view'),
    path('auth/password-reset-sent/', views.password_reset_sent, name='reset-sent'),
    path('series/', views.Series, name='series'),
    path('anime/', views.Anime, name='anime'),
    path('search-result/', views.searchresult, name='search'),
]

