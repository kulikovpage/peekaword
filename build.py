#!/usr/bin/env python3
"""Peekaword website on GitHub Pages (https://kulikovpage.github.io/peekaword/).

Writes index.html (support page, the App Store "Support URL") and privacy/index.html (the "Privacy Policy URL").
All texts for the 7 app languages live here: edit, run `python3 build.py`, commit and push.
One page per kind; languages are sections switched by `#en`, `#uk`… (the browser language picks one by default).
"""
from pathlib import Path

ROOT = Path(__file__).parent
ISSUES = "https://github.com/kulikovpage/peekaword/issues"
LANGS = [("en", "English"), ("uk", "Українська"), ("ru", "Русский"), ("pl", "Polski"),
         ("es", "Español"), ("fr", "Français"), ("pt", "Português")]

TAGLINE = {
    "en": "A new word on your Lock Screen",
    "uk": "Нове слово на екрані блокування",
    "ru": "Новое слово на экране блокировки",
    "pl": "Nowe słowo na ekranie blokady",
    "es": "Una palabra nueva en tu pantalla bloqueada",
    "fr": "Un nouveau mot sur votre écran verrouillé",
    "pt": "Uma palavra nova na sua Tela Bloqueada",
}

# Support page: (heading, paragraphs). "{issues}" becomes the GitHub issues link.
SUPPORT = {
    "en": ("Help", [
        ("Add the widget", ["<b>Lock Screen:</b> touch and hold the Lock Screen → Customise → Lock Screen → tap below the clock → Peekaword.",
                            "<b>Home Screen:</b> touch and hold an empty spot → + or Edit → Add Widget → Peekaword.",
                            "The app shows the same steps as a video: Settings → How to add the widget."]),
        ("Reminders", ["Settings → Reminders: turn them on and pick a time. At most one a day, and only when there is a reason."]),
        ("Subscription", ["Optional: all learning is free and has no ads.",
                          "Manage or cancel: iOS Settings → your name → Subscriptions. After reinstalling: Settings → Support the project → Restore purchases."]),
        ("Contact", ["Found a bug or a wrong translation? <a href=\"{issues}\">Open an issue on GitHub</a>."]),
    ]),
    "uk": ("Допомога", [
        ("Додати віджет", ["<b>Екран блокування:</b> затисни екран блокування → «Налаштувати» → «Екран блокування» → торкнись під годинником → Peekaword.",
                           "<b>Робочий стіл:</b> затисни порожнє місце → «+» або «Редагувати» → «Додати віджет» → Peekaword.",
                           "У застосунку ці кроки є у відео: Налаштування → «Як додати віджет»."]),
        ("Нагадування", ["Налаштування → «Нагадування»: увімкни й обери час. Не більше одного на день і лише коли є привід."]),
        ("Підписка", ["Необов'язкова: усе навчання безкоштовне й без реклами.",
                      "Керувати чи скасувати: Параметри iOS → твоє ім'я → Підписки. Після перевстановлення: Налаштування → «Підтримати проєкт» → «Відновити покупки»."]),
        ("Зв'язок", ["Знайшов помилку чи неточний переклад? <a href=\"{issues}\">Напиши на GitHub</a>."]),
    ]),
    "ru": ("Помощь", [
        ("Добавить виджет", ["<b>Экран блокировки:</b> зажми экран блокировки → «Настроить» → «Экран блокировки» → нажми под часами → Peekaword.",
                             "<b>Рабочий стол:</b> зажми пустое место → «+» или «Править» → «Добавить виджет» → Peekaword.",
                             "В приложении эти шаги есть в видео: Настройки → «Как добавить виджет»."]),
        ("Напоминания", ["Настройки → «Напоминания»: включи и выбери время. Не больше одного в день и только по делу."]),
        ("Подписка", ["Необязательная: вся учёба бесплатна и без рекламы.",
                      "Управлять или отменить: Настройки iOS → твоё имя → Подписки. После переустановки: Настройки → «Поддержать проект» → «Восстановить покупки»."]),
        ("Связь", ["Нашёл ошибку или неточный перевод? <a href=\"{issues}\">Напиши на GitHub</a>."]),
    ]),
    "pl": ("Pomoc", [
        ("Dodaj widżet", ["<b>Ekran blokady:</b> przytrzymaj ekran blokady → „Dostosuj” → „Ekran blokady” → stuknij pod zegarem → Peekaword.",
                          "<b>Ekran początkowy:</b> przytrzymaj puste miejsce → + lub „Edycja” → „Dodaj widżet” → Peekaword.",
                          "W aplikacji te kroki są na filmie: Ustawienia → „Jak dodać widżet”."]),
        ("Przypomnienia", ["Ustawienia → „Przypomnienia”: włącz i wybierz godzinę. Najwyżej jedno dziennie i tylko z powodu."]),
        ("Subskrypcja", ["Opcjonalna: cała nauka jest darmowa i bez reklam.",
                         "Zarządzanie i anulowanie: Ustawienia iOS → Twoje imię → Subskrypcje. Po ponownej instalacji: Ustawienia → „Wesprzyj projekt” → „Przywróć zakupy”."]),
        ("Kontakt", ["Znalazłeś błąd albo nietrafione tłumaczenie? <a href=\"{issues}\">Napisz na GitHubie</a>."]),
    ]),
    "es": ("Ayuda", [
        ("Añadir el widget", ["<b>Pantalla bloqueada:</b> mantén pulsada la pantalla bloqueada → Personalizar → Pantalla bloqueada → toca bajo la hora → Peekaword.",
                              "<b>Pantalla de inicio:</b> mantén pulsado un espacio vacío → + o Editar → Añadir widget → Peekaword.",
                              "En la app estos pasos están en vídeo: Ajustes → Cómo añadir el widget."]),
        ("Recordatorios", ["Ajustes → Recordatorios: actívalos y elige la hora. Como mucho uno al día y solo si hay motivo."]),
        ("Suscripción", ["Opcional: todo el aprendizaje es gratis y sin anuncios.",
                         "Gestionar o cancelar: Ajustes de iOS → tu nombre → Suscripciones. Tras reinstalar: Ajustes → Apoya el proyecto → Restaurar compras."]),
        ("Contacto", ["¿Encontraste un error o una traducción imprecisa? <a href=\"{issues}\">Escríbenos en GitHub</a>."]),
    ]),
    "fr": ("Aide", [
        ("Ajouter le widget", ["<b>Écran verrouillé :</b> maintenez le doigt sur l'écran verrouillé → Personnaliser → Écran verrouillé → touchez sous l'heure → Peekaword.",
                               "<b>Écran d'accueil :</b> maintenez le doigt sur un espace vide → + ou Modifier → Ajouter un widget → Peekaword.",
                               "Dans l'app, ces étapes sont en vidéo : Réglages → Ajouter le widget."]),
        ("Rappels", ["Réglages → Rappels : activez-les et choisissez l'heure. Au plus un par jour, et seulement s'il y a une raison."]),
        ("Abonnement", ["Facultatif : tout l'apprentissage est gratuit et sans publicité.",
                        "Gérer ou annuler : Réglages d'iOS → votre nom → Abonnements. Après réinstallation : Réglages → Soutenir le projet → Restaurer les achats."]),
        ("Contact", ["Un bug ou une traduction inexacte ? <a href=\"{issues}\">Écrivez-nous sur GitHub</a>."]),
    ]),
    "pt": ("Ajuda", [
        ("Adicionar o widget", ["<b>Tela Bloqueada:</b> toque e segure a Tela Bloqueada → Personalizar → Tela Bloqueada → toque abaixo do relógio → Peekaword.",
                                "<b>Tela de Início:</b> toque e segure um espaço vazio → + ou Editar → Adicionar Widget → Peekaword.",
                                "No app esses passos estão em vídeo: Ajustes → Como adicionar o widget."]),
        ("Lembretes", ["Ajustes → Lembretes: ative e escolha o horário. No máximo um por dia e só quando há motivo."]),
        ("Assinatura", ["Opcional: todo o aprendizado é gratuito e sem anúncios.",
                        "Gerenciar ou cancelar: Ajustes do iOS → seu nome → Assinaturas. Depois de reinstalar: Ajustes → Apoie o projeto → Restaurar compras."]),
        ("Contato", ["Achou um erro ou uma tradução imprecisa? <a href=\"{issues}\">Escreva no GitHub</a>."]),
    ]),
}

