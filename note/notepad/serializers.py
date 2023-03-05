from rest_framework import serializers
from .models import Notepad


class NotepadSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Notepad
        fields = ['id', 'heading', 'text']