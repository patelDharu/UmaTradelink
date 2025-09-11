from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),

    # About Us pages
    path('about/who-we-are/', views.who_we_are, name="who_we_are"),
    path('about/our-journey/', views.our_journey, name="our_journey"),
    path('about/management-speak/', views.management_speak, name="management_speak"),
    path('about/mission/', views.mission, name="mission"),
    path('about/csr/', views.csr, name="csr"),

    # Our Strength
    path('strength/reach/', views.reach, name="reach"),
    path('strength/industries/', views.industries, name="industries"),

    # Services
    path('services/sales-marketing/', views.sales_marketing, name="sales_marketing"),
    path('services/cargo-consolidation/', views.cargo_consolidation, name="cargo_consolidation"),
    path('services/logistics/', views.logistics, name="logistics"),
    path('services/sourcing/', views.sourcing, name="sourcing"),

    # Careers & Contact
    path('career/', views.career, name="career"),
    path('contact/', views.contact, name="contact"),
]
