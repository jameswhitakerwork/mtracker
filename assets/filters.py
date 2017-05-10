import django_filters
from django_filters import ChoiceFilter, BooleanFilter
from .models import *
from hr.models import Staff

class AssetFilter(django_filters.FilterSet):
    os = Office.objects.all()
    OFFICE_CHOICES = ((o.id, o.name) for o in os)

    ps = Program.objects.all()
    PROGRAM_CHOICES = ((p.id, p.name) for p in ps)

    ts = AssetType.objects.all()
    ASSETTYPE_CHOICES = ((t.id, t.name) for t in ts)

    ss = Staff.objects.all()
    STAFF_CHOICES = ((s.id, s.__unicode__()) for s in ss)

    office_filter = ChoiceFilter(
        label='Office',
        method='filter_office',
        choices=OFFICE_CHOICES
    )

    program_filter = ChoiceFilter(
        label='Program',
        method='filter_program',
        choices=PROGRAM_CHOICES
    )

    assettype_filter = ChoiceFilter(
        label='Asset Type',
        method='filter_assettype',
        choices=ASSETTYPE_CHOICES
    )

    staff_filter = ChoiceFilter(
        label='Staff',
        method='filter_staff',
        choices=STAFF_CHOICES
    )

    def filter_office(self, queryset, name, value):
        return queryset.filter(office__id=value)

    def filter_program(self, queryset, name, value):
        return queryset.filter(program__id=value)

    def filter_assettype(self, queryset, name, value):
        return queryset.filter(asset_type__id=value)

    def filter_staff(self, queryset, name, value):
        q_ids = [s.id for s in queryset if s.assigned() == value]
        return queryset.filter(id__in=q_ids)

    class Meta:
        object = Asset
        exclude = ['', ]
