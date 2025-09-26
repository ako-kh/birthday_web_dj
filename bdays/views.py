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

class BdaysListView(ListView):
    template_name = "birthdays/home.html"

    def get_queryset(self):
        queryset = BirthdayModel.objects.all()
        for person in  queryset:
            person.days_left = days_until_birthday(person)
        return queryset

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     days_left_dict = {}
    #     for obj in self.queryset:
    #         days_left_dict[obj.id] = days_until_birthday(obj)
    #     context["days_left_dict"] = days_left_dict
    #     return context


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
