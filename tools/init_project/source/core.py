import os

def check_env():
    PFE_ENV = os.getenv("PFE_PATH")
    if not PFE_ENV:
        raise RuntimeError("PFE environment not set.")
    print(PFE_ENV)

def main(name):

    pass

if __name__ == '__main__':

    check_env()
    # main("TEST")
