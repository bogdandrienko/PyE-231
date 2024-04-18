from rest_framework import serializers
from django_app import models


class ContactAllSerializer(serializers.ModelSerializer):
    position_rel = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = models.Contact
        fields = "__all__"  # include / exclude/ ['username',...]

    def get_position_rel(self, obj: models.Contact):
        try:
            return str(obj.position.name)
        except Exception as error:
            return ""
