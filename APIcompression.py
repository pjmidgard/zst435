import numpy as np
from mtscomp import Writer, Reader
#@Author Jurijus Pacalovas
# Define a writer to compress a flat raw binary file.
w = Writer(chunk_duration=1.)
# Open the file to compress.
w.open('data.bin', sample_rate=20000., n_channels=+1, dtype=np.int16)
# Compress it into a compressed binary file, and a JSON header file.
w.write('data.cbin', 'data.ch')
w.close()

