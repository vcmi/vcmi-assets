import subprocess
from pprint import pprint

appiconset_resolutions = {20: {"scale": [1, 2, 3], "original": 32}, 29: {"scale": [1, 2, 3], "original": 32}, 40: {"scale": [1, 2, 3], "original": 32}, 60: {"scale": [2, 3], "original": 32}, 76: {"scale": [1, 2], "original": 32}, 83.5: {"scale": [2], "original": 32}}

pprint(appiconset_resolutions)
for res, val in appiconset_resolutions.items():
    for scale in val["scale"]:
        output = f"Icon-App-{res}x{res}@{scale}x.png"
        print(output)
        command = r"inkscape -w " + f"{res*scale} vcmiclient.{val['original']}x{val['original']}.svg -o appiconset/{output}"
        print(command)
        subprocess.run(command)
