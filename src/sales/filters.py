import django_filters

from .models import Contact, ContactSource, SkillProfile

class ContactFilter(django_filters.FilterSet):
    start_date = django_filters.DateFilter(field_name='next_contact_date', lookup_expr=('gt'), label="Сл. звонок с")
    end_date = django_filters.DateFilter(field_name='next_contact_date', lookup_expr=('lt'), label="Сл. звонок до")
    phone_main = django_filters.CharFilter(label="Телефон", field_name="phone_main", lookup_expr="icontains")
    first_name = django_filters.CharFilter(label="Имя", field_name="first_name", lookup_expr="icontains")
    last_name = django_filters.CharFilter(label="Фамилия", field_name="last_name", lookup_expr="icontains")
    lead_quality = django_filters.ChoiceFilter(field_name="lead_quality",
                                               choices=((-2, "Отказ"), (-1, "Недозвон"), (0, "Новый"), (1, "Интересно"), (2, "Другая Вакансия"), (3, "Приоритет"), (4,"Сделка")))
    comment = django_filters.CharFilter(label="Дополнительно", field_name="comment", lookup_expr="icontains")
    source = django_filters.ChoiceFilter(label="Источник", field_name="source", choices=[(c.id, c.name) for c in ContactSource.objects.all()])
    interaction__result = django_filters.CharFilter(label="Взаимодействие", lookup_expr="icontains")
    profiles__name = django_filters.MultipleChoiceFilter(label="Професия", lookup_expr="icontains", distinct=True,
                                                         choices=[(c.name, c.name) for c in SkillProfile.objects.all()])

    class Meta:
        model = Contact
        fields = {
            "viber" : ["icontains"],
        }

