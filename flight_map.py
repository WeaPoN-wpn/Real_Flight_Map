import streamlit as st
import pandas as pd
import requests
import folium
from streamlit_folium import st_folium

# API配置
API_URL = "https://api.aviationstack.com/v1/flights"
ACCESS_KEY = "7872878ff908c1337431412f4ab5921a"

# 页面配置
st.set_page_config(page_title="Flight Live Map", layout="wide")
st.title("✈️ Flight Live Map")
st.markdown("实时航班地图（带飞机图标），数据来源：AviationStack API")

@st.cache_data(ttl=300)  # 缓存5分钟
def fetch_flight_data():
    params = {
        'access_key': ACCESS_KEY,
        'limit': 100  # 拉取100条数据
    }
    response = requests.get(API_URL, params=params)
    if response.status_code == 200:
        data = response.json()
        df = pd.json_normalize(data['data'])
        return df
    else:
        st.error("❌ 无法获取航班数据，请检查API或网络")
        return pd.DataFrame()

# 获取数据
flight_df = fetch_flight_data()

if not flight_df.empty:
    # 过滤有实时坐标的航班
    live_flights = flight_df.dropna(subset=['live.longitude', 'live.latitude', 'live.altitude'])

    # 显示部分航班数据
    st.subheader("📊 当前实时航班数据")
    st.dataframe(
        live_flights[['airline.name', 'flight.iata', 'departure.airport',
                      'arrival.airport', 'live.latitude', 'live.longitude', 'live.altitude']].head(10)
    )

    st.subheader("🗺️ 实时航班地图")

    # 初始化地图中心
    m = folium.Map(location=[live_flights['live.latitude'].mean(), live_flights['live.longitude'].mean()],
                   zoom_start=2, tiles='CartoDB Positron')

    # 遍历航班打上飞机图标
    for _, row in live_flights.iterrows():
        popup_text = f"""
        航空公司: {row['airline.name']}<br>
        航班号: {row['flight.iata']}<br>
        起飞机场: {row['departure.airport']}<br>
        降落机场: {row['arrival.airport']}<br>
        海拔: {row['live.altitude']} 米
        """
        folium.Marker(
            location=[row['live.latitude'], row['live.longitude']],
            icon=folium.DivIcon(html='✈️', icon_size=(28, 28)),
            popup=folium.Popup(popup_text, max_width=300)
        ).add_to(m)

    # 渲染地图
    st_data = st_folium(m, width=1200, height=600)
else:
    st.error("⚠️ 当前没有可用的航班数据可视化。")