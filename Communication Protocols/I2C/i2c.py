import smbus

BUS = 1  # Which smbus to use, i.e /dev/i2c-1 is bus = 1
ADDRESS = 0x48  # Address of the device to talk to over I2C/smbus

#Setup SMBus access
bus = smbus.SMBus(BUS)

# Read two bytes from register 01, the config register
config = bus.read_word_data(ADDRESS, 0x01) & 0xFFFF
print('Config value: 0x{0:04X}'.format(config))

# Write two bytes to the config register
new_config = 0b0100001110000011
bus.write_word_data(ADDRESS, 0x01, new_config)

# Read two bytes from register 00, the ADC value.
value = bus.read_word_data(ADDRESS, 0x00) & 0xFFFF
# Swap byte order from little endian to big endian
value = ((value & 0xFFFF) << 8) | (value >> 8)
print('Raw ADC value: 0x{0:04X}'.format(value))