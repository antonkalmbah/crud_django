from notepad.models import Notepad


def index_view(request, id):
    note = Notepad.objects.get(id=id)
