import random

from service import get_episodes, show_id_latest, download_episodes


def main():
    # SHOW THE HEADER
    welcome_msg()

    # DOWNLOAD THE EPISODE DATA
    download_episodes()

    # GET LATEST SHOW ID
    latest_show_id = show_id_latest()
    print("Working with total of {} episodes".format(latest_show_id))

    # DISPLAY RESULTS
    show_results()


def show_results():
    start = random.randint(90, 110)
    latest_id = show_id_latest()
    end = random.randint(130, latest_id + 1)
    for show_id in range(start, end):
        # GET EPISODE
        info = get_episodes(show_id)
        print("{}. {}".format(info.show_id, info.title))


def welcome_msg():
    print("Welcome to the talk python info downloader.")
    print()


if __name__ == '__main__':
    main()
