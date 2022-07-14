from weights.models import Weight
from profiles.models import Profile


def get_bmi(user):
    """ BMI calculation util. """

    # weight_obj = Weight.objects.filter(author=user).last()
    height_obj = Profile.objects.filter(author=user).last()

    # if author has weight
    if (Weight.objects.filter(author=user)):
        weight_obj = Weight.objects.filter(author=user).latest('datestamp')

        # if weight_obj is None, height_obj is None, and height_obj.height
        if (weight_obj is not None) and (height_obj is not None) and (height_obj.height):
            bmi = round(weight_obj.weight / ((height_obj.height * 0.01) ** 2))
        else:
            bmi = 'Unset'
    else:
        bmi = 'Unset'
    return bmi


def get_bmi_interpretation(x):
    """ get bmi interpretation util. """
    """
    BMI interpretation
    - BMI <18.5             Below normal weight
    - BMI >=18.5 and <25    Normal weight
    - BMI >=25 and <30      Overweight
    - BMI >=30 and <35      Class I obesity
    - BMI >=35 and <40      Class II obesity
    - BMI >=40              Clas III Obesity
    """
    bmi = x
    if bmi == 'Unset':
        result = ''
    else:
        if bmi < 18.5:
            result = 'Below Normal Weight'
        elif 18.5 <= bmi < 25:
            result = 'Normal Weight'
        elif 25 <= bmi < 30:
            result = 'Overweight'
        elif 30 <= bmi < 35:
            result = 'Class I Obesity'
        elif 35 <= bmi < 40:
            result = 'Class II Obesity'
        elif bmi >= 40:
            result = 'Class III Obesity'
    return result
