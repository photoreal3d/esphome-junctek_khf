# esphome-junctek_khf
Компонент для интеграции в Home Assistant монитора аккумуляторной батареи Junctek KH-F с помощью ESPHome.

## Возможности
Подключение к монитору Junctek KH-F через разъем "RS-485 Link" и отображение следующих значений:

* Процент заряда АКБ (%)
* Оставшаяся емкость батареи (Ah)
* Оставшееся время работы (min)
* Ток батареи (A)
* Напряжение батареи (V)
* Мощность батареи (W)
* Мощность заряда АКБ (W) 
* Мощность разряда АКБ (W)
* Температура батареи
* Статус АКБ

## Необходимое оборудование
* NodeMCU v3.0 на базе ESP8266 (или другая платформа, поддерживаемая в ESPHome)
* монитор аккумуляторной батареи Junctek KH-F с дисплеем

## Особенности
* Дисплей монитора Junctek KH-F должен быть подключен и активен (т.к. дисплей отправляет запросы в измерительный модуль, а устройство на базе ESPHome только считывает полученные в ответ данные, таким образом обеспечивается одновременная работа дисплея и передача данных в Home Assistant).

## Подключение
Подключить пин "TX" (D0, GPIO16) платы Node MCU к выводу "В" разъема RS-485 Link измерительного модуля Junctek KH-F.
Подключить пин "RX" (D1, GPIO5) платы Node MCU к выводу "A" разъема RS-485 Link измерительного модуля Junctek KH-F.
Подключить пин "G" (GND) платы Node MCU к выводу "GND" разъема RS-485 Link измерительного модуля Junctek KH-F.
Подключить питание +5В на плату Node MCU через разъем USB или на выводы VIN и GND.

## Настройка
- установить интеграцию ESPHome Builder в Home Assistant
- создать новое устройство
- отредактировать конфигурационный файл устройства в соответствии:

```yaml
esphome:
  name: kh-f-battery-monitor
  friendly_name: KH-F Battery Monitor

esp8266:
  board: esp01_1m

# Enable logging
logger:

# Enable Home Assistant API
api:
  encryption:
    key: "*"

ota:
  - platform: esphome
    password: "*"

wifi:
  ssid: !secret wifi_ssid
  password: !secret wifi_password

  # Enable fallback hotspot (captive portal) in case wifi connection fails
  ap:
    ssid: "Kh-F-Battery-Monitor"
    password: "*"

captive_portal:

external_components:
  - source:
      type: git
      url: https://github.com/photoreal3d/esphome-junctek_khf
      ref: main
    components: [ junctek_kgf ]
    refresh: 0s

uart:
  tx_pin: GPIO16
  rx_pin: GPIO5
  baud_rate: 115200

sensor:
  - platform: junctek_kgf
    address: 1
    invert_current: true
    update_stats_interval: 1000 #1 seconds
    voltage:
      name: "Battery voltage"
    current:
      name: "Battery current"
    power:
      name: "Battery power"
    battery_level:
      name: "Battery level"
    amp_hour_remain:
      name: "Battery remaining capacity"           
    temperature:
      name: "Battery temperature"
    output_status:
      name: "Battery status"
    battery_life:
      name: "Battery remaining time"
    battery_charged_energy:
      name: "Battery charge power"
    battery_discharged_energy:
      name: "Battery discharge power"
```


