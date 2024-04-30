from django.urls import path
from .views import (
    DepartmentView, 
    PersonnelListCreateView, 
    PersonnelGetUpdateDeleteView, 
    DepartmentPersonnelView, 
    DepartmentPersonnelViewCustom,
)

urlpatterns = [
    path("department/", DepartmentView.as_view()),
    path("personnel/", PersonnelListCreateView.as_view()),
    path("personnel/<int:pk>/", PersonnelGetUpdateDeleteView.as_view()),
    path("department/<str:department>/", DepartmentPersonnelView.as_view()),
    # path("department/<str:name>/", DepartmentPersonnelViewCustom.as_view()),
]
