import os
from datetime import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'pms.settings')

import django

django.setup()

from api.models import User, Role, Permission, Organization, PetitionType, RankType, Prefix, Priority, Category, \
    PetitionDetailType, PetitionDetailStatus

organizations = [
    {
        'id': 1, 'name': 'Test Superuser Branch', 'description': 'Test Superuser Branch', 'parent': None, 'organization_type': 'Root',
        'is_delete': 'No',
        'insert_date': datetime.now(), 'insert_by': 'System', 'update_date': datetime.now(), 'update_by': 'System',
        'location': 'Rawalpindi', 'datacenter_id': 1, 'username_prefix': '', 'signal_center_id': 1, 'arm_type': 1,
        'ams_type': 1, 'online_status': 'Online', 'org_code': 1, 'org_status': 'System', 'city_code': 1,
    },
]

roles = [
    {
        'name': 'AG',
        'code_name': 'ag',
        'permissions': [
            'role_read', 'user_read', 'organization_read', 'petition_read', 'petition_update',
            'petition_close', 'petition_call',  'dashboard_show',  'petition_type_read', 'rank_type_read',
            'prefix_read', 'priority_read', 'category_read', 'petition_detail_type_read',
            'petition_detail_status_read', 'document_read', 'petition_link_read', 'petition_link_update',
            'petition_link_delete', 'organization_child_read', 'petition_delete'
        ]
    },
    {
        'name': 'DD Petition',
        'code_name': 'dd_petition',
        'permissions': [
            'role_read', 'user_read', 'organization_read', 'petition_create', 'petition_read', 'petition_update',
            'petition_show', 'petition_close', 'petition_detail_update', 'petition_call', 'marked_petition_show',
            'all_petition_show', 'dashboard_show', 'daily_report_show', 'overall_report_show', 'suggestion_create',
            'petition_type_read', 'rank_type_read', 'prefix_read', 'priority_read', 'category_read',
            'petition_detail_type_read', 'petition_detail_status_read', 'document_create', 'document_read',
            'document_show', 'approve_can', 'approve_auto', 'petition_link_create', 'petition_link_read',
            'petition_link_update', 'petition_link_delete', 'petition_link_show', 'approve_link_can',
            'approve_link_auto', 'petition_can_search', 'organization_child_create', 'organization_child_read',
            'organization_child_update', 'organization_child_show', 'petition_delete'
        ]
    },
    {
        'name': 'DG',
        'code_name': 'dg',
        'permissions': [
            'role_read', 'user_read', 'organization_read', 'petition_create', 'petition_read', 'petition_update',
            'petition_show', 'petition_detail_update', 'petition_call', 'marked_petition_show',
            'all_petition_show', 'dashboard_show', 'daily_report_show', 'overall_report_show', 'suggestion_create',
            'petition_type_read', 'rank_type_read', 'prefix_read', 'priority_read', 'category_read',
            'petition_detail_type_read', 'petition_detail_status_read', 'document_create', 'document_read',
            'document_show', 'approve_can', 'approve_auto', 'petition_link_create', 'petition_link_read',
            'petition_link_update', 'petition_link_delete', 'petition_link_show', 'approve_link_can',
            'approve_link_auto', 'petition_can_search', 'organization_child_create', 'organization_child_read',
            'organization_child_update', 'organization_child_show', 'petition_delete'
        ]
    },
    {
        'name': 'Dir',
        'code_name': 'dir',
        'permissions': [
            'role_read', 'user_read', 'organization_read', 'petition_create', 'petition_read', 'petition_update',
            'petition_show', 'petition_detail_update', 'petition_call', 'marked_petition_show', 'dashboard_show',
            'daily_report_show', 'overall_report_show', 'petition_type_read', 'rank_type_read', 'prefix_read',
            'priority_read', 'category_read', 'petition_detail_type_read', 'petition_detail_status_read',
            'document_create', 'document_read', 'document_show', 'approve_can', 'approve_auto', 'petition_link_create',
            'petition_link_read', 'petition_link_update', 'petition_link_show', 'approve_link_can', 'approve_link_auto',
            'petition_can_search', 'suggestion_create', 'organization_child_create', 'organization_child_read',
            'organization_child_update', 'organization_child_show', 'petition_delete'
        ]
    },
    {
        'name': 'Col',
        'code_name': 'col',
        'permissions': [
            'role_read', 'user_read', 'organization_read', 'petition_create', 'petition_read', 'petition_update',
            'petition_show', 'petition_detail_update', 'petition_call', 'marked_petition_show', 'dashboard_show',
            'daily_report_show', 'overall_report_show', 'petition_type_read', 'rank_type_read', 'prefix_read',
            'priority_read', 'category_read', 'petition_detail_type_read', 'petition_detail_status_read',
            'document_create', 'document_read', 'document_show', 'approve_can', 'approve_auto', 'petition_link_create',
            'petition_link_read', 'petition_link_update', 'petition_link_show', 'approve_link_can', 'approve_link_auto',
            'petition_can_search', 'suggestion_create', 'organization_child_create', 'organization_child_read',
            'organization_child_update', 'organization_child_show', 'petition_delete'
        ]
    },
    {
        'name': 'Lt. Col',
        'code_name': 'lt.Col',
        'permissions': [
            'role_read', 'user_read', 'organization_read', 'petition_create', 'petition_read', 'petition_update',
            'petition_show', 'petition_detail_update', 'petition_call', 'marked_petition_show', 'dashboard_show',
            'daily_report_show', 'overall_report_show', 'petition_type_read', 'rank_type_read', 'prefix_read',
            'priority_read', 'category_read', 'petition_detail_type_read', 'petition_detail_status_read',
            'document_create', 'document_read', 'document_show', 'approve_can', 'approve_auto', 'petition_link_create',
            'petition_link_read', 'petition_link_update', 'petition_link_show', 'approve_link_can', 'approve_link_auto',
            'petition_can_search', 'suggestion_create', 'organization_child_create', 'organization_child_read',
            'organization_child_update', 'organization_child_show', 'petition_delete'
        ]
    },
    {
        'name': 'Major',
        'code_name': 'maj',
        'permissions': [
            'role_read', 'user_read', 'organization_read', 'petition_create', 'petition_read', 'petition_update',
            'petition_show', 'petition_detail_update', 'petition_call', 'marked_petition_show',
            'daily_report_show', 'overall_report_show', 'petition_type_read', 'rank_type_read', 'prefix_read',
            'priority_read', 'category_read', 'petition_detail_type_read', 'petition_detail_status_read',
            'document_create', 'document_read', 'document_show', 'approve_can', 'approve_auto', 'petition_link_create',
            'petition_link_read', 'petition_link_update', 'petition_link_show', 'approve_link_can', 'approve_link_auto',
            'petition_can_search', 'organization_child_create', 'organization_child_read',
            'organization_child_update', 'organization_child_show', 'petition_delete'
        ]
    },
    {
        'name': 'Captain',
        'code_name': 'cap',
        'permissions': [
            'role_read', 'user_read', 'organization_read', 'petition_create', 'petition_read', 'petition_update',
            'petition_show', 'petition_detail_update', 'petition_call', 'marked_petition_show', 'daily_report_show',
            'overall_report_show', 'petition_type_read', 'rank_type_read', 'prefix_read', 'priority_read',
            'category_read', 'petition_detail_type_read', 'petition_detail_status_read', 'document_create',
            'document_read', 'document_show', 'petition_link_create', 'petition_link_read',
            'petition_link_update', 'petition_link_show', 'petition_can_search', 'organization_child_create',
            'organization_child_read', 'organization_child_update', 'organization_child_show', 'petition_delete'
        ]
    },
    {
        'name': 'Clerk',
        'code_name': 'clk',
        'permissions': [
            'role_read', 'user_read', 'organization_read', 'petition_create', 'petition_read', 'petition_update',
            'petition_show', 'petition_detail_update', 'petition_call', 'marked_petition_show', 'daily_report_show',
            'overall_report_show', 'petition_type_read', 'rank_type_read', 'prefix_read', 'priority_read',
            'category_read', 'petition_detail_type_read', 'petition_detail_status_read', 'document_create',
            'document_read', 'document_show', 'petition_link_create', 'petition_link_read',
            'petition_link_update', 'petition_link_show', 'petition_can_search', 'organization_child_create',
            'organization_child_read', 'organization_child_update', 'organization_child_show', 'petition_delete'
        ]
    },
    {
        'name': 'NormalUser',
        'code_name': 'nu',
        'permissions': [
            'role_read', 'user_read', 'organization_read', 'petition_create', 'petition_read', 'petition_update',
            'petition_show', 'marked_petition_show', 'petition_detail_update', 'petition_call', 'petition_type_read',
            'rank_type_read', 'prefix_read', 'priority_read', 'category_read', 'petition_detail_type_read',
            'petition_detail_status_read', 'document_create', 'document_read', 'document_show', 'petition_link_create',
            'petition_link_read', 'petition_link_update', 'petition_link_show', 'petition_can_search',
            'organization_child_create', 'organization_child_read', 'organization_child_update',
            'organization_child_show', 'petition_delete'
        ]
    },
    {
        'name': 'PMC',
        'code_name': 'pmc',
        'permissions': [
            'role_read', 'user_read', 'organization_read', 'petition_create', 'petition_read', 'petition_update',
            'petition_show', 'petition_detail_update', 'petition_call', 'marked_petition_show', 'dashboard_show',
            'daily_report_show', 'overall_report_show', 'petition_type_read', 'rank_type_read', 'prefix_read',
            'priority_read', 'category_read', 'petition_detail_type_read', 'petition_detail_status_read',
            'document_create', 'document_read', 'document_show', 'approve_can', 'approve_auto', 'petition_link_create',
            'petition_link_read', 'petition_link_update', 'petition_link_show', 'approve_link_can', 'approve_link_auto',
            'petition_can_search', 'suggestion_create', 'organization_child_create', 'organization_child_read',
            'organization_child_update', 'organization_child_show', 'petition_delete',
            'petition_update_sponsor_organization'
        ]
    },
]

