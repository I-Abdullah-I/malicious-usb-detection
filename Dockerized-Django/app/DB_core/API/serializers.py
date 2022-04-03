from rest_framework import serializers
from DB_core.models import Malware


class MalwareSerializer(serializers.ModelSerializer):
    class Meta:
        model = Malware
        fields = "__all__"
        extra_kwargs = {"whitelisted": {"required": False}}
