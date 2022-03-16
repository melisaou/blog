# blog

### Instruksi menjalankan aplikasi secara lokal
1. Jalankan **git clone https://github.com/melisaou/blog.git**
2. Masuk ke direktori repo tersebut dan buat virtual environment dengan command<br>
**python -m venv env**
3. Aktifkan virtual environment dan install package yang diperlukan dengan command
(untuk Windows)<br>
**env\Scripts\activate.bat** atau **env\Scripts\activate.ps1** (pada
PowerShell)<br>
**pip install -r requirements.txt**
4. Jalankan web secara lokal dengan command<br>
**python manage.py runserver**
5. Akses server web lokal menggunakan web browser dengan address
http://localhost:8000/ <br>
*) Hanya superuser saja yang dapat menambahkan postingan blog melalui Django
site admin (http://localhost:8000/admin) atau melalui website itu sendiri
dengan login terlebih dahulu <br>
Untuk membuat superuser, jalankan **python manage.py createsuperuser**
6. Ketika sudah selesai, nonaktifkan virtual environment dengan command
**deactivate**

### Catatan
* Saya menggunakan versi Python 3.8.5 dan Django 3.2.7
* Website ini juga sudah di-deploy pada Heroku (https://melisaou.herokuapp.com/)
