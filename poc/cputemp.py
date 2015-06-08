class CPUTemp:
    def __init__(self, tempfilename = "/sys/class/thermal/thermal_zone0/temp"):
        self.tempfilename = tempfilename

    def __enter__(self):
        self.open()
        return self

    def open(self):
        self.tempfile = open(self.tempfilename, "r")
    
    def read(self):
        self.tempfile.seek(0)
        return self.tempfile.read(5)

    def __exit__(self, type, value, traceback):
        self.close()
            
    def close(self):
        self.tempfile.close()

if __name__ == "__main__":
    with CPUTemp() as cpu_temp:
        print(cpu_temp.read())
