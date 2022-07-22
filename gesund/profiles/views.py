from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView
from utils import get_age, get_bmi, get_bmi_interpretation, get_total_xp
from weights.models import Weight

from .models import Profile


class ProfileTemplateView(TemplateView):
    """ Profile templateview. """
    template_name = 'profiles/index.html'

    def get_initials(self):
        """ Get name initials. """
        full_name = Profile.objects.filter(author=self.request.user).last().name
        if full_name:
            name_list = full_name.split()
            initials = ""
            for name in name_list:
                initials += name[0].upper()
        else:
            initials = ""
        return initials

    def get_context_data(self, *args, **kwargs):
        context = super(ProfileTemplateView, self).get_context_data(*args, **kwargs)
        context['name_initials'] = self.get_initials()
        # get all records filtered by author
        context['profile_list'] = Profile.objects.all().filter(author=self.request.user)
        # gets first record filtered by author
        context['profile_obj'] = Profile.objects.filter(author=self.request.user).last()
        context['profile_obj_age'] = get_age(self.request.user)

        bmi = get_bmi(self.request.user)
        context['profile_obj_bmi'] = bmi
        context['profile_obj_bmi_interpretation'] = get_bmi_interpretation(bmi)
        context['total_xp'] = get_total_xp(self.request.user)

        context['weight_obj'] = Weight.objects.filter(author=self.request.user).last()

        return context


class ProfileUpdateView(UpdateView):
    """ Update profile. """
    model = Profile
    context_object_name = 'profile_obj'
    template_name = 'profiles/update.html'
    fields = ('name', 'dob', 'gender', 'height')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
