import scipy
import numpy as np
import scipy.signal
import scipy.ndimage
import scipy.io
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import kurtosis, skew
import pandas as pd
from rpeakdetectr.rpeakdetect import detect_beats, plot_peak_detection

class ECG:
    def __init__(self, mat):
        self.mat = mat
        self.ecg_signal = self.mat.get("val")
        self.rr = detect_beats(self.ecg_signal[0], 300)
        self.pr = np.diff(self.rr)  #Difference between RR

    def data(self):
        pass
    