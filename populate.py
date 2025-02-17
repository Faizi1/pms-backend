import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'pms.settings')

import django

django.setup()

from django.utils import timezone

from api.models import User, Role, Permission

users = [
    {
        'id': 1, 'username': 'faiz', 'name': 'Faiz', 'profile_status': 'Current', 'is_delete': 'No', 'role': 'nu'
    },
    {
        'id': 2, 'username': 'alex', 'name': 'Alex', 'profile_status': 'Current', 'is_delete': 'No', 'role': 'nu'
    },
    {
        'id': 3, 'username': 'test', 'name': 'Test', 'profile_status': 'Current', 'is_delete': 'No', 'role': 'nu'
    },
]

roles = [
    {
        'name': 'NormalUser',
        'code_name': 'nu',
        'permissions': [
                'user_read', 'read_role',
        ]
    },
]

def populate():
    permissions = Permission.objects.all()

    try:
        role = Role.objects.get(code_name='su')
        role.permissions.clear()
    except Role.DoesNotExist:
        role = Role.objects.create(name='SuperUser', code_name='su')

    role.permissions.add(*permissions)
    role.save()

    try:
        user = User.objects.get(username='superuser')
    except User.DoesNotExist:
        user = User.objects.create_superuser(
            id=999,
            username="superuser",
            password="123",
        )
        user.name = 'Superuser'
        user.role = Role.objects.get(code_name='su')
        user.save()

    for role in roles:
        try:
            Role.objects.get(code_name=role['code_name'])
        except Role.DoesNotExist:
            r = Role.objects.create(name=role['name'], code_name=role['code_name'],
                                    created_by=User.objects.get(username='superuser'),
                                    updated_by=User.objects.get(username='superuser'), )
            for permission in role['permissions']:
                r.permissions.add(Permission.objects.get(code_name=permission))
            r.save()

    for user in users:
        try:
            User.objects.get(id=user['id'])
        except User.DoesNotExist:
            User.objects.create(
                id=user['id'],
                username=user['username'],
                name=user['name'],
                profile_status=user['profile_status'],
                is_delete=user['is_delete'],
                role=Role.objects.get(code_name=user['role']),
            )


if __name__ == '__main__':
    print("Starting PMS population script...")
    populate()
