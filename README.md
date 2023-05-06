# Submission Instructions
Sử dụng ngôn ngữ lập trình Python thực hiện cài đặt và giải quyết các bài toán mô tả phía dưới. Chương trình cho mỗi bài nằm trong 01 file được đặt tên `FITSP23msvCNDHW01xx.py`. Khi làm hết bạn có 08 files tương ứng với 08 bài.

Trong đó: 
- msv thay thế bằng mã sinh viên của mình gồm cả chữ và số, phần chữ viết hoa; 
- xx thay bằng hai chữ số sau BN trong bài tương ứng.

Trên đầu các file mã chương trình, thêm phần *comment* trong đo cung cấp thông tin cá nhân:
```
# Họ và tên
# Mã sinh viên
# Nhóm lớp tín chỉ
# Lớp quản lý
# Bài mấy
```
Với mỗi bài giải quyết, kèm theo một file `*.txt` có cùng tên với file mã chương trình trong đó cung cấp các testcase đã thử và các kết quả của các testcase đó theo cấu trúc:
```
# Test case xx
Input
[nội dung input]
Output
[nội dung output]
```

# Assignment Content
## BN01:
Cho một file thông tin bệnh nhân (dữ liệu ở dạng CSV). Nhiệm vụ xây dựng các hàm:
1. Liệt kê danh sách các lựa chọn cho phân hoạch dữ liệu và hình thành cây quyết định
2. Thực hiện xây dựng cây quyết định theo một thứ tự nào đó của danh sách các lựa chọn có được ở phần 1)
3. Ở mỗi bước trong quá trình xây dựng, tính toán IG tương ứng
4. Hiển thị các thông tin hoặc lưu vào file

## BN02:
Một nguồn rời rạc không nhớ được mô tả bằng một từ điển như sau (minh họa cho nguồn có kích thước bằng 4):
```
{
    'source':'X',
    'elsym': ['x_1','x_2','x_3','x_4'],
    'elprob': [0.125,0.25,0.125,0.5]
}
```
Nhiệm vụ xây dựng hàm thực hiện:
1. Mã hóa biểu diễn nguồn theo phương pháp mã hóa Huffman;
2. Sử dụng hàm ở bước 1 thực hiện mã hóa một văn bản ký tự đọc vào từ file *.txt
3. Giải mã cho một chuỗi mã cho trước được nhập từ bàn phím hoặc đọc từ file *.txt;
4. Tính toán các tham số của mã
5. Hiển thị thông tin hoặc lưu vào file

Quá trình mã hóa thực hiện đúng theo thuật toán và có 02 lựa chọn trong bước 2.3 (sắp xếp dãy sau khi nhóm: chìm nhất, trội nhất) Kết quả hàm mã hóa trả về (với sắp xếp trìm nhất):
```
{
    'source':'X',
    'elsym': ['x_1','x_2','x_3','x_4'],
    'elprob': [0.125,0.25,0.125,0.5],
    'elcodeword':['000','01','001','1'],
    'avg_l':1.75,
    'sigma_l_2': 0.6875,
    'isNewLess': 1,
    'isLeftBrachZero':1
}
```
Trong từ điển kết quả:
- elcodeword: danh sách các từ mã tương ứng với các tin, theo đúng thứ tự các tin;
- avg_l: độ dài trung bình từ mã của bộ mã
- sigma_l_2: phương sai độ dài từ mã của bộ mã
- isNewLess: 1 với sắp xếp chìm nhất, ngược lại bằng 0
- isLeftBrachZero: 1 nếu gán nhánh trái bằng 0, nhánh phải bằng 1

## BN03:
Một bộ mã (sản phẩm của một phép mã hóa) được cho ở dạng từ điển:
```
{
    'codename':'C',
    'codewords':['1','01,'001','000']
}
```
Trong đó:
- codename: tên của bộ mã
- codewords: danh sách các từ mã của bộ mã

Nhiệm vụ xây dựng các hàm thực hiện:
1. Cho biết các đặc tính cơ bản của bộ mã: đều/không đều,suy biến hay
không suy biến, minh họa suy biến (nếu có), giải mã duy nhất nhay không,
minh họa giải mã không duy nhất (nếu có), có tính prefix hay không,
minh họa không prefix (nếu có)
2. Bộ mã có phải là mã khối tuyến tính?
3. Tập các véc-tơ mã đã cho có phải là hệ cơ sở
4. Bộ mã đã cho có phải mã vòng (mã cyclic) tuyến tính?
5. Với hai bộ mã, chúng có phải là một (là hoán vị của nhau)


