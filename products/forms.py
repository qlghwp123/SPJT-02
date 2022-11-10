from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        self.fields["title"].label = "제품명"
        self.fields["title"].widget.attrs.update(
            {
                "placeholder": "제품명을 입력해주세요.",
                "class": "form-control",
                "id": "form_title",
                "autofocus": True,
                "style": "width: 91%;",
            }
        )
        self.fields["price"].label = "가격"
        self.fields["price"].widget.attrs.update(
            {
                "placeholder": "가격을 입력해주세요.",
                "class": "form-control",
                "id": "form_title",
                "style": "width: 91%;",
            }
        )
        self.fields["description"].label = "제품 설명"
        self.fields["description"].widget.attrs.update(
            {
                "placeholder": "제품 설명을 입력해주세요.",
                "class": "form-control",
                "id": "form_title",
                "style": "width: 91%;",
            }
        )
        self.fields["stock"].label = "재고"
        self.fields["stock"].widget.attrs.update(
            {
                "placeholder": "재고를 입력해주세요.",
                "class": "form-control",
                "id": "form_title",
                "style": "width: 91%; height:40%;",
            }
        )
        self.fields["sales_rate"].label = "할인율"
        self.fields["sales_rate"].widget.attrs.update(
            {
                "placeholder": "재고를 입력해주세요.",
                "class": "form-control",
                "id": "form_title",
                "style": "width: 91%;",
            }
        )
        self.fields["produt_thum_img"].label = "상품 사진"
        self.fields["produt_thum_img"].widget.attrs.update(
            {
                "placeholder": "상품 대표 사진을 업로드 해주세요.",
                "class": "form-control",
                "id": "form_title",
                "style": "width: 91%;",
            }
        )
        self.fields["produt_desc_img"].label = "성분 사진"
        self.fields["produt_desc_img"].widget.attrs.update(
            {
                "placeholder": "상품 성분 사진을 업로드 해주세요.",
                "class": "form-control",
                "id": "form_title",
                "style": "width: 91%;",
            }
        )
        self.fields["allergy"].label = "알러지 정보"
        self.fields["allergy"].widget.attrs.update(
            {
                "placeholder": "알러지 정보를 선택해주세요.",
                "class": "form-control",
                "id": "form_title",
                "style": "width: 91%;",
            }
        )

    class Meta:
        model = Product
        fields = [
            "title",
            "price",
            "description",
            "stock",
            "sales_rate",
            "produt_thum_img",
            "produt_desc_img",
            "allergy",
        ]
