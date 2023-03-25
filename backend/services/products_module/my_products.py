if Product.objects.all().count == 0:
    product1 = Product.objects.create(title="Мобильный телефон Samsung Galaxy S22 Ultra 12/512GB Phantom Black (SM-S908BZKHSEK)", 
                                    description= 'Экран (6.8", Dynamic AMOLED 2X, 3088x1440) / Samsung Exynos 2200 (2.8 ГГц + 2.5 ГГц + 1.8 ГГц) / основная квадро-камера: 108 Мп + 12 Мп + 10 Мп + 10 Мп, фронтальная 40 Мп / RAM 12 ГБ / 512 ГБ встроенной памяти / 3G / LTE / 5G / GPS / поддержка 2х SIM-карт (Nano-SIM) / Android 12 / 5000 мА*ч',
                                    price= 51099,
                                    currency=currency,
                                    owner=user1,
                                    img='https://content2.rozetka.com.ua/goods/images/big/253281756.jpg')
    product2 = Product.objects.create(title="Мобильный телефон Samsung Galaxy M13 4/64GB Light Blue (SM-M135FLBDSEK)", 
                                    description= 'Экран (6.6", PLS, 2408x1080) / Samsung Exynos 850 (2.0 ГГц) / тройная основная камера: 50 Мп + 5 Мп + 2 Мп, фронтальная камера: 8 Мп / RAM 4 ГБ / 64 ГБ встроенной памяти + microSD (до 1 ТБ) / 3G / LTE / GPS / поддержка 2х SIM-карт (Nano-SIM) / Android 12 / 5000 мА*ч',
                                    price= 6749,
                                    currency=currency,
                                    owner=user1,
                                    img='https://content2.rozetka.com.ua/goods/images/big/277025916.jpg')
    product3 = Product.objects.create(title="Мобильный телефон Nokia G10 3/32GB Blue (719901148421)", 
                                    description= 'Экран (6.5", IPS 1600x720) / MediaTek Helio G25 (2.0 ГГц) / тройная основная камера: 13 Мп + 2 Мп + 2 Мп, фронтальная 8 Мп / RAM 3 ГБ / 32 ГБ встроенной памяти + microSD (до 512 ГБ) / 3G / LTE / GPS / поддержка 2х SIM-карт (Nano-SIM) / Android 11 / 5050 мА*ч',
                                    price= 4499,
                                    currency=currency,
                                    owner=user1,
                                    img='https://content2.rozetka.com.ua/goods/images/big/175052344.jpg')
    product4 = Product.objects.create(title="Телевизор Samsung UE55AU7100UXUA", 
                                    description= 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Pariatur autem reprehenderit cum nemo! Voluptatum, sequi aliquid ratione eaque non vitae, id ipsum saepe esse qui dolorem soluta quasi necessitatibus laudantium.',
                                    price= 23999,
                                    currency=currency,
                                    owner=user1,
                                    img='https://content.rozetka.com.ua/goods/images/big/303985527.jpg')
    product5 = Product.objects.create(title="Телевизор Samsung QE65Q70BAUXUA", 
                                    description= '...',
                                    price= 62999,
                                    currency=currency,
                                    owner=user1,
                                    img='')