## BN04:
Một ma trận có thể đơn giản biểu diễn bằng kiểu dữ liệu list trong Python
(mặc dù không tối ưu nhưng đổi lại không cần cài thêm thư viện) như sau:
`H = [[1,0,1,1,1,0,0],[0,1,0,1,1,1,0],[0,0,1,0,1,1,1]]`

Tương ứng với:
```
    1 0 1 1 1 0 0
    0 1 0 1 1 1 0
    0 0 1 0 1 1 1
```
Tương tự, một véc-tơ có thể biểu diễn bởi
`c = [1,1,0,1,0,0]` cho trước ma trận kiểm tra H của một mã khối tuyến tính. Nhiệm vụ thực hiện xây dựng hàm:
1. Tìm dmin dựa theo số cột của ma trận kiểm tra H
2. Kiểm tra một vec-tơ cho trước có phải là một vec-tơ mã hợp lệ
3. Liệt kê các từ mã cho bộ mã
4. Tìm dmin theo định nghĩa
5. Tìm dmin theo tính chất của mã khối tuyến tính

## BN05:
Khảo sát các giá trị cho trước trong các trường hợp thiết kế mã khối tuyến
tính, xác định các giới hạn Greismer, Plotkin, Hamming tương ứng và vẽ
đồ thị các giới hạn đó

## BN06:
Một đa thức bậc n có thể mô tả theo 3 cách: 
- (1) véc-tơ các hệ số của đa
thức; 
- (2) vector các hệ số mũ của đa thức; 
- (3) chuỗi các hệ số của đa
thức

Trong các biểu diễn này cũng có thể biểu diễn từ trái sang phải hoặc từ phải sang trái. Ví dụ:

- `isReverse = 1` **# Biểu diễn đảo ngược: MSB ở tận cùng bên phải**
    - `poly01 = [1,0,1,0,1,1,0]` # 1+x^2+x^4+x^5: dạng hệ số đa thức
    - `poly02 = [0,2,4,5]` # 1+x^2+x^4+x^5: dạng hệ số mũ của đa thức
    - `poly03 = "1010110"` # 1+x^2+x^4+x^5: dạng chuỗi các hệ số đa thức

- `isReverse = 0` **# Biểu diễn xuôi: MSB ở tận cùng bên trái**
    - `poly01 = [0,0,1,0,1,1,1]` # 1+x+x^2+x^4: dạng hệ số đa thức
    - `poly02 = [5,4,2,0]` # 1+x^2+x^4+x^5: dạng hệ số mũ của đa thức
    - `poly03 = "1010110"` # x+x^2+x^4+x^6: dạng chuỗi các hệ số đa thức

Nhiệm vụ viết các hàm thực hiện:
1. Liệt kê tất cả các đa tức tối giản (bất khả quy) bậc k (k nhập vào từ bàn phím hoặc đọc từ file)
2. Kiểm tra một đa thức cho trước có phải tối giản hay không
3. Phân tích x^n+1 thành các nhân tử tối giản
4. Liệt kê tất cả các nhân tử (ước số) phân biệt của x^n+1


## BN07:

Cho một mã vòng tuyến tính biểu diễn ở dạng từ điển như sau:
```
{
    'codename':'C',
    'nL':7,
    'poly':[0,1,2,4],
    'isGPoly':0
}
```
Trong đó:
- `codename`: tên của bộ mã
- `nL`: độ dài của các từ mã của bộ mã
- `poly`: da thức tương ứng với bộ mã, có thể là đa thức sinh, hoặc đa thức kiểm tra
- `isGPoly`: 1 nếu poly là đa thức sinh, ngược lại bằng 0

Nhiệm vụ thực hiện viết các hàm:
1. Liệt kê tất cả các tổng kiểm tra có thể có cho mã
2. Kiểm tra xem có phải mã vòng tuyến tính có khả năng trực giao đầy đủ
3. Kiểm tra xem có phải mã vòng tuyến tính có khả năng trực giao
   
## BN08:
Cho một nguồn rời rạc không nhớ kích thước bằng 3 gồm x_1, x_2, và x_3 với các xác suất xuất hiện lần lượt là p, q, r

Nhiệm vụ xây dựng các hàm thực hiện:
1. Với bộ giá trị p, q, r cho trước tính Entropy của nguồn
2. Cho các giá trị p, q, r thay đổi, tính Entropy của tất cả các bộ giá
trị có được của p,q,r. Vẽ đồ thị 3D tập giá trị kết quả thu được theo
p,q,r
3. Cho r = p0 xác định nhưng với tất cả các giá trị cố định có
thể. Với mỗi giá trị của r (p0) tìm tất cả các bộ giá trị của p và q,
tính Entropy tương ứng với các bộ (p,q,p0) tương ứng; trong các giá trị
tính được, tìm giá trị cực đại, gọi là Hp0_max
Vẽ tập giá trị Hp0_max theo p0
