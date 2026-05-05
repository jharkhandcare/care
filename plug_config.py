from plugs.manager import PlugManager
from plugs.plug import Plug

gateway_device_plugin = Plug(
    name="gateway_device",
    package_name="git+https://github.com/10bedicu/care_teleicu_devices.git",
    version="@main",
    configs={}
)

camera_device_plugin = Plug(
    name="camera_device",
    package_name="git+https://github.com/10bedicu/care_teleicu_devices.git",
    version="@main",
    configs={}
)

vitals_observation_device_plugin = Plug(
    name="vitals_observation_device",
    package_name="git+https://github.com/10bedicu/care_teleicu_devices.git",
    version="@main",
    configs={}
)

scribe_plug = Plug(
    name="care_scribe",
    package_name="git+https://github.com/10bedicu/care_scribe.git",
    version="@master",
    configs={}
)

care_teleicu_plug = Plug(
    name="care_teleicu",
    package_name="git+https://github.com/10bedicu/care_teleicu.git",
    version="@master",
    configs={},
)

care_abdm_plug = Plug(
    name="abdm",
    package_name="git+https://github.com/10bedicu/care_abdm.git",
    version="@develop",
    configs={},
)

plugs = [
    gateway_device_plugin,
    camera_device_plugin,
    vitals_observation_device_plugin,
    scribe_plug,
    care_teleicu_plug,
    care_abdm_plug
]

manager = PlugManager(plugs)
