#Initial Database
inventory_database = [
    {'sku_code':'100001',
    'sku_desc':"Indomie  Goreng",
    'division': 'Food',
    'category':'Noodles',
    'stocks_qty':1000,
    'cogs':2500},

    {'sku_code':'100002',
    'sku_desc':"Dragon Floor Mop",
    'division': 'GMS',
    'category':'Mop',
    'stocks_qty':50,
    'cogs': 25000},

    {'sku_code':'100003',
    'sku_desc':"Sendal Jepit Swallow",
    'division': 'Nonfood',
    'category':'Sandal',
    'stocks_qty':80,
    'cogs':10000},

    {'sku_code':'100004',
    'sku_desc':"Nescafe Latte",
    'division': 'Food',
    'category':'Bev',
    'stocks_qty':750,
    'cogs':6300}
]

def navigation_menu():
    print(f"""
    {'_'*100}
    {' '*25}Welcome to Warehouse Inventory Management System{' '*17}
    {'_'*100}
    {" "*100}
    {" "*5}Navigation Menu
    {" "*5}------------------------------------------
    {" "*5}[1]. Mendaftarkan SKU. 
    {" "*5}[2]. Menampilkan Data. 
    {" "*5}[3]. Memperbaharui Data. 
    {" "*5}[4]. Menghapus Data.
    {" "*5}[5]. Exit. [X]
    """)
    input_menu = input("Masukkan menu navigasi yang akan dipilih : ")
    return input_menu

def sub_menu_1():
    print("""Menu Daftar SKU 
    [1]. Daftar SKU.
    [2]. Kembali ke menu utama.
    """)
    input_sub_menu = input("Masukkan menu navigasi yang akan dipilih : ")
    return input_sub_menu

def sub_menu_2():
    print("""Menu Tampilkan Data 
    [1]. Tampilkan Data Stock Gudang Berdasarkan Jumlah Stock Secara Ascending.
    [2]. Tampilkan Data Stock Gudang Berdasarkan Jumlah Stock Secara Descending.
    [3]. Tampilkan Data Stock Gudang Berdasarkan Kode SKU Secara Ascending.
    [4]. Tampilkan Data Stock Gudang Berdasarkan Kode SKU Secara Descending.
    [5]. Kembali ke menu utama.
    """)
    input_sub_menu = input("Masukkan menu navigasi yang akan dipilih : ")
    return input_sub_menu

def sub_menu_3():
    print("""Menu Perbaharui Data 
    [1]. Perbaharui data sku_code.
    [2]. Perbaharui data sku_desc.
    [3]. Perbaharui data division.
    [4]. Perbaharui data category.
    [5]. Perbaharui data COGS.
    [6]. Perbaharui data stocks_qty.
    [7]. Kembali ke menu utama.
    """)
    input_sub_menu = input("Masukkan menu navigasi yang akan dipilih : ")
    return input_sub_menu

def sub_menu_4():
    print("""Menu Hapus Data 
    [1]. Hapus data.
    [2]. Kembali ke menu utama.
    """)
    input_sub_menu = input("Masukkan menu navigasi yang akan dipilih : ")
    return input_sub_menu


def sku_checker(sku):
    indx = -1
    for i in range(len(inventory_database)):
        for key,value in inventory_database[i].items():
            if inventory_database[i]['sku_code'] == sku:
                indx = i #if found then indx is not -1
                break
        if i == indx:
            break
    return indx

def input_data_sku(sku_code, sku_desc, division, category, cogs, qty):
    inventory_database.append({
                    'sku_code' : sku_code,
                    'sku_desc': sku_desc,
                    'division': division,
                    'category' : category,
                    'cogs': cogs,
                    'stocks_qty': qty,
                })
    print("Data berhasil ditambahkan!.")
def perbaharui_sku_code(index, sku_code_baru):
    sku_lama = inventory_database[index]['sku_code']
    inventory_database[index]['sku_code'] = sku_code_baru
    print(f'''
    {100*"="}
    {40*"="} SKU CODE Berhasil Diperbaharui ! {40*"="}
    {100*"="}
    {30*" "}      SKU Sebelumnya \t\t= {sku_lama}
    {30*" "}      SKU Baru \t\t= {sku_code_baru}
    {100*"="}
''')
    
