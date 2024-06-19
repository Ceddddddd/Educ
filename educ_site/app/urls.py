from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',views.home, name='home'),
    path('download_education/', views.download_education, name='download_education'),
    path('grade/1-2/', views.activity_grade_1, name='grade_1-2'),
    path('grade/3-4/', views.activity_grade_3, name='grade_3-4'),
    path('grade/5-6/', views.activity_grade_5, name='grade_5-6'),
    path('activities/view/<int:activity_id>/', views.view_activity, name='view_activity'),
    path('activities/download/<int:activity_id>/', views.download_activity, name='download_activity'),
    path('quizzes/view/<int:quiz_id>/', views.view_quiz, name='view_quiz'),
    path('quizzes/download/<int:quiz_id>/', views.download_quiz, name='download_quiz'),
    path('learning/view/<int:learning_id>/', views.view_learning, name='view_learning'),
    path('learning/download/<int:learning_id>/', views.download_learning, name='download_learning'),
    path('search/', views.search, name='search'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)