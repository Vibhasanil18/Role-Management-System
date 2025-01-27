
from django.urls import path
from . import views

urlpatterns = [
    path('roles/', views.role_dashboard, name='role_dashboard'),  # Dashboard to list roles
    path('roles/add/', views.add_role, name='add_role'),  # Add a new role
    path('roles/edit/<int:role_id>/', views.edit_role, name='edit_role'),  # Edit a role
    path('roles/delete/<int:role_id>/', views.delete_role, name='delete_role'),  # Delete a role (soft delete)
]
