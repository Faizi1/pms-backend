from rest_framework import serializers

from api.models import Role, User


class UserSerializer(serializers.ModelSerializer):
    role_data = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "name",
            "password",
            "profile_status",
            "profile_image",
            "role",
            "role_data",
        )

        read_only_fields = ("id", "username", "name", "is_delete")
        extra_kwargs = {"password": {"write_only": True}}

    def get_role_data(self, obj):
        if not obj.role:
            return None

        role = Role.objects.get(pk=obj.role.id)
        data = {"id": role.id, "name": role.name, "code_name": role.code_name}
        return data
