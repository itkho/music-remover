from multiprocessing import freeze_support

from src.app import main


if __name__ == "__main__":
    freeze_support()
    main()