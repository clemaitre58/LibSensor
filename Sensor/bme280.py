import time
# Default I2C address for device.
BME280_I2CADDR_DEFAULT = 0x76

# Register addresses.
BME280_HUM_LSB = 0xFE
BME280_HUM_MSB = 0xFD
BME280_TEMP_XLSB = 0xFC
BME280_TEMP_LSB = 0xFB
BME280_TEMP_MSB = 0xFA
BME280_PRESS_XLSB = 0xF9
BME280_PRESS_LSB = 0xF8
BME280_PRESS_MSB = 0xF7
BME280_CONFIG = 0xF5
BME280_CTRL_MEAS = 0xF4
BME280_STATUS = 0xF3
BME280_CRTL_HUM = 0xF2
BME280_RESET = 0xE0
BME_280_ID = 0xD0

# Calibration Register :

BME280_DIG_T1 = 0x88
BME280_DIG_T2 = 0x8A
BME280_DIG_T3 = 0x8C

BME280_DIG_P1 = 0x8E
BME280_DIG_P2 = 0x90
BME280_DIG_P3 = 0x92
BME280_DIG_P4 = 0x94
BME280_DIG_P5 = 0x96
BME280_DIG_P6 = 0x98
BME280_DIG_P7 = 0x9A
BME280_DIG_P8 = 0x9C
BME280_DIG_P9 = 0x9E

BME280_DIG_H1 = 0xA1
BME280_DIG_H2 = 0xE1
BME280_DIG_H3 = 0xE3
BME280_DIG_H4 = 0xE4
BME280_DIG_H5 = 0xE5
BME280_DIG_H6 = 0xE6
BME280_DIG_H7 = 0xE7

# Configuration

# osrs_h

BME280_OSRS_H_SKIPPED = 0b000
BME280_OSRS_H_1 = 0b001
BME280_OSRS_H_2 = 0b010
BME280_OSRS_H_4 = 0b011
BME280_OSRS_H_8 = 0b100
BME280_OSRS_H_16 = 0b101

# osrs_p


BME280_OSRS_P_SKIPPED = 0b000
BME280_OSRS_P_1 = 0b001
BME280_OSRS_P_2 = 0b010
BME280_OSRS_P_4 = 0b011
BME280_OSRS_P_8 = 0b100
BME280_OSRS_P_16 = 0b101

# osrs_t

BME280_OSRS_T_SKIPPED = 0b000
BME280_OSRS_T_1 = 0b001
BME280_OSRS_T_2 = 0b010
BME280_OSRS_T_4 = 0b011
BME280_OSRS_T_8 = 0b100
BME280_OSRS_T_16 = 0b101

# mode

BME280_MODE_SLEEP = 0b00
BME280_MODE_FORCED = 0b01
BME280_MODE_NORMAL = 0b11

# t_sb

BME280_T_SB_0_5 = 0b000
BME280_T_SB_62_5 = 0b001
BME280_T_SB_125 = 0b010
BME280_T_SB_250 = 0b011
BME280_T_SB_500 = 0b100
BME280_T_SB_1000 = 0b101
BME280_T_SB_10 = 0b110
BME280_T_SB_20 = 0b111

# filter coef

BME280_FILTER_OFF = 0b000
BME280_FILTER_2 = 0b001
BME280_FILTER_4 = 0b010
BME280_FILTER_8 = 0b011
BME280_FILTER_16 = 0b100


