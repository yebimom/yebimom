find . -name '*.py' -exec autopep8 --in-place --verbose --aggressive --aggressive '{}' \;
find . -name '*.py' -exec pep8 --verbose '{}' \;
