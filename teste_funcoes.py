

# from sys import getsizeof as size
# from collections import Counter
#
# var = """
# Am 9. November 1989 sitzt Günter Schabowski, Mitglied des Politbüros der Deutschen Demokratischen Republik (DDR),
# auf einem roten Sessel im Pressezentrum des Zentralkomitees der Staatspartei SED in Ostberlin. Eine Stunde lang
# antwortet er auf Fragen von Journalisten aus der ganzen Welt. Kurz vor dem Ende hat ein italienischer Journalist noch
# eine Frage. Schabowski nimmt einen Zettel aus der Jacke. Nur kurz hat er den Text davor gelesen, eigentlich soll er
# die Medien erst am nächsten Morgen darüber informieren. Es soll in Zukunft einfacher werden, aus der DDR auszureisen,
# sagt er. Das ist bis jetzt nämlich noch verboten. Deshalb sind viele Tausend DDR-Bürger zuletzt über die damalige
# Tschechoslowakei in die Bundes republik Deutschland geflohen. Sie wollen sich nicht mehr in ihrem Land einsperren
# lassen. Außerdem wollen sie politische Reformen. Die Regierung muss deshalb etwas tun. Jetzt sollen DDR-Bürger Reisen
# beantragen können. Die Anträge sollen schnell geprüft werden. Es ist 18.53 Uhr, als Schabowski den Zettel nimmt und
# die Sätze vorliest. Im Fernsehen der DDR ist die Pressekonferenz live zu sehen. Ein Journalist will wissen, ab wann
# die neue Regelung gelten soll. Schabowski zuckt mit den Schultern. Dann sagt er die Worte, nach denen die Welt eine
# andere ist: „Das tritt nach meiner Kenntnis … ist das sofort, unverzüglich.“ Ein Fehler. Erst ab dem nächsten Morgen,
# vier Uhr, sollte die Regel eigentlich gelten. An der Grenze ist noch niemand informiert.
# """
#
# "Counter gera uma grande quantidade de armazenamento"
# "Sua vantagem é somente o acesso fácil ao dado por chave"
# scan = Counter(var.split())
# print(size(scan))   # 5184
# print(scan)
#
# "Counter com most common tupla gera quantidade de armazenamento bem reduzida"
# "O acesso não é fácil, e por isso, além de fazer o procedimento, é preciso gerar uma pequeno algoritmo"
# scan2 = Counter(var.split()).most_common(len(var.split()))  # tuple() pode ser usado para diminuir ainda mais
# print(size(scan2))  # 724
# print(scan2)
#
# "Esse pequeno algoritmo consegue achar o dado desejado"
# data = input('Data name -> ')
# for each_data in scan2:
#     if each_data[0] == data:
#         print((each_data[0], each_data[1]))