def perbaharui_sku_desc(index, sku_desc_baru):
    sku_lama = inventory_database[index]['sku_desc']
    inventory_database[index]['sku_desc'] = sku_desc_baru
    print(f'''
    {100*"="}
    {40*"="} SKU DESC Berhasil Diperbaharui ! {40*"="}
    {100*"="}
    {30*" "}      SKU Sebelumnya \t\t= {sku_lama}
    {30*" "}      SKU Baru \t\t= {sku_desc_baru}
    {100*"="}
''')
    
def perbaharui_divisi(index, divisi_baru):
    sku_lama = inventory_database[index]['division']
    inventory_database[index]['division'] = divisi_baru
    print(f'''
    {100*"="}
    {40*"="} Divisi Berhasil Diperbaharui ! {40*"="}
    {100*"="}
    {30*" "}      Divisi Sebelumnya \t\t= {sku_lama}
    {30*" "}      Divisi Baru \t\t= {divisi_baru}
    {100*"="}
''')
    
def perbaharui_category(index, category_baru):
    sku_lama = inventory_database[index]['category']
    inventory_database[index]['category'] = category_baru
    print(f'''
    {100*"="}
    {40*"="} Category Berhasil Diperbaharui ! {40*"="}
    {100*"="}
    {30*" "}      Category Sebelumnya \t\t= {sku_lama}
    {30*" "}      Category Baru \t\t= {category_baru}
    {100*"="}
''')
    
def perbaharui_cogs(index, cogs_baru):
    sku_lama = inventory_database[index]['cogs']
    inventory_database[index]['cogs'] = cogs_baru
    print(f'''
    {100*"="}
    {40*"="} COGS Berhasil Diperbaharui ! {40*"="}
    {100*"="}
    {30*" "}      COGS Sebelumnya \t\t= {sku_lama}
    {30*" "}      COGS Baru \t\t= {cogs_baru}
    {100*"="}
''')
    
def perbaharui_qty(index, qty_baru):
    sku_lama = inventory_database[index]['stocks_qty']
    inventory_database[index]['stocks_qty'] = qty_baru
    print(f'''
    {100*"="}
    {40*"="} Qty Stocks Berhasil Diperbaharui ! {40*"="}
    {100*"="}
    {30*" "}      Qty Stocks Sebelumnya \t\t= {sku_lama}
    {30*" "}      Qty Stocks Baru \t\t= {qty_baru}
    {100*"="}
''')



def show_stocks_by_qty_asc():
    list_kosong=[]
    for i in range(len(inventory_database)):
        for key,value in inventory_database[i].items(): 
            if key == "stocks_qty":
                list_kosong.append(
                    [
                        inventory_database[i]["stocks_qty"], 
                        inventory_database[i]["sku_code"],
                        inventory_database[i]["sku_desc"],
                        inventory_database[i]["division"],
                        inventory_database[i]["category"],
                        inventory_database[i]["cogs"]
                ]) 
    list_kosong.sort() #List kosong di sort
    print("="*130)
    print()
    print(f"{'_'*53} INVENTORY TABLE {'_'*70}")
    print(f"{'_'*140}")
    print(f"{' '*10} Urutan |{' '*4}  Divisi     |{' '*5} SKU_CODE       |      QTY     |      COGS   ")
    print(f"{'-'*140}")
    for i in range(len(list_kosong)):
        print(f"{' '* 5}       ke-{i+1}. \t{list_kosong[i][3]}\t        \t{list_kosong[i][1]}  \t   {list_kosong[i][0]}\t   \t {list_kosong[i][5]} ") #Menampilkan data siswa yang berasal dari list kosong
    print(f"{'-'*140}")
    print(f"{'_'*105} ORDERED BY QTY ASCENDING")
    list_kosong=[] #Mengosongkan kembali list kosong

