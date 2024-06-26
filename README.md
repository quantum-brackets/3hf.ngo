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
- Static files
  - `python -m manage collectstatic`

## Deployment

[![Website](https://github.com/hengage/hearts-and-hands/actions/workflows/deployment.yml/badge.svg)](https://github.com/hengage/hearts-and-hands/actions/workflows/deployment.yml)

- Merge to `main` to deploy website changes

## Database

[![Backup](https://github.com/hengage/hearts-and-hands/actions/workflows/database.yml/badge.svg)](https://github.com/hengage/hearts-and-hands/actions/workflows/database.yml)

- Backed up as a repository artifact, on every deployment and daily at 12am.
- All DB schema changes should be [N-1 compatible](https://stackoverflow.blog/2020/05/13/ensuring-backwards-compatibility-in-distributed-systems/)

## Logs

- [`File manager > Logs > passenger.logs`](https://3hf.ngo:2083/cpsess2857681328/frontend/jupiter/filemanager/showfile.html?file=passenger.log&fileop=&dir=%2Fhome%2Fhnhhfoun%2Flogs&dirop=&charset=&file_charset=&baseurl=&basedir=)
