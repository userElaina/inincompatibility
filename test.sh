pandoc --from=markdown --to=rst --output=README.rst README.md

rm -rf dist
py -m build
twine check dist/*
twine upload --repository testpypi dist/* --verbose

# test

twine upload dist/* --verbose
