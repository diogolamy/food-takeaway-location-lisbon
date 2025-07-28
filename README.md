# 📍 Food Takeaway Location Lisbon

**Data-driven analysis to select the best location for opening a new takeaway food shop in Lisbon.**

---

## 🥡 Project Objective

This project aims to identify the most strategic location in Lisbon to open a new **takeaway food shop**, using socio-economic, demographic and geographic data. The goal is to combine **data science techniques** and **local knowledge** to support a real-world business decision.

---

## 🧩 Project Context

In cities like Lisbon, choosing the right location can significantly impact the success of a food business. We analyze:
- **Median income per civil parish**
- **Population density**
- **Inequality indicators (Gini coefficient)**
- **Competitor density (planned)**
- **Commuting/workplace population (optional)**

---

## 📊 Data Sources

Current and planned data includes:

- **INE – Instituto Nacional de Estatística**  
  - [Estatísticas do Rendimento ao Nível Local – 2022](https://www.ine.pt)
  - Median income per person per city parish (https://www.ine.pt/xportal/xmain?xpid=INE&xpgid=ine_indicadores&indOcorrCod=0012757&contexto=bd&selTab=tab2)
  - Gini coefficient per city parish (https://www.ine.pt/xportal/xmain?xpid=INE&xpgid=ine_indicadores&indOcorrCod=0012761&contexto=bd&selTab=tab2)
  - Economic activity per city parish (https://www.ine.pt/xportal/xmain?xpid=INE&xpgid=ine_indicadores&indOcorrCod=0014449&contexto=bd&selTab=tab2)

- **PORDATA**  
  - Population density (https://www.ine.pt/xportal/xmain?xpid=INE&xpgid=ine_indicadores&indOcorrCod=0011613&contexto=bd&selTab=tab2)
  - Working population by parish (https://www.ine.pt/xportal/xmain?xpid=INE&xpgid=ine_indicadores&indOcorrCod=0011690&contexto=bd&selTab=tab2)
  - Median rent per m2 per city parish (https://www.ine.pt/xportal/xmain?xpid=INE&xpgid=ine_indicadores&indOcorrCod=0012598&contexto=bd&selTab=tab2)
  - % of foreign population per city parish (https://www.ine.pt/xportal/xmain?xpid=INE&xpgid=ine_indicadores&indOcorrCod=0011647&contexto=bd&selTab=tab2)
  - Number of marital family units per city parish (https://www.ine.pt/xportal/xmain?xpid=INE&xpgid=ine_indicadores&indOcorrCod=0012858&contexto=bd&selTab=tab2)
  - Number of single-parent household per city parish (https://www.ine.pt/xportal/xmain?xpid=INE&xpgid=ine_indicadores&indOcorrCod=0012405&contexto=bd&selTab=tab2)
  - Number of private households per city parish (https://www.ine.pt/xportal/xmain?xpid=INE&xpgid=ine_indicadores&indOcorrCod=0012459&contexto=bd&selTab=tab2)   

- **OpenStreetMap / Google Places API** *(planned)*  
  - To map existing food shops, cafés, and takeaway spots

---

## 🛠️ Tools & Tech Stack

- `Python 3.x`
- `Pandas`, `NumPy`
- `GeoPandas`, `Shapely`
- `Matplotlib`, `Seaborn`, `Folium`
- `QGIS` or `Kepler.gl` (for map exploration)

---

## 🧪 Methodology (Outline)

1. **Data Collection**  
   Scraping, API access, CSV import from official sources

2. **Geospatial Join**  
   Merge income, population, and inequality data with shapefiles of Lisbon parishes

3. **Scoring System** *(to be developed)*  
   Create a ranking system that combines indicators to recommend ideal locations

4. **Visualization**  
   Interactive maps and charts to support decision-making

---

## 📍 Outcome

The output of this project will be:
- A **ranked list of recommended parishes/freguesias**
- **Interactive maps** showing socio-economic patterns
- A modular and reusable **Python script** that can be easily adapted to analyze other cities or new locations

---

## 🚧 Roadmap

- [x] Define project scope
- [x] Gather income + inequality data (INE)
- [ ] Add population + business density
- [ ] Build location scoring model
- [ ] Create interactive map dashboard
- [ ] Prepare final decision report

---

## 💡 Inspiration

This project is inspired by Lisbon-based takeaway models, and is part of a broader exploration of **data-informed small business planning**.

---

## 📂 License

This project is open-source under the [MIT License](LICENSE).

---
