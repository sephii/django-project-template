#!/usr/bin/env python
import os
import sys

from {{ project_name }} import get_project_root_path, import_env_vars


# Add the site ID CLI arg to the environment, which allows for the site
# used in any site related queries to be manually set for management
# commands.
for i, arg in enumerate(sys.argv):
    if arg.startswith("--site"):
        os.environ["MEZZANINE_SITE_ID"] = arg.split("=")[1]
        sys.argv.pop(i)

if __name__ == "__main__":
    if 'test' in sys.argv:
        env_dir = os.path.join('envdir', 'tests')
    else:
        env_dir = os.path.join('envdir', 'local')

    import_env_vars(os.path.join(get_project_root_path(), env_dir))

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "{{ project_name }}.settings.dev")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
