from django.shortcuts import render
from fishtagging.models import Species, Disposition, States, Taggers, TagTypes, LandLocation, Recapture, TagPurchases, Tags, WHZoneCodes
from fishtagging.serializers import SpeciesSerializer, DispositionSerializer, LandLocationSerializer, StatesSerializer, TaggersSerializer
from rest_framework import generics

from rest_framework import permissions

from django.contrib.auth.models import User
from snippets.serializers import UserSerializer

class SpeciesList(generics.ListCreateAPIView):
    queryset = Species.objects.all()
    serializer_class = SpeciesSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save()

class SpeciesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Species.objects.all()
    serializer_class = SpeciesSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class DispositionList(generics.ListCreateAPIView):
    queryset = Disposition.objects.all()
    serializer_class = DispositionSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save()

class DispositionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Disposition.objects.all()
    serializer_class = DispositionSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)



class LandLocationList(generics.ListCreateAPIView):
    queryset = LandLocation.objects.all()
    serializer_class = LandLocationSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save()

class LandLocationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = LandLocation.objects.all()
    serializer_class = LandLocationSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)



class StatesList(generics.ListCreateAPIView):
    queryset = States.objects.all()
    serializer_class = StatesSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save()

class StatesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = States.objects.all()
    serializer_class = StatesSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)



class TaggersList(generics.ListCreateAPIView):
    queryset = Taggers.objects.all()
    serializer_class = TaggersSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save()

class TaggersDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Taggers.objects.all()
    serializer_class = TaggersSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)