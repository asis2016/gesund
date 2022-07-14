import xlsxwriter
from django.http import HttpResponse
from io import BytesIO
from weights.models import Weight


def export_weights(request):
    """ Export weights records into excel. """
    output = BytesIO()
    workbook = xlsxwriter.Workbook(output, {'in_memory': True})
    bold = workbook.add_format({'bold': True})

    worksheet = workbook.add_worksheet('weights')

    weights = Weight.objects.filter(author=request.user)

    row = 1
    col = 0

    for weight in weights:
        worksheet.write(row, col, weight.id)
        worksheet.write(row, col + 1, weight.author.id)
        worksheet.write(row, col + 2, str(weight.datestamp))
        worksheet.write(row, col + 3, weight.weight)
        row += 1

    worksheet.write('A1', 'id', bold)
    worksheet.write('B1', 'author_id', bold)
    worksheet.write('C1', 'Date', bold)
    worksheet.write('D1', 'Weight', bold)

    workbook.close()

    output.seek(0)
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment;filename="my_data_weights.xlsx"'
    response.write(output.read())

    return response
