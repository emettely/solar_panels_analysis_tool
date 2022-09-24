# Solar Panels Analysis Tool

## Context

This is a tool developed in Python3 to aid with calculating the number of years
it will take to breakeven.

## Default values

|Option name|Description|Default Value|
|---|---|---|
|`--pv-capacity`|The solar panel system energy generation capacity|4kW|
|`--gen-kwh`|The maximum energy generated per 1kW solar panel system. This will largely depend on the orientation of the PV panels and the location of the property. For example, a SSW-facing roof in South West England will do better than a North-facing roof in Wales.|1000 kW/h
|`--gen-percent`|The percentage of how much will actually be generated out of the maximum generated over the year. We default to 50% as we assume if we average out the electricity generation for the whole year, we only generate half of the maximum capacity.| 50%| 
|`--cost-rate`|The energy charge rate from energy companies. We use the October 2022 value in London.|51.4 p/kWh
|`--seg-rate`|The SEG (Smart Export Guarantee) rate from energy companies.|5.5 p/kWh
|`--inverter-cost`|The cost for inverters.|£470|
|`--pv-cost`|The cost to install PV panels|£5000|
|`--battery-cost`|The cost to install batteries|£7500|
|`--ignore-battery`|Ignore batteries: this will ignore the cost of batteries, and assume that you will be exporting to the grid for any electricity generated.|false|

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
                        total capacity of solar panels in kilo watts
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
```usage: calculate.py [-h] [-k PV_CAPACITY] [-u USAGE] [-g GEN_KWH]
                    [-p GEN_PERCENT] [-e COST_RATE] [-s SEG_RATE]
                    [-i INVERTER_COST] [-c PV_COST] [-b BATTERY_COST]
                    [-l LOCATION] [--battery] [--no-battery]

Get solar panel breakeven cost

optional arguments:
  -h, --help            show this help message and exit
  -k PV_CAPACITY, --pv-capacity PV_CAPACITY
                        total capacity of solar panels in kilo watts (default:
                        4.8)
  -u USAGE, --usage USAGE
                        total electric usage of solar panels in kilo watts per
                        annum (default: 3680)
  -g GEN_KWH, --gen-kwh GEN_KWH
                        total energy generated per 1kwh PV (default: 1000)
  -p GEN_PERCENT, --gen-percent GEN_PERCENT
                        the percentage of actual energy generation (default:
                        90)
  -e COST_RATE, --cost-rate COST_RATE
                        charge rate from energy companies in pence per kWh
                        (default: 36)
  -s SEG_RATE, --seg-rate SEG_RATE
                        the SEG rate from energy companies in pence per kWh
                        (default: 5.5)
  -i INVERTER_COST, --inverter-cost INVERTER_COST
                        the cost of the inverter (default: 470)
  -c PV_COST, --pv-cost PV_COST
                        the cost of the solar panels, including installation
                        (default: 7500)
  -b BATTERY_COST, --battery-cost BATTERY_COST
                        the cost of the battery/batteries, including
                        installation (default: 5500)
  -l LOCATION, --location LOCATION
                        the location where PV system will be installed
                        (default: London)
  --battery
  --no-battery
