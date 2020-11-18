import csv
from django.utils.timezone import datetime
from django.http.response import HttpResponse


class ExportCsvMixin:
    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        filename = datetime.now().timestamp()

        response = HttpResponse(
            content_type='application/csv;charset=windows-1252')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(
            filename)
        writer = csv.writer(response, delimiter=";", dialect=csv.excel)

        writer.writerow([field.verbose_name for field in meta.fields])
        for obj in queryset:
            writer.writerow([getattr(obj, field.name)
                             for field in meta.fields])
        return response

    export_as_csv.short_description = 'Exportar para excel'
