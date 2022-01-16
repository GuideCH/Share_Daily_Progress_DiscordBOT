import discord
client = discord.Client()

import textwrap

tokens = 'TOKENS_HERE'
#look at line 62 for language changing

#OnEvent That this bot logged in
@client.event
async def on_ready():
  print('ล๊อกอินในชื่อ{0.user}'.format(client))

#OnEvent That anyone Send message
@client.event
async def on_message(message):
    lowercasemsg = message.content.lower()

    #DELETE MSG Function
    async def delete_(message):
        await message.delete()

    #return if message owner is this bot
    if message.author == client.user:

        return

    #if it's not this bot Then Proceed
    else:
        #MSG to notice user (DM) in case they write wrong format
        template_msg = '''

        ---------------------
        - **โปรดใช้รูปแบบที่ถูกต้อง** -
        ---------------------
        **เมื่อวาน:** ...
        **วันนี้จะ:** ...
        **ปัญหาที่เจอ:** ...
        ---------ตัวอย่าง-----------
        **เมื่อวาน:** ทำเว็บไซต์
        **วันนี้จะ:** ทำระบบลีอกอิน
        **ปัญหาที่เจอ:** Error ใน Session ตอนทำ OAuth2
        --------------------------------------------------------------------
        '''
        #MSG to notice user (DM) in case they write wrong format
        template_msg_eng = '''

        ---------------------
        - **Please Use The Correct Format** -
        ---------------------
        **Yesterday I:** ...
        **Today I will:** ...
        **Potential hard problems:** ...
        --------Example----------
        **Yesterday I:** Made Webserver
        **Today I will:** Learn about websocket
        **Potential hard problems:** what the hell is websocket!?
        --------------------------------------------------------------------
        '''

        #change this line to template_msg = textwrap.dedent(template_msg_eng) for english language user
        template_msg = textwrap.dedent(template_msg)
        #use textwrap because there'll be too much space from using ''' text ''' check in textwrap use case yourself

        #IF there's EXACLY met Template Text in String   (and also started with correct form)
        if('**เมื่อวาน:**' and '**วันนี้จะ:**' and '**ปัญหาที่เจอ:**') in lowercasemsg or ('**yesterday i:**' and '**today i will:**' and '**potential hard problems:**') in lowercasemsg:
            if lowercasemsg.startswith('**เมื่อวาน:**') or ('**yesterday i:**'):

                #----- use to count ('\n')  # NOTE: \n = line break or ENTER or RETURN
                counter = 0
                #-----

                #Use for loop to cou    nt \n in text and keep in counter
                for char in lowercasemsg:
                    if char == ('\n'):
                        counter += 1

                if counter >= 2:
                    return

#-------in case not corect format DELETE MSG and DM
                else:
                    await delete_(message)
                    await message.author.send(template_msg)
            else:
                await delete_(message)
                await message.author.send(template_msg)
        else:
            await delete_(message)
            await message.author.send(template_msg)

        return

client.run(tokens)
