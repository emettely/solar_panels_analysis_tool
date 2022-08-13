# Solar Panels Analysis Tool
## Usage
```shell
usage: calculate.py [-h] [-k PV_CAPACITY] [-g GEN_KWH] [-p GEN_PERCENT]
                    [-e COST_RATE] [-s SEG_RATE] [-i INVERTER_COST]
                    [-c PV_COST] [-b BATTERY_COST]
                    [--ignore-battery IGNORE_BATTERY]

Get solar panel breakeven cost

optional arguments:
  -h, --help            show this help message and exit
  -k PV_CAPACITY, --pv-capacity PV_CAPACITY
                        total capacity of solar panels in kilo watts per hour
                        (default: 4)
  -g GEN_KWH, --gen-kwh GEN_KWH
                        total energy generated per 1kwh PV (default: 1000)
  -p GEN_PERCENT, --gen-percent GEN_PERCENT
                        the percentage of actual energy generation (default:
                        50)
  -e COST_RATE, --cost-rate COST_RATE
                        charge rate from energy companies in pence per kWh
                        (default: 50)
  -s SEG_RATE, --seg-rate SEG_RATE
                        the SEG rate from energy companies in pence per kWh
                        (default: 5.5)
  -i INVERTER_COST, --inverter-cost INVERTER_COST
                        the cost of the inverter (default: 470)
  -c PV_COST, --pv-cost PV_COST
                        the cost of the solar panels, including installation
                        (default: 5000)
  -b BATTERY_COST, --battery-cost BATTERY_COST
                        the cost of the battery/batteries, including
                        installation (default: 7500)
  --ignore-battery IGNORE_BATTERY
```