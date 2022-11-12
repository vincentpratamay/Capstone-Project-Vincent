list_pasien = [
    ['Andy', 27, 'Laki-laki'],
    ['Bagas', 22, 'Laki-laki'],
    ['Susi', 16, 'Perempuan'],
    ['Anto', 29, 'Laki-laki'],
    ['Intan', 33, 'Perempuan']
]

while True:
    pilihan_menu = input('''
        Selamat Datang di Rumah Sakit Anugerah

        List Menu:
        1. Menampilkan Daftar Pasien
        2. Menambah Pasien
        3. Menghapus Pasien
        4. Exit Program

        Masukkan angka menu yang ingin dijalankan: ''')

    if(pilihan_menu == '1'):

        print('Daftar Pasien\n')
        print('Index\t| Nama  \t| Usia\t| Jenis Kelamin')
        
        for i in range(len(list_pasien)):
            print(f'{i}\t| {list_pasien[i][0]}  \t| {list_pasien[i][1]}\t| {list_pasien[i][2]}')

    elif(pilihan_menu == '2'):

        while True:
            nama_pasien = input('Masukkan nama pasien: ').capitalize()
            umur_pasien = int(input('Masukkan umur pasien: '))
            jenis_kelamin_pasien = input('Masukkan jenis kelamin pasien: ')

            print('\nTambahkan data pasien pada database? (Y/N)')
            user_input = input('\nKetik Y jika Anda yakin, N untuk batalkan: ').upper()
  
            if user_input == 'Y':
                break
            elif user_input == 'N':
                continue
            else:
                print('Input yang Anda masukkan invalid.')
                  
        for pasien in range(len(list_pasien)):
            if (list_pasien[pasien][0] == nama_pasien) and (list_pasien[pasien][2] == umur_pasien):
                list_pasien[pasien][1] += jenis_kelamin_pasien
                break
        else:
            list_pasien.append([nama_pasien, umur_pasien, jenis_kelamin_pasien])
            break
        
        print('Daftar Pasien\n')
        print('Index\t| Nama  \t| Umur\t| Jenis Kelamin')
        
        for i in range(len(list_pasien)):
            print(f'{i}\t| {list_pasien[i][0]}  \t| {list_pasien[i][1]}\t| {list_pasien[i][2]}')

    elif(pilihan_menu == '3'):

        print('Daftar Pasien\n')
        print('Index\t| Nama  \t| Umur\t| Jenis Kelamin')
        
        for i in range(len(list_pasien)):
            print(f'{i}\t| {list_pasien[i][0]}  \t| {list_pasien[i][1]}\t| {list_pasien[i][2]}')

        while True:
            index_pasien = input('Masukkan index pasien yang ingin dihapus: ')
            if index_pasien.isdigit() == False:
                index_pasien
            else:
                index_pasien = int(index_pasien)
                if index_pasien not in range(len(list_pasien)):
                    print(f'Tidak ada index {index_pasien} pada database. Silakan masukkan angka index yang sesuai.')
                else:
                    print('\nHapus data pasien dari database? (Y/N)')
                    user_input = input('\nKetik Y jika Anda yakin, N untuk batalkan: ').upper()
                
                    if user_input == 'Y':
                        break
                    elif user_input == 'N':
                        index_pasien
                    else:
                        user_input

        del list_pasien[index_pasien]

        print('Daftar Pasien\n')
        print('Index\t| Nama  \t| Umur\t| Jenis Kelamin')
        
        for i in range(len(list_pasien)):
            print(f'{i}\t| {list_pasien[i][0]}  \t| {list_pasien[i][1]}\t| {list_pasien[i][2]}')
              
    elif(pilihan_menu == '4'):
        break