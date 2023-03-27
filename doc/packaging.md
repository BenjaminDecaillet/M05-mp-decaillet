# Packaging
If you do not have a ".pypirc" file in your HOME directory. You need to create a ".pypirc" file in your root folder that contains the following :<br/>
[distutils]<br/>
index-servers =<br/>
pypi<br/>
testpypi<br/>
[pypi]<br/>
username = your_PyPi_username<br/>
password = your_PyPi_password<br/>
[testpypi]<br/>
username = your_test_PyPi_username<br/>
password = your_test_PyPi_password<br/>


```bash
rmd -rf dist decm05.egg-info
python setup.py sdist
twine check dist/*
twine upload -r testpypi dist\decm05* --config-file ./.pypirc
```

```winbatch
rmdir dist decm05.egg-info /S/Q
python setup.py sdist
twine check dist/*
twine upload -r testpypi dist\decm05* --config-file ./.pypirc
```