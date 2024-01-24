# PythonDjango
 
Các thư viện cần cài:
 - pip install django
 - pip install pymysql
 - pip install mysqlclient

Các VS Code Plugin cần cài:
 - python
 - HTML BoilerPlate
 - CSS Peak

Các câu lệnh:

django-admin startproject name
django-admin startapp name
python manage.py migrate
python manage.py runserver host:port


Các khái niệm về models và cách django tự động hóa mối quan hệ giữa các models thành database scheme:

 - models: là các Python Class đóng vai trò là các đối tượng chính trong app của bạn. models mang tính chất, hành vi giống như những môi trường khác như java spring...
 - Khi định nghĩa models, bạn có thể tạo lập mối quan hệ giữa các models qua biến ForeigKey để sau đó báo hiệu cho django rằng đây là một mối quan hệ giữa 2(trở lên) models
 - Chạy lệnh $python manage.py migrate ngay sau đó sẽ khiến django yêu cầu database tạo dựng các bảng, với mỗi model tương ứng là một bảng, mỗi field trong model sẽ là một column, và primary key sẽ tự động được tạo, và giá trị dưới dạng số integer có tính chất increment.
 - Lúc này trong Database thì các bảng sẽ tự động có mối quan hệ với nhau thông qua foreign key.
 - Django cung cấp sẵn loạt API để điều khiển các models giúp khởi tạo, xóa, thêm, thay đổi các records vào database
  
 
 Tổng quan về một Projects:
  - để tạo project, chúng ta mở cmd/powershell và chạy lệnh "django-admin startproject name" trong đó name tùy chọn, và django-admin đã nằm sẵn trong path của Windows sau khi chúng ta cài Django bằng lệnh pip install django
   - project sau khi khởi tạo bao gồm các thư mục **như trong bộ explorer
