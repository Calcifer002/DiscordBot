import discord
from discord.ext import commands
import random
import praw

client = commands.Bot(command_prefix = '')

async def on_message(self,message):
    if message.author==self.user:
        return

    if message.content=='ping':
        await message.channel.send('pong')
        

   
@client.event
async def on_ready():
    print('Bot is ready')

@client.event
async def on_member_join(member):
    print(f'(member) has joined a server.')
    
@client.event
async def on_member_remove(member):
    print(f'(member) has left a server.')

@client.command(aliases=['hello','helo','Helo','HELLO'])
async def  Hello(ctx):
    await ctx.send(f'Please die')

@client.command(aliases=['bruh'])
async def Bruh(ctx):
    await ctx.send(f'Shut up')
@client.command()
async def Adithya(ctx):
    await ctx.send(f'GAEEEE')

@client.command(aliases=['okie','Okie','ok','OK','Ok','okies','Okies'])
async def Okay(ctx):
    await ctx.send(f'-_-')

    





@client.command()
async def Man(ctx):
    await ctx.send(f'Woman')

@client.command(aliases=['lmao','lol','LOL','Lol'])
async def Lmao(ctx):
    await ctx.send(f'The joke wasnt even that funny')

@client.command(aliases=['lmahoe','Lmahoe','lal','Lal','lawl','Lawl','lel','Lel','Lemma','Lma','lma','leul','Leul'])
async def lemma(ctx):
    await ctx.send(f'Spell it properly you dumb fug')
@client.command()
async def MC(ctx):
    await ctx.send(f'use bot testing site')

@client.command(aliases=['Yea','ya','Ya','yea','yes','YES','yee','Yee','yep','Yep'])
async def Yes(ctx):
     await ctx.send(f'That reply was as uninteresting as my batter')

@client.command()
async def Mc(ctx):
    await ctx.send(f'use bot testing site')


@c


@client.command(aliases=['cat','catto','Catto','Cet','cet'])
async def Cat(ctx):
    await ctx.send(f'How dare u say the name of the lord so casually?!')

@client.command(aliases=['Big','Smol','smol','small','hard','fit','Small','Hard','Fit in','Long','long','Short','Tiny'])
async def bad_hoomans(ctx):
    await ctx.send(f'Thats what she said')

@client.command(aliases=['Fuck','fk','Fk','Cock','cock','shit','SHIT','Shit','dick','Dick','Hoe','hoe','Ho','ho'])
async def fuck(ctx):
    await ctx.send(f'Stop swearing!THIS IS A CHRISTIAN SERVER.')

