from dataclasses import dataclass
from typing import Dict, List


@dataclass
class WaterScenario:
    rainfall_index: float
    runoff_rate: float
    soil_absorption: float
    groundwater_recharge: float
    urban_impermeability: float
    irrigation_efficiency: float
    reuse_rate: float
    leakage_rate: float
    ai_iot_adoption: float
    governance_quality: float
    climate_pressure: float


def clamp(value: float, low: float = 0, high: float = 100) -> float:
    return max(low, min(high, value))


def calculate_water_balance(s: WaterScenario) -> Dict[str, float]:
    """Simplified index-based water system model.

    All inputs are 0-100 indexes. Outputs are also 0-100 style indicators.
    This is not a hydrological engineering model; it is a systems-thinking simulator.
    """
    effective_rainfall = s.rainfall_index * (1 - s.runoff_rate / 100)
    retained_water = effective_rainfall * (0.45 + 0.55 * s.soil_absorption / 100)
    recharge_capacity = retained_water * (s.groundwater_recharge / 100)
    urban_loss = s.urban_impermeability * 0.35
    infrastructure_loss = s.leakage_rate * 0.45
    irrigation_gain = s.irrigation_efficiency * 0.25
    reuse_gain = s.reuse_rate * 0.20
    digital_optimization_gain = s.ai_iot_adoption * 0.12
    governance_multiplier = 0.65 + (s.governance_quality / 100) * 0.45
    climate_penalty = s.climate_pressure * 0.35

    resilience_raw = (
        retained_water * 0.30
        + recharge_capacity * 0.20
        + irrigation_gain
        + reuse_gain
        + digital_optimization_gain
        - urban_loss
        - infrastructure_loss
        - climate_penalty
    ) * governance_multiplier

    resilience_score = clamp(resilience_raw)

    scarcity_risk = clamp(100 - resilience_score + s.climate_pressure * 0.15)
    system_loss = clamp((s.runoff_rate * 0.35) + (s.leakage_rate * 0.25) + (s.urban_impermeability * 0.25))
    optimization_maturity = clamp((s.irrigation_efficiency + s.ai_iot_adoption + s.reuse_rate + s.governance_quality) / 4)

    return {
        "Effective rainfall": clamp(effective_rainfall),
        "Retained water": clamp(retained_water),
        "Groundwater recharge capacity": clamp(recharge_capacity),
        "System loss": system_loss,
        "Optimization maturity": optimization_maturity,
        "Water system resilience score": resilience_score,
        "Scarcity risk": scarcity_risk,
    }


def identify_bottlenecks(s: WaterScenario) -> List[str]:
    bottlenecks = []
    if s.runoff_rate > 55:
        bottlenecks.append("Water leaves the system too quickly through runoff.")
    if s.soil_absorption < 45:
        bottlenecks.append("Soil is not functioning as a water reservoir.")
    if s.groundwater_recharge < 45:
        bottlenecks.append("Groundwater recharge is weak, so long-term resilience is low.")
    if s.urban_impermeability > 60:
        bottlenecks.append("Urban surfaces drain water instead of absorbing it.")
    if s.irrigation_efficiency < 55:
        bottlenecks.append("Irrigation still behaves like a routine operation, not an optimized decision system.")
    if s.reuse_rate < 30:
        bottlenecks.append("Reuse is low, so water is not circulating through the system multiple times.")
    if s.leakage_rate > 30:
        bottlenecks.append("Leakage creates hidden infrastructure losses.")
    if s.ai_iot_adoption < 40:
        bottlenecks.append("Low sensor, AI, or IoT adoption limits real-time decision-making.")
    if s.governance_quality < 45:
        bottlenecks.append("Coordination and governance are limiting implementation.")
    if s.climate_pressure > 70:
        bottlenecks.append("Climate pressure is high, so static planning is risky.")
    return bottlenecks or ["No single dominant bottleneck. The system needs balanced optimization."]


def recommend_interventions(s: WaterScenario) -> List[Dict[str, str]]:
    recommendations = []

    def add(priority: str, intervention: str, reason: str):
        recommendations.append({"Priority": priority, "Intervention": intervention, "Why it matters": reason})

    if s.runoff_rate > 45:
        add("High", "Water retention: swales, small dams, retention basins, floodplain reconnection", "Slow water down and keep it local instead of losing it immediately.")
    if s.soil_absorption < 60:
        add("High", "Soil restoration: cover crops, no-till, mulching, compost, biochar", "Turn soil into a distributed water reservoir.")
    if s.irrigation_efficiency < 75:
        add("High", "Precision irrigation and root-zone delivery", "Apply exactly what is needed, where it is needed, with fewer losses.")
    if s.ai_iot_adoption < 65:
        add("Medium", "AI + IoT monitoring: soil sensors, weather data, predictive scheduling", "Make irrigation a decision system instead of a fixed routine.")
    if s.urban_impermeability > 45:
        add("Medium", "Sponge-city design: permeable surfaces, green roofs, rain gardens, trees", "Cities should absorb water, not only drain it.")
    if s.reuse_rate < 45:
        add("Medium", "Reuse and circular water flows", "Use water more than once before it exits the system.")
    if s.leakage_rate > 20:
        add("High", "Leak detection and pipe renewal", "Reducing hidden losses often beats adding new supply.")
    if s.governance_quality < 60:
        add("High", "Governance layer: shared data, incentives, financing, accountability", "Technical tools fail when coordination fails.")
    if s.climate_pressure > 65:
        add("High", "Scenario planning and adaptive operating rules", "Climate volatility requires flexible decision rules, not fixed assumptions.")

    if not recommendations:
        add("Medium", "Maintain balanced optimization", "The system looks relatively balanced; keep improving measurement, retention, reuse, and governance together.")

    return recommendations
