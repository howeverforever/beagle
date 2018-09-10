BMP_BUS = 2

BMP280_ADDR = 0x76
DEFAULT_SEA_LEVEL_PA = 101325

# temperature and pressure registers
BMP280_TEMPERATURE_XLSB = 0xFC
BMP280_TEMPERATURE_LSB = 0xFB
BMP280_TEMPERATURE_MSB = 0xFA
BMP280_PRESSURE_XLSB = 0xF9
BMP280_PRESSURE_LSB = 0xF8
BMP280_PRESSURE_MSB = 0xF7

# config register and settings
BMP280_CONFIG = 0xF5
# time sample delay settings
BMP280_TSB_0 = 0x00
BMP280_TSB_63 = 0x01 << 5
BMP280_TSB_125 = 0x02 << 5
BMP280_TSB_250 = 0x03 << 5
BMP280_TSB_500 = 0x04 << 5
BMP280_TSB_1000 = 0x05 << 5
BMP280_TSB_2000 = 0x06 << 5
BMP280_TSB_4000 = 0x07 << 5
# IIR filter settings
BMP280_FILTER_OFF = 0x00 << 2
BMP280_FILTER_2 = 0x01 << 2
BMP280_FILTER_4 = 0x02 << 2
BMP280_FILTER_8 = 0x03 << 2
BMP280_FILTER_16 = 0x04 << 2
# SPI enable
BMP280_SPI3W_EN = 0x01

# control measurement register and settings
BMP280_CTRL_MEAS = 0xF4
# temperature oversample
BMP_TEMP_OVERSAMPLE_OFF = 0x00
BMP_TEMP_OVERSAMPLE_1 = 0x01 << 5
BMP_TEMP_OVERSAMPLE_2 = 0x02 << 5
BMP_TEMP_OVERSAMPLE_4 = 0x03 << 5
BMP_TEMP_OVERSAMPLE_8 = 0x04 << 5
BMP_TEMP_OVERSAMPLE_16 = 0x05 << 5
# pressure oversample
BMP_PRES_OVERSAMPLE_1 = 0x01 << 2
BMP_PRES_OVERSAMPLE_2 = 0x02 << 2
BMP_PRES_OVERSAMPLE_4 = 0x03 << 2
BMP_PRES_OVERSAMPLE_8 = 0x04 << 2
BMP_PRES_OVERSAMPLE_16 = 0x05 << 2
# mode
BMP_MODE_SLEEP = 0x00
BMP_MODE_FORCED = 0x01
BMP_MODE_NORMAL = 0x03

# status register
BMP280_STATUS_REG = 0xF3
BMP280_MEAS_STATUS = 0x01 << 3
BMP280_IM_UPDATE_STATUS = 0x01

# reset register, write reset_word to reset
BMP280_RESET_REG = 0xE0
BMP280_RESET_WORD = 0xB6

# chip ID, should return 0x58
BMP280_CHIP_ID_REG = 0xD0
BMP280_CHIP_ID = 0x58

# calibration constant registers
BMP280_DIG_T1 = 0x88
BMP280_DIG_T2 = 0x8A
BMP280_DIG_T3 = 0x8C
BMP280_DIG_P1 = 0x8E
BMP280_DIG_P2 = 0x90
BMP280_DIG_P3 = 0x92
BMP280_DIG_P4 = 0x94
BMP280_DIG_P5 = 0x96
BMP280_DIG_P6 = 0x98
BMP280_DIG_P7 = 0x9A
BMP280_DIG_P8 = 0x9C
BMP280_DIG_P9 = 0x9E
BMP280_CAL26 = 0xE1