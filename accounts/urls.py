from django.conf.urls import url, include
from accounts.views import logout, login, registration, user_profile
from keto_pantry import urls_reset

urlpatterns = [
    url(r'^logout/', logout, name="logout"),
    url(r'^login/', login, name="login"),
    url(r'^register/', registration, name="registration"),
    url(r'^password-reset/', include(urls_reset)),
    url(r'^profile/', user_profile, name="profile")
]
