import streamlit as st
from geopy.geocoders import Nominatim
import folium
from streamlit_folium import folium_static

st.title("디지털 지도 ver.2 (여러 장소 + 경로)")

places_input = st.text_area(
    "장소를 줄바꿈으로 입력하세요\n예:\nSeoul\nGangnam\nBusan"
)

if st.button("지도 생성"):
    geolocator = Nominatim(user_agent="map_app")

   # places = [p.strip() for p in places_input.split("\n") if p.strip()]

    places = []

    for p in places_input.split("\n"):
        if p.strip():
            places.append(p.strip())
    
    print(places)

    coordinates = []

    for place in places:
        location = geolocator.geocode(place)

        if location:
            coordinates.append((location.latitude, location.longitude))
        else:
            st.warning(f"{place} 위치를 찾을 수 없음")

    if coordinates:

        print("cood",coordinates)

        m = folium.Map(location=coordinates[0], zoom_start=12)

        for i, (lat, lon) in enumerate(coordinates):
            folium.Marker(
                [lat, lon],
                popup=f"{places[i]}"
            ).add_to(m)

        folium.PolyLine(
                locations=coordinates,
                color="blue",
                weight = 5
            ).add_to(m)

        folium_static(m, width=700, height=500)

    else:
        st.error("유효한 장소가 없습니다.")