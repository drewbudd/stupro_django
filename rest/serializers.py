from django.contrib.auth.models import User, Group
from rest_framework import serializers
from cadmodels.models import CADModel, Marker, Status, Type

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class CADModelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CADModel
        fields = ('id', 'name', 'checked_out', 'creation_date')

class MarkerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Marker
        fields = ('id', 'cad_model', 'name', 'status', 'type', 'creation_date', 'coord_x', 'coord_y', 'coord_z', 'comments')

class StatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Status
        fields = ('id', 'name')

class TypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Type
        fields = ('id', 'name')