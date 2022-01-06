import django_filters

from users.models import Transaction


class TransactionFilter(django_filters.FilterSet):

    def __init__(self, data=None, *args, **kwargs):
        if data is not None:
            data = data.copy()
            for name, f in self.base_filters.items():
                initial = f.extra.get('initial')
                if not data.get(name) and initial:
                    data[name] = initial
        super().__init__(data, *args, **kwargs)

    created_at_to = django_filters.IsoDateTimeFilter(field_name="created_at", lookup_expr="lt", label='created_at To')
    created_at_from = django_filters.IsoDateTimeFilter(
        field_name="created_at", lookup_expr="gte", label='created_at From'
    )

    class Meta:
        model = Transaction
        fields = ['created_at_to', 'created_at_from', ]
