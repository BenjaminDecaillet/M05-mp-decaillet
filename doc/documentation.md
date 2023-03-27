# Documentation

This projects uses [sphinx](https://www.sphinx-doc.org/en/master/) to generate its documentation.

## Generate sphinx doc locally
* activate your virtualenv: `workon m05-mp-decaillet`
* remove previously auto-generated doc (if any):
  - on OSX and Linux: `rm -rf ./doc/apidoc`
  - on windows: `rmdir /S/Q .\doc\apidoc`
* build doc:
  ```bash
  sphinx-apidoc decm05/ -o ./doc/apidoc --no-toc --separate --module-first
  sphinx-build doc sphinx
  ```
* open generated file **sphinx/index.html** in your web browser

## Deployment to github pages
On branch `main`, [GitHub actions](https://github.com/master-ai-batch5/M05-mp-decaillet/actions/workflows/main.yml) will auto-deploy
doc to [Github pages](https://master-ai-batch5.github.io/M05-mp-decaillet/) (docs from other branches are not deployed until merged
to `main` - see [contributing](contributing.md))
