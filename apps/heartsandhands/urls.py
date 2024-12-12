from django.urls import path

from . import views


urlpatterns = [
   path('', views.HomeView.as_view(), name='home'),
   path('ads.txt', views.ads_txt, name='ads.txt'),
   path('contact/', views.ContactUsView.as_view(), name='contact_us'),
   path('about-us/', views.AboutUsView.as_view(), name='about_us'),
   path('donate/', views.DonateView.as_view(), name='donate'),
   path('donation-successful/', views.DonationSuccessFul.as_view(), name='donation-successful'),
   path("verify-paystack-payment/", views.verify_paystack_success, name="verify-paystack-payment")
]
