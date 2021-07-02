from CliniqueManager import CliniqueManager

class CliniqueMain:
    
    def main(self):
        cliniqueManager = CliniqueManager()
        #cliniqueManager.addDoctor()
        cliniqueManager.addPatient()

if __name__ == '__main__':
    cliniqueMain = CliniqueMain()
    cliniqueMain.main()