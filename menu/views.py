from django.core.files import File
from rest_framework.views import APIView
from .serializers import BigMenuSerializer, SmallMenuSerializer, ProductSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import BigMenu, SmallMenu, Product
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from .models import Product


def cart_view(request):
    small_menu_detail = [
        {'title': 'frappuchino i kapuchino oreo', 'price': '21000', 'img': 'frappuchino i kapuchino oreo.jpg',
         'smallmenu': 'Qaxva', 'papka': 'Kaxva'},
        {'title': 'Ays Latte', 'price': '19000', 'img': 'Ays Latte.jpg', 'smallmenu': 'Qaxva', 'papka': 'Kaxva'},
        {'title': 'Ays Amerikano', 'price': '16000', 'img': 'Ays Amerikano.jpg', 'smallmenu': 'Qaxva',
         'papka': 'Kaxva'},
        {'title': 'Latte', 'price': '23000', 'img': 'Latte.jpg', 'smallmenu': 'Qaxva', 'papka': 'Kaxva'},
        {'title': 'Kapuchino', 'price': '20000', 'img': 'Kapuchino.jpg', 'smallmenu': 'Qaxva', 'papka': 'Kaxva'},
        {'title': 'Amerikano', 'price': '19000', 'img': 'Amerikano.jpg', 'smallmenu': 'Qaxva', 'papka': 'Kaxva'},
        {'title': 'Espresso', 'price': '15000', 'img': 'Espresso.jpg', 'smallmenu': 'Qaxva', 'papka': 'Kaxva'},

        {'title': 'Gavxar 1l', 'price': '45000', 'img': 'Gavxar 1l.jpg', 'smallmenu': 'Limonad', 'papka': 'Limonad'},
        {'title': 'Mango-marakuya 1l', 'price': '45000', 'img': 'Mango-marakuya 1l.jpg', 'smallmenu': 'Limonad',
         'papka': 'Limonad'},
        {'title': 'Tarxun 1l', 'price': '45000', 'img': 'Tarxun 1l.jpg', 'smallmenu': 'Limonad', 'papka': 'Limonad'},
        {'title': 'Dyushes 1l', 'price': '45000', 'img': 'Dyushes 1l.jpg', 'smallmenu': 'Limonad', 'papka': 'Limonad'},
        {'title': 'Gavxar', 'price': '25000', 'img': 'Gavxar.jpg', 'smallmenu': 'Limonad', 'papka': 'Limonad'},
        {'title': 'Tarxun limonad', 'price': '25000', 'img': 'Tarxun limonad.jpg', 'smallmenu': 'Limonad',
         'papka': 'Limonad'},
        {'title': 'Dyushes limonad', 'price': '20000', 'img': 'Dyushes limonad.jpg', 'smallmenu': 'Limonad',
         'papka': 'Limonad'},

        {'title': 'CocaCola 0,25L', 'price': '7000', 'img': 'KOLA 0,25.jpg', 'smallmenu': 'Ichimliklar',
         'papka': 'Ichimliklar'},
        {'title': 'CocaCola 0.33l', 'price': '12000', 'img': 'Kola 0.33l.jpg', 'smallmenu': 'Ichimliklar',
         'papka': 'Ichimliklar'},
        {'title': 'CocaCola 1l', 'price': '13000', 'img': 'Kola 1l.jpg', 'smallmenu': 'Ichimliklar',
         'papka': 'Ichimliklar'},
        {'title': 'CocaCola 0.5l', 'price': '8000', 'img': 'Kola 0.5l.jpg', 'smallmenu': 'Ichimliklar',
         'papka': 'Ichimliklar'},
        {'title': 'CocaCola 1.5l', 'price': '18000', 'img': 'Kola 1.5l.jpg', 'smallmenu': 'Ichimliklar',
         'papka': 'Ichimliklar'},
        {'title': 'Moxito 0.5l', 'price': '15000', 'img': 'Moxito 0.5l.jpg', 'smallmenu': 'Ichimliklar',
         'papka': 'Ichimliklar'},
        {'title': 'Sprite 0.25l', 'price': '7000', 'img': 'Sprite 0.25l.jpg', 'smallmenu': 'Ichimliklar',
         'papka': 'Ichimliklar'},
        {'title': 'Fanta 0.25l', 'price': '7000', 'img': 'Fanta 0.25l.jpg', 'smallmenu': 'Ichimliklar',
         'papka': 'Ichimliklar'},
        {'title': 'Rayal granat', 'price': '10000', 'img': 'Rayal granat.jpg', 'smallmenu': 'Ichimliklar',
         'papka': 'Ichimliklar'},
        {'title': 'Fuse tea 1l', 'price': '11000', 'img': 'Fuse tea 1l.jpg', 'smallmenu': 'Ichimliklar',
         'papka': 'Ichimliklar'},
        {'title': 'Borjomi 0.5l', 'price': '17000', 'img': 'Borjomi 0.5l.jpg', 'smallmenu': 'Ichimliklar',
         'papka': 'Ichimliklar'},
        {'title': 'Suv 0.5l', 'price': '4000', 'img': 'Suv 0.5l.jpg', 'smallmenu': 'Ichimliklar',
         'papka': 'Ichimliklar'},
        {'title': 'Suv 1.0l', 'price': '5000', 'img': 'Suv 1.0l.jpg', 'smallmenu': 'Ichimliklar',
         'papka': 'Ichimliklar'},
        {'title': 'Suv 1.5l', 'price': '7000', 'img': 'Suv 1.5l.jpg', 'smallmenu': 'Ichimliklar',
         'papka': 'Ichimliklar'},
        {'title': 'Pepsi 0.45l', 'price': '11000', 'img': 'Pepsi 0.45l.jpg', 'smallmenu': 'Ichimliklar',
         'papka': 'Ichimliklar'},
        {'title': 'Pepsi 1.0l', 'price': '12000', 'img': 'Pepsi 1.0l.jpg', 'smallmenu': 'Ichimliklar',
         'papka': 'Ichimliklar'},
        {'title': 'Pepsi 1.5l', 'price': '17000', 'img': 'Pepsi 1.5l.jpg', 'smallmenu': 'Ichimliklar',
         'papka': 'Ichimliklar'},
        {'title': 'Sprite 0.33l', 'price': '12000', 'img': 'Sprite 0.33l.jpg', 'smallmenu': 'Ichimliklar',
         'papka': 'Ichimliklar'},
        {'title': 'Sprite 0.5l', 'price': '8000', 'img': 'Sprite 0.5l.jpg', 'smallmenu': 'Ichimliklar',
         'papka': 'Ichimliklar'},
        {'title': 'Sprite 1l', 'price': '12000', 'img': 'Sprite 1l.jpg', 'smallmenu': 'Ichimliklar',
         'papka': 'Ichimliklar'},
        {'title': 'Sprite 1.5l', 'price': '17000', 'img': 'Sprite 1.5l.jpg', 'smallmenu': 'Ichimliklar',
         'papka': 'Ichimliklar'},
        {'title': 'Fanta 0.33l', 'price': '12000', 'img': 'Fanta 0.33l.jpg', 'smallmenu': 'Ichimliklar',
         'papka': 'Ichimliklar'},
        {'title': 'Fanta 0.5l', 'price': '8000', 'img': 'Fanta 0.5l.jpg', 'smallmenu': 'Ichimliklar',
         'papka': 'Ichimliklar'},
        {'title': 'Fanta 1l', 'price': '13000', 'img': 'Fanta 1l.jpg', 'smallmenu': 'Ichimliklar',
         'papka': 'Ichimliklar'},
        {'title': 'Fanta 1.5l', 'price': '18000', 'img': 'Fanta 1.5l.jpg', 'smallmenu': 'Ichimliklar',
         'papka': 'Ichimliklar'},
        {'title': 'Chortoq 0.5l', 'price': '12000', 'img': 'Chortoq 0.5l.jpg', 'smallmenu': 'Ichimliklar',
         'papka': 'Ichimliklar'},

        {'title': 'Sundis', 'price': '30000', 'img': 'Sundis.jpg', 'smallmenu': 'Sok', 'papka': 'Sok'},
        {'title': 'Sok Bliss', 'price': '17000', 'img': 'Sok Bliss.jpg', 'smallmenu': 'Sok', 'papka': 'Sok'},
        {'title': 'Olmali sok  1l', 'price': '25000', 'img': 'domashniy yablochniy sok  1l.jpg', 'smallmenu': 'Sok',
         'papka': 'Sok'},
        {'title': 'Sok Viko', 'price': '20000', 'img': 'Sok Viko.jpg', 'smallmenu': 'Sok', 'papka': 'Sok'},

        {'title': 'Xabib 0,5', 'price': '14000', 'img': 'Xabib 0,5.jpg', 'smallmenu': 'Energetik',
         'papka': 'Energetik'},
        {'title': 'Adrenalin 0.25l', 'price': '14000', 'img': 'Adrenalin 0.25l.jpg', 'smallmenu': 'Energetik',
         'papka': 'Energetik'},
        {'title': 'Adrenalin 0.5l', 'price': '19000', 'img': 'Adrenalin 0.5l.jpg', 'smallmenu': 'Energetik',
         'papka': 'Energetik'},
        {'title': 'Red bull 0.25l', 'price': '25000', 'img': 'Red bull 0.25l.jpg', 'smallmenu': 'Energetik',
         'papka': 'Energetik'},
        {'title': 'Flesh 0.5l', 'price': '12000', 'img': 'Flesh 0.5l.jpg', 'smallmenu': 'Energetik',
         'papka': 'Energetik'},

        {'title': 'RAFAELLO 200G', 'price': '105000', 'img': 'RAFAELLO 200 G.jpg', 'smallmenu': 'Shokolad',
         'papka': 'Shokalad'},
        {'title': 'Shokolad Kommunarka 200g', 'price': '35000', 'img': 'Shokolad Kommunarka 200g.jpg',
         'smallmenu': 'Shokolad', 'papka': 'Shokalad'},
        {'title': 'Kinder Surprise', 'price': '17000', 'img': 'Kinder Surprise.jpg', 'smallmenu': 'Shokolad',
         'papka': 'Shokalad'},
        {'title': 'Shokolad Bounty', 'price': '11000', 'img': 'Shokolad Bounty.jpg', 'smallmenu': 'Shokolad',
         'papka': 'Shokalad'},
        {'title': 'Shokolad  Nestle', 'price': '14000', 'img': 'Shokolad  Nestle.jpg', 'smallmenu': 'Shokolad',
         'papka': 'Shokalad'},
        {'title': 'Shokolad Kit-kat kichik', 'price': '8000', 'img': 'Shokolad Kit-kat kichik.jpg',
         'smallmenu': 'Shokolad', 'papka': 'Shokalad'},
        {'title': 'Shokolad Snickers', 'price': '10000', 'img': 'Shokolad Snickers.jpg', 'smallmenu': 'Shokolad',
         'papka': 'Shokalad'},
        {'title': 'Shokolad Snickers super', 'price': '13000', 'img': 'Shokolad Snickers super.jpg',
         'smallmenu': 'Shokolad', 'papka': 'Shokalad'},

        {'title': 'Наполеон с черносливом', 'price': '26000', 'img': 'Napoleon s chernoslivom.jpg',
         'smallmenu': 'Shirinlik', 'papka': 'Shirinliklar'},
        {'title': 'Меренговый рулет с рикоттой и клубникой', 'price': '26000',
         'img': 'Merengoviy rulet s rikottoy i klubnikoy.jpg', 'smallmenu': 'Shirinlik', 'papka': 'Shirinliklar'},
        {'title': 'Меренговый рулет с фисташками и ананасом', 'price': '26000',
         'img': 'Merengoviy rulet s fistashkami i ananasom.jpg', 'smallmenu': 'Shirinlik', 'papka': 'Shirinliklar'},
        {'title': 'Птичка пирожное', 'price': '24000', 'img': 'Ptichka pirojnoe.jpg', 'smallmenu': 'Shirinlik',
         'papka': 'Shirinliklar'},
        {'title': 'Орешки пирожное', 'price': '28000', 'img': 'Oreshki pirojnoe.jpg', 'smallmenu': 'Shirinlik',
         'papka': 'Shirinliklar'},
        {'title': 'Ириска пирожное', 'price': '24000', 'img': 'Iriska pirojnoe.jpg', 'smallmenu': 'Shirinlik',
         'papka': 'Shirinliklar'},
        {'title': 'Фисташковый пломбир', 'price': '24000', 'img': 'Fistashkoviy plombir.jpg', 'smallmenu': 'Shirinlik',
         'papka': 'Shirinliklar'},
        {'title': 'Йогуртовые пирожное с ягодами', 'price': '24000', 'img': 'Yogurtovie pirojnoe s yagodami.jpg',
         'smallmenu': 'Shirinlik', 'papka': 'Shirinliklar'},
        {'title': 'Пирожное черный принц', 'price': '28000', 'img': 'Pirojnoe cherniy prints.jpg',
         'smallmenu': 'Shirinlik', 'papka': 'Shirinliklar'},
        {'title': 'Бруни пирожние', 'price': '24000', 'img': 'Bruni pirojnie.jpg', 'smallmenu': 'Shirinlik',
         'papka': 'Shirinliklar'},
        {'title': 'Пирожние Малиновый', 'price': '24000', 'img': 'Pirojnie Malinoviy.jpg', 'smallmenu': 'Shirinlik',
         'papka': 'Shirinliklar'},
        {'title': 'Пирожние Латте', 'price': '28000', 'img': 'Pirojnie Latte.jpg', 'smallmenu': 'Shirinlik',
         'papka': 'Shirinliklar'},
        {'title': 'Пирожное Прага', 'price': '24000', 'img': 'Pirojnoe Praga.jpg', 'smallmenu': 'Shirinlik',
         'papka': 'Shirinliklar'},
        {'title': 'Макаронс', 'price': '12000', 'img': 'Makarons.jpg', 'smallmenu': 'Shirinlik',
         'papka': 'Shirinliklar'},
        {'title': 'Пирожное Сникерс', 'price': '28000', 'img': 'Pirojnoe Snikers.jpg', 'smallmenu': 'Shirinlik',
         'papka': 'Shirinliklar'},
        {'title': 'Вишнёвый чизкейк', 'price': '24000', 'img': 'Vishnyoviy chizkeyk.jpg', 'smallmenu': 'Shirinlik',
         'papka': 'Shirinliklar'},
        {'title': 'Пирожное Банановое', 'price': '24000', 'img': 'Pirojnoe Bananovoe.jpg', 'smallmenu': 'Shirinlik',
         'papka': 'Shirinliklar'},
        {'title': 'Шоколадли чизкейк Нью-Йорк', 'price': '28000', 'img': 'Shokoladli chizkeyk Nyu-York.jpg',
         'smallmenu': 'Shirinlik', 'papka': 'Shirinliklar'},
        {'title': 'Пирожное Птичье молоко', 'price': '24000', 'img': 'Pirojnoe Ptiche moloko.jpg',
         'smallmenu': 'Shirinlik', 'papka': 'Shirinliklar'},
        {'title': 'Пирожное Шарик', 'price': '24000', 'img': 'Pirojnoe Sharik.jpg', 'smallmenu': 'Shirinlik',
         'papka': 'Shirinliklar'},
        {'title': 'Пирожное Наполеон', 'price': '24000', 'img': 'Pirojnoe Napoleon.jpg', 'smallmenu': 'Shirinlik',
         'papka': 'Shirinliklar'},
        {'title': 'Пирожное Улитка', 'price': '24000', 'img': 'Pirojnoe Ulitka.jpg', 'smallmenu': 'Shirinlik',
         'papka': 'Shirinliklar'},
        {'title': 'Пирожное Мишутка', 'price': '24000', 'img': 'Pirojnoe Mishutka.jpg', 'smallmenu': 'Shirinlik',
         'papka': 'Shirinliklar'},
        {'title': 'Меренговый рулет', 'price': '24000', 'img': 'Merengoviy rulet.jpg', 'smallmenu': 'Shirinlik',
         'papka': 'Shirinliklar'},
        {'title': 'Пирожное Красный бархат', 'price': '24000', 'img': 'Pirojnoe Krasniy barxat.jpg',
         'smallmenu': 'Shirinlik', 'papka': 'Shirinliklar'},
        {'title': 'Пирожное Маковый карамель', 'price': '24000', 'img': 'Pirojnoe Makoviy karamel.jpg',
         'smallmenu': 'Shirinlik', 'papka': 'Shirinliklar'},
        {'title': 'Турк пахлаваси 1 д', 'price': '19000', 'img': 'Turk paxlavasi 1 d.jpg', 'smallmenu': 'Shirinlik',
         'papka': 'Shirinliklar'},
        {'title': 'Чизкейк Нью-Йорк', 'price': '28000', 'img': 'Chizkeyk Nyu-York.jpg', 'smallmenu': 'Shirinlik',
         'papka': 'Shirinliklar'},
        {'title': 'Торт 1кг', 'price': '80000', 'img': 'Tort 1kg.jpg', 'smallmenu': 'Shirinlik',
         'papka': 'Shirinliklar'},
        {'title': 'Пирожное Bounty', 'price': '28000', 'img': 'Pirojnoe Bounty.jpg', 'smallmenu': 'Shirinlik',
         'papka': 'Shirinliklar'},
        {'title': 'Пирожное Медовик', 'price': '24000', 'img': 'Pirojnoe Medovik.jpg', 'smallmenu': 'Shirinlik',
         'papka': 'Shirinliklar'},

        {'title': 'Десерт ассорти', 'price': '36000', 'img': 'Desert assorti.jpg', 'smallmenu': 'Syurpriz',
         'papka': 'Syurpriz'},
        {'title': 'Медовый сюрприз с мороженным', 'price': '55000', 'img': 'Medoviy syurpriz s morojennim.jpg',
         'smallmenu': 'Syurpriz', 'papka': 'Syurpriz'},
        {'title': 'Чизкейк сан себастьян с мороженым', 'price': '59000',
         'img': 'Chizkeyk san sebastyan s morojenim.jpg', 'smallmenu': 'Syurpriz', 'papka': 'Syurpriz'},
        {'title': 'Desert spring', 'price': '65000', 'img': 'Desert spring.jpg', 'smallmenu': 'Syurpriz',
         'papka': 'Syurpriz'},
        {'title': 'Сюрприз тирамису с мороженым', 'price': '55000', 'img': 'Syurpriz tiramisu s morojenim.jpg',
         'smallmenu': 'Syurpriz', 'papka': 'Syurpriz'},
        {'title': 'сюрприз карамельный', 'price': '55000', 'img': 'syurpriz karamelniy.jpg', 'smallmenu': 'Syurpriz',
         'papka': 'Syurpriz'},
        {'title': 'Десерт Чудо', 'price': '65000', 'img': 'Desert Chudo.jpg', 'smallmenu': 'Syurpriz',
         'papka': 'Syurpriz'},
        {'title': 'Воздушные вафли с мороженом соусе', 'price': '65000',
         'img': 'Vozdushnie vafli s morojenom souse.jpg', 'smallmenu': 'Syurpriz', 'papka': 'Syurpriz'},
        {'title': 'Воздушные вафли в шоколадном соусе', 'price': '65000',
         'img': 'Vozdushnie vafli v shokoladnom souse.jpg', 'smallmenu': 'Syurpriz', 'papka': 'Syurpriz'},
        {'title': 'Сюрприз cникерс', 'price': '45000', 'img': 'Syurpriz cnikers.jpg', 'smallmenu': 'Syurpriz',
         'papka': 'Syurpriz'},
        {'title': 'Сюрприз Рафаэлло', 'price': '55000', 'img': 'Syurpriz Rafaello.jpg', 'smallmenu': 'Syurpriz',
         'papka': 'Syurpriz'},
        {'title': 'Клубничный Сюрприз', 'price': '45000', 'img': 'Klubnichniy Syurpriz.jpg', 'smallmenu': 'Syurpriz',
         'papka': 'Syurpriz'},
        {'title': 'Шоколадный Сюрприз с мороженое', 'price': '45000', 'img': 'Shokoladniy Syurpriz s morojenoe.jpg',
         'smallmenu': 'Syurpriz', 'papka': 'Syurpriz'},

        {'title': 'Turk Non assorti', 'price': '25000', 'img': 'Turk Non assorti.jpg', 'smallmenu': 'Non',
         'papka': 'Non'},
        {'title': 'Avgon Nan kunjutsiz', 'price': '14000', 'img': 'Avgon Nan kunjutsiz.jpg', 'smallmenu': 'Non',
         'papka': 'Non'},
        {'title': 'Non assorti 0.5x', 'price': '16000', 'img': 'Non assorti 0.5x.jpg', 'smallmenu': 'Non',
         'papka': 'Non'},
        {'title': 'Go‘shtli patir 0.5x', 'price': '16000', 'img': 'Go‘shtli patir 0.5x.jpg', 'smallmenu': 'Non',
         'papka': 'Non'},
        {'title': 'Go‘shtli patir', 'price': '32000', 'img': 'Go‘shtli patir.jpg', 'smallmenu': 'Non', 'papka': 'Non'},
        {'title': 'Qora non 0.5x', 'price': '4000', 'img': 'Qora non 0.5x.jpg', 'smallmenu': 'Non', 'papka': 'Non'},
        {'title': 'Qora non', 'price': '7000', 'img': 'Qora non.jpg', 'smallmenu': 'Non', 'papka': 'Non'},
        {'title': 'Patir 0.5x', 'price': '8000', 'img': 'Patir 0.5x.jpg', 'smallmenu': 'Non', 'papka': 'Non'},
        {'title': 'Patir', 'price': '15000', 'img': 'Patir.jpg', 'smallmenu': 'Non', 'papka': 'Non'},
        {'title': 'Oq non', 'price': '5000', 'img': 'Oq non.jpg', 'smallmenu': 'Non', 'papka': 'Non'},
        {'title': 'Churak 0.5x', 'price': '6000', 'img': 'Churak 0.5x.jpg', 'smallmenu': 'Non', 'papka': 'Non'},
        {'title': 'Churak', 'price': '10000', 'img': 'Churak.jpg', 'smallmenu': 'Non', 'papka': 'Non'},
        {'title': 'Non assorti', 'price': '25000', 'img': 'Non assorti.jpg', 'smallmenu': 'Non', 'papka': 'Non'},
        {'title': 'Afgan noni', 'price': '17000', 'img': 'Afgan noni.jpg', 'smallmenu': 'Non', 'papka': 'Non'},
        {'title': 'Turk non', 'price': '7000', 'img': 'Turk non.jpg', 'smallmenu': 'Non', 'papka': 'Non'},

        {'title': "Limon choy ko‘k(paketli)", 'price': '13000', 'img': 'Limon Chay kuk(paketli).jpg',
         'smallmenu': 'Choy', 'papka': 'Choy'},
        {'title': 'Ko‘k choy (paketli)', 'price': '8000', 'img': 'Kuk Chay (paketli).jpg', 'smallmenu': 'Choy',
         'papka': 'Choy'},
        {'title': 'Oddiy ko‘k choy', 'price': '7000', 'img': 'Oddiy Ko‘k chay.jpg', 'smallmenu': 'Choy',
         'papka': 'Choy'},
        {'title': 'Sutli qora choy', 'price': '31000', 'img': 'Sutli kora choy.jpg', 'smallmenu': 'Choy',
         'papka': 'Choy'},
        {'title': 'Qora choy', 'price': '8000', 'img': 'Chay Kora.jpg', 'smallmenu': 'Choy', 'papka': 'Choy'},
        {'title': 'Limon choy qora', 'price': '13000', 'img': 'Limon Chay kora.jpg', 'smallmenu': 'Choy',
         'papka': 'Choy'},
        {'title': 'Mevali choy', 'price': '28000', 'img': 'Mevali chay.jpg', 'smallmenu': 'Choy', 'papka': 'Choy'},
        {'title': 'Chay(kiyik o‘ti)', 'price': '8000', 'img': 'Chay(kiyik o‘ti).jpg', 'smallmenu': 'Choy',
         'papka': 'Choy'},

        {'title': 'Avtorskiy salat', 'price': '33000', 'img': 'Avtorskiy salat.jpg', 'smallmenu': 'Salat',
         'papka': 'Salat'},
        {'title': 'Salat Mujskoy Kapriz', 'price': '36000', 'img': 'Salat Mujskoy Kapriz.jpg', 'smallmenu': 'Salat',
         'papka': 'Salat'},
        {'title': 'Skazka salat', 'price': '41000', 'img': 'Skazka salat.jpg', 'smallmenu': 'Salat', 'papka': 'Salat'},
        {'title': 'Salyoniy Damashniy Pomidor', 'price': '15000', 'img': 'Salyoniy Damashniy Pomidor.jpg',
         'smallmenu': 'Salat', 'papka': 'Salat'},
        {'title': 'Salyoniy Damashniy Ogurtsi', 'price': '19000', 'img': 'Salyoniy Damashniy Ogurtsi.jpg',
         'smallmenu': 'Salat', 'papka': 'Salat'},
        {'title': 'Salyoniy Karam Kizil', 'price': '9000', 'img': 'Salyoniy Karam Kizil.jpg', 'smallmenu': 'Salat',
         'papka': 'Salat'},
        {'title': 'Salyoniy Karam', 'price': '9000', 'img': 'Salyoniy Karam.jpg', 'smallmenu': 'Salat',
         'papka': 'Salat'},
        {'title': 'Salyoniy Assorti', 'price': '21000', 'img': 'Salyoniy Assorti.jpg', 'smallmenu': 'Salat',
         'papka': 'Salat'},
        {'title': 'Vitaminka Salat', 'price': '26000', 'img': 'Vitaminka Salat.jpg', 'smallmenu': 'Salat',
         'papka': 'Salat'},
        {'title': 'Selyodka', 'price': '37000', 'img': 'Selyodka.jpg', 'smallmenu': 'Salat', 'papka': 'Salat'},
        {'title': 'Cho‘pon Salat', 'price': '25000', 'img': 'Chupan Salat.jpg', 'smallmenu': 'Salat', 'papka': 'Salat'},
        {'title': 'Olivie go‘shtli', 'price': '33000', 'img': 'Olivie go‘shtli.jpg', 'smallmenu': 'Salat',
         'papka': 'Salat'},
        {'title': 'Sezar salat (klassicheskiy)', 'price': '35000', 'img': 'tsezar salat (klassicheskiy).jpg',
         'smallmenu': 'Salat', 'papka': 'Salat'},
        {'title': 'Chakki', 'price': '16000', 'img': 'Chakki.jpg', 'smallmenu': 'Salat', 'papka': 'Salat'},
        {'title': 'Gulshan Salat', 'price': '34000', 'img': 'Gulshan Salat.jpg', 'smallmenu': 'Salat',
         'papka': 'Salat'},
        {'title': 'Svejiy Salat', 'price': '19000', 'img': 'Svejiy Salat.jpg', 'smallmenu': 'Salat', 'papka': 'Salat'},
        {'title': 'Parxez Salat', 'price': '28000', 'img': 'Parxez Salat.jpg', 'smallmenu': 'Salat', 'papka': 'Salat'},
        {'title': 'Achchiq chuchuk Salat', 'price': '17000', 'img': 'Achchiq chuchuk Salat.jpg', 'smallmenu': 'Salat',
         'papka': 'Salat'},
        {'title': 'Grecheskiy Salat', 'price': '36000', 'img': 'Grecheskiy Salat.jpg', 'smallmenu': 'Salat',
         'papka': 'Salat'},
        {'title': 'Turetskiy Salat', 'price': '36000', 'img': 'Turetskiy Salat.jpg', 'smallmenu': 'Salat',
         'papka': 'Salat'},
        {'title': 'Yaponskiy Salat', 'price': '38000', 'img': 'Yaponskiy Salat.jpg', 'smallmenu': 'Salat',
         'papka': 'Salat'},
        {'title': 'Aziza Salat', 'price': '37000', 'img': 'Aziza Salat.jpg', 'smallmenu': 'Salat', 'papka': 'Salat'},
        {'title': 'Muxlisa Salat', 'price': '35000', 'img': 'Muxlisa Salat.jpg', 'smallmenu': 'Salat',
         'papka': 'Salat'},
        {'title': 'Gavxar Salat', 'price': '39000', 'img': 'Gavxar Salat.jpg', 'smallmenu': 'Salat', 'papka': 'Salat'},
        {'title': 'Ovoshnaya narezka', 'price': '45000', 'img': 'Ovoshnaya narezka.jpg', 'smallmenu': 'Salat',
         'papka': 'Salat'},

        {'title': 'VIP myasnoy', 'price': '135000', 'img': 'VIP myasnoy.jpg', 'smallmenu': 'Salqin gazak',
         'papka': 'Salqin gazak'},
        {'title': 'Qazi 1 sht', 'price': '8000', 'img': 'Qazi 1 sht.jpg', 'smallmenu': 'Salqin gazak',
         'papka': 'Salqin gazak'},
        {'title': 'Norin sho‘rva', 'price': '7000', 'img': 'Norin sho‘rva.jpg', 'smallmenu': 'Salqin gazak',
         'papka': 'Salqin gazak'},
        {'title': 'Norin 1kg', 'price': '125000', 'img': 'Norin 1kg.jpg', 'smallmenu': 'Salqin gazak',
         'papka': 'Salqin gazak'},
        {'title': 'Norin', 'price': '33000', 'img': 'Norin.jpg', 'smallmenu': 'Salqin gazak', 'papka': 'Salqin gazak'},
        {'title': 'Myasnoe assorti', 'price': '100000', 'img': 'Myasnoe assorti.jpg', 'smallmenu': 'Salqin gazak',
         'papka': 'Salqin gazak'},

        {'title': 'Mastava', 'price': '28000', 'img': 'Mastava.jpg', 'smallmenu': 'Sho‘rva', 'papka': 'Sho‘rva'},
        {'title': 'Golubsi sho‘rva', 'price': '29000', 'img': 'Golubtsi sho‘rva.jpg', 'smallmenu': 'Sho‘rva',
         'papka': 'Sho‘rva'},
        {'title': 'Teftel sho‘rva', 'price': '28000', 'img': 'Teftel sho‘rva.jpg', 'smallmenu': 'Sho‘rva',
         'papka': 'Sho‘rva'},
        {'title': 'Sho‘rva Barak', 'price': '33000', 'img': 'Sho‘rva Barak.jpg', 'smallmenu': 'Sho‘rva',
         'papka': 'Sho‘rva'},
        {'title': 'Un oshi 0.5', 'price': '16000', 'img': 'Un oshi 0.5.jpg', 'smallmenu': 'Sho‘rva',
         'papka': 'Sho‘rva'},
        {'title': 'Bedana sho‘rva', 'price': '39000', 'img': 'Bedana sho‘rva.jpg', 'smallmenu': 'Sho‘rva',
         'papka': 'Sho‘rva'},
        {'title': 'Osma sho‘rva', 'price': '28000', 'img': 'Osma sho‘rva.jpg', 'smallmenu': 'Sho‘rva',
         'papka': 'Sho‘rva'},
        {'title': 'Un oshi', 'price': '25000', 'img': 'Un oshi.jpg', 'smallmenu': 'Sho‘rva', 'papka': 'Sho‘rva'},

        {'title': 'Kare Yagnenka', 'price': '105000', 'img': 'Kare Yagnenka.jpg', 'smallmenu': 'Yevropa taomlari',
         'papka': 'Evropa taomlari'},
        {'title': 'Dana Biftek', 'price': '82000', 'img': 'Dana Biftek.jpg', 'smallmenu': 'Yevropa taomlari',
         'papka': 'Evropa taomlari'},
        {'title': 'Telyatina v gribnom souse', 'price': '81000', 'img': 'Telyatina v gribnom souse.jpg',
         'smallmenu': 'Yevropa taomlari', 'papka': 'Evropa taomlari'},
        {'title': 'Kotleti s pyure', 'price': '67000', 'img': 'Kotleti s pyure.jpg', 'smallmenu': 'Yevropa taomlari',
         'papka': 'Evropa taomlari'},
        {'title': 'Bug‘da pishirilgan kotlet [1 dona]', 'price': '17000',
         'img': 'Bug‘da pishirilgan kotlet [1 dona].jpg', 'smallmenu': 'Yevropa taomlari', 'papka': 'Evropa taomlari'},
        {'title': 'Mol go‘shtli kotlet (1 dona)', 'price': '17000', 'img': 'Mol go‘shtli kotlet (1 dona).jpg',
         'smallmenu': 'Yevropa taomlari', 'papka': 'Evropa taomlari'},
        {'title': 'Medaloni iz govyadini', 'price': '115000', 'img': 'Medaloni iz govyadini.jpg',
         'smallmenu': 'Yevropa taomlari', 'papka': 'Evropa taomlari'},
        {'title': 'Steyk Tenderlion', 'price': '248000', 'img': 'Steyk Tenderlion.jpg', 'smallmenu': 'Yevropa taomlari',
         'papka': 'Evropa taomlari'},

        {'title': 'Zi‘girik 1 portsiya', 'price': '66000', 'img': 'Zigirik 1 portsiya.jpg',
         'smallmenu': 'Milliy taomlar', 'papka': 'Milliy taomlar'},
        {'title': 'Qorin tuyoq 1 portsiya', 'price': '65000', 'img': 'Korin tuyok 1 portsiya.jpg',
         'smallmenu': 'Milliy taomlar', 'papka': 'Milliy taomlar'},
        {'title': 'Golubtsi assorti', 'price': '225000', 'img': 'Golubtsi assorti.jpg', 'smallmenu': 'Milliy taomlar',
         'papka': 'Milliy taomlar'},
        {'title': 'Domashniy palov (pod zakaz)', 'price': '310000', 'img': 'Domashniy plov (pod zakaz).jpg',
         'smallmenu': 'Milliy taomlar', 'papka': 'Milliy taomlar'},
        {'title': 'Kebab v slivochnom souse 1kg', 'price': '205000', 'img': 'Kebab v slivochnom souse 1kg.jpg',
         'smallmenu': 'Milliy taomlar', 'papka': 'Milliy taomlar'},
        {'title': 'Kebab v slivochnom souse', 'price': '58000', 'img': 'Kebab v slivochnom souse.jpg',
         'smallmenu': 'Milliy taomlar', 'papka': 'Milliy taomlar'},
        {'title': 'Yazik v slivochnom masle 1kg', 'price': '205000', 'img': 'Yazik v slivochnom masle 1kg.jpg',
         'smallmenu': 'Milliy taomlar', 'papka': 'Milliy taomlar'},
        {'title': 'Zakaz palov', 'price': '570000', 'img': 'Zakaz palov.jpg', 'smallmenu': 'Milliy taomlar',
         'papka': 'Milliy taomlar'},
        {'title': 'Sho‘r kabob 1kg', 'price': '186000', 'img': 'Sho‘r kabob 1kg.jpg', 'smallmenu': 'Milliy taomlar',
         'papka': 'Milliy taomlar'},
        {'title': 'Qovurma lag‘mon', 'price': '41000', 'img': 'Qovurma lag‘mon.jpg', 'smallmenu': 'Milliy taomlar',
         'papka': 'Milliy taomlar'},
        {'title': 'Karma', 'price': '295000', 'img': 'Karma.jpg', 'smallmenu': 'Milliy taomlar',
         'papka': 'Milliy taomlar'},
        {'title': 'Sho‘r kabob 1 portsiya', 'price': '48000', 'img': 'Sho‘r kabob 1 portsiya.jpg',
         'smallmenu': 'Milliy taomlar', 'papka': 'Milliy taomlar'},
        {'title': 'Lyulya kebab', 'price': '59000', 'img': 'Lyulya kebab.jpg', 'smallmenu': 'Milliy taomlar',
         'papka': 'Milliy taomlar'},
        {'title': "Saryog'ga tovuq", 'price': '75000', 'img': "saryog'ga tovuq.jpg", 'smallmenu': 'Milliy taomlar',
         'papka': 'Milliy taomlar'},
        {'title': 'Uyg‘ur lag‘mon', 'price': '41000', 'img': 'Uyg‘ur lag‘man.jpg', 'smallmenu': 'Milliy taomlar',
         'papka': 'Milliy taomlar'},

        {'title': 'Milliy Miks', 'price': '357000', 'img': 'Milliy Miks.jpg', 'smallmenu': 'Go‘shtli taomlar',
         'papka': 'Go‘shtli taomlar'},
        {'title': 'Miks Kebab(4 odam uchun)', 'price': '305000', 'img': 'Miks Kebab na 4 person.jpg',
         'smallmenu': 'Go‘shtli taomlar', 'papka': 'Go‘shtli taomlar'},
        {'title': 'Chef Milliy assorti', 'price': '415000', 'img': 'Chef Milliy assorti.jpg',
         'smallmenu': 'Go‘shtli taomlar', 'papka': 'Go‘shtli taomlar'},
        {'title': 'Xan 0.5', 'price': '280000', 'img': 'Xan 0.5.jpg', 'smallmenu': 'Go‘shtli taomlar',
         'papka': 'Go‘shtli taomlar'},
        {'title': 'Asado', 'price': '290000', 'img': 'Asado.jpg', 'smallmenu': 'Go‘shtli taomlar',
         'papka': 'Go‘shtli taomlar'},
        {'title': 'Govyajya koreyka na mangale 1kg', 'price': '180000', 'img': 'Govyajya koreyka na mangale 1kg.jpg',
         'smallmenu': 'Go‘shtli taomlar', 'papka': 'Go‘shtli taomlar'},
        {'title': 'Shashlik assorti', 'price': '350000', 'img': 'Shashlik assorti.jpg', 'smallmenu': 'Go‘shtli taomlar',
         'papka': 'Go‘shtli taomlar'},
        {'title': 'Gavxar mangal assorti (6 kishilik)', 'price': '430000',
         'img': 'Gavxar mangal assorti (6 kishilik).jpg', 'smallmenu': 'Go‘shtli taomlar', 'papka': 'Go‘shtli taomlar'},
        {'title': 'Gavxar mangal assorti (4 kishilik)', 'price': '350000',
         'img': 'Gavxar mangal assorti (4 kishilik).jpg', 'smallmenu': 'Go‘shtli taomlar', 'papka': 'Go‘shtli taomlar'},
        {'title': 'Gavxar mangal assorti (2 kishilik)', 'price': '185000',
         'img': 'Gavxar mangal assorti (2 kishilik).jpg', 'smallmenu': 'Go‘shtli taomlar', 'papka': 'Go‘shtli taomlar'},
        {'title': 'Flank steyk', 'price': '255000', 'img': 'Flank steyk.jpg', 'smallmenu': 'Go‘shtli taomlar',
         'papka': 'Go‘shtli taomlar'},
        {'title': 'Steyk assorti', 'price': '465000', 'img': 'Steyk assorti.jpg', 'smallmenu': 'Go‘shtli taomlar',
         'papka': 'Go‘shtli taomlar'},
        {'title': 'XAN', 'price': '460000', 'img': 'XAN.jpg', 'smallmenu': 'Go‘shtli taomlar',
         'papka': 'Go‘shtli taomlar'},

        {'title': 'Katlama Chalpak', 'price': '48000', 'img': 'Katlama Chalpak.jpg', 'smallmenu': 'Xamirli taomlar',
         'papka': 'Xamirli taomlar'},
        {'title': 'Ismalak Kapshirma', 'price': '10000', 'img': 'Ismalak Kapshirma.jpg', 'smallmenu': 'Xamirli taomlar',
         'papka': 'Xamirli taomlar'},
        {'title': 'Gumma (kichik)', 'price': '7000', 'img': 'Gumma (kichik).jpg', 'smallmenu': 'Xamirli taomlar',
         'papka': 'Xamirli taomlar'},
        {'title': 'Kapshirma (kichik)', 'price': '7000', 'img': 'Kapshirma (kichik).jpg',
         'smallmenu': 'Xamirli taomlar', 'papka': 'Xamirli taomlar'},
        {'title': 'Manti 1 sht', 'price': '11000', 'img': 'Manti 1 sht.jpg', 'smallmenu': 'Xamirli taomlar',
         'papka': 'Xamirli taomlar'},
        {'title': 'Tomchi Somsa', 'price': '14000', 'img': 'Tomchi Somsa.jpg', 'smallmenu': 'Xamirli taomlar',
         'papka': 'Xamirli taomlar'},
        {'title': 'Shivit oshi', 'price': '35000', 'img': 'Shivit oshi.jpg', 'smallmenu': 'Xamirli taomlar',
         'papka': 'Xamirli taomlar'},
        {'title': 'Tandir somsa', 'price': '14000', 'img': 'Tandir somsa.jpg', 'smallmenu': 'Xamirli taomlar',
         'papka': 'Xamirli taomlar'},
        {'title': 'Gumma', 'price': '12000', 'img': 'Gumma.jpg', 'smallmenu': 'Xamirli taomlar',
         'papka': 'Xamirli taomlar'},
        {'title': 'Kapshirma', 'price': '12000', 'img': 'Kapshirma.jpg', 'smallmenu': 'Xamirli taomlar',
         'papka': 'Xamirli taomlar'},
        {'title': 'Kartoshka barak', 'price': '22000', 'img': 'Kartoshka barak.jpg', 'smallmenu': 'Xamirli taomlar',
         'papka': 'Xamirli taomlar'},
        {'title': 'Barak assorti', 'price': '90000', 'img': 'Barak assorti.jpg', 'smallmenu': 'Xamirli taomlar',
         'papka': 'Xamirli taomlar'},
        {'title': 'Ko‘k barak', 'price': '25000', 'img': 'Ko‘k barak.jpg', 'smallmenu': 'Xamirli taomlar',
         'papka': 'Xamirli taomlar'},
        {'title': 'Kadi  barak', 'price': '21000', 'img': 'Kadi  barak.jpg', 'smallmenu': 'Xamirli taomlar',
         'papka': 'Xamirli taomlar'},
        {'title': 'Qo‘tir barak', 'price': '29000', 'img': 'Kutir barak.jpg', 'smallmenu': 'Xamirli taomlar',
         'papka': 'Xamirli taomlar'},
        {'title': 'Tuxum barak', 'price': '24000', 'img': 'Tuxum barak.jpg', 'smallmenu': 'Xamirli taomlar',
         'papka': 'Xamirli taomlar'},

        {'title': 'Grechka', 'price': '5000', 'img': 'Grechka.jpg', 'smallmenu': 'Garnir va Sous',
         'papka': 'Garniri i Sousa'},
        {'title': 'Sous Barbekyu', 'price': '5000', 'img': 'Sous Barbekyu.jpg', 'smallmenu': 'Garnir va Sous',
         'papka': 'Garniri i Sousa'},
        {'title': 'Sous Ovoshnaya Ikra', 'price': '8000', 'img': 'Sous Ovoshnaya Ikra.jpg',
         'smallmenu': 'Garnir va Sous', 'papka': 'Garniri i Sousa'},
        {'title': 'Xaynts (ketchup)', 'price': '5000', 'img': 'Xaynts (ketchup).jpg', 'smallmenu': 'Garnir va Sous',
         'papka': 'Garniri i Sousa'},
        {'title': 'Smetana', 'price': '3000', 'img': 'Smetana.jpg', 'smallmenu': 'Garnir va Sous',
         'papka': 'Garniri i Sousa'},
        {'title': 'Sous chili', 'price': '3000', 'img': 'Sous chili.jpg', 'smallmenu': 'Garnir va Sous',
         'papka': 'Garniri i Sousa'},
        {'title': 'Chesnoqli sous', 'price': '4000', 'img': 'Chesnoqli sous.jpg', 'smallmenu': 'Garnir va Sous',
         'papka': 'Garniri i Sousa'},
        {'title': 'Qatiq', 'price': '5000', 'img': 'Qatiq.jpg', 'smallmenu': 'Garnir va Sous',
         'papka': 'Garniri i Sousa'},
        {'title': 'Kukuruza na grile', 'price': '11000', 'img': 'Kukuruza na grile.jpg', 'smallmenu': 'Garnir va Sous',
         'papka': 'Garniri i Sousa'},
        {'title': 'Ovoshi na grile', 'price': '28000', 'img': 'Ovoshi na grile.jpg', 'smallmenu': 'Garnir va Sous',
         'papka': 'Garniri i Sousa'},
        {'title': 'Aydaxo', 'price': '18000', 'img': 'Aydaxo.jpg', 'smallmenu': 'Garnir va Sous',
         'papka': 'Garniri i Sousa'},
        {'title': 'Pyure', 'price': '7000', 'img': 'Pyure.jpg', 'smallmenu': 'Garnir va Sous',
         'papka': 'Garniri i Sousa'},
        {'title': 'Fri', 'price': '17000', 'img': 'Fri.jpg', 'smallmenu': 'Garnir va Sous', 'papka': 'Garniri i Sousa'},

        {'title': 'Falgada pishirilgan laqqa 1 KG', 'price': '269000', 'img': 'Lakka zapechennaya v folge 1 KG.jpg',
         'smallmenu': 'Baliq taomlari', 'papka': 'Baliq taomlari'},
        {'title': 'Setkaga laqqa 1 kg', 'price': '272000', 'img': 'Lakka na setke 1 kg.jpg',
         'smallmenu': 'Baliq taomlari', 'papka': 'Baliq taomlari'},
        {'title': 'Sazan (qizil sous bilan) 1 kg', 'price': '115000', 'img': 'Sazan (qizil sous bilan) 1 kg.jpg',
         'smallmenu': 'Baliq taomlari', 'papka': 'Baliq taomlari'},
        {'title': 'Laqqa baliq 1 kg', 'price': '240000', 'img': 'Laqqa baliq 1 kg.jpg', 'smallmenu': 'Baliq taomlari',
         'papka': 'Baliq taomlari'},
        {'title': 'Setka Sazan 1 kg', 'price': '110000', 'img': 'Setka Sazan 1 kg.jpg', 'smallmenu': 'Baliq taomlari',
         'papka': 'Baliq taomlari'},
        {'title': 'Falgada pishirilgan Sazan', 'price': '115000', 'img': 'Falgada pishirilgan Sazan.jpg',
         'smallmenu': 'Baliq taomlari', 'papka': 'Baliq taomlari'},
        {'title': 'Qovurilgan Sazan', 'price': '110000', 'img': 'Qovurilgan Sazan.jpg', 'smallmenu': 'Baliq taomlari',
         'papka': 'Baliq taomlari'},

        {'title': 'Kavkazskiy shashlik 1 sht', 'price': '45000', 'img': 'Kavkazskiy shashlik 1 sht.jpg',
         'smallmenu': 'Shashlik', 'papka': 'Shashlik'},
        {'title': 'Rulet Shashlik 1 sht', 'price': '27000', 'img': 'Rulet Shashlik 1 sht.jpg', 'smallmenu': 'Shashlik',
         'papka': 'Shashlik'},
        {'title': 'Kuskovoy shashlik Bez Jira 1 sht', 'price': '27000', 'img': 'Kuskovoy shashlik Bez Jira 1 sht.jpg',
         'smallmenu': 'Shashlik', 'papka': 'Shashlik'},
        {'title': 'Shashlik assorti 0.5', 'price': '185000', 'img': 'Shashlik assorti 0.5.jpg', 'smallmenu': 'Shashlik',
         'papka': 'Shashlik'},
        {'title': 'Katlet na mangale 1 sht', 'price': '21000', 'img': 'Katlet  na mangale 1 sht.jpg',
         'smallmenu': 'Shashlik', 'papka': 'Shashlik'},
        {'title': 'Shashlik dumba 1 sht', 'price': '18000', 'img': 'Shashlik dumba 1 sht.jpg', 'smallmenu': 'Shashlik',
         'papka': 'Shashlik'},
        {'title': 'Napoleon shashlik 1 sht', 'price': '23000', 'img': 'Napoleon shashlik 1 sht.jpg',
         'smallmenu': 'Shashlik', 'papka': 'Shashlik'},
        {'title': 'Besh panja shashlik', 'price': '85000', 'img': 'Besh panja shashlik.jpg', 'smallmenu': 'Shashlik',
         'papka': 'Shashlik'},
        {'title': 'Shashlik molotiy', 'price': '16000', 'img': 'Shashlik molotiy.jpg', 'smallmenu': 'Shashlik',
         'papka': 'Shashlik'},
        {'title': 'Setka kabob 0,5', 'price': '89000', 'img': 'Setka kabob 0,5.jpg', 'smallmenu': 'Shashlik',
         'papka': 'Shashlik'},
        {'title': 'Asl shashlik 1 sht', 'price': '16000', 'img': 'Asl shashlik 1 sht.jpg', 'smallmenu': 'Shashlik',
         'papka': 'Shashlik'},
        {'title': 'Shashlik mol go‘shtidan 1 sht', 'price': '23000', 'img': 'Shashlik mol go‘shtidan 1 sht.jpg',
         'smallmenu': 'Shashlik', 'papka': 'Shashlik'},
        {'title': 'Shashlik assorti', 'price': '350000', 'img': 'Shashlik assorti.jpg', 'smallmenu': 'Shashlik',
         'papka': 'Shashlik'},
        {'title': 'Jigar shashligi 1 sht', 'price': '19000', 'img': 'Jigar shashligi 1 sht.jpg',
         'smallmenu': 'Shashlik', 'papka': 'Shashlik'},
        {'title': 'Shashlik kuskovoy (baranina) 1 sht', 'price': '23000',
         'img': 'Shashlik kuskovoy (baranina) 1 sht.jpg', 'smallmenu': 'Shashlik', 'papka': 'Shashlik'},
        {'title': 'Shashlik o‘rama 1 sht', 'price': '16000', 'img': 'Shashlik o‘rama 1 sht.jpg',
         'smallmenu': 'Shashlik', 'papka': 'Shashlik'},
        {'title': 'Shashlik Gijduvon (molotiy) 1 sht', 'price': '16000', 'img': 'Shashlik Gijduvon (molotiy) 1 sht.jpg',
         'smallmenu': 'Shashlik', 'papka': 'Shashlik'},

        {'title': 'Adana Kebab', 'price': '48000', 'img': 'Adana Kebab.jpg', 'smallmenu': 'Turk yemaklari',
         'papka': 'Turk yemaklari'},
        {'title': 'Kasarli kufte', 'price': '70000', 'img': 'Kasarli kufte.jpg', 'smallmenu': 'Turk yemaklari',
         'papka': 'Turk yemaklari'},
        {'title': 'Burger', 'price': '38000', 'img': 'Burger.jpg', 'smallmenu': 'Turk yemaklari',
         'papka': 'Turk yemaklari'},
        {'title': 'Chedarli kufte', 'price': '84000', 'img': 'Chedarli kufte.jpg', 'smallmenu': 'Turk yemaklari',
         'papka': 'Turk yemaklari'},

        {'title': 'Пицца Четыре Сезона', 'price': '79000', 'img': 'Pitsa Chetire Sezona.jpg', 'smallmenu': 'Pitsa',
         'papka': 'Pitsa'},
        {'title': 'Пицца Мясное Удовольствие', 'price': '78000', 'img': 'Pitsa Myasnoe Udovolstvie.jpg',
         'smallmenu': 'Pitsa', 'papka': 'Pitsa'},
        {'title': 'Пицца-чизбургер', 'price': '95000', 'img': 'Pitsa-chizburger.jpg', 'smallmenu': 'Pitsa',
         'papka': 'Pitsa'},
        {'title': 'Пицца Маргарита', 'price': '55000', 'img': 'Pitsa Margarita.jpg', 'smallmenu': 'Pitsa',
         'papka': 'Pitsa'},
        {'title': 'Пицца с мясом', 'price': '92000', 'img': 'Pitsa s myasom.jpg', 'smallmenu': 'Pitsa',
         'papka': 'Pitsa'},
        {'title': 'Пицца Пепперони', 'price': '72000', 'img': 'Pitsa Pepperoni.jpg', 'smallmenu': 'Pitsa',
         'papka': 'Pitsa'},

        {'title': 'Afg‘on non', 'price': '17000', 'img': 'Afg‘on non.jpg', 'smallmenu': 'Tandir', 'papka': 'Tandir'},
        {'title': 'Turk non', 'price': '7000', 'img': 'Turk non.jpg', 'smallmenu': 'Tandir', 'papka': 'Tandir'},
        {'title': 'Qiymali kasharli пиде', 'price': '56000', 'img': 'Kimali kasharli pide.jpg', 'smallmenu': 'Tandir',
         'papka': 'Tandir'},
        {'title': 'Laxmajun', 'price': '27000', 'img': 'Laxmajun.jpg', 'smallmenu': 'Tandir', 'papka': 'Tandir'},
        {'title': 'Kasharli (sirniy) пиде', 'price': '40000', 'img': 'Kasharli (sirniy) pide.jpg',
         'smallmenu': 'Tandir', 'papka': 'Tandir'},
        {'title': 'Турецкие пиде с фаршем и сыром', 'price': '65000', 'img': 'Turetskie pide s farshem i sirom.jpg',
         'smallmenu': 'Tandir', 'papka': 'Tandir'},
        {'title': 'Кимали (мясной фарш) пиде', 'price': '51000', 'img': 'Kimali (myasnoy farsh) pide.jpg',
         'smallmenu': 'Tandir', 'papka': 'Tandir'},
        {'title': "Qushboshi  (to'g'ralgan mol go'shti) пиде", 'price': '61000',
         'img': "Qushboshi  (to'g'ralga mol go'shti) pide.jpg", 'smallmenu': 'Tandir', 'papka': 'Tandir'},

        {'title': 'Anor Sok 1l', 'price': '115000', 'img': 'Anor Sok 1 l.jpg', 'smallmenu': 'Mevalar',
         'papka': 'Mevalar'},
        {'title': "Qovun to'g'ralgan", 'price': '21000', 'img': "Qovun to'g'ralgan.jpg", 'smallmenu': 'Mevalar',
         'papka': 'Mevalar'},
        {'title': 'VIP  Assorti', 'price': '380000', 'img': 'V  I  P  Assorti.jpg', 'smallmenu': 'Mevalar',
         'papka': 'Mevalar'},
        {'title': 'Ananas 1 ta', 'price': '205000', 'img': 'Ananas 1sht.jpg', 'smallmenu': 'Mevalar',
         'papka': 'Mevalar'},
        {'title': 'Apelsin sok', 'price': '135000', 'img': 'Apelsin sok.jpg', 'smallmenu': 'Mevalar',
         'papka': 'Mevalar'},
        {'title': 'Sabzi sok', 'price': '26000', 'img': 'Sabzi sok.jpg', 'smallmenu': 'Mevalar', 'papka': 'Mevalar'},
        {'title': 'Olma-sabzi soki', 'price': '45000', 'img': 'Olma sabzi soki.jpg', 'smallmenu': 'Mevalar',
         'papka': 'Mevalar'},
        {'title': 'Olma sok 1l', 'price': '75000', 'img': 'Olma sok 1l.jpg', 'smallmenu': 'Mevalar',
         'papka': 'Mevalar'},
        {'title': 'Limon sok 1l', 'price': '155000', 'img': 'Limon sok 1l.jpg', 'smallmenu': 'Mevalar',
         'papka': 'Mevalar'},
        {'title': 'Fruktovoe assorti [b]', 'price': '250000', 'img': 'Fruktovoe assorti [b].jpg',
         'smallmenu': 'Mevalar', 'papka': 'Mevalar'},
        {'title': 'Fruktovoe assorti [c]', 'price': '165000', 'img': 'Fruktovoe assorti [c].jpg',
         'smallmenu': 'Mevalar', 'papka': 'Mevalar'},
        {'title': 'Fruktovoe assorti [m]', 'price': '100000', 'img': 'Fruktovoe assorti [m].jpg',
         'smallmenu': 'Mevalar', 'papka': 'Mevalar'},

        {'title': 'Carbonara con pollo', 'price': '54000', 'img': 'Carbonara con pollo.jpg',
         'smallmenu': 'Italian Pasta', 'papka': 'Pasta Italiana'},
        {'title': 'Fettuccine con pollo e funghi', 'price': '56000', 'img': 'Fettuccine con pollo e funghi.jpg',
         'smallmenu': 'Italian Pasta', 'papka': 'Pasta Italiana'}
    ]
    # for i in small_menu_detail:
    #     with open(f"D:\\gavhardaki rasmla\\gavhardaki rasmla\\{i['papka']}\\{i["img"]}", 'rb') as img_file:
    #         # Rasmni Django ImageField formatiga o'tkazish
    #         img = File(img_file)
    #         title = i['title']
    #         price = i['price']
    #         small_menu_instance, created = SmallMenu.objects.get_or_create(title=i['smallmenu'])
    #         Product.objects.create(
    #             title=title,
    #             img=img,
    #             price=price,
    #             smallmenu=small_menu_instance
    #         )

    small_list = [

        {
            "img": "Qaxva.jpg",
            "big_menu": "Bar"
        },

        {
            "img": "Limonad.jpg",
            "big_menu": "Bar"
        },
        {
            "img": "Ichimliklar.jpg",
            "big_menu": "Bar"
        },
        {
            "img": "Energetik.jpg",
            "big_menu": "Bar"
        },
        {
            "img": "Sok.jpg",
            "big_menu": "Bar"
        },
        {
            "img": "Shokolad.jpg",
            "big_menu": "Bar"
        },
        {
            "img": "Moxito.jpg",
            "big_menu": "Bar"
        },
        {
            "img": "Shirinlik.jpg",
            "big_menu": "Shirinliklar"
        },
        {
            "img": "Syurpriz.jpg",
            "big_menu": "Shirinliklar"
        },
        {
            "img": "Non.jpg",
            "big_menu": "Non va Choy"
        },
        {
            "img": "Choy.jpg",
            "big_menu": "Non va Choy"
        },
        {
            "img": "Salat.jpg",
            "big_menu": "Taomlar"
        },
        {
            "img": "Salqin gazak.jpg",
            "big_menu": "Taomlar"
        },
        {
            "img": "Sho‘rva.jpg",
            "big_menu": "Taomlar"
        },
        {
            "img": "Yevropa taomlari.jpg",
            "big_menu": "Taomlar"
        },
        {
            "img": "Milliy taomlar.jpg",
            "big_menu": "Taomlar"
        },
        {
            "img": "Go‘shtli taomlar.jpg",
            "big_menu": "Taomlar"
        },
        {
            "img": "Xamirli taomlar.jpg",
            "big_menu": "Taomlar"
        },
        {
            "img": "Garnir va Sous.jpg",
            "big_menu": "Taomlar"
        },
        {
            "img": "Baliq taomlari.jpg",
            "big_menu": "Taomlar"
        },
        {
            "img": "Shashlik.jpg",
            "big_menu": "Taomlar"
        },
        {
            "img": "Turk yemaklari.jpg",
            "big_menu": "Taomlar"
        },
        {
            "img": "Pitsa.jpg",
            "big_menu": "Taomlar"
        },
        {
            "img": "Tandir.jpg",
            "big_menu": "Taomlar"
        },
        {
            "img": "Mevalar.jpg",
            "big_menu": "Taomlar"
        },
        {
            "img": "Italian Pasta.jpg",
            "big_menu": "Taomlar"
        },
    ]

    # for i in small_list:
    #     with open(f"D:\\gavhardaki rasmla\\gavhardaki rasmla\\qoshildi\\{i["img"]}", 'rb') as img_file:
    #         # Rasmni Django ImageField formatiga o'tkazish
    #         img = File(img_file)
    #         title = i["img"].split('.')[0]
    #         big_menu_title = i["big_menu"]
    #         big_menu_instance, created = BigMenu.objects.get_or_create(title=big_menu_title)
    #
    #         # BigMenu modeliga saqlash
    #         SmallMenu.objects.create(
    #             title=title,
    #             img=img,
    #             bigmenu=big_menu_instance
    #         )
    #

    big = ["Bar.jpg",
           "Shirinliklar.jpg",
           "Non va Choy.jpg",
           "Taomlar.jpg"
           ]
    # for i in big:
    #     with open(f"D:\\gavhardaki rasmla\\gavhardaki rasmla\\qoshildi\\{i}", 'rb') as img_file:
    #         # Rasmni Django ImageField formatiga o'tkazish
    #         img = File(img_file)
    #         title = i.split('.')[0]
    #         BigMenu.objects.create(
    #             title=title,
    #             img=img
    #         )

    return render(request, 'cart.html')


