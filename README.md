# WeatherGetter
For a project i needed a CSV file containing last 15 years of weather data of Istanbul containing minimum temperature, date and snow amount. This is a simple script written for getting the data from weatherstack as JSON, cleaning it and saving it as a CSV file.

Weatherstack supports "get requests" within the period of max 30 days. That is why i needed to send multiple requests and then append them together.
