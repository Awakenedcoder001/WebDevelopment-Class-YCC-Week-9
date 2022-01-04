import csv
def csv_operator():
    write_file= open("writting1.txt", 'w')
    scv_writer= csv.writer(write_file)
    scv_writer.writerow(["Favourite Hero\n", "Favourite food\n", "favourite song \n", "favouriter post\n", "favouriter place\n", "favourite person"])
    print("all the datas are here")
    
if __name__ == '__main__':
    csv_operator()

    