PRIVACY_LINK = {"en": "Privacy Policy", "uk": "Політика конфіденційності", "ru": "Политика конфиденциальности",
                "pl": "Polityka prywatności", "es": "Política de privacidad", "fr": "Politique de confidentialité",
                "pt": "Política de privacidade"}
SUPPORT_LINK = {"en": "Help", "uk": "Допомога", "ru": "Помощь", "pl": "Pomoc", "es": "Ayuda", "fr": "Aide", "pt": "Ajuda"}

# Privacy policy: (title, updated, sections).
PRIVACY = {
    "en": ("Privacy Policy", "Updated October 5, 2026", [
        ("In short", "Peekaword collects no personal data. No account, no ads, no analytics, no tracking."),
        ("Your data", "Settings, learning progress, daily goal and streak are stored on your iPhone and shared between the app and its widgets. Progress (words, stats, streak and your own words) is also saved in your iCloud, so a new phone doesn't lose it. It stays in your iCloud; we have no access to it. Deleting the app deletes the data from the device."),
        ("Pronunciation", "Words are spoken by the voices built into iOS, on your device."),
        ("Reminders", "Reminders are local notifications created on your iPhone. They are optional and can be turned off in the app's Settings or in iOS Settings."),
        ("Purchases", "Optional purchases (a subscription or a one-time purchase) are processed by Apple through the App Store. We never receive your name, email or payment details: the app only checks on your device what you have bought. Manage or cancel a subscription in iOS Settings → your name → Subscriptions."),
        ("Crash reports", "If you have chosen in iOS Settings to share analytics with app developers, Apple may send us anonymous crash and performance reports. They contain no personal information."),
        ("Children", "The app is suitable for all ages and collects no data from anyone, including children."),
        ("Changes", "If this policy changes, we will update this page and the date above."),
        ("Contact", "Questions? <a href=\"{issues}\">Open an issue on GitHub</a>."),
    ]),
    "uk": ("Політика конфіденційності", "Оновлено 5 жовтня 2026 р.", [
        ("Коротко", "Peekaword не збирає персональних даних. Немає облікового запису, реклами, аналітики й відстеження."),
        ("Ваші дані", "Налаштування, прогрес, мета на день і серія зберігаються на вашому iPhone і спільні для застосунку та його віджетів. Прогрес (слова, статистика, серія і ваші слова) також зберігається у вашому iCloud, щоб не загубитися при зміні телефона. Він лишається у вашому iCloud, ми не маємо до нього доступу. Якщо видалити застосунок, дані видаляються з пристрою."),
        ("Вимова", "Слова озвучують вбудовані голоси iOS безпосередньо на пристрої."),
        ("Нагадування", "Це локальні сповіщення, які створюються на вашому iPhone. Вони необов'язкові, їх можна вимкнути в налаштуваннях застосунку або в Параметрах iOS."),
        ("Покупки", "Необов'язкові покупки (підписку або разову покупку) обробляє Apple через App Store. Ми не отримуємо ваше ім'я, пошту чи платіжні дані: застосунок лише перевіряє на пристрої, що придбано. Керувати підпискою та скасувати її: Параметри iOS → ваше ім'я → Підписки."),
        ("Звіти про збої", "Якщо в Параметрах iOS дозволено надсилати аналітику розробникам, Apple може передавати нам анонімні звіти про збої та продуктивність. Вони не містять персональних даних."),
        ("Діти", "Застосунок підходить для будь-якого віку й ні в кого не збирає даних, зокрема в дітей."),
        ("Зміни", "Якщо політика зміниться, ми оновимо цю сторінку й дату вгорі."),
        ("Зв'язок", "Запитання? <a href=\"{issues}\">Напишіть на GitHub</a>."),
    ]),
    "ru": ("Политика конфиденциальности", "Обновлено 5 октября 2026 г.", [
        ("Коротко", "Peekaword не собирает персональные данные. Нет аккаунта, рекламы, аналитики и отслеживания."),
        ("Ваши данные", "Настройки, прогресс, цель на день и серия хранятся на вашем iPhone и общие для приложения и его виджетов. Прогресс (слова, статистика, серия и ваши слова) также сохраняется в вашем iCloud, чтобы не потеряться при смене телефона. Он остаётся в вашем iCloud, у нас к нему доступа нет. При удалении приложения данные удаляются с устройства."),
        ("Произношение", "Слова озвучивают встроенные голоса iOS прямо на устройстве."),
        ("Напоминания", "Это локальные уведомления, которые создаются на вашем iPhone. Они необязательны, их можно выключить в настройках приложения или в настройках iOS."),
        ("Покупки", "Необязательные покупки (подписку или разовую покупку) обрабатывает Apple через App Store. Мы не получаем ваше имя, почту и платёжные данные: приложение лишь проверяет на устройстве, что куплено. Управлять подпиской и отменить её: Настройки iOS → ваше имя → Подписки."),
        ("Отчёты о сбоях", "Если в настройках iOS разрешена отправка аналитики разработчикам, Apple может передавать нам анонимные отчёты о сбоях и производительности. В них нет персональных данных."),
        ("Дети", "Приложение подходит для любого возраста и ни у кого не собирает данные, в том числе у детей."),
        ("Изменения", "Если политика изменится, мы обновим эту страницу и дату вверху."),
        ("Связь", "Вопросы? <a href=\"{issues}\">Напишите на GitHub</a>."),
    ]),
    "pl": ("Polityka prywatności", "Zaktualizowano 5 października 2026 r.", [
        ("W skrócie", "Peekaword nie zbiera danych osobowych. Bez konta, reklam, analityki i śledzenia."),
        ("Twoje dane", "Ustawienia, postępy, cel dzienny i seria są przechowywane na Twoim iPhonie i wspólne dla aplikacji oraz jej widżetów. Postępy (słowa, statystyki, seria i własne słowa) są też zapisywane w Twoim iCloud, żeby nie zginęły przy zmianie telefonu. Zostają w Twoim iCloud, nie mamy do nich dostępu. Usunięcie aplikacji usuwa dane z urządzenia."),
        ("Wymowa", "Słowa czytają głosy wbudowane w iOS, bezpośrednio na urządzeniu."),
        ("Przypomnienia", "To lokalne powiadomienia tworzone na Twoim iPhonie. Są opcjonalne i można je wyłączyć w ustawieniach aplikacji lub w Ustawieniach iOS."),
        ("Zakupy", "Opcjonalne zakupy (subskrypcję lub zakup jednorazowy) obsługuje Apple w App Store. Nie otrzymujemy Twojego imienia, adresu e-mail ani danych płatniczych: aplikacja jedynie sprawdza na urządzeniu, co zostało kupione. Zarządzanie subskrypcją i anulowanie: Ustawienia iOS → Twoje imię → Subskrypcje."),
        ("Raporty o awariach", "Jeśli w Ustawieniach iOS zgodzisz się udostępniać dane analityczne twórcom aplikacji, Apple może przekazywać nam anonimowe raporty o awariach i wydajności. Nie zawierają danych osobowych."),
        ("Dzieci", "Aplikacja jest odpowiednia dla każdego wieku i nie zbiera danych od nikogo, w tym od dzieci."),
        ("Zmiany", "Jeśli polityka się zmieni, zaktualizujemy tę stronę i datę u góry."),
        ("Kontakt", "Pytania? <a href=\"{issues}\">Napisz na GitHubie</a>."),
    ]),
    "es": ("Política de privacidad", "Actualizada el 5 de octubre de 2026", [
        ("En resumen", "Peekaword no recopila datos personales. Sin cuenta, sin anuncios, sin analíticas ni seguimiento."),
        ("Tus datos", "Los ajustes, el progreso, la meta diaria y la racha se guardan en tu iPhone y se comparten entre la app y sus widgets. El progreso (palabras, estadísticas, racha y tus propias palabras) también se guarda en tu iCloud para no perderlo al cambiar de teléfono. Se queda en tu iCloud y no tenemos acceso a él. Al eliminar la app, los datos se borran del dispositivo."),
        ("Pronunciación", "Las palabras las leen las voces integradas de iOS, en tu dispositivo."),
        ("Recordatorios", "Son notificaciones locales creadas en tu iPhone. Son opcionales y puedes desactivarlas en los ajustes de la app o en los Ajustes de iOS."),
        ("Compras", "Las compras opcionales (una suscripción o un pago único) las gestiona Apple a través del App Store. No recibimos tu nombre, correo ni datos de pago: la app solo comprueba en el dispositivo qué has comprado. Para gestionar o cancelar la suscripción: Ajustes de iOS → tu nombre → Suscripciones."),
        ("Informes de errores", "Si en los Ajustes de iOS permites compartir análisis con los desarrolladores, Apple puede enviarnos informes anónimos de fallos y rendimiento. No contienen datos personales."),
        ("Niños", "La app es apta para todas las edades y no recopila datos de nadie, incluidos los niños."),
        ("Cambios", "Si esta política cambia, actualizaremos esta página y la fecha de arriba."),
        ("Contacto", "¿Preguntas? <a href=\"{issues}\">Escríbenos en GitHub</a>."),
    ]),
    "fr": ("Politique de confidentialité", "Mise à jour le 5 octobre 2026", [
        ("En bref", "Peekaword ne collecte aucune donnée personnelle. Pas de compte, pas de publicité, pas d'analyse ni de suivi."),
        ("Vos données", "Les réglages, la progression, l'objectif du jour et la série sont stockés sur votre iPhone et partagés entre l'app et ses widgets. La progression (mots, statistiques, série et vos propres mots) est aussi enregistrée dans votre iCloud pour ne pas la perdre en changeant de téléphone. Elle reste dans votre iCloud ; nous n'y avons pas accès. Supprimer l'app efface les données de l'appareil."),
        ("Prononciation", "Les mots sont lus par les voix intégrées à iOS, sur votre appareil."),
        ("Rappels", "Ce sont des notifications locales créées sur votre iPhone. Elles sont facultatives et peuvent être désactivées dans les réglages de l'app ou dans les Réglages d'iOS."),
        ("Achats", "Les achats facultatifs (un abonnement ou un achat unique) sont gérés par Apple via l'App Store. Nous ne recevons ni votre nom, ni votre e-mail, ni vos données de paiement : l'app vérifie seulement sur l'appareil ce qui a été acheté. Pour gérer ou annuler l'abonnement : Réglages d'iOS → votre nom → Abonnements."),
        ("Rapports de plantage", "Si vous avez autorisé dans les Réglages d'iOS le partage des analyses avec les développeurs, Apple peut nous transmettre des rapports anonymes de plantage et de performance. Ils ne contiennent aucune donnée personnelle."),
        ("Enfants", "L'app convient à tous les âges et ne collecte de données auprès de personne, y compris les enfants."),
        ("Modifications", "Si cette politique change, nous mettrons à jour cette page et la date ci-dessus."),
        ("Contact", "Des questions ? <a href=\"{issues}\">Écrivez-nous sur GitHub</a>."),
    ]),
    "pt": ("Política de privacidade", "Atualizada em 5 de outubro de 2026", [
        ("Resumo", "O Peekaword não coleta dados pessoais. Sem conta, sem anúncios, sem análises e sem rastreamento."),
        ("Seus dados", "Ajustes, progresso, meta diária e sequência ficam no seu iPhone e são compartilhados entre o app e seus widgets. O progresso (palavras, estatísticas, sequência e suas próprias palavras) também é salvo no seu iCloud para não se perder ao trocar de telefone. Ele fica no seu iCloud e não temos acesso a ele. Ao apagar o app, os dados são apagados do aparelho."),
        ("Pronúncia", "As palavras são lidas pelas vozes integradas do iOS, no próprio dispositivo."),
        ("Lembretes", "São notificações locais criadas no seu iPhone. São opcionais e você pode desativá-las nos ajustes do app ou nos Ajustes do iOS."),
        ("Compras", "As compras opcionais (uma assinatura ou uma compra única) são processadas pela Apple na App Store. Não recebemos seu nome, e-mail nem dados de pagamento: o app só verifica no dispositivo o que foi comprado. Para gerenciar ou cancelar a assinatura: Ajustes do iOS → seu nome → Assinaturas."),
        ("Relatórios de falhas", "Se você permitiu nos Ajustes do iOS compartilhar análises com desenvolvedores, a Apple pode nos enviar relatórios anônimos de falhas e desempenho. Eles não contêm dados pessoais."),
        ("Crianças", "O app é adequado para todas as idades e não coleta dados de ninguém, inclusive de crianças."),
        ("Alterações", "Se esta política mudar, atualizaremos esta página e a data acima."),
        ("Contato", "Dúvidas? <a href=\"{issues}\">Escreva no GitHub</a>."),
    ]),
}

