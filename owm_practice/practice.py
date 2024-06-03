from pyowm import OWM
from config import KEY
# from pyowm.utils import config
# from pyowm.utils import timestamps

# ---------- FREE API KEY examples ---------------------

owm = OWM(KEY)
mgr = owm.weather_manager()


# Search for current weather in London (Great Britain) and get details
observation = mgr.weather_at_place(input("Enter your city: "))

w = observation.weather

print(w.detailed_status)
print(w.wind())
print(w.humidity)
print(w.temperature('celsius'))
print(w.rain)
print(w.heat_index)
print(w.clouds)
print(w.sunset_time())
