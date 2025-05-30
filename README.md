# esphome-junctek_khf
Component for esphome to read status from a Junctek KH-F battery monitor via UART. It also reads settings so it is able correctly calculate battery percentage left. But settings are not exposed to HomeAssistant.

## Features
Connects to the Junctek KGF series battery monitor via UART (RS-485 *adapter NOT needed*) and retrieves the following values:

* Battery Voltage
* Battery Percent
* Battery Current
* Power
* Temperature
* Battery Ah Remaining
* Battery Charging Energy
* Battery Discharging Energy
* Battery life remaining
* Output Status

## Requirements
* ESPHome

## Known problems
* If could call it a problem - when data not available from Junctek interface - you keep seeing the latest value in sensors. Which may misslead. Sensors will not be updated nor they be set to Unavailable.

## Usage
### Connect hardware.
The ESP32 TX and RX needs to be connected to RS-485 Link port directly (RX to A, TX to B without UART-to-RS485 converter). Monitor SHOULD BE connected too and active. Monitor makes calls to Junctek asking for data, ESP just reads the response and parses it. So you keep the monitor + will have data comming to your IoT system.

## ESPHOME Config
The applicable config for the device should look something like:

```yaml
logger:
  baud_rate: 0

external_components:
  - source:
      type: git
      url: https://github.com/photoreal3d/esphome-junctek_khf
      ref: main
    components: [ junctek_kgf ]
    refresh: 0s

uart:
  tx_pin: TX #26
  rx_pin: RX #27
  baud_rate: 115200

sensor:
  - platform: junctek_kgf
    address: 1
    invert_current: true
    update_stats_interval: 3000 #3 seconds
    voltage:
      name: "Voltage"
    current:
      name: "Current"
    power:
      name: "Power"
    battery_level:
      name: "Volume"
    amp_hour_remain:
      name: "Remaining capacity"
    amp_hour_used_total:
      name: "Discharge energy"
    amp_hour_charged_total:
      name: "Charge energy"
    temperature:
      name: "Temperature"
    output_status:
      name: "Status"
    battery_life:
      name: "Remaining time"
```

Not all sensors need to be added.
Address is assumed to be 1 if not provided. (this is configured on the monitor)
invert_current: This inverts the reported current, it's recommended to include this option with either true or false (which ever makes the current make more sense for your setup). The default is currently false (and false will match previous behaviour), but may change to true in future updates.

