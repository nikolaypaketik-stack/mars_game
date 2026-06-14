from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parent.parent
ASSETS_DIR = ROOT_DIR / "assets"

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)
FPS = 60

INTRO_TEXT = "десь на околицях марса"
ENDING_TEXT = "Піу-піу-піу крутий бос файт всі програли)"

INTRO_DURATION_MS = 5_000
INTRO_TYPE_SPEED_MS = 80
ENDING_DURATION_MS = 5_000
BOSS_SPAWN_DELAY_MS = 15_000
CHASE_HISTORY_DELAY = 120


def asset_path(*parts: str) -> str:
    return str(ASSETS_DIR.joinpath(*parts))


def asset_file(relative_path: str) -> str:
    return str(ASSETS_DIR / Path(relative_path))
