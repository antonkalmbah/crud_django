from rest_framework import serializers
from .model import Notepad

class NotepadSerializers(serializers.ModelSerializer):
    class Meta:
        model = Notepad
        fields = ['id', 'heading', 'text']