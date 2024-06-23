import subprocess
import os

def derle_ve_calist(dil, dosya_adi, cikti_adi):
    if dil == "assembly":
        # Assembly için NASM derleyici kullanarak derleme işlemi
        derleme_komutu = ["nasm", "-f", "win32", dosya_adi, "-o", cikti_adi + ".obj"]
        linkleme_komutu = ["gcc", cikti_adi + ".obj", "-o", cikti_adi]
    elif dil == "makefile":
        # Makefile için make komutu ile derleme işlemi
        derleme_komutu = ["make"]
        linkleme_komutu = ["./" + cikti_adi]
    elif dil == "java":
        # Java için javac komutu ile derleme işlemi
        derleme_komutu = ["javac", dosya_adi]
        linkleme_komutu = ["java", cikti_adi]
    elif dil == "c":
        # C için cl komutu ile derleme işlemi (Windows)
        derleme_komutu = ["cl", "/Fe:" + cikti_adi, dosya_adi]
        linkleme_komutu = [cikti_adi]
    elif dil == "cpp":
        # C++ için cl komutu ile derleme işlemi (Windows)
        derleme_komutu = ["cl", "/EHsc", "/Fe:" + cikti_adi, dosya_adi]
        linkleme_komutu = [cikti_adi]
    else:
        print("Desteklenmeyen dil: ", dil)
        return
    
    try:
        if dil == "assembly":
            # Assembly için derleme
            result = subprocess.run(derleme_komutu, capture_output=True, text=True, check=True)
            print("Assembly derleme işlemi tamamlandı.")
            # Linkleme ve çalıştırma
            subprocess.run(linkleme_komutu)
        else:
            # Diğer diller için derleme ve çalıştırma
            subprocess.run(derleme_komutu, check=True)
            print(dil.capitalize(), "derleme işlemi tamamlandı.")
            subprocess.run(linkleme_komutu)
        
    except subprocess.CalledProcessError as e:
        print("Derleme veya çalıştırma sırasında bir hata oluştu:")
        print(e.stderr)

# Kullanıcıdan dil, dosya adı ve çıktı adını al
dil = input("Derlenecek programın dilini girin (assembly/makefile/java/c/cpp): ")
dosya_adi = input("Derlenecek dosyanın adını girin: ")
cikti_adi = input("Oluşturulacak programın adını girin: ")

# Fonksiyonu çağırarak derle ve çalıştır
derle_ve_calist(dil, dosya_adi, cikti_adi)
import subprocess
import os

def derle_ve_calist(dil, dosya_adi, cikti_adi):
    if dil == "assembly":
        # Assembly için NASM derleyici kullanarak derleme işlemi
        derleme_komutu = ["nasm", "-f", "win32", dosya_adi, "-o", cikti_adi + ".obj"]
        linkleme_komutu = ["gcc", cikti_adi + ".obj", "-o", cikti_adi]
    elif dil == "makefile":
        # Makefile için make komutu ile derleme işlemi
        derleme_komutu = ["make"]
        linkleme_komutu = ["./" + cikti_adi]
    elif dil == "java":
        # Java için javac komutu ile derleme işlemi
        derleme_komutu = ["javac", dosya_adi]
        linkleme_komutu = ["java", cikti_adi]
    elif dil == "c":
        # C için cl komutu ile derleme işlemi (Windows)
        derleme_komutu = ["cl", "/Fe:" + cikti_adi, dosya_adi]
        linkleme_komutu = [cikti_adi]
    elif dil == "cpp":
        # C++ için cl komutu ile derleme işlemi (Windows)
        derleme_komutu = ["cl", "/EHsc", "/Fe:" + cikti_adi, dosya_adi]
        linkleme_komutu = [cikti_adi]
    else:
        print("Desteklenmeyen dil: ", dil)
        return
    
    try:
        if dil == "assembly":
            # Assembly için derleme
            result = subprocess.run(derleme_komutu, capture_output=True, text=True, check=True)
            print("Assembly derleme işlemi tamamlandı.")
            # Linkleme ve çalıştırma
            subprocess.run(linkleme_komutu)
        else:
            # Diğer diller için derleme ve çalıştırma
            subprocess.run(derleme_komutu, check=True)
            print(dil.capitalize(), "derleme işlemi tamamlandı.")
            subprocess.run(linkleme_komutu)
        
    except subprocess.CalledProcessError as e:
        print("Derleme veya çalıştırma sırasında bir hata oluştu:")
        print(e.stderr)

# Kullanıcıdan dil, dosya adı ve çıktı adını al
dil = input("Derlenecek programın dilini girin (assembly/makefile/java/c/cpp): ")
dosya_adi = input("Derlenecek dosyanın adını girin: ")
cikti_adi = input("Oluşturulacak programın adını girin: ")

# Fonksiyonu çağırarak derle ve çalıştır
derle_ve_calist(dil, dosya_adi, cikti_adi)