CSS = """
:root{--bg:#F4F7F1;--card:#FFFFFF;--text:#1C1D2B;--muted:#5E6170;--accent:#4D52B4;--accent2:#4E9CE8;--line:#E2E6DC;color-scheme:light}
@media (prefers-color-scheme:dark){:root{--bg:#121320;--card:#1D1F30;--text:#ECEDF5;--muted:#A3A6B8;--accent:#8E93F0;--accent2:#6FB2F0;--line:#2C2F45;color-scheme:dark}}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--text);font:17px/1.55 -apple-system,BlinkMacSystemFont,"SF Pro Text","Segoe UI",Roboto,sans-serif;-webkit-text-size-adjust:100%}
.wrap{max-width:720px;margin:0 auto;padding:32px 16px 48px}
header{display:flex;gap:16px;align-items:center;margin-bottom:20px}
header img{width:72px;height:72px;border-radius:17px;box-shadow:0 6px 20px rgba(77,82,180,.25)}
header h1{margin:0;font-size:26px;line-height:1.2}
header p{margin:2px 0 0;color:var(--muted)}
nav.langs{display:flex;flex-wrap:wrap;gap:8px;margin:0 0 24px}
nav.langs a{padding:6px 12px;border-radius:999px;background:var(--card);border:1px solid var(--line);color:var(--text);text-decoration:none;font-size:15px}
nav.langs a.on{background:var(--accent);border-color:var(--accent);color:#fff}
.lang{display:none}
#lang-en{display:block}
h2{font-size:22px;margin:0 0 4px}
.date{color:var(--muted);margin:0 0 16px;font-size:15px}
section.card{background:var(--card);border:1px solid var(--line);border-radius:18px;padding:16px 18px;margin:0 0 12px}
section.card h3{margin:0 0 6px;font-size:17px}
section.card p{margin:0 0 8px}
section.card p:last-child{margin:0}
a{color:var(--accent)}
footer{margin-top:28px;color:var(--muted);font-size:15px;display:flex;gap:16px;flex-wrap:wrap}
"""

