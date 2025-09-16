import streamlit as st
import requests
from datetime import datetime

st.set_page_config(page_title="Wearther — Weather + Wardrobe", page_icon="🧥", layout="centered")

st.title("🧥 Wearther")
st.write("Type a city, get the 7-day forecast, and smart outfit suggestions.")

# --- Helpers ---
GEO_URL = "https://geocoding-api.open-meteo.com/v1/search"
WX_URL = "https://api.open-meteo.com/v1/forecast"

def geocode_city(city: str):
    """Use Open-Meteo Geocoding to turn a city name into lat/lon."""
    r = requests.get(GEO_URL, params={"name": city, "count": 1, "language": "en", "format": "json"}, timeout=10)
    r.raise_for_status()
    data = r.json()
    if not data.get("results"):
        return None
    top = data["results"][0]
    return {
        "name": top.get("name"),
        "country": top.get("country"),
        "lat": top["latitude"],
        "lon": top["longitude"],
        "timezone": top.get("timezone", "UTC")
    }

def fetch_forecast(lat: float, lon: float, tz: str):
    """Fetch 7-day daily forecast from Open-Meteo (no API key)."""
    params = {
        "latitude": lat,
        "longitude": lon,
        "timezone": tz,
        "daily": [
            "temperature_2m_max",
            "temperature_2m_min",
            "precipitation_sum",
            "windspeed_10m_max"
        ],
        "forecast_days": 7
    }
    # Open-Meteo accepts repeated daily parameters as comma-sep string:
    params["daily"] = ",".join(params["daily"])
    r = requests.get(WX_URL, params=params, timeout=10)
    r.raise_for_status()
    return r.json()

def outfit_advice(tmax, tmin, precip, wind):
    """Very simple rules → a friendly outfit tip."""
    avg = (tmax + tmin) / 2 if (tmax is not None and tmin is not None) else tmax or tmin

    layers = []
    if avg is None:
        return "👕 Dress comfortably."
    if avg >= 28:
        layers.append("🩳 T-shirt & shorts")
    elif avg >= 22:
        layers.append("👕 Light shirt")
    elif avg >= 16:
        layers.append("👕 Long-sleeve + light jacket")
    elif avg >= 8:
        layers.append("🧥 Jacket + jeans")
    else:
        layers.append("🧥 Heavy coat, layers")

    if (precip or 0) >= 5:
        layers.append("🌂 Umbrella/rain jacket")
    if (wind or 0) >= 40:
        layers.append("🧢 Windbreaker")

    return " • ".join(layers)

# --- UI ---
with st.form("search"):
    city = st.text_input("City", placeholder="e.g., Johannesburg")
    go = st.form_submit_button("Get forecast")

if go and city.strip():
    try:
        loc = geocode_city(city.strip())
        if not loc:
            st.warning("Couldn’t find that city. Try another name.")
        else:
            st.success(f"Location: {loc['name']}, {loc['country']}  ·  ({loc['lat']:.2f}, {loc['lon']:.2f})  ·  TZ: {loc['timezone']}")
            data = fetch_forecast(loc["lat"], loc["lon"], loc["timezone"])
            daily = data.get("daily", {})
            dates = daily.get("time", [])
            tmax = daily.get("temperature_2m_max", [])
            tmin = daily.get("temperature_2m_min", [])
            rain = daily.get("precipitation_sum", [])
            wind = daily.get("windspeed_10m_max", [])

            # Table-like cards
            for i, d in enumerate(dates):
                day = datetime.fromisoformat(d).strftime("%a %d %b")
                mx = tmax[i] if i < len(tmax) else None
                mn = tmin[i] if i < len(tmin) else None
                rn = rain[i] if i < len(rain) else None
                wd = wind[i] if i < len(wind) else None
                tip = outfit_advice(mx, mn, rn, wd)

                with st.container(border=True):
                    st.markdown(f"### {day}")
                    st.write(
                        f"**Max/Min:** {mx}°C / {mn}°C  ·  "
                        f"**Rain:** {rn} mm  ·  **Max wind:** {wd} km/h"
                    )
                    st.write(tip)

            st.caption("Data: Open-Meteo (no API key).")
    except requests.RequestException as e:
        st.error(f"Network error: {e}")
