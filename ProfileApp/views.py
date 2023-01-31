from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
def personal(request):
    return render(request, 'personal.html')
def sale(request):
    return render(request,'sale.html')
def interests (request):
    return render(request, 'interests.html')
def educational(request):
    return render(request, 'educational.html')
def rolemodel(request):
    return render(request, 'rolemodel.html')
def showMyData(request):
    showID = '65342310263-8'
    showName = "จินตนา รัตนะวัน"
    showAddress = "106/1 หมู่ 4 ต.หนองอึ่ง อ.ราษีไศล จ.ศรีสะเกษ"
    showtel = "0957104776"
    showgender = "หญิง"
    showBirthday = "09 มีนาคม 2544"
    showWeight = 53
    showHeight = 154
    showstatus = "นักศึกษา"
    showSchool = "มหาวิทยาลัยเทคโนโลยีราชมงคลอีสาน วิทยาเขตขอนแก่น"

    products = []

    product =['บรู๊ค',500.00,'../../static/images/a1.png']
    products.append(product)
    product =['แฟรงกี้', 400.00, '../../static/images/b2.png']
    products.append(product)
    product =['โลบิ้', 200.00, '../../static/images/c3.png']
    products.append(product)
    product =['นามิ', 650.00, '../../static/images/d4.png']
    products.append(product)
    product =['จินเบน', 350.00, '../../static/images/e5.png']
    products.append(product)
    product = ['เปอร์', 250.00, '../../static/images/f6.png']
    products.append(product)
    product = ['ช็อป', 600.00, '../../static/images/g7.png']
    products.append(product)
    product = ['อูซบ', 750.00, '../../static/images/h8.png']
    products.append(product)
    product = ['ซันจิ', 820.00, '../../static/images/i9.png']
    products.append(product)
    product = ['ลูฟี่', 730.00, '../../static/images/qq10.png']
    products.append(product)

    context = {'showID': showID, 'showName': showName, 'showAddress': showAddress, 'showtel': showtel,
               'showgender': showgender, 'showBirthday': showBirthday, 'showWeight': showWeight, 'showHeight': showHeight,
               'showstatus': showstatus, 'showSchool': showSchool, 'products': products}
    return render(request, 'showMyData.html', context)