# Without a #hash, the browser's language picks the section; the pill of the shown language is highlighted.
# Sections are "lang-xx", not "xx", so the browser doesn't scroll past the header to the #xx anchor.
# Without JavaScript the English section shows.
JS = """
(function(){var codes=%s;function pick(){var h=location.hash.slice(1);if(codes.indexOf(h)<0){var l=(navigator.languages||[navigator.language||'en']);
for(var i=0;i<l.length;i++){var c=(l[i]||'').slice(0,2).toLowerCase();if(codes.indexOf(c)>=0){h=c;break}}if(codes.indexOf(h)<0)h='en';
history.replaceState(null,'','#'+h)}document.querySelectorAll('nav.langs a').forEach(function(a){a.classList.toggle('on',a.getAttribute('href')==='#'+h)});
document.querySelectorAll('.lang').forEach(function(s){s.style.display=s.id==='lang-'+h?'block':'none'});var t=document.querySelector('#lang-'+h+' [data-title]');
if(t)document.title=t.getAttribute('data-title')}pick();addEventListener('hashchange',pick)})();
"""


def page(title, prefix, sections, footer):
    codes = [c for c, _ in LANGS]
    nav = "".join(f'<a href="#{c}">{name}</a>' for c, name in LANGS)
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<link rel="icon" href="{prefix}favicon.png">
<style>{CSS}</style>
</head>
<body>
<div class="wrap">
<header><img src="{prefix}icon.png" alt=""><div><h1>Peekaword</h1><p>Vocabulary Widget</p></div></header>
<nav class="langs">{nav}</nav>
<main>
{sections}
</main>
<footer>{footer}</footer>
</div>
<script>{JS % codes}</script>
</body>
</html>
"""


def support_sections():
    out = []
    for code, _ in LANGS:
        heading, items = SUPPORT[code]
        cards = "".join(f'<section class="card"><h3>{h}</h3>' + "".join(f"<p>{p.format(issues=ISSUES)}</p>" for p in ps)
                        + "</section>" for h, ps in items)
        out.append(f'<div class="lang" id="lang-{code}" lang="{code}"><h2 data-title="Peekaword — {heading}">{TAGLINE[code]}</h2>'
                   f'<p class="date">{heading}</p>{cards}'
                   f'<p><a href="privacy/#{code}">{PRIVACY_LINK[code]}</a></p></div>')
    return "\n".join(out)


def privacy_sections():
    out = []
    for code, _ in LANGS:
        title, updated, items = PRIVACY[code]
        cards = "".join(f'<section class="card"><h3>{h}</h3><p>{p.format(issues=ISSUES)}</p></section>' for h, p in items)
        out.append(f'<div class="lang" id="lang-{code}" lang="{code}"><h2 data-title="Peekaword — {title}">{title}</h2>'
                   f'<p class="date">Peekaword: Vocabulary Widget · {updated}</p>{cards}'
                   f'<p><a href="../#{code}">{SUPPORT_LINK[code]}</a></p></div>')
    return "\n".join(out)


(ROOT / "index.html").write_text(page("Peekaword — Help", "", support_sections(),
                                      '<a href="privacy/">Privacy Policy</a><span>© 2026 Peekaword</span>'), encoding="utf-8")
(ROOT / "privacy").mkdir(exist_ok=True)
(ROOT / "privacy" / "index.html").write_text(page("Peekaword — Privacy Policy", "../", privacy_sections(),
                                                  '<a href="../">Help</a><span>© 2026 Peekaword</span>'), encoding="utf-8")
print("index.html, privacy/index.html")
