import time
import os, sys
import banner
from telethon import TelegramClient, events, sync
color = '\033[1;35m'
os.system("termux-open-url https://t.me/magicbot_uz")
ip_id=input(color+"API_id kodini kiriting:")
ip_hash=input("API_hash kodini kiriting:")

api_id = ip_id
api_hash = ip_hash



client = TelegramClient('anon', api_id, api_hash)


@client.on(events.NewMessage)
async def my_event_handler(event):
    if event.raw_text == "help":
    	await event.reply("""
    	🦊 MagicBotUz - Bu magicbot userbotining 2- versiasi hatoliklar tuzatilgan ban bermaydi, flood rejimiga tushmaysiz, 2022-yil 8-may soat 16:19 da dasturlandi. 
    	🦊Buyruqlar qatori
    	🔰kulgichlar - .smile
    	🔰yuraklar 1 - .hearth
    	🔰yuraklar 2 - .hearts
    	🔰yuraklat 3 - .heart
    	🔰yuraklar 4 - .love
    	🔰sevgi izhor 9 tilda - .loveu
    	🔰Animation yozuv - .type soz yozas
    	🔰uzb bayrogi va sozi - .uzb
    	🔰loading - .loading
    	🔰globus animation - .year
    	🔰soat animation - .clock
    	🔰oy animation - .moon
    	🔰kulish - .lul
    	🔰salomlashish - .salom
    	🔰hayrlashish - .hayr
    	🔰? big text - .?
    	🔰negativlar uchun - .negative
    	🔰like - .like
    	🔰dislike - .dislike
    	🔰ranglar - .colors
    	🕹️dasturchi @darknet_off1cial
    	🕹️yangiliklar @magicbot_uz
    	🕹️contributor @sinto_f
    	
    	""")
    if '.smile' in event.raw_text:
                smile = ['😀', '🤨', '🤐', '🤑', '🤫', '😏', '😎', '😊', '🤡']
                time.sleep(0.5)
                for i in range(2):
                	time.sleep(0.5)
                	for d in smile:
                		time.sleep(0.5)
                		await event.edit(d)
    if '.hearth' in event.raw_text:
    	hearth = ["💔", "🧡", "💛", "💚", "💙", "💜", "🤎", "🖤", "🤍", "❤️"]
    	time.sleep(0.5)
    	for i in range(2):
            time.sleep(0.5)
            for a in hearth:
                time.sleep(0.5)
                await event.edit(a)
    if '.hearts' in event.raw_text:
    	hearts = ["❤️.", "❤️💙.", "❤️💙🖤.", "❤️💙🖤🤎.", "❤️💙🖤🤎💜.", "❤️💙🖤🤎💜💚.", "❤️💙🖤🤎💜💚💛.", "❤️💙🖤🤎💜💚💛🧡."]
    	time.sleep(0.1)
    	for i in range(2):
            time.sleep(0.7)
            for r in hearts:
                time.sleep(0.7)
                await event.edit(r)
    if '.loveu' in event.raw_text:
    	loveu = ["men seni sevaman❤️", "i love you❤️", "я люблю тебя❤️", "أنا أحبه❤️", "塞瓦曼❤️", "나는 너를 사랑해요❤️", "Seni seviyorum❤️"]
    	time.sleep(1.2)
    	for i in range(2):
    		time.sleep(1.2)
    		for k in loveu:
    			time.sleep(1.2)
    			await event.edit(k)
    if '.love' in event.raw_text:
    	love = ["""────(ღ)(ღ)(ღ)────(ღ)(ღ)(ღ) """, """────(ღ)(ღ)(ღ)────(ღ)(ღ)(ღ) 
──(ღ)██████(ღ)(ღ)██████(ღ) """, """────(ღ)(ღ)(ღ)────(ღ)(ღ)(ღ) 
──(ღ)██████(ღ)(ღ)██████(ღ) 
─(ღ)████████(ღ)████████(ღ) """, """────(ღ)(ღ)(ღ)────(ღ)(ღ)(ღ) 
──(ღ)██████(ღ)(ღ)██████(ღ) 
─(ღ)████████(ღ)████████(ღ) 
─(ღ)██████████████████(ღ) """, """────(ღ)(ღ)(ღ)────(ღ)(ღ)(ღ) 
──(ღ)██████(ღ)(ღ)██████(ღ) 
─(ღ)████████(ღ)████████(ღ) 
─(ღ)██████████████████(ღ) 
──(ღ)████████████████(ღ) """, """────(ღ)(ღ)(ღ)────(ღ)(ღ)(ღ) 
──(ღ)██████(ღ)(ღ)██████(ღ) 
─(ღ)████████(ღ)████████(ღ) 
─(ღ)██████████████████(ღ) 
──(ღ)████████████████(ღ) 
────(ღ)████████████(ღ) """, """────(ღ)(ღ)(ღ)────(ღ)(ღ)(ღ) 
──(ღ)██████(ღ)(ღ)██████(ღ) 
─(ღ)████████(ღ)████████(ღ) 
─(ღ)██████████████████(ღ) 
──(ღ)████████████████(ღ) 
────(ღ)████████████(ღ) 
──────(ღ)████████(ღ) """, """────(ღ)(ღ)(ღ)────(ღ)(ღ)(ღ) 
──(ღ)██████(ღ)(ღ)██████(ღ) 
─(ღ)████████(ღ)████████(ღ) 
─(ღ)██████████████████(ღ) 
──(ღ)████████████████(ღ) 
────(ღ)████████████(ღ) 
──────(ღ)████████(ღ) 
────────(ღ)████(ღ) """, """────(ღ)(ღ)(ღ)────(ღ)(ღ)(ღ) 
──(ღ)██████(ღ)(ღ)██████(ღ) 
─(ღ)████████(ღ)████████(ღ) 
─(ღ)██████████████████(ღ) 
──(ღ)████████████████(ღ) 
────(ღ)████████████(ღ) 
──────(ღ)████████(ღ) 
────────(ღ)████(ღ) 
─────────(ღ)██(ღ) """, """────(ღ)(ღ)(ღ)────(ღ)(ღ)(ღ) 
──(ღ)██████(ღ)(ღ)██████(ღ) 
─(ღ)████████(ღ)████████(ღ) 
─(ღ)██████████████████(ღ) 
──(ღ)████████████████(ღ) 
────(ღ)████████████(ღ) 
──────(ღ)████████(ღ) 
────────(ღ)████(ღ) 
─────────(ღ)██(ღ) 
───────────(ღ)"""]
    	time.sleep(0.5)
    	for i in range(2):
    		time.sleep(0.5)
    		for n in love:
    			time.sleep(0.5)
    			await event.edit(n)
    if '.heart' in event.raw_text:
    	heart = ["❤️", "🧡", "💛", "💚", "💜", "🤍"]
    	time.sleep(0.5)
    	for i in range(5):
    		time.sleep(0.5)
    		for e in heart:
    			time.sleep(0.5)
    			await event.edit(e)
    if '.uzb' in event.raw_text:
    	uzb = ["""
🟦🟦🟦               🟩🟩🟩
🟦🟦🟦               🟩🟩🟩
🟦🟦🟦               🟩🟩🟩
🟦🟦🟦               🟩🟩🟩
🟦🟦🟦               🟩🟩🟩
🟦🟦🟦               🟩🟩🟩
🟦🟦🟦⬜⬜⬜🟩🟩🟩
     🟦🟦⬜⬜⬜🟩🟩
          🟦⬜⬜⬜🟩
""", """
🟦🟦🟦⬜⬜⬜🟩🟩🟩
🟦🟦🟦⬜⬜⬜🟩🟩🟩
🟦🟦🟦⬜⬜⬜🟩🟩
                    ⬜⬜🟩
               ⬜⬜⬜
          🟦⬜⬜
     🟦🟦⬜⬜⬜🟩🟩🟩
🟦🟦🟦⬜⬜⬜🟩🟩🟩
🟦🟦🟦⬜⬜⬜🟩🟩🟩
""", """
🟦🟦🟦⬜⬜⬜🟩🟩
🟦🟦🟦⬜⬜⬜🟩🟩🟩
🟦🟦🟦               🟩🟩🟩
🟦🟦🟦⬜⬜⬜🟩🟩🟩
🟦🟦🟦⬜⬜⬜🟩🟩
🟦🟦🟦⬜⬜⬜🟩🟩🟩
🟦🟦🟦               🟩🟩🟩
🟦🟦🟦⬜⬜⬜🟩🟩🟩
🟦🟦🟦⬜⬜⬜🟩🟩     
""", """
🟦🟦🟦               🟩🟩🟩
🟦🟦🟦               🟩🟩🟩
🟦🟦🟦               🟩🟩🟩
🟦🟦🟦               🟩🟩🟩
🟦🟦🟦               🟩🟩🟩
🟦🟦🟦               🟩🟩🟩
🟦🟦🟦⬜⬜⬜🟩🟩🟩
     🟦🟦⬜⬜⬜🟩🟩
          🟦⬜⬜⬜🟩

🟦🟦🟦⬜⬜⬜🟩🟩🟩
🟦🟦🟦⬜⬜⬜🟩🟩🟩
🟦🟦🟦⬜⬜⬜🟩🟩
                    ⬜⬜🟩
               ⬜⬜⬜
          🟦⬜⬜
     🟦🟦⬜⬜⬜🟩🟩🟩
🟦🟦🟦⬜⬜⬜🟩🟩🟩
🟦🟦🟦⬜⬜⬜🟩🟩🟩

🟦🟦🟦⬜⬜⬜🟩🟩
🟦🟦🟦⬜⬜⬜🟩🟩🟩
🟦🟦🟦               🟩🟩🟩
🟦🟦🟦⬜⬜⬜🟩🟩🟩
🟦🟦🟦⬜⬜⬜🟩🟩
🟦🟦🟦⬜⬜⬜🟩🟩🟩
🟦🟦🟦               🟩🟩🟩
🟦🟦🟦⬜⬜⬜🟩🟩🟩
🟦🟦🟦⬜⬜⬜🟩🟩     

🟦🟦🟦⬜⬜⬜🟩🟩
🟦🟦🟦⬜⬜⬜🟩🟩🟩
🟦🟦🟦               🟩🟩🟩
🟦🟦🟦⬜⬜⬜🟩🟩🟩
🟦🟦🟦⬜⬜⬜🟩🟩
🟦🟦🟦⬜⬜⬜🟩🟩🟩
🟦🟦🟦               🟩🟩🟩
🟦🟦🟦⬜⬜⬜🟩🟩🟩
🟦🟦🟦⬜⬜⬜🟩🟩     
"""]
    	time.sleep(0.5)
    	for i in range(5):
    		time.sleep(0.5)
    		for t in uzb:
    			time.sleep(0.5)
    			await event.edit(t)
    if '.loading' in event.raw_text:
    	loading = ["10%", "20%", "30%", "40%", "50%", "60%", "70%", "80%", "90%", "100%" ,"Tugadi..."]
    	time.sleep(1)
    	for a in loading:
    		time.sleep(1)
    		await event.edit(a)
    if '.lul' in event.raw_text:
    	lul = ["😂🤣😂🤣", "🤣😂🤣😂"]
    	time.sleep(0.5)
    	for i in range(5):
    		time.sleep(0.5)
    		for r in lul:
    			time.sleep(0.5)
    			await event.edit(r)
    if '.moon' in event.raw_text:
    	moon = ["🌑🌕", "🌘🌒", "🌗🌓", "🌖🌒", "🌕🌑"]
    	time.sleep(0.5)
    	for i in range(5):
    		time.sleep(0.5)
    		for k in moon:
    			time.sleep(0.5)
    			await event.edit(k)
    if '.year' in event.raw_text:
    	year = ["🌏🌎🌍", "🌎🌍🌏", "🌍🌏🌎"]
    	time.sleep(0.5)
    	for i in range(5):
    		time.sleep(0.5)
    		for n in year:
    			time.sleep(0.5)
    			await event.edit(n)
    if '.clock' in event.raw_text:
    	clock = ["🕚", "🕙", "🕘", "🕙", "🕛"]
    	time.sleep(0.5)
    	for i in range(5):
    		time.sleep(0.5)
    		for e in clock:
    			time.sleep(0.5)
    			await event.edit(e)
    if '.salom' in event.raw_text:
    	salom = ["""

███░░███░░███

███░░███░░░░░

███░░███░░███

███▄▄███░░███

████████░░███

███▀▀███░░███

███░░███░░███

███░░███░░███

███░░███░░███"""]
    	time.sleep(0.5)
    	for t in salom:
    		time.sleep(0.5)
    		await event.edit(t)
    if '.hayir' in event.raw_text:
    	hayr = ["""╭──╮──────────╭╮───╭╮──╭╮─╭╮────
│╭╮│──────────││───││──││─││────
│╰╯│╭──╮╭──╮╭─╯│───│╰─╮│╰─╯│╭──╮
╰─╮││╭╮││╭╮││╭╮│───│╭╮│╰─╮╭╯││─┤
╭─╯││╰╯││╰╯││╰╯│───│╰╯│╭─╯│─││─┤
╰──╯╰──╯╰──╯╰──╯───╰──╯╰──╯─╰──╯
"""]
    	time.sleep(0.5)
    	for d in hayr:
    		time.sleep(0.5)
    		await event.edit(d)
    if '.nima' in event.raw_text:
    	nima = ["""┌───┐
│┌─┐│
└┘┌┘│
──│┌┘
──┌┐─
──└┘─
"""]
    	for a in nima:
    		await event.edit(a)
    if '.negative' in event.raw_text:
    	negative = ["💩", "🖕", "👎", "🤞", "🤏"]
    	time.sleep(0.7)
    	for i in range(3):
    		time.sleep(0.7)
    		for a in negative:
    			time.sleep(0.7)
    			await event.edit(a)
    if '.colors' in event.raw_text:
    	colors = ["🟥🟧🟨🟩🟦", "🟧🟥🟨🟩🟦", "🟨🟧🟥🟩🟦", "🟩🟨🟧🟥🟦", "", "🟦🟩🟨🟧🟥"]
    	time.sleep(0.3)
    	for i in range(10):
    		time.sleep(0.3)
    		for r in colors:
    			time.sleep(0.3)
    			await event.edit(r)
    if '.like' in event.raw_text:
    	like = ["👋", "👌", "✌️", "👏", "🤝", "👍"]
    	time.sleep(0.6)
    	for i in range(2):
    		time.sleep(0.6)
    		for k in like:
    			time.sleep(0.6)
    			await event.edit(k)
    if '.dislike' in event.raw_text:
    	dislike = ["🤞", "🖕", "🤏", "👇", "👊", "👎"]
    	time.sleep(0.6)
    	for i in range(2):
    		time.sleep(0.6)
    		for n in dislike:
    			time.sleep(0.6)
    			await event.edit(n)
    if '.story' in event.raw_text:
    	story = ["""🟦""", "🟦🟦", "🟦🟦🟦", """🟦🟦🟦
⬜️""", """🟦🟦🟦
⬜️⬜️""", """🟦🟦🟦
⬜️⬜️⬜️""", """🟦🟦🟦
⬜️⬜️⬜️
🟩""", """🟦🟦🟦
⬜️⬜️⬜️
🟩🟩""", """🟦🟦🟦
⬜️⬜️⬜️
🟩🟩🟩""", """🟦🟦🟦
🇺 ⬜️⬜️
🟩🟩🟩""", """🟦🟦🟦
🇺 🇿  ⬜️
🟩🟩🟩""", """🟦🟦🟦
🇺  🇿  🇧 
🟩🟩🟩""", """🟦🟦🟦
⬜️⬜️⬜️
🟩🟩🟩"""]
    	time.sleep(0.5)
    	for i in range(2):
    		time.sleep(0.5)
    		for e in story:
    			time.sleep(0.6)
    			await event.edit(e)
    
                
                
    elif ".type" == event.raw_text[:5] and len(event.raw_text) > 6:
        orig_text = event.raw_text.split(".type ", maxsplit=1)[1]
        text = orig_text
        pb = ""
        typing_symbol = "|"

        while (pb != orig_text):
            try:
                await event.edit(pb + typing_symbol)
                time.sleep(0.09)

                pb += text[0]
                text = text[1:]

                await event.edit(pb)
                time.sleep(0.09)

            except Exception as e:
                print(e)
   





	



client.start()
client.run_until_disconnected()