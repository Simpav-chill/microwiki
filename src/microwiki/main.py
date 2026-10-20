from os import mkdir
from pathlib import Path

from platformdirs import PlatformDirs

from ui import main

if __name__ == "__main__":
    pdirs = PlatformDirs("microwiki", "justtechno")
    if not Path(pdirs.user_data_dir).exists():
        mkdir(pdirs.user_data_dir)
    main()
