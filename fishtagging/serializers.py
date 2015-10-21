from django.forms import widgets
from rest_framework import serializers
from fishtagging.models import Species, Disposition, States, Taggers, TagTypes, LandLocation, Recapture, TagPurchases, Tags, WHZoneCodes
from django.contrib.auth.models import User

class SpeciesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Species
        fields = ('code','species')

class DispositionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Disposition
        fields = ('id', 'disposition')

class LandLocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = LandLocation
        fields = ('id', 'legend')

class StatesSerializer(serializers.ModelSerializer):

    class Meta:
        model = States
        fields = ('id', 'st')

class TaggersSerializer(serializers.ModelSerializer):

    class Meta:
        model = Taggers
        fields = ('id', 'first', 'last', 'suffix', 'prefix', 'nick', 'address1', 'address', 'muni','zip','email',
                  'phone','cell','business','member','duesDueDate','dateJoined')

class TagTypesSerializer(serializers.ModelSerializer):

    class Meta:
        model = TagTypes
        fields = ('id', 'typenum','tagtype','lotsize','lotprice','needleprice','start','end')

class DispositionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Disposition
        fields = ('id', 'disposition')

class WHZoneCodesSerializer(serializers.ModelSerializer):

    class Meta:
        model = WHZoneCodes
        fields = ('id', 'zoneno','masterzone','description')