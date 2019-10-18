name = "hdnsi"

version = "master"

authors = [
    "J-Cube",
    "DNA Research"
]

description = \
    """
    A USD render delegate plugin for the 3Delight NSI renderer.
    """

requires = [
    "3delight-1.6.4+",
    "cmake-3+",
    "gcc-6+",
    "usd-19.11+"
]

variants = [
    ["platform-linux"]
]

build_system = "cmake"

with scope("config") as config:
    config.build_thread_count = "logical_cores"

uuid = "hdnsi-{version}".format(version=str(version))

def commands():
    env.LD_LIBRARY_PATH.prepend("{root}/lib")
    env.PXR_PLUGINPATH_NAME.append("{root}/plugin/usd/hdNSI/resources")

    # Helper environment variables.
    env.HDNSI_INCLUDE_PATH.set("{root}/include")
    env.HDNSI_LIBRARY_PATH.set("{root}/lib")