@client.command(alises=['truth'])
async def t(ctx):
    responses=['If you could be any celebrity, who would you be and why?',
               'Have you ever faked a sickness to stay home from school?',
               'Have you ever used your lunch money for something other than lunch?',
               'What’s the dumbest thing you ever said or done, around a boy/girl you liked?',
               'Have you ever watched a movie or TV show that you know you’re not allowed?',
               'Have you ever cried during a movie? If so, which one?',
               'What is something you wish you were better at?',
               'Have you ever broken something and blamed someone else?',
               'When was the last time you did something nice for someone else?',            
               'What is something you have always wanted to try but have been too scared of?',
               'If you were a king of your own kingdom, what would be your first order?',
               'If you could trade places with anybody in the world, would you do it? If yes, who would it be?',
               'If a genie came out of a lamp, what would your 3 wishes be?',
               'Have you ever thought about changing your name? If yes, to what?',
               'Which cartoon character do you resemble the most?',
               'Whats the maximum amount you think you can survive without your cell phone?',
               'Would you rather be able to play any musical instrument in the world or speak with animals?',
               'Would you rather be the most popular or the smartest kid at school?',
               'What would you do if you lived in the body of someone of the opposite sex for one day?',
               'What is the most shameful thing you have done in your life?',
               'What is the worst thing you have ever done to somebody?',
               'Have you ever had a crush on someone that your best friend has dated?',
               'Tell everybody an embarrassing story about yourself',
               'What were your first impressions of me (3rd person in the vc list)?',
               'What are the three qualities you feel are most important in a friend?',
               'What are the three qualities you feel are most important in a girlfriend/boyfriend',
               'What is one thing you have never told anyone else?',
               'How many best friends have you had during your lifetime?',
               'What would you do with a million dollars if you ever won the lottery?',
               'Are you scared of dying? Why?',
               'What is your favorite feature about yourself?',
               'What personality traits do you think are most important in someone you are dating?',
               'What do you think is your biggest physical flaw?',
               'Who was your first crush, or who is your current crush?',
               'When was your first crush',
               'What would you do on the perfect first date?',
               'If you could invent anything, what would it be?',
               'If you could be a Disney character, who would you be and why?',
               'What kids movie do you still secretly watch over and over?',
               'Which song are you embarrassed that you love?',
               'Would you rather have a sneeze that sounds like a train horn or only be able to do a creepy high-pitched giggle as a laugh?',
               'Would you rather eat a pigeon or a subway rat?',
               'Would you eat an ice cream sunday topped with dead flies in exchange for $50?',
               'If you couldnt go to the college or get the job of your dreams, what would you do?',
               'Whats your biggest pet peeve?',
               'What is your special talent?',
               'Whats the best meal youve ever had?',
               'What would you do if you were invisible for a day?',
               'If your life were made into a movie who would play you?',
               'What happened on the worst day of your life?',
               'What personality traits would cause you to end a friendship?',
               'If you could be born again, who would you come back as?',
               'Of all the people you know, who has the most beautiful eyes?',
               'Whats your favorite feature on someone of the opposite sex?',
               'What was the last song you listened to on your phone?',
               'What was the last thing you photographed with your phone?',
               'Which family member are you most like?',
               'Who in your family are you afraid youll turn out like some day?',
               'Who in your family has seen you cry in the last year?',
               'Do you choose to hang out with your siblings?',
               'What do you and your siblings do when no one else is home?',
               'Whats the worst thing youve ever said to your parents?',
               'What do you parents do that you dont want anyone else to see?',
               'Have you ever blamed your sibling for something that was actually your fault?',
               'Where would you like to go on a first date?',
               'Are you obsessed with a celebrity?',
               'Would you break up with someone by sending them a text?',
               'Are you jealous of someone because of who they date?',
               'How would you want the love of your life to propose to you?',
               'What kind of a person would you want to be married to in the future?',
               'Have you ever fallen in love with someone at first sight?',
               'Who was the worst friend you have had and why?',
               'What is the cruelest thing you have done to a friend?',
               'Which subject do you hate the most?',
               'Which is the most boring class you had to attend?',
               'Who is the creepiest kid you know in school?',
               'Have you ever faced an embarrassing situation with your dress when you’re in public?',
               'Have you ever felt bad about your body size?',
               'How do you want to look like either chubby or skinny?',
               'What is the silliest thing you have an emotional attachment to?',
               'Do you believe in love at first sight',
               'What is the scariest dream you have ever had?',
               'What is your biggest fear in a relationship?',
               'What is your favourite movie?',
               'Do you believe in any superstitions? If so, which ones?',
               'What’s one movie you’re embarrassed to admit you enjoy?',
               ' What’s your most embarrassing grooming habit?',
               'When’s the last time you apologized? What for?',
               'How do you really feel about the Twilight saga?',
               'If you were guaranteed to never get caught, who on Earth would you murder?',
               'What’s the cheapest gift you’ve ever gotten for someone else?',
               'What app do you waste the most time on?',
               'What’s the weirdest thing you’ve done on a plane?',
               'What is the youngest age partner you’d date?',
               'What is the oldest age partner youd date?',
               ' What celebrity do you think is overrated?',
               'What’s something that overwhelms you?',
               'What was the greatest day of your life?',
               'What’s one useless skill you’d love to learn anyway?',
               'If I went through your cabinets, what’s the weirdest thing I’d find',
               'Have you ever gotten mad at a friend for posting an unflattering picture of you?',
               'What’s your most absurd dealbreaker?',
               'Name a band you only pretend to like.',
               'What’s the last thing you Googled?',
               'What is that one thing you would never do for all the money in the world?',
               'If you could only hear one song for the rest of your life, what would it be?',
               'What’s the last YouTube video you watched?',
               'Where’s one place you’re dying to visit?',
               'What word do you hate the most?',
               'What’s the most embarrassing thing you’ve ever posted on social media?',
               'Have you ever kept a library book? For how long?',
               'If you could hire someone to do one thing for you, what would it be?',
               'What’s the best lie you’ve ever told anyone?',
               'Who’s the last person you lurked on social media?',
               'What’s your most embarrassing childhood memory?',
               'Have you ever pretended to not get a text to get out of doing something?',
               'Do you have any hidden talents? What are they?',
               'When’s the last time you got caught in a lie?',
               'What do you think happens when you die?',
               'Would you marry someone rich even if you weren’t in love with them?',
               'What’s the worst advice you’ve ever given someone else?',
               'What’s the worst advice someone else has ever given you?',
               'Would you volunteer as tribute for anyone in this room in The Hunger Games?',
               'Who’s the last person who called you?',
               'When’s the last time you wanted to hit somebody?',
               'When was the last time you were really angry? Why?',
               'What’s your favorite guilty pleasure song?',
               'Would you ever get plastic surgery?',
               'Have you ever had a near-death experience?',
               'What’s a skill you wish you had?',
               'Have you ever thrown up in public?',
               ' What’s the most common misconception about you?',
               'Have you ever seriously injured another person?',
               'What’s one responsibility you wish you didn’t have?',
               'What’s the pettiest thing you’ve ever done?',
               'What’s something you’ve done that you still feel guilty about?',
               'What’s the most inappropriate time you’ve ever laughed?',
               'What’s your best pickup line?',
               'What’s your sleaziest pickup line?',
               'What’s the dumbest thing you’ve ever lied about?',
               'What’s your least favorite memory from high school?',
               ' What song do you sing most in the shower?',
               'What’s something you’re embarrassed that you’re good at?',
               'What was your most humbling moment?',
               'Who would you bring with you on a deserted island?',
               'What’s something weird you do in your sleep?',
               'Who is your anime waifu?',
               'Who is your anime husbando?',
               'What’s something you know you need to do but aren’t looking forward to at all?',
               ' What’s the most offensive joke you’ve found funny?',
               'What are you most proud of in your life?',
               'Would you ever get a prenup?',]
    await ctx.send(f'PLZ DONT SKIP FFS : {random.choice(responses)}')

@client.command()
async def meme(ctx):
    channel= ctx.message.channel 
    embed=discord.Embed(
        title='BUHAHAHA',
        description='Get a life',
        colour= discord.Colour.blue()

        )

    embed.set_image(url='https://i.imgflip.com/46bybr.jpg')
    

    await ctx.send(embed=embed)
    
               
    

@client.command(aliases=['8ball','halp'])
async def _8ball(ctx,*,question):
    responses=['That question is almost as dumb as you',
               'Why?It would be useless on you',
               'Dont waste your time asking me if your stupid dreams will work out or not,we all know its a no',
               'I dont think so but hey it depends on you',
               'Dont u have anything better to do with your time ?',
               'Get a life',
               'Maybe try some rat poison,I hear it works wonders',
               'My programme just failed because your question is just that dumb',
               'FFS GET A LIFE',
                ]
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online,activity=discord.Game('Genocide'))
client.run('DSYi7LqBS5TPDN0XRPxB4TPAe52gZHQG')
