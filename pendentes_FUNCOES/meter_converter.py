

def mtd_meter_converter(to_type: str, meter_value: float):
    """"""

    measures = 'quilômetro,hectometro,decametro,metro,decímetro,centímetro,milímetro'.split(',')
    # measures = 'kilometer,hectometer,dekameter,meter,decimeter,centimeter,millimeter'.split(',')
    values = [0.001, 0.01, 0.1, 1, 10, 100, 1000]

    counter = 0

    while counter < len(measures):
        if to_type == measures[counter]:
            calculus = meter_value * values[counter]
            frame = f'{meter_value} metros é o equivalente a: {calculus} {to_type}(s)'
            return frame
        else:
            counter += 1
