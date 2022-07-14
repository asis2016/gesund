from django.contrib import admin
from django.urls import include, path, re_path
from dashboard.views import DashboardTemplateview

urlpatterns = [
    path('', DashboardTemplateview.as_view(), name='dashboard'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),

    # api
    path('api/v1/', include('api.urls')),
    path('api-auth/', include('rest_framework.urls')),

    #
    path('about/', include('aboutus.urls')),
    path('challenges/', include('challenges.urls')),
    path('exports/', include('exports.urls')),
    path('foods/', include('calories.urls')),
    path('goals/', include('goals.urls')),
    path('history/', include('history.urls')),
    path('leaderboards/', include('leaderboards.urls')),
    path('pomodoros/', include('pomodoros.urls')),
    path('profile/', include('profiles.urls')),
    path('steps/', include('steps.urls')),
    path('steps/', include('steps.urls')),
    path('water-tracker/', include('water_intake.urls')),
    path('weight/', include('weights.urls')),
    path('xps/', include('xps.urls')),
]
