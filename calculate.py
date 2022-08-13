import argparse


# TODO: this could be tailored to more specific areas, orientation, etc
def calc_annual_energy_generated(capacity_in_kwh, gen_per_kwh,
                                 gen_rate):
    return capacity_in_kwh * (gen_per_kwh / 100) * gen_rate


def get_annual_net(generated_energy, cost_rate, seg_rate, inverter_cost=None):
    net_from_energy = (generated_energy * (cost_rate + seg_rate)) / 100
    if inverter_cost:
        return net_from_energy - (inverter_cost / 10)
    else:
        return net_from_energy


def get_breakeven_in_years(installation_cost, generated_energy, cost_rate,
                           seg_rate, inverter_cost=None):
    annual_net = get_annual_net(generated_energy, cost_rate, seg_rate,
                                inverter_cost)
    return installation_cost / annual_net


def fmt_tmpl_no_batt(breakeven, cost_of_installation, pv_cap, annual_energy_gen,
                     cost_rate):
    return f"""
It will take around {round(breakeven)} years to breakeven.
Solar panels\t\t\t£{cost_of_installation} 
Solar Panel capacity\t\t{pv_cap} kWh 
Potentially generated kWs\t{annual_energy_gen}
10/22 energy price rates\t{cost_rate} p/kwh
    """


def fmt_tmpl_w_batt(breakeven, cost_of_installation, pv_cap, annual_energy_gen,
                    seg_rate, cost_rate):
    return f"""
It will take around {round(breakeven)} years to breakeven.
Batteries and Solar panels\t£{cost_of_installation} 
Solar Panel capacity\t\t{pv_cap} kWh 
Potentially generated kWs\t{annual_energy_gen}
SEG rates\t\t\t{str(seg_rate)} p/kWh
10/22 energy price rates\t{cost_rate} p/kwh
    """


def main(cmd_args):
    annual_energy_generated = calc_annual_energy_generated(
        cmd_args.pv_capacity, cmd_args.gen_kwh, cmd_args.gen_percent)
    cost_of_installation = cmd_args.pv_cost
    if cmd_args.ignore_battery:
        breakeven = get_breakeven_in_years(cmd_args.pv_cost,
                                           annual_energy_generated,
                                           cmd_args.cost_rate,
                                           cmd_args.seg_rate)
        tmpl = fmt_tmpl_no_batt(breakeven, cost_of_installation,
                                cmd_args.pv_capacity, annual_energy_generated,
                                cmd_args.cost_rate)
    else:
        cost_of_installation += cmd_args.battery_cost
        breakeven = get_breakeven_in_years(
            cost_of_installation,
            annual_energy_generated,
            cmd_args.cost_rate, 0,
            cmd_args.inverter_cost)
        tmpl = fmt_tmpl_w_batt(breakeven, cost_of_installation,
                               cmd_args.pv_capacity, annual_energy_generated,
                               cmd_args.seg_rate, cmd_args.cost_rate)
    print(tmpl)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Get solar panel breakeven cost',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-k', '--pv-capacity', default=4,
                        help="total capacity of solar panels in kilo watts per hour"
                        )
    parser.add_argument('-g', '--gen-kwh', default=1000,
                        help="total energy generated per 1kwh PV"
                        )
    parser.add_argument('-p', '--gen-percent', default=50,
                        help="the percentage of actual energy generation",
                        )
    parser.add_argument('-e', '--cost-rate',
                        default=50,
                        help="charge rate from energy companies in pence per kWh"
                        )
    parser.add_argument('-s', '--seg-rate',
                        default=5.5,
                        help="the SEG rate from energy companies in pence per kWh"
                        )
    parser.add_argument('-i', '--inverter-cost',
                        default=470, help="the cost of the inverter"
                        )
    parser.add_argument('-c', '--pv-cost',
                        default=5000, help="the cost of the solar panels, "
                                           "including installation"
                        )
    parser.add_argument('-b', '--battery-cost',
                        default=7500, help="the cost of the battery/batteries, "
                                           "including installation"
                        )
    parser.add_argument('--ignore-battery', default=False)
    args = parser.parse_args()
    main(args)
