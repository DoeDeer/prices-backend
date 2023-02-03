FROM python:3.10-alpine

# Set working directory and copy sources
WORKDIR /home/prices
COPY . .

# Install dependecies
RUN pip install -r requirements.txt

# Set run environment
ENV APP_PORT=8000
ENV APP_HOST=0.0.0.0
ENV APP_WORKERS=1

# Run app
CMD uvicorn app.main:app --host $APP_HOST --port $APP_PORT --workers $APP_WORKERS
