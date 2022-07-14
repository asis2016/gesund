def progress_level_percentage(percentage):
    """ Progess percentage util.
    - 0-33   red
    - 34-66  yellow
    - 67-100 green
    """
    _percentage = int(percentage)
    if 0 < _percentage <= 33:
        level = 'danger'
    elif 34 <= _percentage <= 66:
        level = 'warning'
    elif _percentage >= 67:
        level = 'success'
    else:
        level = 'none'
    return level
