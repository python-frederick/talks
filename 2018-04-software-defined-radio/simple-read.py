from rtlsdr import RtlSdr

sdr = RtlSdr()

# configure device
sdr.sample_rate = 2.048e6  # Hz
sdr.center_freq = 1039e5     # Hz
sdr.freq_correction = 60   # PPM
sdr.gain = 'auto'

for i in sdr.read_samples(512):
    print(i)
    print(type(i))
