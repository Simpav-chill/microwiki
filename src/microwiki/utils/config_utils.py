"""utils for working with config"""

import json
import os
from pathlib import Path

from platformdirs import PlatformDirs

def parse_config():
    pdirs = PlatformDirs("microwiki", "justtechno") 
    configdirpath = Path(pdirs.user_config_dir)
    configfilepath = Path(f"{pdirs.user_config_dir}/config.json")
    if configdirpath.is_dir() and configfilepath.is_file():
        with open(configfilepath, "r", encoding="utf-8") as file:
            config = json.load(file)
        return config
    else:
        if not configdirpath.is_dir():
            os.mkdir(pdirs.user_config_dir)
        with open(configfilepath, "w", encoding="utf-8") as file:
            baseconfigdict = {
                "theme": "nord",
                "wikistorage": f"{pdirs.user_data_dir}",
                "editor": "Built-in",
                "keymap": {
                    "force_mod": "ctrl",
                    "go_back": "m",
                    "open_fm": "alt+f",
                    "confirm": "wiki",
                    "rename": "ctrl+r",
                    "delete": "ctrl+d",
                    "create": "ctrl+a",
                    "open_editor": "alt+e",
                    "write_changes": "ctrl+s",
                    "movement": {
                        "up": "k",
                        "down": "j",
                        "left": "h",
                        "right": "l",
                        }
                    }
            }
            baseconfigjson = json.dumps(baseconfigdict, indent=4, ensure_ascii=False)
            file.write(baseconfigjson)
        return baseconfigdict
