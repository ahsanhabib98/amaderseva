from django.urls import path
from .views import *


urlpatterns = [
    path('add-mobilephone/',create_mobilephone_service , name = 'create_mobilephone_service'),
    path('mobilephone-details/<int:id>/',details_mobilephone_service , name = 'detail_mobilephone_service'),
    path('mobilephone-edit/<int:id>/',edit_mobilephone_service , name = 'edit_mobilephone_service'),

    path('add-computing/',create_computing_service , name = 'create_computing_service'),
    path('computing-details/<int:id>/',details_computing_service , name = 'detail_computing_service'),
    path('computing-edit/<int:id>/',edit_computing_service , name = 'edit_computing_service'),

    path('add-television/',create_television_service , name = 'create_television_service'),
    path('television-details/<int:id>/',details_television_service , name = 'detail_television_service'),
    path('television-edit/<int:id>/',edit_television_service , name = 'edit_television_service'),

    path('add-others/',create_others_service , name = 'create_others_service'),
    path('others-details/<int:id>/',details_others_service , name = 'detail_others_service'),
    path('others-edit/<int:id>/',edit_others_service , name = 'edit_others_service'),

    path('add-apartment/',create_apartment_service , name = 'create_apartment_service'),
    path('apartment-details/<int:id>/',details_apartment_service , name = 'detail_apartment_service'),
    path('apartment-edit/<int:id>/',edit_apartment_service , name = 'edit_apartment_service'),

    path('add-ecommerce/',create_ecommerce_service , name = 'create_ecommerce_service'),
    path('ecommerce-details/<int:id>/',details_ecommerce_service , name = 'detail_ecommerce_service'),
    path('ecommerce-edit/<int:id>/',edit_ecommerce_service , name = 'edit_ecommerce_service'),

    path('add-education/',create_education_service , name = 'create_education_service'),
    path('education-details/<int:id>/',details_education_service , name = 'detail_education_service'),
    path('education-edit/<int:id>/',edit_education_service , name = 'edit_education_service'),

    path('service-list/', service_list , name = 'service_list'),

    path('categorywise-mobile/', categorywise_mobile , name = 'categorywise_mobile'),
    path('categorywise-compute/', categorywise_compute , name = 'categorywise_compute'),
    path('categorywise-tv/', categorywise_tv , name = 'categorywise_tv'),
    path('categorywise-other/', categorywise_other , name = 'categorywise_other'),
    path('categorywise-apartment/', categorywise_apartment , name = 'categorywise_apartment'),
    path('categorywise-ecommerce/', categorywise_ecommerce , name = 'categorywise_ecommerce'),
    path('categorywise-education/', categorywise_education , name = 'categorywise_education'),
    path('searchingwise-service/', searchingwise_service , name = 'searchingwise_service'),
    path('servicewise-profile/<int:id>', servicewise_profile , name = 'servicewise-profile'),

]
