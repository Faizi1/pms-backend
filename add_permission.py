import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'pms.settings')

import django

django.setup()

from api.models import Permission

permissions = [
    Permission(name='Create Role', code_name='role_create', module_name='Role', description='User can create role'),
    Permission(name='Read Role', code_name='role_read', module_name='Role', description='User can read role'),
    Permission(name='Update Role', code_name='role_update', module_name='Role', description='User can update role'),
    Permission(name='Delete Role', code_name='role_delete', module_name='Role', description='User can delete role'),
    Permission(name='Show Role', code_name='role_show', module_name='Role', description='User can show user'),
    Permission(name='Read User', code_name='user_read', module_name='User', description='User can read user'),
    Permission(name='Update User', code_name='user_update', module_name='User', description='User can update user'),
    Permission(name='Show User', code_name='user_show', module_name='User', description='User can show user'),

    # Dashboard
    Permission(name='Show Dashboard', code_name='dashboard_show', module_name='Dashboard', description='User can show dashboard'),
    Permission(name='Show Case', code_name='show_case', module_name='Case', description='User can view case'),


]


def add_permission():
    for permission in permissions:
        try:
            Permission.objects.get(code_name=permission.code_name)
        except Permission.DoesNotExist:
            permission.save()


if __name__ == '__main__':
    print("Adding permissions to PMS...")
    add_permission()