def bigmenu_list(request):
    bigmenus = BigMenu.objects.all()
    smallmenus = SmallMenu.objects.all()
    random_small = smallmenus.order_by('?')[:15]
    return render(request, 'index.html', {'bigmenus': bigmenus, 'random_small': random_small})



def bigmenu_detail(request, pk):
    bigmenu = BigMenu.objects.get(id=pk)
    smallmenus = bigmenu.smallmenu_set.all()  # Bu yerda `smallmenu_set` ishlatiladi
    return render(request, 'bigmenu_detail.html', {'bigmenu': bigmenu, 'smallmenus': smallmenus})


def smallmenu_detail(request, pk):
    smallmenu = get_object_or_404(SmallMenu, id=pk)
    smallmenus = SmallMenu.objects.all()
    products = smallmenu.product_set.all()
    return render(request, 'small_menu_detail.html',
                  {'smallmenu': smallmenu, 'products': products, 'smallmenus': smallmenus})


# BigMenu API
class BigMenuListView(APIView):
    def get(self, request):
        bigmenus = BigMenu.objects.all()
        serializer = BigMenuSerializer(bigmenus, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BigMenuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BigMenuDetailView(APIView):
    def get_object(self, pk):
        try:
            return BigMenu.objects.get(pk=pk)
        except BigMenu.DoesNotExist:
            return None

    def get(self, request, pk):
        bigmenu = self.get_object(pk)
        if bigmenu is None:
            return Response({"error": "BigMenu not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = BigMenuSerializer(bigmenu)
        return Response(serializer.data)

    def put(self, request, pk):
        bigmenu = self.get_object(pk)
        if bigmenu is None:
            return Response({"error": "BigMenu not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = BigMenuSerializer(bigmenu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        bigmenu = self.get_object(pk)
        if bigmenu is None:
            return Response({"error": "BigMenu not found"}, status=status.HTTP_404_NOT_FOUND)

        bigmenu.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# SmallMenu API
class SmallMenuListView(APIView):
    def get(self, request):
        smallmenus = SmallMenu.objects.all()
        serializer = SmallMenuSerializer(smallmenus, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SmallMenuSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SmallMenuDetailView(APIView):
    def get_object(self, pk):
        try:
            return SmallMenu.objects.get(pk=pk)
        except SmallMenu.DoesNotExist:
            return None

    def get(self, request, pk):
        smallmenu = self.get_object(pk)
        if smallmenu is None:
            return Response({"error": "SmallMenu not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = SmallMenuSerializer(smallmenu)
        return Response(serializer.data)

    def put(self, request, pk):
        smallmenu = self.get_object(pk)
        if smallmenu is None:
            return Response({"error": "SmallMenu not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = SmallMenuSerializer(smallmenu, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        smallmenu = self.get_object(pk)
        if smallmenu is None:
            return Response({"error": "SmallMenu not found"}, status=status.HTTP_404_NOT_FOUND)

        smallmenu.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Product API
class ProductListView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetailView(APIView):
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return None

    def get(self, request, pk):
        product = self.get_object(pk)
        if product is None:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def put(self, request, pk):
        product = self.get_object(pk)
        if product is None:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk):
        product = self.get_object(pk)
        if product is None:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = ProductSerializer(product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        product = self.get_object(pk)
        if product is None:
            return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)

        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
