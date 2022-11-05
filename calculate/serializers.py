from rest_framework import serializers

class HNGSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ["*"]