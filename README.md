DSS-Django
==========

Ini adalah "Sistem Pendukung Keputusan Pemberian Beasiswa Menggunakan Metode Profile Matching" berbasis Django.


![Data Ranking](http://i59.tinypic.com/2isegzq.png "Data Ranking")


![Tambah Data](http://i57.tinypic.com/6oe6fq.png "Tambah Data")




Requirement
-----------


- Python 2.7


Install semua modul yang dibutuhkan menggunakan pip,


- Django
- South
- Django-Suit
- Django-Tables2
- Python-Psycopg2
- Bootstrap 3


Install
-------

Setelah membuat database di local, dan men-stup file Settings.py, ketik perintah2 berikut :

`$ git clone https://github.com/alzearafat/DSS-Django.git`

`cd DSS-Django`

`$ python manage.py syncdb`

`$ python manage.py schemamigration --intial mahasiswa`

`$ python manage.py migrate mahasiswa --fake`

`$ python manage.py migrate mahasiswa`

`$ python manage.py runserver`

DONE!


Special Thanks
--------------

Puty Syakira  <3
