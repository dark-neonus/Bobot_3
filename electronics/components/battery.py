from skidl import Part, TEMPLATE

Battery_Cell = Part(
    "Device",
    "Battery",
    dest=TEMPLATE,
    value="Li-ion 21700 5000mAh",
    # Part source
    price_uah=135,
    buy_link="https://prom.ua/ua/m7985862593714244078-akumulyator-eve-inr.html",
    # Battery specs
    capacity_mah=5000,
    # Electrical specs
    v_out_range=[3.6, 4.2],
    i_max_out_amp=15,
    # Physical specs
    weight_g=69
)
