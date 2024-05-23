from rest_framework import  serializers
from ..models import Prof
class ProfSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prof
        fields = ['id', 'name', 'registration_date', 'image', 'department', 'rank']
# class Prof(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=200, required=True)
#     registration_date = serializers.DateTimeField(read_only=True)
#     image = serializers.CharField(max_length=100, required=False, allow_null=True)
#     department = serializers.CharField(max_length=100, required=True)
#     rank = serializers.CharField(max_length=50, required=True)