def show_stocks_by_qty_desc():
    list_kosong=[]
    for i in range(len(inventory_database)):
        for key,value in inventory_database[i].items(): 
            if key == "stocks_qty":
                list_kosong.append(
                    [
                        inventory_database[i]["stocks_qty"], 
                        inventory_database[i]["sku_code"],
                        inventory_database[i]["sku_desc"],
                        inventory_database[i]["division"],
                        inventory_database[i]["category"],
                        inventory_database[i]["cogs"]
                ]) 
    list_kosong.sort(reverse=True) #List kosong di sort
    print("="*130)
    print()
    print(f"{'_'*53} INVENTORY TABLE {'_'*70}")
    print(f"{'_'*140}")
    print(f"{' '*10} Urutan |{' '*4}  Divisi     |{' '*5} SKU_CODE       |      QTY     |      COGS   ")
    print(f"{'-'*140}")
    for i in range(len(list_kosong)):
        print(f"{' '* 5}       ke-{i+1}. \t{list_kosong[i][3]}\t        \t{list_kosong[i][1]}  \t   {list_kosong[i][0]}\t   \t {list_kosong[i][5]} ") #Menampilkan data siswa yang berasal dari list kosong
    print(f"{'-'*140}")
    print(f"{'_'*105} ORDERED BY QTY DESCENDING")
    list_kosong=[] #Mengosongkan kembali list kosong


def show_stocks_by_code_asc():
    list_kosong=[]
    for i in range(len(inventory_database)):
        for key,value in inventory_database[i].items(): 
            if key == "stocks_qty":
                list_kosong.append(
                    [
                        inventory_database[i]["sku_code"],
                        inventory_database[i]["stocks_qty"], 
                        inventory_database[i]["sku_desc"],
                        inventory_database[i]["division"],
                        inventory_database[i]["category"],
                        inventory_database[i]["cogs"]
                ]) 
    list_kosong.sort() #List kosong di sort
    print("="*130)
    print()
    print(f"{'_'*53} INVENTORY TABLE {'_'*70}")
    print(f"{'_'*140}")
    print(f"{' '*10} Urutan |{' '*4}  Divisi     |{' '*5} SKU_CODE       |      QTY     |      COGS   ")
    print(f"{'-'*140}")
    for i in range(len(list_kosong)):
        print(f"{' '* 5}       ke-{i+1}. \t{list_kosong[i][3]}\t        \t{list_kosong[i][0]}  \t   {list_kosong[i][1]}\t   \t {list_kosong[i][5]} ") #Menampilkan data siswa yang berasal dari list kosong
    print(f"{'-'*140}")
    print(f"{'_'*105} ORDERED BY QTY DESCENDING")
    list_kosong=[] #Mengosongkan kembali list kosong
def show_stocks_by_code_desc():
    list_kosong=[]
    for i in range(len(inventory_database)):
        for key,value in inventory_database[i].items(): 
            if key == "stocks_qty":
                list_kosong.append(
                    [
                        inventory_database[i]["sku_code"],
                        inventory_database[i]["stocks_qty"], 
                        inventory_database[i]["sku_desc"],
                        inventory_database[i]["division"],
                        inventory_database[i]["category"],
                        inventory_database[i]["cogs"]
                ]) 
    list_kosong.sort(reverse=True) #List kosong di sort
    print("="*130)
    print()
    print(f"{'_'*53} INVENTORY TABLE {'_'*70}")
    print(f"{'_'*140}")
    print(f"{' '*10} Urutan |{' '*4}  Divisi     |{' '*5} SKU_CODE       |      QTY     |      COGS   ")
    print(f"{'-'*140}")
    for i in range(len(list_kosong)):
        print(f"{' '* 5}       ke-{i+1}. \t{list_kosong[i][3]}\t        \t{list_kosong[i][0]}  \t   {list_kosong[i][1]}\t   \t {list_kosong[i][5]} ") #Menampilkan data siswa yang berasal dari list kosong
    print(f"{'-'*140}")
    print(f"{'_'*105} ORDERED BY CODE DESCENDING")
    list_kosong=[] #Mengosongkan kembali list kosong

def delete_sku(index):
    del inventory_database[index]
    print("Data berhasil dihapus!")