class BME280(object):

    """Class which allows manipulate the BME280 conponent from bosch"""

    def __init__(self, mode=BME280_MODE_NORMAL, osrs_h=BME280_OSRS_H_1,
                 osrs_p=BME280_OSRS_P_1, osrs_t=BME280_OSRS_T_1,
                 coef_filter=BME280_FILTER_OFF, address=BME280_I2CADDR_DEFAULT,
                 i2c=None, standby=BME280_T_SB_1000, **kwargs):
        """TODO: to be defined1.

        :mode: TODO
        :osrs_h: TODO
        :osrs_p: TODO
        :osrs_t: TODO
        :coef_filter: TODO
        :address: TODO
        :i2c: TODO
        :**kwargs: TODO

        """
        # check if mode value is correct
        if mode not in [BME280_MODE_SLEEP, BME280_MODE_FORCED,
                        BME280_MODE_NORMAL]:
            raise ValueError(
                    'Unexpected mode value {0}.'.format(mode))
        self._mode = mode
        # check if osrs_h value is correct
        if osrs_h not in [BME280_OSRS_H_SKIPPED, BME280_OSRS_H_1,
                          BME280_OSRS_H_2, BME280_OSRS_H_2, BME280_OSRS_H_4,
                          BME280_OSRS_H_8, BME280_OSRS_H_16]:
            raise ValueError(
                    'Unexpected osrs_h value {0}.'.format(osrs_h))
        self._osrs_h = osrs_h
        # check if osrs_h value is correct
        if osrs_p not in [BME280_OSRS_P_SKIPPED, BME280_OSRS_P_1,
                          BME280_OSRS_P_2, BME280_OSRS_P_2, BME280_OSRS_P_4,
                          BME280_OSRS_P_8, BME280_OSRS_P_16]:
            raise ValueError(
                    'Unexpected osrs_p value {0}.'.format(osrs_p))
        self._osrs_p = osrs_p
        # check if osrs_t value is correct
        if osrs_t not in [BME280_OSRS_T_SKIPPED, BME280_OSRS_T_1,
                          BME280_OSRS_T_2, BME280_OSRS_T_2, BME280_OSRS_T_4,
                          BME280_OSRS_T_8, BME280_OSRS_T_16]:
            raise ValueError(
                    'Unexpected osrs_t value {0}.'.format(osrs_t))
            self._osrs_t = osrs_t
        # check if coef_filter value is correct
        if coef_filter not in [BME280_FILTER_OFF, BME280_FILTER_2,
                               BME280_FILTER_4,
                               BME280_FILTER_8, BME280_FILTER_16]:
            raise ValueError(
                    'Unexpected coef_filter value {0}.'.format(coef_filter))
        self._coef_filter = coef_filter
        # check if adderess value is correct
        if address not in [BME280_I2CADDR_DEFAULT, 0x77]:
            raise ValueError(
                    'Unexpected address value {0}.'.format(address))
        self._address = address
        # check if adderess value is correct
        if standby not in [BME280_T_SB_0_5, BME280_T_SB_62_5, BME280_T_SB_125,
                           BME280_T_SB_250, BME280_T_SB_500, BME280_T_SB_1000,
                           BME280_T_SB_10, BME280_T_SB_20]:
            raise ValueError(
                    'Unexpected stanby value {0}.'.format(standby))
        self._standby = standby
        # create i2c device
        if i2c is None:
            import Adafruit_GPIO.I2C as I2C
            i2c = I2C
        # create I2C Device
        try:
            self._device = i2c.get_i2c_device(self._address, **kwargs)
        except IOError:
            print("Unable to communicate with Sensor")
            exit()
        # Load calibration valuesi
        self._load_calibration()

        # Config component
        self._device.write8(BME280_CTRL_MEAS, 0x24)
        time.sleep(0.002)
        self._device.write8(BME280_CONFIG, ((self._standby << 5) |
                            (self._coef_filter << 2)))
        time.sleep(0.002)
        self._device.write8(BME280_CRTL_HUM, self._osrs_h)
        self._device.write8(BME280_CTRL_MEAS, ((self._osrs_t << 5) |
                            (self._osrs_p << 2) | 3))
        self.temp = 0.0

    def _load_calibration(self):
        """Load Calibration of the factory in order to compute real value
        :returns: TODO

        """
        self.dig_T1 = self._device.readU16LE(BME280_DIG_T1)
        self.dig_T2 = self._device.readU16LE(BME280_DIG_T2)
        self.dig_T3 = self._device.readU16LE(BME280_DIG_T3)

        self.dig_P1 = self._device.readU16LE(BME280_DIG_P1)
        self.dig_P2 = self._device.readU16LE(BME280_DIG_P2)
        self.dig_P3 = self._device.readU16LE(BME280_DIG_P3)
        self.dig_P4 = self._device.readU16LE(BME280_DIG_P4)
        self.dig_P5 = self._device.readU16LE(BME280_DIG_P5)
        self.dig_P6 = self._device.readU16LE(BME280_DIG_P6)
        self.dig_P7 = self._device.readU16LE(BME280_DIG_P7)
        self.dig_P8 = self._device.readU16LE(BME280_DIG_P8)
        self.dig_P9 = self._device.readU16LE(BME280_DIG_P9)

        self.dig_H1 = self._device.readU8(BME280_DIG_H1)
        self.dig_H2 = self._device.readU16LE(BME280_DIG_H2)
        self.dig_H3 = self._device.readU8(BME280_DIG_H3)
        self.dig_H6 = self._device.readU8(BME280_DIG_H7)

        h4 = self._device.readS8(BME280_DIG_H4)
        h4 = (h4 << 4)
        self.dig_H4 = h4 | (self._device.readU8(BME280_DIG_H5) & 0x0F)

        h5 = self._device.readS8(BME280_DIG_H6)
        h5 = (h5 << 4)
        self.dig_H5 = h5 | (self._device.readU8(BME280_DIG_H5) >> 4 & 0x0F)

    def _read_raw_temp(self):
        """TODO: Docstring for _read_raw_temp.
        :returns: TODO

        """
        while(self._device.readU8(BME280_STATUS) & 0x08):
            time.sleep(0.002)
        self.BME280_data = self._device.readList(BME280_PRESS_MSB, 8)
        raw = ((self.BME280_data[3] << 16) | (self.BME280_data[4] << 8) |
               self.BME280_data[5]) >> 4
        return raw

    def _read_raw_pressure(self):
        """TODO: Docstring for _read_raw_pressure.
        :returns: TODO

        """
        raw = ((self.BME280_data[0] << 16) | (self.BME280_data[1] << 8) |
               self.BME280_data[2]) >> 4
        return raw

    def _read_raw_humidity(self):
        """TODO: Docstring for _read_raw_humidity.
        :returns: TODO

        """
        raw = ((self.BME280_data[6] << 8) | (self.BME280_data[7]))
        return raw

    def read_temperature(self):
        """TODO: Docstring for read_temperature.

        :arg1: TODO
        :returns: TODO

        """
        # float in Python is double precision
        UT = float(self.read_raw_temp())
        var1 = ((UT / 16384.0 - float(self.dig_T1) / 1024.0) *
                float(self.dig_T2))
        var2 = ((UT / 131072.0 - float(self.dig_T1) / 8192.0) * (UT / 131072.0
                - float(self.dig_T1) / 8192.0)) * float(self.dig_T3)
        self.t_fine = int(var1 + var2)
        temp = (var1 + var2) / 5120.0
        return temp

    def read_pressure(self):
        """TODO: Docstring for read_pressure.

        :f: TODO
        :returns: TODO

        """
        adc = float(self.read_raw_pressure())
        var1 = float(self.t_fine) / 2.0 - 64000.0
        var2 = var1 * var1 * float(self.dig_P6) / 32768.0
        var2 = var2 + var1 * float(self.dig_P5) * 2.0
        var2 = var2 / 4.0 + float(self.dig_P4) * 65536.0
        var1 = (float(self.dig_P3) * var1 * var1 / 524288.0 +
                float(self.dig_P2) * var1) / 524288.0
        var1 = (1.0 + var1 / 32768.0) * float(self.dig_P1)
        if var1 == 0:
            return 0
        p = 1048576.0 - adc
        p = ((p - var2 / 4096.0) * 6250.0) / var1
        var1 = float(self.dig_P9) * p * p / 2147483648.0
        var2 = p * float(self.dig_P8) / 32768.0
        p = p + (var1 + var2 + float(self.dig_P7)) / 16.0
        return p

    def read_humidity(self):
        """TODO: Docstring for read_humidity.
        :returns: TODO

        """
        adc = float(self.read_raw_humidity())
        h = float(self.t_fine) - 76800.0
        h = (adc - (float(self.dig_H4) * 64.0 + float(self.dig_H5) /
             16384.0 * h)) * (float(self.dig_H2) / 65536.0 * (1.0 +
                              float(self.dig_H6) / 67108864.0 * h *
                              (1.0 + float(self.dig_H3) / 67108864.0 * h)))
        h = h * (1.0 - float(self.dig_H1) * h / 524288.0)
        if h > 100:
            h = 100
        elif h < 0:
            h = 0
        return h

    def read_dewpoint(self):
        """TODO: Docstring for read_dewpoint.
        :returns: TODO

        """
        celsius = self.read_temperature()
        humidity = self.read_humidity()
        dewpoint = celsius - ((100 - humidity) / 5)
        return dewpoint
