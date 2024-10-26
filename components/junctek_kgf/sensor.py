import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import uart, sensor
from esphome.const import (
    CONF_RAW,
    CONF_ID,
    CONF_ADDRESS,
    CONF_INPUT,
    CONF_NUMBER,
    CONF_HARDWARE_UART,
    CONF_TEMPERATURE,
    CONF_VOLTAGE,
    CONF_CURRENT,
    CONF_BATTERY_LEVEL,
    CONF_DIRECTION,

    DEVICE_CLASS_VOLTAGE,
    STATE_CLASS_MEASUREMENT,
    STATE_CLASS_TOTAL_INCREASING,
    UNIT_VOLT,
    UNIT_CELSIUS,
    UNIT_AMPERE,
    UNIT_WATT,
    UNIT_OHM,
    CONF_UPDATE_INTERVAL,
    UNIT_EMPTY,
    UNIT_PERCENT,
    ICON_EMPTY,
    UNIT_KILOWATT_HOURS,
    UNIT_MINUTE,
    ICON_EMPTY,
    ICON_POWER,
    ICON_BATTERY,
    ICON_THERMOMETER,
    ICON_FLASH,
    ICON_PERCENT,
    ICON_TIMER,
    ICON_POWER,
    DEVICE_CLASS_CURRENT,
    DEVICE_CLASS_BATTERY,
    DEVICE_CLASS_TEMPERATURE,
    DEVICE_CLASS_SWITCH,
    DEVICE_CLASS_POWER,
    DEVICE_CLASS_ENERGY,
    DEVICE_CLASS_DURATION,
    DEVICE_CLASS_BATTERY_CHARGING,
)

UNIT_AMPER_HOURS = 'Ah'
DEPENDENCIES = ["uart"]
AUTO_LOAD = ["sensor"]

# sensors
CONF_CURRENT_DIRECTION="current_direction"
CONF_BATTERY_OHM="battery_ohm"
CONF_BATTERY_CHARGED_ENERGY = 'battery_charged_energy'
CONF_BATTERY_DISCHARGED_ENERGY = 'battery_discharged_energy'
CONF_BATTERY_LIFE = 'battery_life'
CONF_BATTERY_POWER = 'battery_power'
CONF_AMP_HOUR_REMAIN = "amp_hour_remain"
CONF_AMP_HOUR_USED = "amp_hour_used_total"
CONF_AMP_HOUR_CHARGED = "amp_hour_charged_total"
CONF_OUTPUT_STATUS = "output_status"
CONF_POWER = "power"

TYPES = [
    CONF_VOLTAGE,
    CONF_CURRENT,
    CONF_BATTERY_LEVEL,
    CONF_TEMPERATURE,
    CONF_DIRECTION,
    CONF_BATTERY_POWER,
    CONF_BATTERY_LIFE,
    CONF_BATTERY_CHARGED_ENERGY,
    CONF_BATTERY_DISCHARGED_ENERGY,
    CONF_AMP_HOUR_REMAIN,
    CONF_AMP_HOUR_USED,
    CONF_AMP_HOUR_CHARGED,
    CONF_BATTERY_OHM,
    CONF_OUTPUT_STATUS,
    CONF_POWER
]

CONF_INVERT_CURRENT="invert_current"
CONF_UPDATE_SETTINGS_INTERVAL="update_settings_interval"
CONF_UPDATE_STATS_INTERVAL="update_stats_interval"

JuncTekKGF = cg.global_ns.class_(
    "JuncTekKGF", cg.Component, uart.UARTDevice
)

