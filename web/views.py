from django.views import generic


class NoteListView(generic.ListView):
    ...


class NoteDetailView(generic.DetailView):
    ...


class NoteEditView(generic.UpdateView):
    ...


class NoteDeleteView(generic.DeleteView):
    ...


class NoteCreateView(generic.CreateView):
    ...

