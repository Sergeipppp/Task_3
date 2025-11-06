from dataclasses import dataclass

@dataclass
class Urls:
    main_site = 'https://stellarburgers.education-services.ru/'
    login_user_api = main_site + "api/auth/login"
    user = main_site + "api/auth/user"
    register_user = main_site + "api/auth/register"
    profile_site = main_site + "account/profile"
    login_user = main_site + "login"
    order_history = main_site + "account/order-history"
    forgot_password = main_site + "forgot-password"
    reset_password = main_site + "reset-password"
    orders_list = main_site + "feed"
