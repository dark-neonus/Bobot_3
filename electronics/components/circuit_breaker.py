from skidl import TEMPLATE, Part

Circuit_Breaker = Part(
    "Device",
    "CircuitBreaker_1P",
    dest=TEMPLATE,
    value="Circuit Breaker",
    # Part source
    price_uah=130.0,
    buy_link="https://prom.ua/ua/p2666357477-razemy-amass-xt90s.html",
    # Electrical specs
    power_specs=PowerSpec(VoltageSpec(0.0, 14.6, 500.0), CurrentSpec(45.0, 90.0, DeviceType.CONDUCTOR)),
    # Physical specs
    weight_g=15
)
