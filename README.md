# 3HF Website

Website repository for the hearts and hands humanitarian [project](https://github.com/users/iamogbz/projects/2/views/1).

## Development

- `npm install`
- `python -m venv venv`
  - `. venv/bin/activate`
- `pip install -r requirements.txt`
- Run migrations
  - `python -m manage makemigrate`
  - `python -m manage migrate`
- `python -m manage runserver`

## Deployment

- Merge to `main` to deploy website changes

## Database

- TODO: Create ci action to store database file everyday as artifact

## Logs

- File manager > Logs > passenger.logs