def main_app():
    while navigation_menu!= '5':
        input_menu = navigation_menu()
        if input_menu == '1':
            input_sub_menu = sub_menu_1()
            while input_sub_menu not in ['1','2']:
                print(f"{20*'='} Silahkan masukkan menu sesuai dengan pilihan yang tersedia. {20*'='}")
                input_sub_menu = sub_menu_1()
            if input_sub_menu == '1':
                input_sku = input("Masukkan kode SKU : ")
                sku = sku_checker(input_sku)
                sku_numeric  = input_sku.isnumeric()
                #print(sku)
                while sku != -1 or (len(input_sku) > 6) or sku_numeric == False:
                    if sku != -1 :
                        print("SKU sudah terdaftar, silahkan masukkan kode SKU dengan angka lain")
                    elif len(input_sku)>6 or sku_numeric == False:
                        print("Input harus numerik dan tidak lebih dari 6 angka!")
                    input_sku = input("Masukkan kode SKU : ")
                    sku = sku_checker(input_sku)
                    sku_numeric  = input_sku.isnumeric()
                input_sku_desc = input("Masukkan SKU Description : ")
                input_division = input("Masukkan Divisi : ")
                input_category = input("Masukkan Category : ")
                input_cogs = input("Masukkan COGS : ")
                cogs_numeric  = input_cogs.isnumeric()
                
                while (cogs_numeric == False or input_cogs <= '0'):
                    if cogs_numeric == False:
                        print("COGS harus bilangan numerik.")
                    elif input_cogs <= '0' :
                        print("Costs of goods sold (HPP) tidak dapat diinput dengan nilai 0 atau bilangan negatif.")
                        
                    input_cogs = input("Masukkan COGS : ")
                    cogs_numeric  = input_cogs.isnumeric()

                input_qty = input("Masukkan Qty Awal : ")
                qty_numeric = input_qty.isnumeric()
                while (qty_numeric == False or input_qty <= '0'):
                    if qty_numeric == False:
                        print("Costs of goods sold (HPP) tidak dapat diinput dengan nilai 0 atau bilangan negatif.")
                    elif input_qty <= '0' :
                        print("COGS harus bilangan numerik.")
                    input_qty = input("Masukkan Qty Awal : ")
                    qty_numeric  = input_qty.isnumeric()
                input_data_sku(input_sku, input_sku_desc, input_division, input_category, input_cogs, input_qty)
            elif input_sub_menu=='2':
                input_menu = navigation_menu()
        elif input_menu =='2':
            input_sub_menu = sub_menu_2()
            while input_sub_menu not in ['1','2','3','4','5']:
                print(f"{20*'='} Silahkan masukkan menu sesuai dengan pilihan yang tersedia. {20*'='}")
                input_sub_menu = sub_menu_2()
            if input_sub_menu =='1':
                show_stocks_by_qty_asc()
            if input_sub_menu =='2':
                show_stocks_by_qty_desc()
            if input_sub_menu =='3':
                show_stocks_by_code_asc()
            if input_sub_menu =='4':
                show_stocks_by_code_desc()
            if input_sub_menu =='5':
                input_menu = navigation_menu()
        elif input_menu =='3':
            input_sub_menu = sub_menu_3()
            while input_sub_menu not in ['1','2','3','4','5','6','7']:
                print(f"{20*'='} Silahkan masukkan menu sesuai dengan pilihan yang tersedia. {20*'='}")
                input_sub_menu = sub_menu_3()
            if input_sub_menu == '1': #SKU CODE
                input_sku = input("Masukkan kode SKU : ")
                sku = sku_checker(input_sku)
                if sku == -1:
                    print("SKU tidak ditemukan")
                else:
                    update_sku = input("Masukkan Kode SKU yang baru : ")
                    u_sku = sku_checker(update_sku)
                    u_sku_numeric = update_sku.isnumeric()
                    while (len(update_sku) > 6) or u_sku_numeric == False:
                        update_sku = input("Masukkan Kode SKU yang baru : ")
                        u_sku = sku_checker(update_sku)
                    if u_sku == -1:
                        perbaharui_sku_code(sku, update_sku)
                    else:
                        print("SKU Code Baru Sudah Ada dalam database, silahkan menggunakan kode sku yang lain!")
    # [1]. Perbaharui data sku_code.
    # [2]. Perbaharui data sku_desc.
    # [3]. Perbaharui data division.
    # [4]. Perbaharui data category.
    # [5]. Perbaharui data COGS.5
    # [6]. Perbaharui data stocks_qty.
    # [7]. Kembali ke menu utama.
            elif input_sub_menu == '2':
                input_sku = input("Masukkan kode SKU : ")
                sku = sku_checker(input_sku)
                if sku == -1:
                    print("SKU tidak ditemukan")
                else:
                    input_sku_desc_baru = input("Masukkan SKU Description baru : ")
                    perbaharui_sku_desc(sku, input_sku_desc_baru)
            elif input_sub_menu == '3':
                input_sku = input("Masukkan kode SKU : ")
                sku = sku_checker(input_sku)
                if sku == -1:
                    print("SKU tidak ditemukan")
                else:
                    input_divisi_baru = input("Masukkan Division baru : ")
                    perbaharui_divisi(sku, input_divisi_baru)
            elif input_sub_menu == '4':
                input_sku = input("Masukkan kode SKU : ")
                sku = sku_checker(input_sku)
                if sku == -1:
                    print("SKU tidak ditemukan")
                else:
                    input_category_baru = input("Masukkan Category baru : ")
                    perbaharui_category(sku, input_category_baru)
            elif input_sub_menu == '5':
                input_sku = input("Masukkan kode SKU : ")
                sku = sku_checker(input_sku)
                if sku == -1:
                    print("SKU tidak ditemukan")
                else:
                    input_cogs_baru = input("Masukkan COGS yang baru : ")
                    cogs_status = input_cogs_baru.isnumeric()
                    while (cogs_status == False or input_cogs_baru <= '0'):
                        if cogs_status == False:
                            print("COGS harus bilangan numerik.")
                        elif input_cogs_baru <= '0' :
                            print("Costs of goods sold (HPP) tidak dapat diinput dengan nilai 0 atau bilangan negatif.")
                        input_cogs_baru = input("Masukkan COGS yang baru : ")
                        cogs_status  = input_cogs_baru.isnumeric()
                    perbaharui_cogs(sku,input_cogs_baru)
            elif input_sub_menu == '6':
                input_sku = input("Masukkan kode SKU : ")
                sku = sku_checker(input_sku)
                if sku == -1:
                    print("SKU tidak ditemukan")
                else:
                    input_qty_baru = input("Masukkan Qty yang baru : ")
                    qty_status = input_qty_baru.isnumeric()
                    while (qty_status == False or input_qty_baru <= '0'):
                        if qty_status == False:
                            print("Qty harus bilangan numerik.")
                        elif input_qty_baru < '0' :
                            print("Qty tidak dapat diinput dengan bilangan negatif.")
                        input_qty_baru = input("Masukkan Qty yang baru : ")
                        qty_status  = input_qty_baru.isnumeric()
                    perbaharui_qty(sku,input_qty_baru)

            elif input_sub_menu =='7':
                input_menu = navigation_menu()
        elif input_menu =='4':
            input_sub_menu = sub_menu_4()
            while input_sub_menu not in ['1','2']:
                print(f"{20*'='} Silahkan masukkan menu sesuai dengan pilihan yang tersedia. {20*'='}")
                input_sub_menu = sub_menu_4()
            if input_sub_menu == '1':
                input_sku = input("Masukkan kode SKU yang Akan Dihapus : ")
                sku = sku_checker(input_sku)
                if sku == -1:
                    print("SKU tidak ditemukan!")
                else :
                    print('''Apakah anda yakin akan menghapus data ? 
                    [Y] Menghapus Data
                    [N] Tidak Menghapus Data
                    ''')
                    input_validation_menu = input("Masukkan Pilihan : Y/N")
                    while input_validation_menu not in ['Y','y','N','n']:
                        print(f"{20*'='} Silahkan masukkan menu sesuai dengan pilihan yang tersedia. {20*'='}")
                        print('''Apakah anda yakin akan menghapus data ? 
                    [Y] Menghapus Data
                    [N] Tidak Menghapus Data
                    ''')
                        input_validation_menu = input("Masukkan Pilihan : Y/N")
                    if input_validation_menu in ['Y','y']:
                        delete_sku(sku)
                    else :
                        print("Data tidak jadi dihapus. Kembali ke menu utama.")
                        input_menu = navigation_menu()
                        

            elif input_sub_menu == '2':
                input_menu = navigation_menu()
        elif input_menu=='5':
            break
        else:
            print("Masukkan input sesuai dengan pilihan yang tersedia!.")
            navigation_menu()
main_app()
#show_stocks_by_qty_asc()
#navigation_menu()
#show_stocks_by_code_desc()