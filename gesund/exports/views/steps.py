import xlsxwriter
from django.http import HttpResponse
from io import BytesIO
from steps.models import Steps


def export_steps(request):
    """ Export steps records into excel. """
    output = BytesIO()
    workbook = xlsxwriter.Workbook(output, {'in_memory': True})
    bold = workbook.add_format({'bold': True})

    worksheet_steps = workbook.add_worksheet('Steps')

    steps = Steps.objects.filter(author=request.user)

    row = 1
    col = 0

    for step in steps:
        worksheet_steps.write(row, col, step.id)
        worksheet_steps.write(row, col + 1, step.author.id)
        worksheet_steps.write(row, col + 2, str(step.datestamp))
        worksheet_steps.write(row, col + 3, step.step_count)
        row += 1

    worksheet_steps.write('A1', 'id', bold)
    worksheet_steps.write('B1', 'author_id', bold)
    worksheet_steps.write('C1', 'Date', bold)
    worksheet_steps.write('D1', 'Total steps taken', bold)

    workbook.close()

    output.seek(0)
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment;filename="my_data_steps.xlsx"'
    response.write(output.read())

    return response
