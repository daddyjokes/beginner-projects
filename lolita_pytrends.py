from pytrends.request import TrendReq
import xlwt

# SEMrush top 20 (200 related broad searches)\
# GoogleTrends related top searches 'loli' (search)\
# GoogleTrends related top searches 'Lolicon' (topic)\
# All duplicates removed, otherwise not edited
search_list = ['hentai loli','what is a loli','3d loli','dragon loli','loli and pops','are lolis illegal', 'thick loli dragons','loli games','loli gif','loli prom dress','hentai haven loli', 'hentai haven loli tag','hentai loli gif','hentai loli tumblr','e hentai loli','loli neko hentai', 'hentai heaven loli','hentai gif loli','hentai legal loli','dragon loli anime','animated loli', 'cute anime loli','loli animes','anime loli memes','anime loli bondage','hot anime loli', 'loli anime characters','loli anime wallpaper','loli ecchi anime','lolies porn','lolis anime porn','1 studio porn loli','18 loli porn','3 loli hentai porn','3d animated loli porn','3d animated loli porn how do i report','3d beastiality loli porn','3d comic porn loli', '3d hentai loli gore porn','anime girl lolis','1 girl 1 mother hentai lolis', '1 girls 1 mother hentai lolis 3d','18 Fresh school girl tiny slut lola loli destroyed','2 girl neko ninja lolis in swimsuits','3 hot loli girls','3d custom girl evolution loli', '3d custom girl evolution loli feet','3d custom girl evolution loli mod','3d custom girl loli','3d loli gif','3d loli art','hentai 3d loli','3d lolis intensify hmv','hentai loli 3d','custom maid 3d 2 loli','loli 3d game','3d cg loli','3d loli animation', 'thicc loli dragon',"don't lewd the dragon loli","ravioli ravioli don't lewd the dragon loli",'lewd dragon loli','thicc dragon loli','dont lewd the dragon loli','lewd the dragon loli', 'loli gore gif','loli laser gif','loli blowjob gif','loli guro gif','cute loli gif','cute anime loli gif','hentai lolis sex','3d comics adult sex loli','3d comics adult loli incest', '3d comics adult sex loli incest loud house','3d loli sex','3d loli sex game','3d loli sex gif','3d loli sex scene','3d sex games loli','3d sex loli hentai','3d animated loli nude','3d hentai loly nude','3d little nude loli picture','3d loli model nude','3d loli nude gif','3d loli sluts nude','3d nude loli girl','adventure time loli marceline nude', 'loli flash games','best loli games','loli game recorder','loli games dress up', 'loli eroge games','loli h game','dress up loli games','loli mobile games','best loli manga', 'kyou kara ore wa loli no himo manga','legal loli manga','loli doujin manga','loli incest hentai manga', 'mangas de lolis','nama loli manga','read hentai manga loli','4chan loli rape manga', 'ahegao loli manga','lolis videos','videos porno lolis','3d hentai loli video','3d hentai loli video streaming','3d loli hentai video','3d loli hentai x videos','3d loli video', '3d loli video sfm','3d loli videos xxx','3d video game loli porn','3d blonde loli fucked by tentacles hentai','3d blonde loli knight fucked by tentacles','3d blonde loli knight fucked by tentacles hentai','3d fuck house loli','3d fucking gif loli', '3d hentai lolis fucked by gang of monsters','3d little lolis fucked in slow motion', '3d little lolis fucked in slow motion freefetish','3d little lolis fucked in slowmotion', '3d loli fuck','loli memes','loli meme','loli dragon meme','dank loli memes', 'dragon loli meme','loli fbi meme','loli police meme','soft loli breathing meme','15 minutes meme loli', 'lolis xxx','comic xxx lolis','lolis xxx comic','3d hentai loli xxx','3d loli xxx', '3d loli xxx hentai','3d lolis xxx','3d xxx loli','ahegao xxx loli','japanese loli comics','3d comics adult sex loli incest','3d incest loli comics','3d loli comics','3d loli comics collection', 'cute lolis','anime cute loli','cute lolis doing cute things','cute dragon loli','cute loli cosplay', 'cute loli names','anime loli cute','futa lolis','futa x loli','loli & futa','loli and futa','anime loli futa','loli & futa vol 1','loli futas','10 inch loli futa','3d futa loli', '3d futa loli rape','white haired loli','red haired loli','black haired loli','blue hair anime loli', 'blue hair loli','blue haired loli','loli black hair','loli white hair','pink hair loli', 'pink haired loli','legal lolis','legal lolis list', 'make lolis legal again cosplay','legal loli reddit','japanese legal loli','legal loli kaddi', 'make lolis legal again','3d legal loli',\
 'loli anime','anime','lolicon','la loli','manga loli','lolis','loli pop','lolita','loli dragon', 'loli con','what is loli','anime girl loli','loli game','cute loli','japanese loli','lol','pedro loli','little loli','shota','loli meaning','neko loli','loli rock','lolli',\
'loli','av','лоли','โล ลิ','anime lolis','ろりこん','控','โล ลิ ต้า','蘿 莉 塔']

# List manually formed after reading results from "search_list"
sig_list = ['hentai loli','what is a loli','3d loli','dragon loli','loli games','loli gif','loli prom dress',\
            'loli anime','anime','lolicon','manga loli','lolis','loli pop','lolita','loli dragon','what is loli',\
            'anime girl loli','loli game','cute loli','japanese loli','lol','pedro loli','little loli','shota',\
            'loli meaning','neko loli','lolli','loli','av','anime lolis','控']

# States, includes District of Columbia
states = ['AL','AK','AZ','AR','CA','CO','CT','DE','DC','FL','GA','HI','ID','IL','IN','IA','KS', 'KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC', 'ND','OH','OK','OR','PA','RI','SC','SD','TN','TX','UT','VT','VA','WA','WV','WI','WY']

# Choose what table to generate
list = sig_list

# Export to Excel Spreadsheet; SETUP
book = xlwt.Workbook(encoding='utf-8')
sheet = book.add_sheet('Sheet 1')
# Write state column
for n_states in range(len(states)):
    sheet.write(n_states+1, 0, states[n_states]) #(ROW, COLUMN)

# Failsafe
failsafe = False
if failsafe == False:
    if list == sig_list:
        book.save('webscrapersheet_sig.xls')
    else:
        book.save('webscrapersheet.xls')
    failsafe = True

# Get data
pytrends = TrendReq(hl='en-US', tz=360)

for i in range(len(list)):
    search = list[i]
    pytrends.build_payload([search], cat=0, timeframe='2010-01-01 2010-12-31', geo='US', gprop='')
    interest = pytrends.interest_by_region(resolution='COUNTRY')

    # Status report
    print(str(i+1) +str('/') +str(len(list)) +str(': ') +str(search))

    # Export data to spreadsheet
    # Write query
    sheet.write(0, i+1, list[i]) #(ROW, COLUMN)
    # Write interest
    for n in range(len(interest[search])):
        sheet.write(n+1, i+1, str(interest.iloc[n,0])) #(ROW, COLUMN)

# Save spreadsheet
if list == sig_list:
    book.save('webscrapersheet_sig.xls')
else:
    book.save('webscrapersheet.xls')