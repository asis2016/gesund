import xlsxwriter
from calories.models import CalorieIntake
from django.http import HttpResponse
from goals.models import Goals
from history.models import History
from io import BytesIO
from pomodoros.models import Pomodoro
from profiles.models import Profile
from steps.models import Steps
from water_intake.models import WaterIntake
from weights.models import Weight
from xps.models import XP


def calories(workbook, user, bold):
    ''' Calories. '''
    worksheet = workbook.add_worksheet('Calories intake')

    calories_intake = CalorieIntake.objects.filter(author=user)

    row = 1
    col = 0

    for i in calories_intake:
        worksheet.write(row, col, i.id)
        worksheet.write(row, col + 1, i.author.id)
        worksheet.write(row, col + 2, str(i.datestamp))
        worksheet.write(row, col + 3, i.food)
        worksheet.write(row, col + 4, i.consume)
        worksheet.write(row, col + 5, i.description)
        worksheet.write(row, col + 6, i.calories)
        worksheet.write(row, col + 7, i.protein)
        worksheet.write(row, col + 8, i.fat)
        worksheet.write(row, col + 9, i.carb)
        worksheet.write(row, col + 10, i.sugar)
        worksheet.write(row, col + 11, i.fiber)
        worksheet.write(row, col + 12, str(i.food_detail_ref))
        row += 1

    worksheet.write('A1', 'id', bold)
    worksheet.write('B1', 'author_id', bold)
    worksheet.write('C1', 'Date', bold)
    worksheet.write('D1', 'Food', bold)
    worksheet.write('E1', 'Consumed', bold)
    worksheet.write('F1', 'Description', bold)
    worksheet.write('G1', 'Calories (cal)', bold)
    worksheet.write('H1', 'Protein (gm)', bold)
    worksheet.write('I1', 'Fat (gm)', bold)
    worksheet.write('J1', 'Carbs (gm)', bold)
    worksheet.write('K1', 'Sugar (gm)', bold)
    worksheet.write('L1', 'Fiber (gm)', bold)
    worksheet.write('M1', 'food_ref', bold)


def goals(workbook, user, bold):
    ''' Goals. '''
    worksheet = workbook.add_worksheet('Goals')

    goals = Goals.objects.filter(author=user)

    row = 1
    col = 0

    for goal in goals:
        worksheet.write(row, col, goal.id)
        worksheet.write(row, col + 1, goal.author.id)
        worksheet.write(row, col + 2, goal.calories)
        worksheet.write(row, col + 3, goal.steps)
        worksheet.write(row, col + 4, goal.water)
        worksheet.write(row, col + 5, goal.weight)
        row += 1

    worksheet.write('A1', 'id', bold)
    worksheet.write('B1', 'author_id', bold)
    worksheet.write('C1', 'Calories', bold)
    worksheet.write('D1', 'Steps', bold)
    worksheet.write('E1', 'Water', bold)
    worksheet.write('F1', 'Weight', bold)


def history(workbook, user, bold):
    ''' History. '''
    worksheet = workbook.add_worksheet('History')

    history = History.objects.filter(author=user)

    row = 1
    col = 0

    for i in history:
        worksheet.write(row, col, i.id)
        worksheet.write(row, col + 1, i.author.id)
        worksheet.write(row, col + 2, str(i.datestamp))
        worksheet.write(row, col + 3, i.app)
        worksheet.write(row, col + 4, i.action)
        worksheet.write(row, col + 5, i.description)
        row += 1

    worksheet.write('A1', 'id', bold)
    worksheet.write('B1', 'author_id', bold)
    worksheet.write('C1', 'Date', bold)
    worksheet.write('D1', 'App', bold)
    worksheet.write('E1', 'Action', bold)
    worksheet.write('F1', 'Description', bold)


def pomodoro(workbook, user, bold):
    ''' Pomodoros. '''
    worksheet = workbook.add_worksheet('Pomodoro')

    pomodoros = Pomodoro.objects.filter(author=user)

    row = 1
    col = 0

    for i in pomodoros:
        worksheet.write(row, col, i.id)
        worksheet.write(row, col + 1, i.author.id)
        worksheet.write(row, col + 2, str(i.datestamp))
        worksheet.write(row, col + 3, str(i.timestamp))
        worksheet.write(row, col + 4, i.pomodoro)
        worksheet.write(row, col + 5, i.short_break)
        worksheet.write(row, col + 6, i.long_break)
        row += 1

    worksheet.write('A1', 'id', bold)
    worksheet.write('B1', 'author_id', bold)
    worksheet.write('C1', 'Date', bold)
    worksheet.write('D1', 'Time', bold)
    worksheet.write('E1', 'Pomodoro (1 pomodoro = 25 mins)', bold)
    worksheet.write('F1', 'Short breaks', bold)
    worksheet.write('G1', 'Logn breaks', bold)


def profile(workbook, user, bold):
    ''' Profile. '''
    worksheet = workbook.add_worksheet('Profile')

    profile = Profile.objects.filter(author=user)

    row = 1
    col = 0

    for i in profile:
        worksheet.write(row, col, i.id)
        worksheet.write(row, col + 1, i.name)
        worksheet.write(row, col + 2, str(i.dob))
        worksheet.write(row, col + 3, i.gender)
        worksheet.write(row, col + 4, i.height)
        row += 1

    worksheet.write('A1', 'id', bold)
    worksheet.write('B1', 'Name', bold)
    worksheet.write('C1', 'DOB', bold)
    worksheet.write('D1', 'Gender', bold)
    worksheet.write('E1', 'Height', bold)


def steps(workbook, user, bold):
    ''' Steps. '''
    worksheet = workbook.add_worksheet('Steps')

    steps = Steps.objects.filter(author=user)

    row = 1
    col = 0

    for step in steps:
        worksheet.write(row, col, step.id)
        worksheet.write(row, col + 1, step.author.id)
        worksheet.write(row, col + 2, str(step.datestamp))
        worksheet.write(row, col + 3, step.step_count)
        row += 1

    worksheet.write('A1', 'id', bold)
    worksheet.write('B1', 'author_id', bold)
    worksheet.write('C1', 'Date', bold)
    worksheet.write('D1', 'Total steps taken', bold)


def water(workbook, user, bold):
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

    profile(workbook, request.user, bold)
    goals(workbook, request.user, bold)
    calories(workbook, request.user, bold)
    steps(workbook, request.user, bold)
    water(workbook, request.user, bold)
    pomodoro(workbook, request.user, bold)
    weights(workbook, request.user, bold)
    xps(workbook, request.user, bold)
    history(workbook, request.user, bold)

    workbook.close()

    output.seek(0)
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment;filename="my_data.xlsx"'
    response.write(output.read())

    return response
