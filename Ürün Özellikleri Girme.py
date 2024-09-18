#Doğrulama Kodu
import requests
from bs4 import BeautifulSoup
url = "https://docs.google.com/spreadsheets/d/1AP9EFAOthh5gsHjBCDHoUMhpef4MSxYg6wBN0ndTcnA/edit#gid=0"
response = requests.get(url)
html_content = response.content
soup = BeautifulSoup(html_content, "html.parser")
first_cell = soup.find("td", {"class": "s2"}).text.strip()
if first_cell != "Aktif":
    exit()
first_cell = soup.find("td", {"class": "s1"}).text.strip()
print(first_cell)


import pandas as pd
import os
import requests
from colorama import init, Fore, Style
import warnings
from io import BytesIO

warnings.filterwarnings("ignore")

pd.options.mode.chained_assignment = None

init(autoreset=True)

print("Oturum Açma Başarılı Oldu")
print(" /﹋\ ")
print("(҂`_´)")
print(Fore.RED + "<,︻╦╤─ ҉ - -")
print("/﹋\\")
print("Mustafa ARI")
print(" ")



google_sheet_url = "https://docs.google.com/spreadsheets/d/1ECaRelQHEfEarkQHcapdjd9o1I_Ut2MvjnTYca8BHQ0/gviz/tq?tqx=out:csv"

try:
    google_df = pd.read_csv(google_sheet_url)
    google_excel_file = "E-Tablo Verileri.xlsx"
    
    # 2. ve 16. sütunlar dışındaki sütunları al
    columns_to_keep = [col for col_idx, col in enumerate(google_df.columns) if col_idx in [1, 15]] 
    
    # Veri çerçevesini istenilen sütunlarla sınırla
    google_df = google_df[columns_to_keep]
    
    # "Formül" sütununu 1. sütun olarak ayarla
    google_df = google_df.rename(columns={google_df.columns[1]: 'Formül'})
    
    # 1. sütundaki boş hücreleri içeren satırları sil
    google_df = google_df.dropna(subset=[google_df.columns[1]])
    
    # 0. sütundaki verilere başına "m1." ekle
    google_df.iloc[:, 0] = 'm1.' + google_df.iloc[:, 0].astype(str)
    
    # 0. sütundaki hücrelerde sondan 1. karakter "." değilse sonuna bir "." ekle
    google_df.iloc[:, 0] = google_df.iloc[:, 0].apply(lambda x: x if x[-1] == '.' else x + '.')

    # 0. sütunun adını "ModelKodu" olarak değiştir
    google_df.rename(columns={google_df.columns[0]: 'ModelKodu'}, inplace=True)
    
    # 1. sütunun adını "Aciklama" olarak değiştir
    google_df.rename(columns={google_df.columns[1]: 'Aciklama'}, inplace=True)

    # Verileri Excel dosyasına kaydet
    google_df.to_excel(google_excel_file, index=False)
except Exception as e:
    print("Bir hata oluştu:", e)







# İndirilecek linkler
links = [
    "https://task.haydigiy.com/FaprikaXls/RADSBM/1/",
    "https://task.haydigiy.com/FaprikaXls/RADSBM/2/",
    "https://task.haydigiy.com/FaprikaXls/RADSBM/3/"
]

# Excel dosyalarını indirip birleştirme
dfs = []
for link in links:
    response = requests.get(link)
    if response.status_code == 200:
        # BytesIO kullanarak indirilen veriyi DataFrame'e dönüştürme
        df = pd.read_excel(BytesIO(response.content))
        dfs.append(df)

# Tüm DataFrame'leri birleştirme
merged_df = pd.concat(dfs, ignore_index=True)

# Sonuç DataFrame'ini tek bir Excel dosyasına yazma
merged_df.to_excel("Ürün Özellikleri.xlsx", index=False)

# Önce Excel dosyasını okuyalım
excel_file = "Ürün Özellikleri.xlsx"
df_merged = pd.read_excel(excel_file)

# 'Aciklama' sütunundaki dolu olan satırları filtrele
df_merged = df_merged[df_merged['Aciklama'].isna()]

# Güncellenmiş DataFrame'i aynı Excel dosyasının üstüne yaz
df_merged.to_excel('Ürün Özellikleri.xlsx', index=False)








# "sonuc_excel" dosyasını oku
sonuc_excel_file = "Ürün Özellikleri.xlsx"
sonuc_df = pd.read_excel(sonuc_excel_file)

# "E-Tablo Verileri" dosyasını oku
e_tablo_excel_file = "E-Tablo Verileri.xlsx"
e_tablo_df = pd.read_excel(e_tablo_excel_file)

# "ModelKodu" sütununda eşleşen satırları bul ve "Aciklama" sütununu kopyala
for index, row in sonuc_df.iterrows():
    model_kodu = row["ModelKodu"]
    e_tablo_row = e_tablo_df[e_tablo_df["ModelKodu"] == model_kodu]
    if not e_tablo_row.empty:
        sonuc_df.at[index, "Aciklama"] = e_tablo_row.iloc[0]["Aciklama"]

# Sonucu kaydet
sonuc_df.to_excel("Ürün Özellikleri.xlsx", index=False)






# Önce Excel dosyasını okuyalım
excel_file = "Ürün Özellikleri.xlsx"
df = pd.read_excel(excel_file)

# "Aciklama" sütununda dolu olan satırları bulalım
filtered_df = df.dropna(subset=["Aciklama"])

# Filtrelenmiş DataFrame'i başka bir Excel dosyasına kaydedelim
filtered_excel_file = "Ürün Özellikleri.xlsx"
filtered_df.to_excel(filtered_excel_file, index=False)



# Dosyayı sil
os.remove("E-Tablo Verileri.xlsx")



