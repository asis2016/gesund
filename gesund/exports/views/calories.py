import xlsxwriter
from calories.models import CalorieIntake
from django.http import HttpResponse
from io import BytesIO


def export_calories(request):
    """ Export calories intake records into excel. """
    output = BytesIO()
    workbook = xlsxwriter.Workbook(output, {'in_memory': True})
    bold = workbook.add_format({'bold': True})

    worksheet_calories = workbook.add_worksheet('Calories intake')

    calories_intake = CalorieIntake.objects.filter(author=request.user)

    row = 1
    col = 0

    for i in calories_intake:
        worksheet_calories.write(row, col, i.id)
        worksheet_calories.write(row, col + 1, i.author.id)
        worksheet_calories.write(row, col + 2, str(i.datestamp))
        worksheet_calories.write(row, col + 3, i.food)
        worksheet_calories.write(row, col + 4, i.consume)
        worksheet_calories.write(row, col + 5, i.description)
        worksheet_calories.write(row, col + 6, i.calories)
        worksheet_calories.write(row, col + 7, i.protein)
        worksheet_calories.write(row, col + 8, i.fat)
        worksheet_calories.write(row, col + 9, i.carb)
        worksheet_calories.write(row, col + 10, i.sugar)
        worksheet_calories.write(row, col + 11, i.fiber)
        worksheet_calories.write(row, col + 12, i.food_detail_ref)
        row += 1

    worksheet_calories.write('A1', 'id', bold)
    worksheet_calories.write('B1', 'author_id', bold)
    worksheet_calories.write('C1', 'Date', bold)
    worksheet_calories.write('D1', 'Food', bold)
    worksheet_calories.write('E1', 'Consumed', bold)
    worksheet_calories.write('F1', 'Description', bold)
    worksheet_calories.write('G1', 'Calories (cal)', bold)
    worksheet_calories.write('H1', 'Protein (gm)', bold)
    worksheet_calories.write('I1', 'Fat (gm)', bold)
    worksheet_calories.write('J1', 'Carbs (gm)', bold)
    worksheet_calories.write('K1', 'Sugar (gm)', bold)
    worksheet_calories.write('L1', 'Fiber (gm)', bold)
    worksheet_calories.write('M1', 'food_ref', bold)

    workbook.close()

    output.seek(0)
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment;filename="my_data_calories_intake.xlsx"'
    response.write(output.read())

    return response
