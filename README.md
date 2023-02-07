# Prices Challenge Xeneta

## Project description

### API

This project is a small HTTP REST API that works with freight delivery prices.
It has only 2 routes - `GET /api/v1/prices/` and `POST /api/v1/prices/compare-price/`  
API docs can be found [here](http://127.0.0.1:8000/docs)

#### GET `/api/v1/prices/`
Route for getting freight prices from a given delivery company on a selected date.
Accepts `day` and `customer` parameters as query string. Supports paging by query string parameter `page`  
Example:
```shell
curl -X 'GET' \
  'http://127.0.0.1:8000/api/v1/prices/?day=2016-01-01&page=1&customer=Acme%20Inc.' \
  -H 'accept: application/json'
```
will return something like this:
```json
[
  {
    "orig_code": "CNSGH",
    "dest_code": "BEANR",
    "price": 300,
    "day": "2016-01-01",
    "average": 400,
    "absolute_diff": 100,
    "percent_diff": 25
  },
  {
    "orig_code": "CNSGH",
    "dest_code": "BEZEE",
    "price": 300,
    "day": "2016-01-01",
    "average": 400,
    "absolute_diff": 100,
    "percent_diff": 25
  }
]
```

#### POST `/api/v1/prices/compare-price/`
Route for comparing your delivery price to others in db.  
On its input accepts next parameters:  
- day
- orig_code
- dest_code
- price
- currency  

Currency will be automatically converted into USD using OpenExchangeRates

Example:
```shell
curl -X 'POST' \
  'http://127.0.0.1:8000/api/v1/prices/compare-price/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "orig_code": "CNSGH",
  "dest_code": "BEZEE",
  "price": 7000,
  "day": "2016-01-01",
  "currency": "NOK"
}'
```
will return something like this:
```json
{
  "average": 400,
  "absolute_diff": 273,
  "percent_diff": 68.2
}
```

### Database

Database consists of three tables:

#### Customer

Information about customers that provide their prices, including:

- `id`: in db customer index
- `title`: customer company name

#### Port

Information about ports, including:

- `code`: 5-character port's code
- `name`: port's full name

#### Prices

Individual daily prices between ports, in USD.

- `id`: in db price index
- `orig_code`: 5-character origin port code
- `dest_code`: 5-character destination port code
- `day`: the day for which the price is valid
- `price`: the price in USD
- `customer`: customer's idx

#### Database setup

- create venv and install project dependencies (needed for migrations execution)
- create `.env` file from `.env-example`: `cp .env-example .env` and replace `POSTGRES_` prefixed values with
your own (or leave untouched if you want local run without problems)
- run database sql dump recovery: `psql -U <db username> -d <db database name> < src/postgres/init_script.sql`
- run migrations tool: `alembic upgrade head`

If you're creating a database locally, you can simply use Makefile shortcut: `make run-locacl-db` if docker installed
on your host

## Project local setup

```shell
make run-local
```
Will do all the work for you.

If you want to run tests:
```shell
make run-test
```

Code linting:
```shell
make lint
```
