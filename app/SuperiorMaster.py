from chaos_master import ChaosMaster
#from master.app.chaos_master import ChaosMaster

class SuperiorMaster:
    def __init__(self, random_picker_url, injector_url):
        self.__masters = {}
        self.random_picker_url = random_picker_url
        self.injector_url = injector_url
        self.__download_masters()

    def add_master(self, uid, interval, group):
        print("hi1")
        print(self.injector_url)
        self.__masters[uid] = ChaosMaster(injector_url=self.injector_url, random_picker_url=self.random_picker_url, interval=interval, group=group)
        print("hi2")
        self.__upload_masters()
        print("hi3")

    def remove_master(self, uid):
        try:
            del self.__masters[uid]
            self.__upload_masters()
        except:
            print("Failed to delete by uid:", uid)

    def change_interval(self, uid, interval):
        try:
            self.__masters[uid].set_interval(interval)
        except:
            print("Failed to change interval of uid: ", uid)

    def change_group(self, uid, group):
        try:
            print("hello")
            self.__masters[uid].set_group(group)
        except:
            print("Failed to change group of uid: ", uid)


    # Uploading to file the masters in the following format: uid,interval,group
    def __upload_masters(self):
        try:
            file = open("masters_info.txt", "w")
            masters_to_save = []
            for master_uid in self.__masters:
                masters_to_save.append(master_uid + "," + str(self.__masters[master_uid].get_interval()) + "," + self.__masters[master_uid].get_group())

            file.writelines(masters_to_save)
            file.close()
            print("Saved masters in file")
        except:
            print("Failed to save masters in file.")

    def __download_masters(self):
        try:
            file = open("masters_info.txt", "r")
            for line in file:
                temp = line.split(',')
                self.add_master(temp[0], int(temp[1]), temp[2])

            file.close()
        except:
            print("Failed to achieve masters from file.")
