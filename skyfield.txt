from datetime import datetime, timezone, timedelta
from skyfield.api import EarthSatellite, Topos, load

# 1. PASTE YOUR HACK THE BOX TLE DATA HERE
# Ensure there are no leading/trailing spaces in the strings
line1 = "1 01337U 00000A   26292.65875000  .00000000  00000-0  14138-3 0  6106"
line2 = "2 01337  15.3732 181.5679 0096198  49.9826 256.4271 15.30311411360786"
sat_name = "DIGITWIN HTB"

# 2. DEFINE THE GROUND STATION (Update with your challenge's Lat/Long)
# Skyfield handles degrees directly.
station_lat = -0.46665441303989996   # Positive for North, Negative for South
station_lon = 31.454850051819996  # Positive for East, Negative for West
ground_station = Topos(latitude_degrees=station_lat, longitude_degrees=station_lon)

# 3. LOAD THE SATELLITE
ts = load.timescale()
satellite = EarthSatellite(line1, line2, sat_name, ts)

# 4. SET THE TIME WINDOW TO SEARCH (e.g., From now until 48 hours later)
# If the CTF challenge specifies a starting epoch time, parse it here instead of UTC now.
start_time = ts.from_datetime(datetime.now(timezone.utc))
end_time = ts.from_datetime(datetime.now(timezone.utc) + timedelta(days=1))

# 5. FIND THE PASSES
# 'find_events' returns arrays of times and event types:
# 0 = Rise (AOS), 1 = Peak/Culmination, 2 = Set (LOS)
# The 3rd parameter (0.0) is the minimum elevation angle (horizon is 0 degrees)
t_events, events = satellite.find_events(ground_station, start_time, end_time, altitude_degrees=0.0)

#print(f"--- Upcoming Visible Passes for {sat_name} ---")
for ti, event_type in zip(t_events, events):
#    event_name = ('Rise (AOS)', 'Culmination (Peak)', 'Set (LOS)')[event_type]
    # Format the time output clearly
#    print(f"{ti.utc_iso()} Z | {event_name}")
    print("{ti.utc_iso()} ")
