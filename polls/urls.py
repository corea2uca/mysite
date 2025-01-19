from django.urls import path
from . import views

# 여기는 app이 polls만 있지만, 여러개 올수 있음, 
# 그래서 app_name 필요
app_name = "polls"

# 기본
urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
    # ex: /polls/5/
    path("<int:question_id>/detail/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]

# # generic view 재사용 가능한 뷰
# urlpatterns = [
#     path("", views.IndexView.as_view(), name="index"),
#     path("<int:pk>/", views.DetailView.as_view(), name="detail"),
#     path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
#     path("<int:question_id>/vote/", views.vote, name="vote"),
# ]