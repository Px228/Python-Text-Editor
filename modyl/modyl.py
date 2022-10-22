from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


def sound_0(none):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.GetMute()
    volume.GetMasterVolumeLevel()
    volume.GetVolumeRange()
    volume.SetMasterVolumeLevel(-65, None)
    print("0")
def sound_40(none):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.GetMute()
    volume.GetMasterVolumeLevel()
    volume.GetVolumeRange()
    volume.SetMasterVolumeLevel(-13.8, None)
    print("40")
def sound_45(none):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.GetMute()
    volume.GetMasterVolumeLevel()
    volume.GetVolumeRange()
    volume.SetMasterVolumeLevel(-12, None)
    print("45")
def sound_50(none):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.GetMute()
    volume.GetMasterVolumeLevel()
    volume.GetVolumeRange()
    volume.SetMasterVolumeLevel(-10.2, None)
    print("50")
def sound_55(none):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.GetMute()
    volume.GetMasterVolumeLevel()
    volume.GetVolumeRange()
    volume.SetMasterVolumeLevel(-8.8, None)
    print("55")
def sound_60(none):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.GetMute()
    volume.GetMasterVolumeLevel()
    volume.GetVolumeRange()
    volume.SetMasterVolumeLevel(-7.6, None)
    print("60")
def sound_65(none):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.GetMute()
    volume.GetMasterVolumeLevel()
    volume.GetVolumeRange()
    volume.SetMasterVolumeLevel(-6.4, None)
    print("65")
def sound_70(none):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.GetMute()
    volume.GetMasterVolumeLevel()
    volume.GetVolumeRange()
    volume.SetMasterVolumeLevel(-5.4, None)
    print("70")


if __name__ == '__main__':
    sound_70(None)
    print("Start: __init__")


