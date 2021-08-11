import numpy as np
import wave
import struct


class my_note:

    def __init__(self,  num_samples, sampling_rate, max_amplitude):
        '''设置一拍采样数，采样率，最大幅值'''
        self._note_fre = {'do_low': 349, 're_low': 392, 'mi_low': 440,
                          'fa_low': 497, 'sol_low': 523, 'la_low': 587, 'si_low': 659,
                          'do': 698, 're': 784, 'mi': 880, 'fa': 988, 'sol': 1046, 'la': 1175, 'si': 1318, 'do_high': 1397}
        self._num_samples = num_samples
        self._sampling_rate = sampling_rate
        self._max_amplitude = max_amplitude

    def generate_note(self, note, time):
        '''创建含有一个音符的正弦信号'''

        # 幅值渐变，保证两音符连接处幅值为0
        # env = np.linspace(self._max_amplitude, 0, int(self._num_samples*time))#包络，一次函数
        # env = np.array([np.exp(x) for x in np.linspace(int(np.log(self._max_amplitude)), 0, int(self._num_samples*time))])  # 包络，指数函数
        # 包络，梯形（前1/4由0直线上升，后1/4直线下降至0，中间不变）
        env1 = np.linspace(0, self._max_amplitude,
                           int(self._num_samples*time*1/4))
        env2 = np.full(int(self._num_samples*time*2/4), self._max_amplitude)
        env3 = np.linspace(self._max_amplitude, 0,
                           int(self._num_samples*time*1/4))
        env = np.concatenate([env1, env2, env3])

        # 根据音符频率及时间长度生成信号
        sin_signal = [np.sin(2 * np.pi * self._note_fre[note] * x/self._sampling_rate)
                      for x in range(int(self._num_samples*time))]

        return sin_signal*env

    def generate_audio(self, file_name, notes, times):
        sine_wave = np.array([])
        for i in range(0, len(times)):  # 创建正弦波并抽样
            sine_wave = np.concatenate(
                [sine_wave, self.generate_note(notes[i], times[i])])

        # 写入文件
        nframes = self._num_samples
        comptype = "NONE"
        compname = "not compressed"
        nchannels = 1
        sampwidth = 2

        wav_file = wave.open(file_name, 'w')
        wav_file.setparams((nchannels, sampwidth, int(
            self._sampling_rate), nframes, comptype, compname))
        for s in sine_wave:  # 写入正弦波
            wav_file.writeframes(struct.pack('h', int(s)))
