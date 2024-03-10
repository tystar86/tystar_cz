# tystar_cz
 
http://getskeleton.com/
https://pre-commit.com/
https://djecrety.ir/, https://gist.github.com/jbothma/8a9a30399c2091d89763bff0a1952da4
https://pipenv-fork.readthedocs.io/en/latest/basics.html#a-note-about-vcs-dependencies
https://django-extensions.readthedocs.io/en/latest/field_extensions.html
https://ckeditor.com/


https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Generic_views
https://docs.djangoproject.com/en/5.0/




# tystar.cz
Application is using Django and Postgres.
## Installation
This and following sections cover local installation & development.
Setup your python environment using [Pipenv](https://docs.pipenv.org/) and install requirements.
```pipenv install```
# To setup code formatting on commit
```pipenv run pre-commit install```
Then you can activate virtualenv using `pipenv shell` or run commands using `pipenv run`.
Copy and fill in environment variables.
```cp .env.example .env```
Initialize database.
```createdb tystar_cz```
```pipenv run migrate```
## Development
Start the server process.
```pipenv run app```
### Tests
```pipenv run pytest```