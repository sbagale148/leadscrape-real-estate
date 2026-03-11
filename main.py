from config import load_settings
from db import init_db


def main() -> None:
    settings = load_settings()
    init_db(settings)
    # Extraction pipeline will be implemented in later milestones.


if __name__ == "__main__":
    main()

