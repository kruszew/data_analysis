import sys
import tkinter as tk

column_to_compare = "Age"
# root = tk.Tk()
if len(sys.argv) > 1:
    file_path = sys.argv[1]

def main():
    if len(sys.argv) != 2:
        print("Podaj plik lub kolumne do programu")
        exit_program()
    check_if_column_exist()
    count_tab()
    menu()
    # root.mainloop()
    

def get_headers(file_path): #tablica z nagłówkami
    with open(file_path, 'r') as file:
        for item in file:
            no_white_space = item.strip()
            list = no_white_space.split(",")
            break
        return list
        
def get_column_number():
    list1 = get_headers(file_path)
    i = 0
    for num in range(0, len(list1) - 1):
        if list1[num] == column_to_compare:
            column_number = i
        else:
            i+= 1

    return column_number

def check_if_column_exist():
    list2 = get_headers(file_path)
    if column_to_compare not in list2:
        print(f"No column named {column_to_compare}")
        exit_program()

def exit_program():
    print("exiting program")
    sys.exit(0)

def get_tab(): #tablica z wartościami 
    tab = []
    try:
            
            name = column_to_compare
            column_number = get_column_number()
            with open(file_path, 'r') as file:
                for item in file:
                    no_white_space = item.strip()
                    list = no_white_space.split(",")
                    if list[column_number] == name:
                        continue
                    elif list[column_number] not in tab:
                        tab.append(list[column_number])
                        tab.sort() 
            return tab

    except FileNotFoundError:
        print(f"nie ma takiego pliku jak {file_path}")
    except Exception as e:
        print(e)

def count_tab():
    name = column_to_compare
    tab_with_all = []
    column_number = get_column_number()
    with open(file_path, 'r') as file:
            for item in file:
                no_white_space = item.strip()
                list = no_white_space.split(",")
                if list[column_number] == name:
                    continue
                else: 
                    tab_with_all.append(list[column_number])
                    tab_with_all.sort()
    iterator_marks = iter(tab_with_all)
    k = 0
    max = 0
    previous = tab_with_all[0]
    for i in range(0, len(tab_with_all)):
        mark = str(next(iterator_marks))
        if previous == NotImplemented:
            continue
        elif mark != previous:
            print("liczba: " + previous)
            if k > max:
                name_of_the_max = previous
                max = k
            print(k)
            k = 0
        k += 1
        if i == len(tab_with_all) - 1:
            print("liczba: " + mark)
            if k > max:
                name_of_the_max = mark
                max = k
            print(k)
        previous = mark
    print("Najwięcej jest: " + name_of_the_max)
    print(max)

def show_rows(columns):
    print(columns)
    name = column_to_compare
    column_number = get_column_number()
    with open(file_path, 'r') as file:
            for item in file:
                no_white_space = item.strip()
                list = no_white_space.split(",")
                if list[column_number] == name:
                    continue

def menu():
    while True:
        print("-----MENU-----")
        print("Wyświetl informację i policz 1 wartość")
        choice = input("wybierz opcję: ")
        match  choice:
            case "1":
                print(get_headers(file_path))
                choose_headers_to_show = input("wybierz które kolumny mają się wyświetlić: ")
                choosen = choose_headers_to_show.split(" ")
                show_rows(choosen)
                
        
 #POMYSŁY
 #1 najczęstszy wiek w bazie danych z wykresem 5 najczęstszych
 #2 wykres 
main()


