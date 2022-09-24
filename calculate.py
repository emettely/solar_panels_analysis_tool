import argparse
from pprint import pprint


# TODO: this could be tailored to more specific areas, orientation, etc
def calc_gen_per_kwh(location, orientation):
    return 1000


def calc_annual_energy_generated(capacity_in_kwh, gen_per_kwh,
                                 gen_rate, location, orientation="S"):
    gen_per_kwh = calc_gen_per_kwh(location, orientation)
    return capacity_in_kwh * (gen_per_kwh / 100) * gen_rate


def get_annual_net(energy_cost_savings, seg_profit, inverter_cost):
    return energy_cost_savings + seg_profit - (inverter_cost / 10) # annual cost of inverter

def get_breakeven_in_years(installation_cost, annual_net):
    return installation_cost / annual_net

def calc_roi_percent(gross, n_years, cost):
    roi_solar = (gross * n_years - cost) / cost
    roi_investment = (((1 + roi_solar)**(1 / n_years)) - 1) * 100
    return roi_investment

def fmt_tmpl_w_batt(breakeven, cost_of_installation, pv_cap, annual_energy_gen, annual_energy_used, annual_energy_exported,
                    seg_rate, cost_rate, annual_net):
    annual_profit = annual_net + annual_energy_exported
    return f"""
It will take around {round(breakeven)} years to breakeven based on 10/22 energy price rates {cost_rate} p/kwh.

Batteries and Solar panels\t£{cost_of_installation} 
Solar Panel capacity\t\t{pv_cap} kW 
SEG rates\t\t\t{str(seg_rate)} p/kWh

Yearly
================
\tGenerated\t\t{annual_energy_gen} kWh
-\tSelf-consumption\t{annual_energy_used} kWh
------------------------------------
=\tExported\t\t{annual_energy_gen - annual_energy_used} kWh

\tEnergy Savings\t\t£{round(annual_net)}
+\tSEG Profit\t\t£{round(annual_energy_exported)}
-------------------------------------
=\tAnnual Net\t\t£{round(annual_profit)}

ROI
================
\t\t\t\t{round(calc_roi_percent(annual_profit, 25, cost_of_installation))} %

    """


def main(cmd_args):
    annual_energy_gen_kwh = calc_annual_energy_generated(
        cmd_args.pv_capacity, cmd_args.gen_kwh, cmd_args.gen_percent,
        cmd_args.location)
    cost_of_installation = cmd_args.pv_cost
    pprint(cmd_args)
    if not cmd_args.battery:
        usage_percent = 0.35

    else:
        usage_percent = 0.72
        cost_of_installation += cmd_args.battery_cost

    annual_self_consumption_kwh = usage_percent * cmd_args.usage
    annual_cost_savings_gbp = annual_self_consumption_kwh * cmd_args.cost_rate / 100
    gross_energy_kwh = annual_energy_gen_kwh - annual_self_consumption_kwh
    annual_export_profit_gbp = (gross_energy_kwh * cmd_args.seg_rate) / 100
    annual_net_gbp = get_annual_net(annual_cost_savings_gbp, annual_export_profit_gbp, cmd_args.inverter_cost)
    breakeven = get_breakeven_in_years(cost_of_installation, annual_net_gbp)
    tmpl = fmt_tmpl_w_batt(breakeven, cost_of_installation,
                            cmd_args.pv_capacity, annual_energy_gen_kwh, annual_self_consumption_kwh, annual_export_profit_gbp,
                            cmd_args.seg_rate, cmd_args.cost_rate, annual_net_gbp)
    print(tmpl)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Get solar panel breakeven cost',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('-k', '--pv-capacity', default=4.8, type=float,
                        help="total capacity of solar panels in kilo watts"
                        )
    parser.add_argument('-u', '--usage', default=3680, type=float,
                        help="total electric usage of solar panels in kilo watts per annum"
                        )
    parser.add_argument('-g', '--gen-kwh', default=1000, type=int,
                        help="total energy generated per 1kwh PV"
                        )
    parser.add_argument('-p', '--gen-percent', default=90, type=int,
                        help="the percentage of actual energy generation",
                        )
    parser.add_argument('-e', '--cost-rate',
                        default=28, type=float,
                        help="charge rate from energy companies in pence per kWh"
                        )
    parser.add_argument('-s', '--seg-rate',
                        default=5.5, type=float,
                        help="the SEG rate from energy companies in pence per kWh"
                        )
    parser.add_argument('-i', '--inverter-cost', type=int,
                        default=470, help="the cost of the inverter"
                        )
    parser.add_argument('-c', '--pv-cost', type=int,
                        default=7500, help="the cost of the solar panels, "
                                           "including installation"
                        )
    parser.add_argument('-b', '--battery-cost', type=int,
                        default=5500, help="the cost of the battery/batteries, "
                                           "including installation"
                        )
    parser.add_argument('-l', '--location',
                        default='London', help="the location where PV system "
                                               "will be installed")
    parser.add_argument('--battery', action='store_true')
    parser.add_argument('--no-battery', dest='battery', action='store_false')
    args = parser.parse_args()
    main(args)
