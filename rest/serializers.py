from django.contrib.auth.models import User, Group
from cadmodels.models import CADModel, Marker, Status, Type
from rest_framework import serializers


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
        fields = ('name', 'checked_out', 'creation_date')

class MarkerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CADModel
        fields = ('cad_model', 'name', 'status', 'type', 'creation_date', 'coord_x', 'coord_y', 'coord_z', 'comments')

class StatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CADModel
        fields = ('name')

class TypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CADModel
        fields = ('name')