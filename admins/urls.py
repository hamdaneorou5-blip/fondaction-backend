from django.urls import path

from .web_views import (
    home,
    login,
    change_admin_password,
    dashboard,
    members_hub,
    admins_hub,
    admin_list,
    create_admin,
    admin_detail,
    reset_admin_password,
    admin_performance_detail,
    export_admin_performance_excel,
    suspend_admin,
    reactivate_admin,
    activity_logs,
    create_member,
    member_list,
    member_detail,
    member_login,
    member_space,
    member_logout,
    logout,
    reset_member_pin,
    member_change_pin,
    member_card,
    download_member_card_pdf,
    edit_member,
    suspend_member,
    activate_member,
    member_creation_history,
    export_members_excel,
    export_admins_excel,
    member_payment,
    start_member_payment,
    payment_return,
    member_transactions,
)

from .api_views import (
    api_login,
    api_change_admin_password,
    api_create_member,
    api_member_history,
    get_member_by_nim,
    api_member_login,
    fedapay_webhook,

)

urlpatterns = [
    path('', home),
    path('login/', login),
    path('logout/', logout),
    path('dashboard/', dashboard),
    path('members-hub/', members_hub),
    path('admins-hub/', admins_hub),

    path('list/', admin_list),
    path('create/', create_admin),
    path('member-by-nim/', get_member_by_nim),
    path('change-password/', change_admin_password),

    path('admins/<int:admin_id>/', admin_detail),
    path('admins/<int:admin_id>/reset-password/', reset_admin_password),
    path('admins/<int:admin_id>/performance/', admin_performance_detail),
    path('admins/<int:admin_id>/performance/export/', export_admin_performance_excel),

    path('suspend/<int:admin_id>/', suspend_admin),
    path('reactivate/<int:admin_id>/', reactivate_admin),

    path('logs/', activity_logs),

    path('members/', member_list),
    path('members/create/', create_member),
    path('members/<int:member_id>/', member_detail),
    path('members/<int:member_id>/edit/', edit_member),
    path('members/<int:member_id>/suspend/', suspend_member),
    path('members/<int:member_id>/activate/', activate_member),
    path('members/<int:member_id>/reset-pin/', reset_member_pin),
    path('members/history/', member_creation_history),
    path('members/export/', export_members_excel),

    path('admins/export/', export_admins_excel),

    path('member-login/', member_login),
    path('member-space/', member_space),
    path('member-logout/', member_logout),
    path('member-change-pin/', member_change_pin),
    path('member-card/', member_card),
    path('member-card/download-pdf/', download_member_card_pdf),
    path('member-payment/', member_payment),
    path('member-payment/start/', start_member_payment),
    path('payment-return/', payment_return),
    path('member-transactions/', member_transactions),

    path('api/login/', api_login, name='api_login'),
    path('api/change-password/', api_change_admin_password, name='api_change_admin_password'),
    path('api/members/create/', api_create_member, name='api_create_member'),
    path('api/members/history/', api_member_history, name='api_member_history'),
    path('api/member/login/', api_member_login, name='api_member_login'),
    path('api/fedapay/webhook/', fedapay_webhook, name='fedapay_webhook'),
    

]