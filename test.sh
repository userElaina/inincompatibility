py -m build
twine check dist/*
twine upload --repository testpypi dist/* --verbose

# test

twine upload dist/* --verbose
