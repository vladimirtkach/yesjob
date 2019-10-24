import django_filters


from employer.models import Vacancy
from .models import Contact, ContactSource, SkillProfile

class ContactFilter(django_filters.FilterSet):
    start_date = django_filters.DateFilter(field_name='next_contact_date', lookup_expr=('gt'), label="Сл. звонок с")
    end_date = django_filters.DateFilter(field_name='next_contact_date', lookup_expr=('lt'), label="Сл. звонок до")
    phone_main = django_filters.CharFilter(label="Телефон", field_name="phone_main", lookup_expr="icontains")
    phone2 = django_filters.CharFilter(label="Телефон 2", field_name="phone2", lookup_expr="icontains")
    viber = django_filters.CharFilter(label="Вайбер", field_name="viber", lookup_expr="icontains")
    telegram = django_filters.CharFilter(label="Телеграм", field_name="telegram", lookup_expr="icontains")
    city = django_filters.CharFilter(label="Город", field_name="city", lookup_expr="icontains")
    email = django_filters.CharFilter(label="Имейл", field_name="email", lookup_expr="icontains")
    first_name = django_filters.CharFilter(label="Имя", field_name="first_name", lookup_expr="icontains")
    last_name = django_filters.CharFilter(label="Фамилия", field_name="last_name", lookup_expr="icontains")
    lead_quality = django_filters.ChoiceFilter(field_name="lead_quality",
                                               choices=((-2, "Отказ"), (-1, "Недозвон"), (0, "Новый"), (1, "Интересно но позже"), (2, "Другая Вакансия"), (3, "Приоритет"), (4,"Сделка")))
    comment = django_filters.CharFilter(label="Дополнительно", field_name="comment", lookup_expr="icontains")
    source = django_filters.ChoiceFilter(label="Источник", field_name="source", choices=[(c.id, c.name) for c in ContactSource.objects.all()])
    interaction__result = django_filters.CharFilter(label="Взаимодействие", lookup_expr="icontains")
    cv_title = django_filters.CharFilter(label="Резюме", field_name="cv_title", lookup_expr="icontains")
    profiles__name = django_filters.ModelMultipleChoiceFilter(label="Професия", lookup_expr="icontains", distinct=True, queryset=SkillProfile.objects.all())
    proposed_vacancy__id = django_filters.MultipleChoiceFilter(label="Предложенные вакансии", lookup_expr="icontains", distinct=True,
                                                         choices=[(c.id, c.position_title) for c in Vacancy.objects.all()])
    is_pair = django_filters.BooleanFilter(label="Семейная пара", field_name="is_pair", lookup_expr="exact")
    is_client = django_filters.BooleanFilter(label="Уже клиент", field_name="is_client", lookup_expr="exact")

    class Meta:
        model = Contact
        exclude = ["color", "created_at", "updated_at", "last_contact_date", "next_contact_date",
                   "agent", "in_sales", "cv_url", "proposed_vacancy", "profiles"]


class ContactFilterSuperAgent(ContactFilter):

    class Meta:
        model = Contact
        fields = ["agent"]