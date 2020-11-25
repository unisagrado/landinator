import csv
import io
from django.utils.timezone import datetime
from django.http.response import HttpResponse

import xlsxwriter


class ExportMixin:
    TYPES = {
        'csv': 'application/csv;charset=windows-1252',
        'xlsx': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    }

    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        response = self.get_response('csv')

        writer = csv.writer(response, delimiter=";", dialect=csv.excel)
        writer.writerow([field.verbose_name for field in meta.fields])
        for obj in queryset:
            attrs = [getattr(obj, field.name) for field in meta.fields]
            writer.writerow(self._get_data(attr) for attr in attrs)
        return response

    export_as_csv.short_description = 'Exportar csv'

    def export_xlsx(self, request, queryset):
        meta = self.model._meta
        fields = [field.verbose_name for field in meta.fields]

        output = io.BytesIO()

        workbook = xlsxwriter.Workbook(
            output, {'in_memory': True, 'remove_timezone': True})
        worksheet = workbook.add_worksheet()

        for col, field_name in enumerate(fields):
            worksheet.write(0, col, field_name.capitalize())

        for row, obj in enumerate(queryset, start=1):
            attrs = (getattr(obj, field.name) for field in meta.fields)
            for col, attr in enumerate(attrs):
                worksheet.write(row, col, self._get_data(attr))

        workbook.close()
        output.seek(0)
        response = self.get_response('xlsx')
        response.write(output.read())
        return response

    export_xlsx.short_description = 'Exportar para excel'

    def _get_data(self, obj):
        if type(obj) is bool:
            if obj:
                return 'Sim'
            return 'Não'
        return str(obj)

    def get_response(self, type):
        current_time = datetime.now().timestamp()
        filename = '{}.{}'.format(current_time, type)
        content_type = self.TYPES.get(type)
        response = HttpResponse(content_type=content_type)
        response['Content-Disposition'] = 'attachment; filename={}'.format(
            filename)
        return response
