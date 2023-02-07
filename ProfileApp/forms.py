from django import forms

class ProductForm(forms.Form):

    BRAND_LIST = [('Nike', 'Nike'),
                  ('Puma', 'Puma'),
                  ('Vans', 'Vans'),
                  ('Adidas', 'Adidas'),
                  ('Lacoste', 'Lacoste'),
                  ('Converse', 'Converse'),

                  ]

    COLOR_LIST = [('White', 'White'),
                  ('Black', 'Black'),
                  ('Pink', 'Pink'),
                  ('Brown', 'Brown'),
                  ('Cream', 'Cream'),
                  ('Silver', 'Silver'),

                ]

    TYPE_LIST = [('Sandals', 'Sandals'),#รองเท้าแตะ
                 ('Shoes to wear', 'Shoes to wear'), #รองเท้าสวม
                 ('Canvas', 'Canvas'),#รองเท้าผ้าใบ
                 ('Tongs','Tongs') #รองเท้าคีบ
                ]

    id = forms.CharField(max_length=13, label="รหัสสินค้า", required=True, widget=forms.TextInput(attrs={'size': '15'}))

    brand = forms.CharField(max_length=30, label="ชื่อเเบรนด์", required=True, widget=forms.Select(choices=BRAND_LIST))

    model = forms.CharField(max_length=30, label="ชื่อรุ่น", required=True, widget=forms.TextInput(attrs={'size': '35'}))

    color = forms.CharField(max_length=30, label="สี", required=True, widget=forms.RadioSelect(choices=COLOR_LIST))

    type = forms.CharField(max_length=30, label="ประเภท", required=True, widget=forms.Select(choices=TYPE_LIST))

    price = forms.IntegerField(label="ราคา", required=True, widget=forms.NumberInput(attrs={'size': '35', 'min': '2000', 'max': '100000'}))
