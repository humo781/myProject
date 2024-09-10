from django.shortcuts import HttpResponse


def first_page(request):
    response = """
        <h1>My library</h1>
        <ol>
            <li><a href="book/1"> 1984</a></>
            <li><a href="book/2"> O'tgan kunlar </a></>
            <li><a href="book/3"> Hayot yutqazgan joyingdan boshlanar </a></>
        </ol>
        
    """
    return HttpResponse(response)


def first_book(request):
    response = """
           <h1>1984</h1>
           <h5>Author: George Orwell</h5>
           <p>
           This article is about the 1949 novel by George Orwell. For the year, see 1984. For other uses,\
            see 1984 (disambiguation). Nineteen Eighty-Four First-edition cover Author	George Orwell \
            Cover artist Michael Kennard[1] Language English Genre Dystopianpolitical fictionsocial science \
             fiction Set in	London, Airstrip One, Oceania Publisher	Secker & Warburg Publication date \
             8 June 1949 Publication place	United Kingdom Media type Print (hardback and paperback) Pages	\
             328 OCLC 470015866 Dewey Decimal 823.912[2] LC Class	PZ3.O793 Ni2 Preceded by	Animal Farm \
            Nineteen Eighty-Four (also published as 1984) is a dystopian novel and cautionary tale by English \
             writer George Orwell. It was published on 8 June 1949 by Secker & Warburg as Orwell's ninth and \
              final book completed in his lifetime.</p>
           <a href="../">back</a>
       """
    return HttpResponse(response)

def second_book(request):
    response = """
           <h1>O'tgan kunlar</h1>
           <h5>Author: Abdulla Qodiriy</h5>
           <p>
           Oʻtkan kunlar, baʼzi manbalarda Oʻtgan kunlar – oʻzbek yozuvchisi Abdulla Qodiriy qalamiga mansub oʻzbek adabiyotidagi ilk roman[1]. 1969-yil „Oʻzbekfilm“ \
            kinostudiyasida ushbu roman asosida „Oʻtgan kunlar“ nomli film suratga olingan. Adib romanni yozishda arab yozuvchisi Jurji Zaydon asarlaridan ilhomlangan. \
             Roman 1920-yillar boshida yozilgan boʻlib, 1922-yil ilk bor „Inqilob“ jurnalida chop etilgan va 1926-yilda alohida kitob holida nashr etilgan.</p>
           <a href="../">back</a>
       """
    return HttpResponse(response)

def third_book(request):
    response = """
           <h1>Hayot yutqazgan joyingdan boshlanar </h1>
           <h5>Author: Amina Shenliko'g'li</h5>
           <p>
           Men Senga muammosiz hayot va'da qilmayman. Bu dunyo mukammallik uchun yaratilmagan. Lekin Jannatda istagan hamma narsamiz bo'ladi. Men o'sha manzilgacha \
            bo'lgan yo’lda Senga yo'ldoshlik qilishni taklif qila olaman xolos. Unga ham agar Alloh izn bersa.</p>
           <a href="../">back</a>
       """
    return HttpResponse(response)
