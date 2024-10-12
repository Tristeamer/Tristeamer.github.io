# some functions needed for the page generator to declutter the main file a bit
# also some variable

import datetime

# definte array for rows in the .csv files
l_content = []
r_content = []
date = datetime.date.today()

def parse_csv(lvlpath, recpath):

    TRISTEAMER = 0
    WILLO = 0
    JEREMY_CLARKSON = 0
    WAHFFLE = 0
    MRLIBRA = 0
    MIQUEL = 0
    TRAVISAURUS = 0
    EVIL = 0
    MELONZ = 0
    FENIX = 0
    FIZZEL = 0
    CARTER = 0
    CHRISTEAMER = 0
    FOODY = 0

# get lines for record .csv file
    with open(lvlpath, "r") as lvl_csv:
        for line in lvl_csv:
            l_content.append(line)

# get lines for level .csv file
    with open(recpath, "r") as rec_csv:
        for line in rec_csv:
            r_content.append(line)

# write the start of the index.html file
    with open("index.html", "w") as index:
        index.write("<!DOCTYPE html>\n")
        index.write("<html>\n")
        index.write("<title>Sigma Grindset Demonlist\u2122</title>\n")
        index.write("<head>\n")
        index.write('  <link rel="stylesheet" href="style/styles.css">\n')
        index.write('</head>\n')
        index.write('<!-- Weird header thing if it works it works-->\n')
        index.write('<div class="header">\n')
        index.write('  <div>\n')
        index.write('    <h1>[Sigma Grindset Demonlist\u2122]</h1>\n')
        index.write('  </div>\n')
        index.write('  <div style="float:right;">\n')
        index.write('    <h2><a href="https://tristeamer.github.io/sgdl/index.html">Mainlist</a>\n')
        index.write('        <a href="https://tristeamer.github.io/sgdl/index.html#extendedlist">Extended List</a>\n')
        index.write('        <a href="pages/legacylist.html">Legacy List</a></h2>\n')
        index.write('  </div>\n')
        index.write('</div>\n')
        index.write(r"<!-- I'm 99% sure there's a better way to do this -->"+'\n')
        index.write('<br>\n')
        index.write('<br>\n') 
        index.write('<br>\n')
        index.write('<br>\n')
        index.write('<br>\n')
        index.write('<br>\n')
        index.write('<body>\n')
        index.write('<!-- div for the rules and other info -->\n')
        index.write('  <div class="sider">\n')
        index.write('      <h4>Rules:</h4>\n')
        index.write("""      <h5 style="text-align: justify;">I. The real demonlist rules apply here (mainly so I don't have to write out my own).</h5>\n""")
        index.write('      <h5 style="text-align: justify;">II. Any records submitted will only be allowed if they are from people *actually* in the discord.</h5>\n')
        index.write("""      <h5 style="text-align: justify;">III. That's pretty much everything I'll add more later if I think of any.</h5>\n""")
        index.write('      <hr style="color:white;">\n')
        index.write('      <h4>Other (kinda important) Stuff:</h4>\n')
        index.write('''      <h5 style="text-align: center;">- <a href="https://pointercrate.com/guidelines/index">Pointercrate's Rules</a></h5>\n''')
        index.write('      <h5 style="text-align: center;">- <a href="pages/statsviewer.html">Stats Viewer</a></h5>\n')
        index.write('      <h5 style="text-align: center;">- <a href="https://forms.gle/jDx28tHq8zhowzF2A">Submit a record here!</a></h5>\n')
        index.write('      <h5 style="text-align: justify; color:rgb(138, 138, 138)">*Note: instead of using the form you can just message me any records on discord instead if you want</h5>\n')
        index.write('      <hr style="color:white">\n')
        index.write('      <h4 style="text-align: center;">Last updated: '+str(date)+'</h4>\n')
        index.write('      <hr style = "color:white">')
        index.write('      <h4 style="font-family: fortnite; font-size:150%;">Wall of fame:</h4>')
        index.write('      <img class="wof" src="images/libra in vc.gif" width="300" height="200" style="margin-left: 10%">')
        index.write('      <img class="wof" src="images/jon.png" width="300" height="200" style="margin-left: 10%">')
        index.write('      <img class="wof" src="images/tim.png" width="300" height="200" style="margin-left: 10%">')
        index.write('      <img class="wof" src="images/shroom.gif" width="300" height="200" style="margin-left: 10%">')
        index.write('      <img class="wof" src="images/milan.png" width="300" height="200" style="margin-left: 10%">')
        index.write('      <img class="wof" src="images/sexualfriday.jpg" width="300" height="200" style="margin-left: 10%">')
        index.write('      <img class="wof" src="images/unknown.png" width="300" height="200" style="margin-left: 10%">')
        index.write('      <img class="wof" src="images/empire.png" width="300" height="200" style="margin-left: 10%">')
        index.write('      <img class="wof" src="images/ad.webp" width="300" height="200" style="margin-left: 10%">')
        index.write('      <img class="wof" src="images/caliph.png" width="300" height="200" style="margin-left: 10%">')
        index.write('      <img class="wof" src="images/orbit.gif" width="300" height="200" style="margin-left: 10%">')
        index.write('      <img class="wof" src="images/omori.webp" width="300" height="200" style="margin-left: 10%">')
        index.write('      <img class="wof" src="images/text.gif" width="300" height="200" style="margin-left: 10%">')
        index.write('  </div>\n')
        index.write('</body>\n')
        index.write('<!-- basic template for demons shown; also clickable for convenience -->\n')

