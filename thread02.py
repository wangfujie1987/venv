import threading


def thread_job():
    print('This is a added Thread,number is %s' % threading.current_thread())


def main():
    added_thread = threading.Thread(target=thread_job)
    added_thread.start()


if __name__ == '_main_':
    main()
