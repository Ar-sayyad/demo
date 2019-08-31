# class Accident(Exception):
#     def __init__(self,msg):
#         self.msg = msg
#
#     def print_exception(self):
#         print("User Defined exception: ",self.msg)
#
# try:
#     raise Accident('Crash between two Vehicles')
# except Accident as e:
#     e.print_exception()

def process_file():
    try:
        f = open("d:\\Python\\data\\book.txt","r")
        s = f.read()
        print(s)
    except FileNotFoundError as e:
        print("Inside Except")
    finally:
        print("cleaning up file")
        f.close()

process_file()
