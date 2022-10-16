from rest_framework import serializers
from .models import *


class BlogModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogModel
        fields = "__all__"


class SocailMediaLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocailMediaLink
        fields = "__all__"
