import pandas as pd
import plotly.express as px
import streamlit as st

from water_model import WaterScenario, calculate_water_balance, identify_bottlenecks, recommend_interventions
from ai_connector import build_strategy_prompt, generate_strategy_memo

st.set_page_config(
    page_title="Global Water System Optimizer",
    page_icon="💧",
    layout="wide",
)

st.title("💧 Global Water System Optimizer")
st.caption("A systems-thinking prototype for water retention, irrigation, reuse, governance, and climate resilience.")

st.markdown(
    """
### Core thesis
Water scarcity is often not only a supply problem.  
It is a **system design problem**: runoff, soil, groundwater, infrastructure, irrigation, reuse, data, and governance interact.
"""
)

with st.sidebar:
    st.header("Scenario controls")
    st.caption("All values use a 0–100 index scale.")

    rainfall_index = st.slider("Rainfall / available natural input", 0, 100, 60)
    climate_pressure = st.slider("Climate pressure", 0, 100, 65)

    st.subheader("Losses")
    runoff_rate = st.slider("Runoff rate", 0, 100, 45)
    leakage_rate = st.slider("Leakage rate", 0, 100, 25)
    urban_impermeability = st.slider("Urban impermeability", 0, 100, 45)

    st.subheader("System capacity")
    soil_absorption = st.slider("Soil absorption", 0, 100, 55)
    groundwater_recharge = st.slider("Groundwater recharge", 0, 100, 50)
    irrigation_efficiency = st.slider("Irrigation efficiency", 0, 100, 70)
    reuse_rate = st.slider("Reuse rate", 0, 100, 35)
    ai_iot_adoption = st.slider("AI / IoT adoption", 0, 100, 55)
    governance_quality = st.slider("Governance / coordination quality", 0, 100, 55)

scenario = WaterScenario(
    rainfall_index=rainfall_index,
    runoff_rate=runoff_rate,
    soil_absorption=soil_absorption,
    groundwater_recharge=groundwater_recharge,
    urban_impermeability=urban_impermeability,
    irrigation_efficiency=irrigation_efficiency,
    reuse_rate=reuse_rate,
    leakage_rate=leakage_rate,
    ai_iot_adoption=ai_iot_adoption,
    governance_quality=governance_quality,
    climate_pressure=climate_pressure,
)

metrics = calculate_water_balance(scenario)
bottlenecks = identify_bottlenecks(scenario)
recommendations = recommend_interventions(scenario)

score = metrics["Water system resilience score"]
risk = metrics["Scarcity risk"]
loss = metrics["System loss"]
maturity = metrics["Optimization maturity"]

c1, c2, c3, c4 = st.columns(4)
c1.metric("Resilience score", f"{score:.1f}/100")
c2.metric("Scarcity risk", f"{risk:.1f}/100")
c3.metric("System loss", f"{loss:.1f}/100")
c4.metric("Optimization maturity", f"{maturity:.1f}/100")

metric_df = pd.DataFrame({"Metric": list(metrics.keys()), "Value": list(metrics.values())})
fig = px.bar(metric_df, x="Metric", y="Value", title="Water system indicators", range_y=[0, 100])
st.plotly_chart(fig, use_container_width=True)

left, right = st.columns([1, 1])

with left:
    st.subheader("🔎 Bottlenecks")
    for item in bottlenecks:
        st.write(f"- {item}")

with right:
    st.subheader("🛠 Recommended interventions")
    rec_df = pd.DataFrame(recommendations)
    st.dataframe(rec_df, use_container_width=True, hide_index=True)

st.divider()

st.subheader("🤖 Optional ChatGPT strategy memo")
st.caption("Works when OPENAI_API_KEY is configured in a .env file. Otherwise the app remains fully usable without AI.")

prompt = build_strategy_prompt(metrics, bottlenecks, recommendations)

with st.expander("Show generated prompt"):
    st.code(prompt, language="markdown")

if st.button("Generate AI strategy memo"):
    with st.spinner("Generating strategy memo..."):
        memo = generate_strategy_memo(prompt)
        st.markdown(memo)

st.divider()

st.subheader("📌 LinkedIn framing")
st.markdown(
    """
**We are not just watering crops anymore.**  
We are optimizing a constrained resource inside a climate-stressed system.

The real question is not whether precision irrigation, reuse, retention, and AI can work.  
The real question is how fast these systems can scale — and whether governance can keep up.
"""
)
