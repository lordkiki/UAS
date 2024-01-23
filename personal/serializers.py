from rest_framework import serializers
from .models import Tbcars

class TbcarsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tbcars
        fields = ('id', 'carname', 'carbrand', 'carmodel', 'carprice')