class Observer:
    def __init__(self):
        self.subscribers_list = []

    def main_loop(self):
        for sub in self.subscribers_list:
            sub.status_check()
        return self.main_loop()



class Subscriber:

    def status_check(self):
        self.check_pacman_pos()



if __name__ == '__main__':
    # Class GAME
    ob = Observer()
    ob.main_loop()