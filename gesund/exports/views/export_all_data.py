import xlsxwriter
from calories.models import CalorieIntake
from django.http import HttpResponse
from goals.models import Goals
from history.models import History
from io import BytesIO
from profiles.models import Profile
from steps.models import Steps
from water_intake.models import WaterIntake
from weights.models import Weight
from xps.models import XP


def calories(workbook, user, bold):
    ''' Calories. '''
    worksheet_calories = workbook.add_worksheet('Calories intake')

    calories_intake = CalorieIntake.objects.filter(author=user)

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


def goals(workbook, user, bold):
    ''' Goals. '''
    worksheet_goals = workbook.add_worksheet('Goals')

    goals = Goals.objects.filter(author=user)

    row = 1
    col = 0

    for goal in goals:
        worksheet_goals.write(row, col, goal.id)
        worksheet_goals.write(row, col + 1, goal.author.id)
        worksheet_goals.write(row, col + 2, goal.calories)
        worksheet_goals.write(row, col + 3, goal.steps)
        worksheet_goals.write(row, col + 4, goal.water)
        worksheet_goals.write(row, col + 5, goal.weight)
        row += 1

    worksheet_goals.write('A1', 'id', bold)
    worksheet_goals.write('B1', 'author_id', bold)
    worksheet_goals.write('C1', 'Calories', bold)
    worksheet_goals.write('D1', 'Steps', bold)
    worksheet_goals.write('E1', 'Water', bold)
    worksheet_goals.write('F1', 'Weight', bold)


def history(workbook, user, bold):
    ''' History. '''
    worksheet_history = workbook.add_worksheet('History')

    history = History.objects.filter(author=user)

    row = 1
    col = 0

    for i in history:
        worksheet_history.write(row, col, i.id)
        worksheet_history.write(row, col + 1, i.author.id)
        worksheet_history.write(row, col + 2, str(i.datestamp))
        worksheet_history.write(row, col + 3, i.app)
        worksheet_history.write(row, col + 4, i.action)
        worksheet_history.write(row, col + 5, i.description)
        row += 1

    worksheet_history.write('A1', 'id', bold)
    worksheet_history.write('B1', 'author_id', bold)
    worksheet_history.write('C1', 'Date', bold)
    worksheet_history.write('D1', 'App', bold)
    worksheet_history.write('E1', 'Action', bold)
    worksheet_history.write('F1', 'Description', bold)


def profile(workbook, user, bold):
    ''' Profile. '''
    worksheet_profile = workbook.add_worksheet('Profile')

    profile = Profile.objects.filter(author=user)

    row = 1
    col = 0

    for i in profile:
        worksheet_profile.write(row, col, i.id)
        worksheet_profile.write(row, col + 1, i.name)
        worksheet_profile.write(row, col + 2, str(i.dob))
        worksheet_profile.write(row, col + 3, i.gender)
        worksheet_profile.write(row, col + 4, i.height)
        row += 1

    worksheet_profile.write('A1', 'id', bold)
    worksheet_profile.write('B1', 'Name', bold)
    worksheet_profile.write('C1', 'DOB', bold)
    worksheet_profile.write('D1', 'Gender', bold)
    worksheet_profile.write('E1', 'Height', bold)


def steps(workbook, user, bold):
    ''' Steps. '''
    worksheet_steps = workbook.add_worksheet('Steps')

    steps = Steps.objects.filter(author=user)

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


def water_intake(workbook, user, bold):
    ''' Water intake. '''
    worksheet = workbook.add_worksheet('Water intake')

    water_intake = WaterIntake.objects.filter(author=user)

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


def weights(workbook, user, bold):
    ''' Weights. '''
    worksheet = workbook.add_worksheet('weights')

    weights = Weight.objects.filter(author=user)

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


def xps(workbook, user, bold):
    ''' XPs. '''
    worksheet = workbook.add_worksheet('xps')

    xps = XP.objects.filter(author=user)

    row = 1
    col = 0

    for xp in xps:
        worksheet.write(row, col, xp.id)
        worksheet.write(row, col + 1, xp.author.id)
        worksheet.write(row, col + 2, str(xp.datestamp))
        worksheet.write(row, col + 3, xp.xp)
        row += 1

    worksheet.write('A1', 'id', bold)
    worksheet.write('B1', 'author_id', bold)
    worksheet.write('C1', 'Date', bold)
    worksheet.write('D1', 'Experience Points (xps)', bold)


def export_data(request):
    """ Exporting data to excel. """
    output = BytesIO()
    workbook = xlsxwriter.Workbook(output, {'in_memory': True})
    bold = workbook.add_format({'bold': True})

    calories(workbook, request.user, bold)
    goals(workbook, request.user, bold)
    history(workbook, request.user, bold)
    profile(workbook, request.user, bold)
    steps(workbook, request.user, bold)
    water_intake(workbook, request.user, bold)
    weights(workbook, request.user, bold)
    xps(workbook, request.user, bold)

    workbook.close()

    output.seek(0)
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment;filename="my_data.xlsx"'
    response.write(output.read())

    return response
