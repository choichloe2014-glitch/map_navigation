import streamlit as st
import pandas as pd
from geopy.geocoders import Nominatim

st.title("디지털 지도 ver.1")

place=st.text_input("장소를 입력하세요(예: Seoul, Gangnam)")
if st.button("검색"):

    geolocator = Nominatim(user_agent="map_app")

    location = geolocator.geocode(place)

    if location:
        st.success(f"{place} 위치 찾음!")

        df = pd.DataFrame({
            "lat": [location.latitude],
            "lon": [location.longitude]
        })

        st.map(df)

    else:
        st.error("장소를 찾을 수 없습니다.")
    print(3)