# get data from each row and format it to be nicer for levels.csv file 
    for i in range(1,151):
        l_content[i] = l_content[i].replace(",,,,,,,,",",")
        if '"' in l_content[i]:
            del_dumb_comma = l_content[i].split('"')
            del_dumb_comma[1] = del_dumb_comma[1].replace(",","♠")
            l_content[i] = ''.join(del_dumb_comma)
        row_content = l_content[i].split(",")
        pg_fname = str(i) + ".html"

        if row_content[8] == "NONE":
            row_content[8] = "https://www.youtube.com/watch?v=cEcDWv96JHQ"
        row_content[8] = row_content[8].replace("https://www.youtube.com/watch?v=","https://www.youtube.com/embed/")

        row_content[7] = row_content[7].replace("♠", ",")

        rec_content = r_content[i].split(",")

        with open("index.html", "a") as index:    
            if i == 75:
                index.write("<!-- #75 level -->\n")
                index.write("<body>\n")
                index.write('  <a href="pages/demons/75.html">\n')
                index.write('  <div class="listedlevel" >\n')
                index.write(r'<div class="ytembed"><iframe style="border-radius: 15px"  width="320" height="180" src="'+row_content[8]+r'?si=8ygZihDvwk3dTucY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe></div>'+'\n')
                index.write('    <h1>#75 - '+row_content[1]+'</h1>\n')
                index.write('    <h2>'+row_content[2]+'</h2>\n')
                index.write('  </div>\n')
                index.write('  </a>\n')
                index.write('  <br>\n')
                index.write('</body>\n')
                index.write('<!-- THE EXTENDED LIST :333333333-->\n')
                index.write('<body>\n')
                index.write('  <div class="extlist">\n')
                index.write('    <img src="images/extlist.gif" style="margin-left: 22%;" alt="THE EXTENDED LIST IS HERE FUCKERS >w<" id="extendedlist">\n')
                index.write(r'    <h5 style="text-align:center">These levels have fallen off of the mainlist, you must obtain 100% on these levels to recieve points :v</h5>'+'\n')
                index.write('    <h5 style="text-align:center; color: rgb(138, 138, 138)">(web design is my passion)</h5>\n')
                index.write('  </div>\n')
                index.write('</body>\n')
            else:
                if is_even(i) == False:
                    index.write('<!-- #'+str(i)+' level -->\n')
                    index.write('<body>\n')
                    index.write('  <a href="pages/demons/'+str(i)+'.html">\n')
                    index.write('  <div class="listedlevel" >\n')
                    index.write(r'    <div class="ytembed"><iframe style="border-radius: 15px"  width="320" height="180" src="'+row_content[8]+r'?si=8ygZihDvwk3dTucY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe></div>'+'\n')
                    index.write('    <h1>#'+str(i)+' - '+row_content[1]+'</h1>\n')
                    index.write('    <h2>'+row_content[2]+'</h2>\n')
                    index.write('  </div>\n')
                    index.write('  </a>\n')
                    index.write('  <br>\n')
                    index.write('</body>\n')
                else:
                    index.write('<!-- #'+str(i)+' level -->\n')
                    index.write('<body>\n')
                    index.write('  <a href="pages/demons/'+str(i)+'.html">\n')
                    index.write('  <div class="listedlevel2" >\n')
                    index.write(r'    <div class="ytembed"><iframe style="border-radius: 15px"  width="320" height="180" src="'+row_content[8]+r'?si=8ygZihDvwk3dTucY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe></div>'+'\n')
                    index.write('    <h1>#'+str(i)+' - '+row_content[1]+'</h1>\n')
                    index.write('    <h2>'+row_content[2]+'</h2>\n')
                    index.write('  </div>\n')
                    index.write('  </a>\n')
                    index.write('  <br>\n')
                    index.write('</body>\n')
            index.close()

        with open(pg_fname, "w") as curr_page:
            curr_page.write("<!DOCTYPE html>\n")
            curr_page.write("<html>\n")
            curr_page.write("<title>#"+str(i)+" - "+row_content[1]+" - Sigma Grindset Demonlist\u2122</title>\n")
            curr_page.write("</html>\n")
            curr_page.write("<head>\n")
            curr_page.write('  <link rel="stylesheet" href="style/dlpgss.css">\n')
            curr_page.write('</head>\n')            
            curr_page.write('<!-- Weird header thing if it works it works-->\n')
            curr_page.write('<div class="header">\n')
            curr_page.write('    <div>\n')
            curr_page.write('      <h1>[Sigma Grindset Demonlist\u2122]</h1>\n')
            curr_page.write('    </div>\n')
            curr_page.write('    <div style="float:right;">\n')
            curr_page.write('      <h2><a href="https://tristeamer.github.io/sgdl/index.html">Return to main page.</a>\n')
            curr_page.write('    </div>\n')
            curr_page.write('</div>\n')
            curr_page.write(r"<!-- I'm 99% sure there's a better way to do this -->\n")
            curr_page.write('<br>\n')
            curr_page.write('<br>\n')
            curr_page.write('<br>\n')
            curr_page.write('<br>\n')
            curr_page.write('<br>\n')
            curr_page.write('<br>\n')
