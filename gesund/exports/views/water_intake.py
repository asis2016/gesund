import xlsxwriter
from django.http import HttpResponse
from io import BytesIO
from water_intake.models import WaterIntake


def export_water_intake(request):
    """ Export water intake records into excel. """
    output = BytesIO()
    workbook = xlsxwriter.Workbook(output, {'in_memory': True})
    bold = workbook.add_format({'bold': True})

    worksheet = workbook.add_worksheet('Water intake')

    water_intake = WaterIntake.objects.filter(author=request.user)

    row = 1
    col = 0

    for i in water_intake:
        worksheet.write(row, col, i.id)
        worksheet.write(row, col + 1, i.author.id)
        worksheet.write(row, col + 2, str(i.datestamp))
        worksheet.write(row, col + 3, i.drink_progress)
        row += 1

    worksheet.write('A1', 'id', bold)
    worksheet.write('B1', 'author_id', bold)
    worksheet.write('C1', 'Date', bold)
    worksheet.write('D1', 'Drank', bold)

    workbook.close()

    output.seek(0)
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment;filename="my_data_water_intake.xlsx"'
    response.write(output.read())

    return response
