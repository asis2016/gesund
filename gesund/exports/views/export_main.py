from .export_all_data import export_data


def export(request):
    response = export_data(request)
    return response
