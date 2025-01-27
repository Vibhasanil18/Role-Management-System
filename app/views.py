# views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Role
from .forms import RoleForm

# Dashboard to view all roles
def role_dashboard(request):
    roles = Role.objects.filter(status=True)  # Fetch active roles only
    return render(request, 'role_dashboard.html', {'roles': roles})

# Add a new role
def add_role(request):
    if request.method == 'POST':
        form = RoleForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Role created successfully!")
            return redirect('role_dashboard')
    else:
        form = RoleForm()
    return render(request, 'add_role.html', {'form': form})

# Edit an existing role
def edit_role(request, role_id):
    role = get_object_or_404(Role, id=role_id)
    if request.method == 'POST':
        form = RoleForm(request.POST, instance=role)
        if form.is_valid():
            form.save()
            messages.success(request, "Role updated successfully!")
            return redirect('role_dashboard')
    else:
        form = RoleForm(instance=role)
    return render(request, 'edit_role.html', {'form': form})

# Soft delete a role (mark as inactive)
def delete_role(request, role_id):
    role = get_object_or_404(Role, id=role_id)
    role.status = False  # Mark the role as inactive (soft delete)
    role.save()
    messages.success(request, "Role deleted successfully!")
    return redirect('role_dashboard')