petition_types = [
    {
        'name': 'Fin Asst',
    },
    {
        'name': 'Pension Matters',
    },
    {
        'name': 'Issue of NOC for Plot',
    },
    {
        'name': 'Loan',
    },
    {
        'name': 'DHAI-Matters',
    },
    {
        'name': 'DHAI-Plot',
    },
    {
        'name': 'Discipline Issues',
    },
    {
        'name': 'Matrimonial Cases',
    },
    {
        'name': 'Enrolment-Sldr',
    },
    {
        'name': 'ISSB-Offrs',
    },
    {
        'name': 'Med Bd Out',
    },
    {
        'name': 'Med Issues',
    },
    {
        'name': 'Re-Imbursement of amount',
    },
    {
        'name': 'Enrolment of Doc',
    },
    {
        'name': 'AWT / FF Matters',
    },
    {
        'name': 'Fin Matters / Car / Scheme',
    },
    {
        'name': 'Misc',
    }
]

petition_detail_types = [
    {
        'name': 'Army',
    },
    {
        'name': 'Civilian',
    },
    {
        'name': 'Anonymous',
    },
]

petition_detail_statuses = [
    {
        'name': 'Serving',
    },
    {
        'name': 'Retired',
    },
    {
        'name': 'War-Wounded',
    },
    {
        'name': 'Shuhda',
    },
]