# change page bg color based on where it is on the list
            if i == 1:
                curr_page.write('<body style="background-image: repeating-linear-gradient(rgb(48, 51, 32),rgb(234, 255, 159), rgb(255, 185, 138),rgb(44, 31, 24));\n')
            if i == 2:
                curr_page.write('<body style="background-image: repeating-linear-gradient(rgb(48, 48, 48),rgb(255, 255, 255), rgb(207, 207, 207),rgb(39, 39, 39));\n')
            if i == 3:
                curr_page.write('<body style="background-image: repeating-linear-gradient(rgb(51, 42, 32),rgb(192, 126, 88), rgb(216, 136, 122),rgb(44, 24, 24));\n')
            if i > 3 and i < 6:
                curr_page.write('<body style="background-image: repeating-linear-gradient(rgb(32, 48, 51),rgb(159, 233, 255), rgb(222, 138, 255),rgb(43, 24, 44));\n')
            if i > 5 and i < 11:
                curr_page.write('<body style="background-image: repeating-linear-gradient(rgb(51, 32, 32),rgb(255, 159, 159), rgb(150, 138, 255),rgb(24, 24, 44));\n')
            if i > 10 and i < 26:
                curr_page.write('<body style="background-image: repeating-linear-gradient(rgb(32, 51, 32),rgb(159, 255, 159), rgb(255, 138, 202),rgb(44, 24, 37));\n')
            if i > 25 and i < 51:
                curr_page.write('<body style="background-image: repeating-linear-gradient(rgb(44, 35, 24),rgb(255, 195, 138),rgb(161, 159, 255),rgb(32, 33, 51));\n')
            if i > 50 and i < 76:
                curr_page.write('<body style="background-image: repeating-linear-gradient(rgb(38, 32, 51),rgb(180, 159, 255), rgb(255, 234, 138),rgb(44, 41, 24));\n')
            if i > 75 and i < 101:
                curr_page.write('<body style="background-image: repeating-linear-gradient(rgb(44, 24, 29),rgb(255, 138, 138), rgb(170, 255, 159),rgb(37, 51, 32));\n')
            if i > 100 and i < 126:
                curr_page.write('<body style="background-image: repeating-linear-gradient(rgb(44, 24, 43),rgb(255, 138, 230), rgb(253, 255, 159),rgb(51, 51, 32));\n')
            if i > 125 and i < 151:
                curr_page.write('<body style="background-image: repeating-linear-gradient(rgb(44, 24, 24),rgb(255, 138, 138), rgb(255, 186, 159),rgb(51, 44, 32));\n')
            curr_page.write('    margin: 0;">\n')
            curr_page.write('<!-- div for the rules and other info -->\n')
            curr_page.write('    <div class="sider">\n')
            curr_page.write('          <h4>Rules:</h4>\n')
            curr_page.write("""          <h5 style="text-align: justify;">I. The real demonlist rules apply here (mainly so I don't have to write out my own).</h5>\n""")
            curr_page.write('          <h5 style="text-align: justify;">II. Any records submitted will only be allowed if they are from people *actually* in the discord.</h5>\n')
            curr_page.write("""          <h5 style="text-align: justify;">III. That's pretty much everything I'll add more later if I think of any.</h5>\n""")
            curr_page.write('          <hr style="color:white;">\n')
            curr_page.write('          <h4>Other (kinda important) Stuff:</h4>\n')
            curr_page.write("""          <h5 style="text-align: center;">- <a href="https://pointercrate.com/guidelines/index">Pointercrate's Rules</a></h5>\n""")
            curr_page.write('          <h5 style="text-align: center;">- <a href="pages/statsviewer.html">Stats Viewer</a></h5>\n')
            curr_page.write('          <h5 style="text-align: center;">- <a href="https://forms.gle/jDx28tHq8zhowzF2A">Submit a record here!</a></h5>\n')
            curr_page.write('          <h5 style="text-align: justify; color:rgb(189, 189, 189)">*Note: instead of using the form you can just message me any records on discord instead if you want</h5>\n')
            curr_page.write('      <hr style="color:white">\n')
            curr_page.write('      <h4 style="text-align: center;">Last updated: '+str(date)+'</h4>\n')
            curr_page.write('    </div>\n')
            curr_page.write('</body>\n')
            curr_page.write('<!-- actual level placed -->\n')
            curr_page.write('<div class="levelplacedfull">\n')
            curr_page.write('\n')
            if i == 1:
                curr_page.write('<p3>'+row_content[1]+'<a style="text-decoration: none; font-size: 150%;" href=2.html> ></a></p3> <br>\n')
            elif i == 150:
                curr_page.write('<p3><a style="text-decoration: none; font-size: 150%;" href=149.html>< </a>'+row_content[1]+'</p3> <br>\n')
            else:
                curr_page.write('<p3><a style="text-decoration: none; font-size: 150%;" href='+str(i-1)+'.html>< </a>'+row_content[1]+'<a style="text-decoration: none; font-size: 150%;" href='+str(i+1)+'.html> ></a></p3> <br>\n')
            curr_page.write('<p4>by '+row_content[2]+', verified by '+row_content[3]+'</p4> <br>\n')
            curr_page.write('<p4 style="color: rgb(187, 187, 187); padding-bottom: 2%;">"'+row_content[7]+'"</p4> <br>\n')
            curr_page.write('<hr style="width: 75%; color:white;">\n')
            curr_page.write(r'<iframe style="box-shadow: 2px 2px 15px #1b1b1b; border-radius: 15px" width="1072" height="603" src="'+row_content[8]+r'?si=P9We5d1GwCnMqau1&amp;controls=0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>'+"\n")
            curr_page.write('<hr style="width: 75%; color:white;">\n')
            curr_page.write('<div class="infodiv">\n')
            curr_page.write('  <h4>Game Version:</h4>\n')
            curr_page.write('  <p4>'+row_content[4]+'</p4>\n')
            curr_page.write('</div>\n')
            curr_page.write('<div class="infodiv">\n')
            curr_page.write('  <h4>Length:</h4>\n')
            curr_page.write('  <p4>'+row_content[5]+'</p4>\n')
            curr_page.write('</div>\n')
            curr_page.write('<div class="infodiv">\n')
            curr_page.write('  <h4>Level ID:</h4>\n')
            curr_page.write('  <p4>'+row_content[6]+'</p4>\n')
            curr_page.write('</div>\n')
            if i <= 75:
                curr_page.write('<div class="pointsdiv" style="margin-left: 25%;">\n')
                curr_page.write('  <h4>Points Awarded (100%):</h4>\n')
                curr_page.write('  <p4>'+str(200-(i-1))+'</p4>\n')
                curr_page.write('</div>\n')
                curr_page.write('<div class="pointsdiv" style="margin-left: 15%;">\n')
                curr_page.write('  <h4>Points Awarded (50%):</h4>\n')
                curr_page.write('  <p4>'+str((200-(i-1))/10)+'</p4>\n')
                curr_page.write('</div>\n')
            else:
                curr_page.write('<div class="pointsdivextended" style="margin-left: 25%;">\n')
                curr_page.write('  <h4>Points Awarded (100%):</h4>\n')
                curr_page.write('  <p4>'+str(200-(i-1))+'</p4>\n')
                curr_page.write('</div>\n')               
            curr_page.write("<!-- We don't talk about this -->\n")
            curr_page.write('<br>\n')
            curr_page.write('<br>\n')
            curr_page.write('<br>\n')
            curr_page.write('<br>\n')
            curr_page.write('<br>\n')
            curr_page.write('<br>\n')
            curr_page.write('<br>\n')
            curr_page.write('<br>\n')
            curr_page.write('<br>\n')
            curr_page.write('<br>\n')
            curr_page.write('<br>\n')
            curr_page.write('<br>\n')
            curr_page.write('<br>\n')
            curr_page.write('<br>\n')
            curr_page.write('</div>\n')
            curr_page.write('<br>\n')
            curr_page.write('<!-- Records part xd-->\n')
            curr_page.write('<div class="levelplacedfull">\n')
            curr_page.write('  <p3>Records:</p3>\n')
            curr_page.write('  <br>\n')
            curr_page.write(r'  <p4>50% or better required to qualify</p4>'+"\n")
            curr_page.write('  <br>\n')
            curr_page.write('  <p4 style="color: rgb(138, 138, 138)">NUMBER record(s) registered, out of which NUMBER are/is 100%</p4>\n')
            curr_page.write('  <br>\n')
            curr_page.write('  <hr style="color:white">\n')
            curr_page.write('  <table>\n')
            curr_page.write('    <tr>\n')
            curr_page.write('      <th>Record Holder:    </th>\n')
            curr_page.write('      <th>Progress:     </th>\n')
            curr_page.write('      <th>Proof:    </th>\n')
            curr_page.write('    </tr>\n')
            curr_page.write('<!-- Each new record will follow this template: -->\n')

            for x in range(1,15):
                if str(rec_content[x]).replace("\n","") != "":
                    prog = int(float(str(rec_content[x]).replace("\n",".0")))
                    rec_content[x] = rec_content[x].replace("\n","")
                    if x == 1:
                        curr_page.write('    <tr>\n')
                        curr_page.write('      <td>Tristeamer</td>\n')
                        curr_page.write('      <td>'+str(rec_content[x])+'%</td>\n')
                        curr_page.write('      <td><a href="(LINK)">Video (not added yet sry)</a></td>\n')
                        curr_page.write('    </tr>\n')
                        points = calc_points(i,prog)
                        TRISTEAMER += points
                    if x == 2:
                        curr_page.write('    <tr>\n')
                        curr_page.write('      <td>Willo</td>\n')
                        curr_page.write('      <td>'+str(rec_content[x])+'%</td>\n')
                        curr_page.write('      <td><a href="(LINK)">Video (not added yet sry)</a></td>\n')
                        curr_page.write('    </tr>\n')
                        points = calc_points(i,prog)
                        WILLO += points
                    if x == 3:
                        curr_page.write('    <tr>\n')
                        curr_page.write('      <td>Jeremy Clarkson</td>\n')
                        curr_page.write('      <td>'+str(rec_content[x])+'%</td>\n')
                        curr_page.write('      <td><a href="(LINK)">Video (not added yet sry)</a></td>\n')
                        curr_page.write('    </tr>\n')
                        points = calc_points(i,prog)
                        JEREMY_CLARKSON += points
                    if x == 4:
                        curr_page.write('    <tr>\n')
                        curr_page.write('      <td>Wahffle</td>\n')
                        curr_page.write('      <td>'+str(rec_content[x])+'%</td>\n')
                        curr_page.write('      <td><a href="(LINK)">Video (not added yet sry)</a></td>\n')
                        curr_page.write('    </tr>\n')
                        points = calc_points(i,prog)
                        WAHFFLE += points
                    if x == 5:
                        curr_page.write('    <tr>\n')
                        curr_page.write('      <td>MrLibra</td>\n')
                        curr_page.write('      <td>'+str(rec_content[x])+'%</td>\n')
                        curr_page.write('      <td><a href="(LINK)">Video (not added yet sry)</a></td>\n')
                        curr_page.write('    </tr>\n')
                        points = calc_points(i,prog)
                        MRLIBRA += points
                    if x == 6:
                        curr_page.write('    <tr>\n')
                        curr_page.write('      <td>MiquelVZLA</td>\n')
                        curr_page.write('      <td>'+str(rec_content[x])+'%</td>\n')
                        curr_page.write('      <td><a href="(LINK)">Video (not added yet sry)</a></td>\n')
                        curr_page.write('    </tr>\n')
                        points = calc_points(i,prog)
                        MIQUEL += points
                    if x == 7:
                        curr_page.write('    <tr>\n')
                        curr_page.write('      <td>Travisaurus</td>\n')
                        curr_page.write('      <td>'+str(rec_content[x])+'%</td>\n')
                        curr_page.write('      <td><a href="(LINK)">Video (not added yet sry)</a></td>\n')
                        curr_page.write('    </tr>\n')
                        points = calc_points(i,prog)
                        TRAVISAURUS += points
                    if x == 8:
                        curr_page.write('    <tr>\n')
                        curr_page.write('      <td>evil</td>\n')
                        curr_page.write('      <td>'+str(rec_content[x])+'%</td>\n')
                        curr_page.write('      <td><a href="(LINK)">Video (not added yet sry)</a></td>\n')
                        curr_page.write('    </tr>\n')
                        points = calc_points(i,prog)
                        EVIL += points
                    if x == 9:
                        curr_page.write('    <tr>\n')
                        curr_page.write('      <td>melonz</td>\n')
                        curr_page.write('      <td>'+str(rec_content[x])+'%</td>\n')
                        curr_page.write('      <td><a href="(LINK)">Video (not added yet sry)</a></td>\n')
                        curr_page.write('    </tr>\n')
                        points = calc_points(i,prog)
                        MELONZ += points
                    if x == 10:
                        curr_page.write('    <tr>\n')
                        curr_page.write('      <td>Fenix</td>\n')
                        curr_page.write('      <td>'+str(rec_content[x])+'%</td>\n')
                        curr_page.write('      <td><a href="(LINK)">Video (not added yet sry)</a></td>\n')
                        curr_page.write('    </tr>\n')
                        points = calc_points(i,prog)
                        FENIX += points
                    if x == 11:
                        curr_page.write('    <tr>\n')
                        curr_page.write('      <td>FizzEL</td>\n')
                        curr_page.write('      <td>'+str(rec_content[x])+'%</td>\n')
                        curr_page.write('      <td><a href="(LINK)">Video (not added yet sry)</a></td>\n')
                        curr_page.write('    </tr>\n')
                        points = calc_points(i,prog)
                        FIZZEL += points
                    if x == 12:
                        curr_page.write('    <tr>\n')
                        curr_page.write('      <td>TheMagicWaterBottle</td>\n')
                        curr_page.write('      <td>'+str(rec_content[x])+'%</td>\n')
                        curr_page.write('      <td><a href="(LINK)">Video (not added yet sry)</a></td>\n')
                        curr_page.write('    </tr>\n')
                        points = calc_points(i,prog)
                        CARTER += points
                    if x == 13:
                        curr_page.write('    <tr>\n')
                        curr_page.write('      <td>Christeamer</td>\n')
                        curr_page.write('      <td>'+str(rec_content[x])+'%</td>\n')
                        curr_page.write('      <td><a href="(LINK)">Video (not added yet sry)</a></td>\n')
                        curr_page.write('    </tr>\n')
                        points = calc_points(i,prog)
                        CHRISTEAMER += points
                    if x == 14:
                        curr_page.write('    <tr>\n')
                        curr_page.write('      <td>Foody</td>\n')
                        curr_page.write('      <td>'+str(rec_content[x])+'%</td>\n')
                        curr_page.write('      <td><a href="(LINK)">Video (not added yet sry)</a></td>\n')
                        curr_page.write('    </tr>\n')
                        points = calc_points(i,prog)
                        FOODY += points
                        
            curr_page.write('<!-- End Template :33333 -->\n')
            curr_page.write('  </table>\n')
            curr_page.write('  <br>\n')
            curr_page.write('</div>\n')
            curr_page.write('<br>\n')
            curr_page.write('<br>\n')
            curr_page.write('<!-- the page footer but this thing is so fucked up ngl idk why -->\n')
            curr_page.write('<div class="footer" style="text-align: center; padding: 10px;">\n')
            curr_page.write('    <p1>Website by <a href="https://twitter.com/Tristeamerowo">tris</a> <3</p1><br>\n')
            curr_page.write("    <p2>Yeah I know it's not that good but I only made this because I was bored.</p2><br>\n")
            curr_page.write('    <p2>Not affiliated with pointercrate obviously (i just used their design as inspiration)</p2><br>\n')
            curr_page.write("    <p2>some text here so it's not empty</p2><br>\n")
            curr_page.write('    <p2><a href="https://tristeamer.github.io">Return to main page here.</a></p2><br>\n')
            curr_page.write('  </div>\n')
            curr_page.write('  </html>\n')

        curr_page.close()

