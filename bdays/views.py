from django.shortcuts import render, get_object_or_404
from django import forms
from django.urls import reverse
from django.views.generic import (
    CreateView,
    DetailView,
    DeleteView,
    ListView,
    UpdateView,
)
from .models import BirthdayModel
from .utils.utils import days_until_birthday
import operator

class BdaysListView(ListView):
    template_name = "birthdays/home.html"

    def get_queryset(self):
        queryset = BirthdayModel.objects.all()
        for person in queryset:
            person.days_left = days_until_birthday(person)

        sort_by = self.request.GET.get('sort_by')

        if sort_by in ['days_left', 'name', 'date']:
            if self.request.GET.get('d', 'asc') == "desc":
                direction = True
            else:
                direction = False

            return sorted(queryset, key=operator.attrgetter(sort_by), reverse=direction)
        return queryset


class BdaysDetailView(DetailView):
    template_name = "birthdays/birthday_detail.html"

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(BirthdayModel, id=id_)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["days_left"] = days_until_birthday(self.object)
        return context


class BdaysCreateView(CreateView):
    template_name = "birthdays/birthday_create.html"
    queryset = BirthdayModel.objects.all()
    fields = [
        "name",
        "date",
        "gift_idea"
    ]

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        form.fields['date'].widget = forms.DateInput(attrs={'type': 'date'})
        return form


class BdaysUpdateView(UpdateView):
    template_name = "birthdays/birthday_create.html"
    queryset = BirthdayModel.objects.all()
    fields = [
        "name",
        "date",
        "gift_idea"
    ]

    def get_form(self, *args, **kwargs):
        form = super().get_form(*args, **kwargs)
        form.fields['date'].widget = forms.DateInput(attrs={'type': 'date'})
        return form

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(BirthdayModel, id=id_)


class BdaysDeleteView(DeleteView):
    template_name = "birthdays/birthday_delete.html"

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(BirthdayModel, id=id_)

    def get_success_url(self):
        return reverse("bdays:bday-list", current_app="bdays")