rank_types = [
    {
        'name': 'Lt. General',
        'category': 1,
    },
    {
        'name': 'Col',
        'category': 2,
    },
    {
        'name': 'Major',
        'category': 3,
    },
    {
        'name': 'Soldier',
        'category': 4,
    }
]

prefixes = [
    {
        'name': 'PA',
    },
    {
        'name': 'PS',
    },
]

priorities = [
    {
        'name': 'Priority 1',
    },
    {
        'name': 'Priority 2',
    },
]

categories = [
    {
        'name': 'Cat 1',
        'description': 'Mk By COAS',
        'is_active': True,
    },
    {
        'name': 'Cat 2',
        'description': 'Mk By AG',
        'is_active': True,
    },
    {
        'name': 'Cat 3',
        'description': 'Normal',
        'is_active': True,
    },
    {
        'name': 'Cat 4',
        'description': 'Mk By Gen Offr	',
        'is_active': True,
    },
    {
        'name': 'Cat 5',
        'description': 'Civs',
        'is_active': True,
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

    for organization in organizations:
        try:
            Organization.objects.get(name=organization['name'])
        except Organization.DoesNotExist:
            parent = None
            if organization['parent']:
                parent = Organization.objects.get(name=organization['parent'])
            Organization.objects.create(
                id=organization['id'],
                name=organization['name'],
                description=organization['description'],
                parent=parent,
                organization_type=organization['organization_type'],
                is_delete=organization['is_delete'],
                insert_date=organization['insert_date'],
                insert_by=organization['insert_by'],
                update_date=organization['update_date'],
                update_by=organization['update_by'],
                location=organization['location'],
                datacenter_id=organization['datacenter_id'],
                username_prefix=organization['username_prefix'],
                signal_center_id=organization['signal_center_id'],
                arm_type=organization['arm_type'],
                ams_type=organization['ams_type'],
                online_status=organization['online_status'],
                org_code=organization['org_code'],
                org_status=organization['org_status'],
                city_code=organization['city_code'],
            )

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
        user.organization = Organization.objects.get(name='Test Superuser Branch')
        user.save()

    for role in roles:
        try:
            Role.objects.get(code_name=role['code_name'])
        except Role.DoesNotExist:
            r = Role.objects.create(name=role['name'], code_name=role['code_name'], created_by=User.objects.get(username='superuser'), updated_by=User.objects.get(username='superuser'),)
            for permission in role['permissions']:
                r.permissions.add(Permission.objects.get(code_name=permission))
            r.save()

    for petition_type in petition_types:
        try:
            PetitionType.objects.get(name=petition_type['name'])
        except PetitionType.DoesNotExist:
            PetitionType.objects.create(name=petition_type['name'], created_by=User.objects.get(username="superuser"), updated_by=User.objects.get(username="superuser"))

    for petition_detail_type in petition_detail_types:
        try:
            PetitionDetailType.objects.get(name=petition_detail_type['name'])
        except PetitionDetailType.DoesNotExist:
            PetitionDetailType.objects.create(name=petition_detail_type['name'], created_by=User.objects.get(username="superuser"), updated_by=User.objects.get(username="superuser"))

    for petition_detail_status in petition_detail_statuses:
        try:
            PetitionDetailStatus.objects.get(name=petition_detail_status['name'])
        except PetitionDetailStatus.DoesNotExist:
            PetitionDetailStatus.objects.create(name=petition_detail_status['name'], created_by=User.objects.get(username="superuser"), updated_by=User.objects.get(username="superuser"))

    for rank_type in rank_types:
        try:
            RankType.objects.get(name=rank_type['name'])
        except RankType.DoesNotExist:
            RankType.objects.create(name=rank_type['name'], category=rank_type['category'], created_by=User.objects.get(username="superuser"), updated_by=User.objects.get(username="superuser"))

    for prefix in prefixes:
        try:
            Prefix.objects.get(name=prefix['name'])
        except Prefix.DoesNotExist:
            Prefix.objects.create(name=prefix['name'], created_by=User.objects.get(username="superuser"), updated_by=User.objects.get(username="superuser"))

    for priority in priorities:
        try:
            Priority.objects.get(name=priority['name'])
        except Priority.DoesNotExist:
            Priority.objects.create(name=priority['name'], created_by=User.objects.get(username="superuser"), updated_by=User.objects.get(username="superuser"))

    for category in categories:
        try:
            Category.objects.get(name=category['name'])
        except Category.DoesNotExist:
            Category.objects.create(name=category['name'], description=category['description'], is_active=category['is_active'], created_by=User.objects.get(username="superuser"), updated_by=User.objects.get(username="superuser"))


if __name__ == '__main__':
    print("Starting PMS production population script...")
    populate()
