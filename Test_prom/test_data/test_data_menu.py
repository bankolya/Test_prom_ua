class LoginData:
    def __init__(self):
        self.button_login = "button._2KaCs:nth-child(1)"
        self.mail_aut = "._1L1lg > div:nth-child(1) > div:nth-child(1) > a:nth-child(1)"
        self.input_mail = 'email_field'
        self.input_password = 'enterPassword'
        self.mail_data = "bankolya217@gmail.com"
        self.password_data = "BanKolya1998@"


class ProductFavoritesData:
    def __init__(self):
        self.favorites_selector = "._1cJIi > svg:nth-child(1)"
        self.favorites_count = {"_1Ol4v": "1"}
        self.favorites_button = "//*/div[3]/div/div[1]/button"
        self.product_name = {"product_name": "Покришка Schwalbe Marathon Supreme 42-622 Evolution OneStar"}
        self.favorites_list_count = {"b-header__controls-item": "1"}
        self.delete_product = ".favoriteList__deleteIcon__9wu9hw"
        self.locator_delete = ".style__ek-box_padding-top_m__2LmLTn > div"
