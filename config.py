from pathlib import Path

ROOT_PATH = Path(__file__).parent
BAD_PATH = ROOT_PATH.joinpath("bad_path")
ITEMS_PATH = ROOT_PATH.joinpath("src", "items.csv")
BROKEN_FILE = ROOT_PATH.joinpath("src", "broken_items.csv")