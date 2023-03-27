# Packaging

This project is deployed to [test.pypi.org as "decm05"](https://test.pypi.org/project/decm05/).

[GitHub actions](https://github.com/master-ai-batch5/M05-mp-decaillet/actions/workflows/main.yml) ensure the automatic deployment of tagged commits. TODO - in fact, not yet...

## Deployment from a local machine

1. Create a .pypirc at project root, per example below:
    ```
    [distutils]
    index-servers = testpypi
    [testpypi]
    username = <your username>
    password = <your password>
    ```

2. activate your virtualenv:
    ```
    conda activate m05-mp-decaillet
    ```

3. set an env variable with the package version:
   ```bash
   export VERSION=0.0.0
   ```

4. If needed, remove local egg from previous run:
   - on OSX and linux: `rm -rf dist decm05.egg-info`
   - on Windows: `rmdir dist decm05.egg-info /`

5. Generate the egg locally:
    ```bash
    python setup.py sdist
    twine check dist/*
    ```
    (Note the content of folder "dist")

6. Upload the egg to test.pypi:
    - on OSX and linux: `twine upload -r testpypi dist/decm05* --config-file .pypirc`
    - on Windows: `twine upload -r testpypi dist\decm05* --config-file .pypirc`
