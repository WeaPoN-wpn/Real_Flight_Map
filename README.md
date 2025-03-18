# ✈️ Flight Live Map

## 项目简介
本项目是一个基于 **Streamlit** 的可视化应用，实时从 **AviationStack API** 获取全球航班数据，并在地图上以飞机图标标注显示每架飞机的实时位置和信息。

## 功能特点
- 实时获取航班信息（航司、航班号、起降机场、海拔等）
- 地图可视化，飞机位置直观展示
- 支持交互查看每架飞机的详细信息（点击飞机图标弹出）
- 使用 Streamlit 快速搭建可视化网页

## 技术栈
- **Python 3**
- **Streamlit**
- **Pandas**
- **Folium + streamlit-folium** （地图与飞机图标展示）
- **AviationStack API**（航班数据来源）

## 快速开始

### 1️⃣ 克隆项目
```
git clone https://github.com/你的用户名/flight-live-map.git
cd flight-live-map
```

### 2️⃣ 安装依赖
建议使用虚拟环境：
```
pip install -r requirements.txt
```

### 3️⃣ 运行项目
```
streamlit run flight_map.py
```

### 4️⃣ 查看效果
默认将在浏览器打开：http://localhost:8501

---

## 文件结构
```
flight-live-map/
├── flight_map.py         # 主应用脚本
├── requirements.txt      # 项目依赖包
└── README.md             # 项目说明文件
```

---

## 数据来源
- **API**: [AviationStack](https://aviationstack.com/)
- **API Key（示例）**: \`7872878ff908c1337431412f4ab5921a\`

---

## 示例效果
- 实时航班表格
- 可交互地图（飞机图标 ✈️ 标记航班位置）

---

## 备注
- 免费版 API 数据有限，建议申请正式版提高调用频率和数据完整性
- 若地图无数据显示，可能为当前 API 返回数据为空或请求次数达到上限

---

## License
MIT License
