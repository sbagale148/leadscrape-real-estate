from config import load_settings, Settings
from db import init_db


def main() -> None:
    settings: Settings = load_settings()
    init_db(settings)
    # Extraction pipeline will be implemented in later milestones.


if __name__ == "__main__":
    main()

