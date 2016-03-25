import os


def get_template(name):
    """Utils to load default framework template."""
    base_dir = os.path.dirname(__file__)
    template_file = os.path.join(base_dir, 'templates', name)
    if not os.path.exists(template_file) and os.path.isfile(template_file):
        raise LookupError('Template not found.')
    return template_file

