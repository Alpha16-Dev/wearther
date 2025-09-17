

# 🧥 Wearther — Weather + Wardrobe Planner

A simple, fast weather & outfit-suggestion app:
- Type a city → get a 7-day forecast → see friendly outfit tips (layers, rain gear, windbreaker).
- Built with **Python + Streamlit** and the **Open-Meteo** APIs (no API key needed).

**Live app:** https://wearther-alpha.streamlit.app/  
**Repo:** https://github.com/Alpha16-Dev/wearther

---

## ✨ Features

- 🔎 City search with geocoding (latitude/longitude lookup)
- 🌤️ 7-day daily forecast: max/min temp, precipitation, wind
- 🧠 Lightweight rule-based outfit suggestions (e.g., add umbrella on rainy days)
- ⚡ No keys / no billing: Open-Meteo APIs are free for non-commercial use

---

## 🧰 Tech stack

- **Frontend/UI:** [Streamlit](https://pypi.org/project/streamlit/)  
- **APIs:** [Open-Meteo Weather Forecast](https://open-meteo.com/en/docs) and [Open-Meteo Geocoding](https://open-meteo.com/en/docs/geocoding-api)  
- **Deploy (free):** Streamlit Community Cloud (connects directly to GitHub)  

> Streamlit Community Cloud deploys apps from GitHub in just a few minutes and handles the containerization for you. :contentReference[oaicite:1]{index=1}  
> Open-Meteo is free for non-commercial use and requires **no API key**. :contentReference[oaicite:2]{index=2}

---

## 🧪 Local development

1. **Clone**:
   ```bash
   git clone https://github.com/Alpha16-Dev/wearther.git
   cd wearther


2. **Create & activate venv** (Windows):

   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

   macOS/Linux:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

3. **Install deps**:

   ```bash
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

4. **Run the app**:

   ```bash
   streamlit run app.py
   ```

   Your browser will open at `http://localhost:8501`. (This is the standard Streamlit run flow.) ([docs.streamlit.io][2])

---

## 🚀 Deploy (Streamlit Community Cloud)

1. Push this repo to GitHub (public is fine).
2. Go to **streamlit.io → Sign in → New app**, select `Alpha16-Dev/wearther`, branch `main`, and **app path** `app.py`.
3. Click **Deploy**. Your app will be live in a couple of minutes. ([docs.streamlit.io][3])

---

## 🔍 How it works

* **Geocoding:** User enters a city → request to Open-Meteo Geocoding API → returns `lat`, `lon`, and the `timezone`. ([open-meteo.com][4])
* **Forecast:** Use Open-Meteo **Forecast API** with `daily=temperature_2m_max,temperature_2m_min,precipitation_sum,windspeed_10m_max` and the returned `timezone` to get a 7-day forecast (comma-separated `daily` params are supported). ([open-meteo.com][5])
* **Outfit tips:** A small rule engine combines avg temp, rain, and wind to recommend layers (e.g., heavy coat for cold, umbrella for rainy, windbreaker for windy).

---

## 📁 Project structure

```
wearther/
├─ app.py            # Streamlit app (UI + API calls + outfit rules)
├─ requirements.txt  # streamlit, requests
└─ README.md
```

---

## ⚠️ Notes

* **Spin-up delay:** Free hosting may pause when idle; the **first** request after a long idle can take a moment to start, then it’s fast again. (Expected for free tiers.)
* **Non-commercial use:** Open-Meteo is free for non-commercial projects; see their docs for details. ([open-meteo.com][6])

---

## 📝 Attribution

* Weather & geocoding by **Open-Meteo**. Docs: Forecast API and Geocoding API. ([open-meteo.com][5])
* Built with **Streamlit**. Install/run instructions follow Streamlit’s official guides. ([docs.streamlit.io][2])

---

## 📜 License

MIT, feel free to fork and adapt.


[1]: https://docs.streamlit.io/deploy/streamlit-community-cloud "Streamlit Community Cloud"
[2]: https://docs.streamlit.io/get-started/installation "Install Streamlit"
[3]: https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app "Prep and deploy your app on Community Cloud"
[4]: https://open-meteo.com/en/docs/geocoding-api "Geocoding API | Open-Meteo.com"
[5]: https://open-meteo.com/en/docs "Weather Forecast API - Open-Meteo.com"
[6]: https://open-meteo.com/ "Open-Meteo.com: 🌤️ Free Open-Source Weather API"