# append the footer to the index.html file
    with open("index.html", "a") as index:
        index.write('<!-- the page footer but this thing is so fucked up ngl idk why -->\n')
        index.write('<div class="footer" style="text-align: center; padding: 10px;">\n')
        index.write('  <p1>Website by <a href="https://twitter.com/Tristeamerowo">tris</a> <3</p1><br>\n')
        index.write("  <p2>Yeah I know it's not that good but I only made this because I was bored.</p2><br>\n")
        index.write('  <p2>Not affiliated with pointercrate obviously (i just used their design as inspiration)</p2><br>\n')
        index.write("  <p2>some text here so it's not empty</p2><br>\n")
        index.write('  <p2><a href="https://tristeamer.github.io">Return to main page here.</a></p2><br>\n')
        index.write('</div>\n')
        index.write('</html>\n')
        index.close()

# create statsviewr page (unfinished!! :OOOOOOOOOOO w,.d,w.a,,s,ad;sladaowd,kopk12kopd1lq;dkd;lwkaqdopska'l)
    with open("statsviewer.html", "w") as stats:
        stats.write('Christeamer: '+str(CHRISTEAMER)+"<br>\n")
        stats.write('evil: '+str(EVIL)+"<br>\n")
        stats.write('Fenix: '+str(FENIX)+"<br>\n")
        stats.write('FizzEl: '+str(FIZZEL)+"<br>\n")
        stats.write('Foody: '+str(FOODY)+"<br>\n")
        stats.write('Jeremy Clarkson: '+str(JEREMY_CLARKSON)+"<br>\n")
        stats.write('melonz: '+str(MELONZ)+"<br>\n")
        stats.write('Miquel: '+str(MIQUEL)+"<br>\n")
        stats.write('MrLibra: '+str(MRLIBRA)+"<br>\n")
        stats.write('TheMagicWaterBottle: '+str(CARTER)+"<br>\n")
        stats.write('Travisaurus: '+str(TRAVISAURUS)+"<br>\n")
        stats.write('Tristeamer: '+str(TRISTEAMER)+"<br>\n")
        stats.write('Wahffle: '+str(WAHFFLE)+"<br>\n")
        stats.write('Willo: '+str(WILLO)+"<br>\n")
        stats.write('<a href="https://tristeamer.github.io/sgdl/index.html">Return to main page.</a>\n')
        stats.write('Would you believe me if I told you that this page is unfinished? idk what to really put here honestly :v<br>\n')

    stats.close()

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False
    
def calc_points(pos, prog):
    points = 0
    if prog == 100:
        points = (200-(pos-1))
    elif pos <=75:
        if prog >= 50:
            points = ((200-(pos-1))/10)
    return points