CONFIG_SCHEMA = cv.All(
    cv.Schema(
        {
            cv.GenerateID(): cv.declare_id(JuncTekKGF),
            cv.Optional(CONF_ADDRESS, default=1): cv.int_range(1, 255),
            cv.Optional(CONF_VOLTAGE): sensor.sensor_schema(
                unit_of_measurement=UNIT_VOLT,
                icon=ICON_FLASH,
                accuracy_decimals=2,
                device_class=DEVICE_CLASS_VOLTAGE,
                state_class=STATE_CLASS_MEASUREMENT                
            ),
            cv.Optional(CONF_CURRENT): sensor.sensor_schema(
                unit_of_measurement=UNIT_AMPERE,
                icon="mdi:current-dc",
                accuracy_decimals=2,
                device_class=DEVICE_CLASS_CURRENT,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
            cv.Optional(CONF_BATTERY_LEVEL): sensor.sensor_schema(
                unit_of_measurement=UNIT_PERCENT,
                icon=ICON_PERCENT,
                accuracy_decimals=2,
                device_class=DEVICE_CLASS_BATTERY,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
            cv.Optional(CONF_BATTERY_OHM): sensor.sensor_schema(
                unit_of_measurement=UNIT_OHM,
                icon="mdi:resistor",
                accuracy_decimals=3,
                device_class=DEVICE_CLASS_BATTERY,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
             cv.Optional(CONF_TEMPERATURE): sensor.sensor_schema(
                unit_of_measurement=UNIT_CELSIUS,
                icon=ICON_THERMOMETER,
                accuracy_decimals=0,
                device_class=DEVICE_CLASS_TEMPERATURE,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
            cv.Optional(CONF_DIRECTION): sensor.sensor_schema(
                accuracy_decimals=0,
            ),
            cv.Optional(CONF_OUTPUT_STATUS): sensor.sensor_schema(
                accuracy_decimals=0,
                icon="mdi:list-status"
            ),
            cv.Optional(CONF_POWER): sensor.sensor_schema(
                unit_of_measurement=UNIT_WATT,
                icon=ICON_POWER,
                accuracy_decimals=2,
                device_class=DEVICE_CLASS_POWER,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
            cv.Optional(CONF_BATTERY_LIFE): sensor.sensor_schema(
                unit_of_measurement=UNIT_MINUTE,
                icon=ICON_TIMER,
                accuracy_decimals=0,
                device_class=DEVICE_CLASS_DURATION,
                state_class=STATE_CLASS_MEASUREMENT,
             ),
            cv.Optional(CONF_BATTERY_CHARGED_ENERGY): sensor.sensor_schema(
                unit_of_measurement=UNIT_WATT,
                icon="mdi:lightning-bolt",
                accuracy_decimals=2,
                device_class=DEVICE_CLASS_POWER,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
            cv.Optional(CONF_BATTERY_DISCHARGED_ENERGY): sensor.sensor_schema(
                unit_of_measurement=UNIT_WATT,
                icon="mdi:lightning-bolt",
                accuracy_decimals=2,
                device_class=DEVICE_CLASS_POWER,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
            cv.Optional(CONF_AMP_HOUR_REMAIN): sensor.sensor_schema(
                unit_of_measurement=UNIT_AMPER_HOURS,
                icon=ICON_BATTERY,
                accuracy_decimals=1,
                device_class=DEVICE_CLASS_BATTERY,
                state_class=STATE_CLASS_MEASUREMENT,
            ),

            cv.Optional(CONF_AMP_HOUR_USED): sensor.sensor_schema(
                unit_of_measurement=UNIT_AMPER_HOURS,
                icon=ICON_BATTERY,
                accuracy_decimals=1,
                device_class=DEVICE_CLASS_BATTERY,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
            cv.Optional(CONF_AMP_HOUR_CHARGED): sensor.sensor_schema(
                unit_of_measurement=UNIT_AMPER_HOURS,
                icon=ICON_BATTERY,
                accuracy_decimals=1,
                device_class=DEVICE_CLASS_BATTERY,
                state_class=STATE_CLASS_MEASUREMENT,
            ),

            cv.Optional(CONF_INVERT_CURRENT, default=False): cv.boolean,
            cv.Optional(CONF_UPDATE_SETTINGS_INTERVAL, default=30000): cv.int_,
            cv.Optional(CONF_UPDATE_STATS_INTERVAL, default=1000): cv.int_,
            cv.Optional(CONF_CURRENT_DIRECTION, default=True): cv.boolean,
        }
    ).extend(uart.UART_DEVICE_SCHEMA)
    )

async def setup_conf(config, key, hub):
    if key in config:
        conf = config[key]
        sens = await sensor.new_sensor(conf)
        cg.add(getattr(hub, f"set_{key}_sensor")(sens))


async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID], config[CONF_ADDRESS], config[CONF_INVERT_CURRENT])
    await cg.register_component(var, config)
    await uart.register_uart_device(var, config)
    for key in TYPES:
        await setup_conf(config, key, var)

    cg.add(var.set_update_settings_interval(config[CONF_UPDATE_SETTINGS_INTERVAL]))
    cg.add(var.set_update_stats_interval(config[CONF_UPDATE_STATS_INTERVAL]))
