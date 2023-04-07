""" Module to delete feeds from the app """
import click


def read_rss():
    """ Since we are going to erase an url, this shows the user, the urls that may be deleted. """
    with open('url_list.txt') as f:
        lista = f.read()
        print(lista)


if __name__ == "__main__":
    read_rss()


def delete_rss():
    """ 'You need to open the file and read its contents in memory, then open the file again write the line to it but without the line you wish to omit.'
        https://intellipaat.com/community/5400/deleting-a-line-from-a-file-in-python """
    delete_rss = input(click.style(' What is the url you want to delete? ', fg='magenta', bold=True))
    with open('url_list.txt', 'r') as f:
        lines = f.readlines()
    with open('url_list.txt', 'w') as f:
        for line in lines:
            if line.strip('\n') != delete_rss:
                f.write(line)


if __name__ == "__main__":
    delete_rss()
