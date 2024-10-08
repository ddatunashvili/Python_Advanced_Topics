# ADVANCED PYTHON

## Table of Contents

| №  | Topic                             | File                                                       |
|----|-----------------------------------|------------------------------------------------------------|
| 1  | აბსტრაქტული მეთოდები              | [`absmethod.py`](#absmethodpy)                             |
| 2  | სიკვდილის შემდეგ                  | [`afterdeath.py`](#afterdeathpy)                           |
| 3  | კლასის მეთოდები                   | [`classmethod.py`](#classmethodpy)                         |
| 4  | ნაგულისხმევი პარამეტრები          | [`default_params.py`](#default_paramspy)                   |
| 5  | მონაცემთა კლასიფიკაცია             | [`dataclasing.py`](#dataclasingpy)                         |
| 6  | აღმწერები                          | [`descriptoring.py`](#descriptoringpy)                     |
| 7  | ფუნქციის ქეშირება კლასებით        | [`func_class_cache.py`](#func_class_cachepy)               |
| 8  | Keep Alive                         | [`keep_alive.py`](#keep_alivepy)                           |
| 9  | მეტაკლასები                         | [`metaclassing.py`](#metaclassingpy)                        |
| 10 | პოლიდეკორატორები                   | [`polydecor.py`](#polydecorpy)                             |
| 11 | პროტოკოლირება                      | [`protocoling.py`](#protocolingpy)                         |
| 12 | reducer-ის ფუნქციები              | [`reducer.py`](#reducerpy)                                |
| 13 | სტატიკური მეთოდები                | [`statical.py`](#staticalpy)                               |
| 14 | Wrap დეკორატორები                 | [`wrapdecor.py`](#wrapdecorpy)                             |

## absmethod.py

ეს ფაილი იკვლევს აბსტრაქტული მეთოდების გამოყენებას პითონში. აბსტრაქტული მეთოდები გამოიყენება საბაზისო კლასიებში (ABCs) და განსაზღვრავს მეთოდებს, რომლებიც უნდა განხორციელდეს ქვეკლასების მიერ, რათა უზრუნველყოს საერთო ინტერფეისი.

## afterdeath.py

ეს სკრიპტი აჩვენებს პითონში გაწმენდისა და რესურსების მართვის მოწინავე ტექნიკას `atexit` მოდულის გამოყენებით. ის უზრუნველყოფს, რომ მითითებული ფუნქციები შესრულდეს პითონის თარჯიმანის შეწყვეტისას, იმისდა მიუხედავად, რომელი ტიპის შეწყვეტაა - ნორმალური თუ გამონაკლისით.

## classmethod.py

განმარტავს `@classmethod` დეკორატორის გამოყენებას Python-ში, რაც საშუალებას გაწვდოს მეთოდები, რომლებიც დაკავშირებულია კლასთან და არა კონკრეტულ მაგალითებთან. ეს მეთოდები ხშირად გამოიყენება კლასი-მეთოდების განსაზღვრაში.

## default_params.py

ეს სკრიპტი აჩვენებს `functools.partial`-ის გამოყენებას ნაწილობრივ გამოყენებული ფუნქციების შესაქმნელად. მიუხედავად იმისა, რომ პირდაპირ არ ეხება ნაგულისხმევ პარამეტრებს, `functools.partial` გაწვდავს ფუნქციებს ნაწილობრივ კონკრეტულ არგუმენტებზე და ამარტივებს მათი გამოძახების პროცესს.

## dataclasing.py

აჩვენებს Python-ის `@dataclass` დეკორატორის გამოყენებას, რომელიც დაინერგა Python 3.7-ში. ეს დეკორატორი ამარტივებს კლასების შექმნას, ავტომატურად გენერირებს სპეციალურ მეთოდებს, როგორიცაა `__init__()`, `__repr__()` და `__eq__()`.

## descriptoring.py

ეს ფაილი ახდენს დესკრიპტორების სიღრმისეულ განხილვას, რაც დაბალი დონის მექანიზმი საშუალებას გაწვდოს, როგორ უნდა იმართოს ატრიბუტების წვდომა ობიექტებში, მათ შორის მორგებული მიმღებები, სეტერები და დელეტერები.

## func_class_cache.py

იკვლევს ფუნქციების გამომავალი ქეშირების ტექნიკას კლასების დონეზე, რაც აუმჯობესებს შესრულებას და ამცირებს ძვირადღირებული ოპერაციების განხორციელების დროს.

## keep_alive.py

ასახავს სტრატეგიებს კავშირების, პროცესების ან სხვა გრძელვადიანი ამოცანების შესანარჩუნებლად, რაც უზრუნველყოფს მათი მუშაობის გაგრძელებას ხანგრძლივი პერიოდის განმავლობაში.

## metaclassing.py

შემოაქვს მეტაკლასები, რომლებიც იწერებიან როგორც „კლასების კლასები“. ეს საშუალებას გაწვდოს კლასების შექმნის პროცესი, დაამატოს გაფართოებული პერსონალიზაცია და ქცევა.

## polydecor.py

მოიცავს დეკორატორების შექმნის ტექნიკას, რომლებიც ადაპტირებენ სხვადასხვა კონტექსტში და აჩვენებს, როგორ უნდა შექმნან დეკორატორები, რომლებიც შეიძლება ხელახლა გამოიყენონ და შეცვალონ ფუნქციის ხელმოწერების საფუძველზე.

## protocoling.py

დეტალურად არის აღწერილი პროტოკოლების გამოყენება ("პროტოკოლის" მოდულიდან) Python-ში, რაც საშუალებას გაწვდოს სტრუქტურული ტიპები მემკვიდრეობის გარეშე და უზრუნველყოფოს ინტერფეისის დიზაინის მოქნილი მიდგომა.

## reducer.py

განიხილავს `reduce()` ფუნქციას `functools` მოდულიდან, რომელიც გამოიყენება კუმულაციური ოპერაციების შესასრულებლად განმეორებადი მონაცემთა სტრუქტურებზე.

## statical.py

განმარტავს `@staticmethod`-ის გამოყენებას Python-ში, რაც განსაზღვრავს მეთოდებს, რომლებიც არ მოქმედებენ ინსტანციაზე ან კლასზე, მაგრამ შედის კლასში ლოგიკური დაჯგუფებისთვის.

## wrapdecor.py

ფოკუსირებულია დეკორატორის მოწინავე ტექნიკაზე, განსაკუთრებით ფუნქციების გაფართოების ტექნიკაზე და ორიგინალური ფუნქციის ხელმოწერის შენარჩუნებისას `functools.wraps`-ის გამოყენებით.

---

თავისუფლად შეისწავლეთ თითოეული ფაილი, რათა უფრო ღრმად გაიგოთ ამ მოწინავე პითონის კონცეფციები. მისასალმებელია წვლილის შეტანა, პრობლემები და მოთხოვნები!
