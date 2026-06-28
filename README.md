# 프로젝트명
Map Navigation

## 프로젝트 설명  

- 장소 입력받아 지도에 보여주기
- 입력받은 여러 장소들의 최단거리 경로와 장소들을 보여주기

## 프로젝트 기능

### 지도에서 장소 찾기
#### app_map_find.py
- 지도에서 원하는 장소를 텍스트로 입력
- 검색버튼을 누르면 그 장소가 지도창에 보임

#### app_map_nave.py
- 지도에 여러 장소들과 그 장소들의 경로를 보여주기:
- 원하는 장소들을 텍스트창에 입력
- 지도 생성 버튼을 누르면 원하는 장소들 사이 최단루트가 지도에 보임

# 기술 스택

- Python 3
- Streamlit: 웹 앱 UI 구성 및 실행
- Geopy (Nominatim): 장소명 -> 위도/경도 변환(지오코딩)
- Folium: 지도 생성, 마커 표시, 경로(Polyline) 시각화
- streamlit-folium: Folium 지도를 Streamlit 화면에 렌더링
- Pandas: 단일 위치 데이터프레임 생성 후 지도 표시(`st.map`)