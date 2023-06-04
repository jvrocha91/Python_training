# Tema: Catalogo de filmes
# O usuario pode buscar o filme que deseja, e receber algumas informações sobre o mesmo, podendo buscar pelo titulo do filme, genero, diretor, atores e ano de lançamento

filmes = [{'titulo':"Forest Gump",
          "genero":['romance','comedia','drama'],'ano':'1994', 'diretor':'Robert Zemeckis','atores':['Tom Hanks', 'Robin Wright'],'descrição':'A man with a low IQ has accomplished great things in his life and been present during significant historic events—in each case, far exceeding what anyone imagined he could do. But despite all he has achieved, his one true love eludes him.'}, 
          
          {'titulo':"Cidade De Deus",
          "genero":['crime','drama'],'ano':'2002','diretor':'Fernando Meirelles','atores':['Alexandre Rodrigues', 'Leandro Firmino'],'descrição':'Buscapé was raised in a very violent environment. Despite the feeling that all odds were against him, he finds out that life can be seen with other eyes…'},
         
          {'titulo':"Pulp Fiction",
          "genero":['crime','thriller'],'ano':'1994','diretor':'Quentin Tarantino','atores':['John Travolta', 'Samuel Jackson'],'descrição':'A burger-loving hit man, his philosophical partner, a drug-addled gangster moll and a washed-up boxer converge in this sprawling, comedic crime caper. Their adventures unfurl in three stories that ingeniously trip back and forth in time.'},
 
          {'titulo':"De volta para o futuro",
          "genero":['aventura','comedia', 'ficção'],'ano':'1985','diretor':' Robert Zemeckis','atores':['Michael J. Fox', 'Christopher Lloyd'],'descrição':'Eighties teenager Marty McFly is accidentally sent back in time to 1955, inadvertently disrupting his parents first meeting and attracting his mothers romantic interest. Marty must repair the damage to history by rekindling his parents romance and - with the help of his eccentric inventor friend Doc Brown - return to 1985.'},
        
          {'titulo':"Sociedade dos poetas mortos",
          "genero":['drama'],'ano':'1989','diretor':' Peter Weir','atores':['Robin Williams', 'Ethan Hawke'],'descrição':'At an elite, old-fashioned boarding school in New England, a passionate English teacher inspires his students to rebel against convention and seize the potential of every day, courting the disdain of the stern headmaster.'},
        
          {'titulo':"Bacurau",
          "genero":['misterio','thriller', 'western'],'ano':'2019','diretor':'Kleber Mendonça Filho','atores':['Barbara Colen', 'Thomas Aquino'],'descrição':'Bacurau, a small town in the Brazilian sertão, mourns the loss of its matriarch, Carmelita, who lived to be 94. Days later, its inhabitants notice that their community has vanished from most maps.'},

          {'titulo':"Vingadores:Ultimato",
          "genero":['aventura','ação', 'ficção'],'ano':'2019','diretor':'Anthony Russo','atores':['Robert Downey Jr', 'Chris Evans'],'descrição':'After the devastating events of Avengers: Infinity War, the universe is in ruins due to the efforts of the Mad Titan, Thanos. With the help of remaining allies, the Avengers must assemble once more in order to undo Thanos actions and restore order to the universe once and for all, no matter what consequences may be in store.'},
          
          {'titulo':"As vantagens de ser invisivel",
          "genero":['drama'],'ano':'2012','diretor':' Stephen Chbosky','atores':['Logan Lerman', 'Emma Watson'],'descrição':'Pittsburgh, Pennsylvania, 1991. High school freshman Charlie is a wallflower, always watching life from the sidelines, until two senior students, Sam and her stepbrother Patrick, become his mentors, helping him discover the joys of friendship, music and love…'},
          
          {'titulo':"Sixteen Candles",
          "genero":['romance','comedia'],'ano':'1984','diretor':' John Hughes','atores':['Molly Ringwald', 'Justin Henry'],'descrição':'A teenage girl deals with her parents forgetting her birthday and a crush on her high school heartthrob.'},
          
          {'titulo':"Kill Bill",
          "genero":['ação','crime'],'ano':'2003','diretor':'Quentin Tarantino','atores':['Uma Thurman', 'Lucy Liu'],'descrição':'An assassin is shot by her ruthless employer, Bill, and other members of their assassination circle but she lives to plot her vengeance.'},
          
          {'titulo':"10 coisas que odeio em voce",
          "genero":['romance','comedia','drama'],'ano':'1999','diretor':'Gil Junger','atores':['Julia Stiles', 'Heath Ledger'],'descrição':'On the first day at his new school, Cameron instantly falls for Bianca, the gorgeous girl of his dreams. The only problem is that Bianca is forbidden to date until her ill-tempered, completely un-dateable older sister Kat goes out, too. In an attempt to solve his problem, Cameron singles out the only guy who could possibly be a match for Kat: a mysterious bad boy with a nasty reputation of his own.'},
          
          {'titulo':"Your Name",
          "genero":['romance','animação','drama'],'ano':'2016','diretor':' Makoto Shinkai','atores':['Rynosuke Kamiki', 'Mone Kamishi'],'descrição':'High schoolers Mitsuha and Taki are complete strangers living separate lives. But one night, they suddenly switch places. Mitsuha wakes up in Taki body, and he in hers. This bizarre occurrence continues to happen randomly, and the two must adjust their lives around each other.'},
          
          {'titulo':"Divertidamente",
          "genero":['aventura','comedia', 'animação','familia','drama'],'ano':'2015','diretor':'Pete Docter','atores':['Amy Poehler', 'Phyllis Smith'],'descrição':'Growing up can be a bumpy road, and its no exception for Riley, who is uprooted from her Midwest life when her father starts a new job in San Francisco. Riley guiding emotions— Joy, Fear, Anger, Disgust and Sadness—live in Headquarters, the control centre inside Riley mind, where they help advise her through everyday life and tries to keep things positive, but the emotions conflict on how best to navigate a new city, house and school.'},
          
          {'titulo':"Green Book",
          "genero":['comedia','drama'],'ano':'2018','diretor':'Peter Farrelly','atores':['Viggo Mortensen', 'Mahershala Ali'],'descrição':'Tony Lip, a bouncer in 1962, is hired to drive pianist Don Shirley on a tour through the Deep South in the days when African Americans, forced to find alternate accommodations and services due to segregation laws below the Mason-Dixon Line, relied on a guide called The Negro Motorist Green Book.'},
          
          {'titulo':"It",
          "genero":['terror','fantasia'],'ano':'2017','diretor':'Andy Muschietti','atores':['Sophia Lillis', 'Finn Wolfhard'],'descrição':'In a small town in Maine, seven children known as The Losers Club come face to face with life problems, bullies and a monster that takes the shape of a clown called Pennywise.'},
          
          {'titulo':"Parasita",
          "genero":['drama','thriller', 'comedia'],'ano':'2019','diretor':'Bong Joon-ho','atores':['Song Kang-ho', 'Lee Sun-kyun'],'descrição':'All unemployed, Ki-taek family takes peculiar interest in the wealthy and glamorous Parks for their livelihood until they get entangled in an unexpected incident.'},
          
          {'titulo':"Curtindo a vida adoidado",
          "genero":['comedia'],'ano':'1986','diretor':'John Hughes','atores':['Matthew Broderick', 'Alan Ruck'],'descrição':'After high school slacker Ferris Bueller successfully fakes an illness in order to skip school for the day, he goes on a series of adventures throughout Chicago with his girlfriend Sloane and best friend Cameron, all the while trying to outwit his wily school principal and fed-up sister.'},
          
          {'titulo':"Clube dos Cinco",
          "genero":['comedia','drama'],'ano':'1985','diretor':'John Hughes','atores':['Molly Ringwald', 'Emilio Estevez'],'descrição':'Five disparate high school students meet in Saturday detention, and discover they have a lot more in common than they thought.'},
        
          {'titulo':"Laranja Mecanica",
          "genero":['ficção','drama'],'ano':'1971','diretor':'Stanley Kubrick','atores':['Malcolm McDowell', 'Patrick Magee'],'descrição':'In a near-future Britain, young Alexander DeLarge and his pals get their kicks beating and raping anyone they please. When not destroying the lives of others, Alex swoons to the music of Beethoven. The state, eager to crack down on juvenile crime, gives an incarcerated Alex the option to undergo an invasive procedure that will rob him of all personal agency. In a time when conscience is a commodity, can Alex change his tune?'},
          
          {'titulo':"Tropa de Elite",
          "genero":['ação','drama', 'crime'],'ano':'2007','diretor':'José Padilha','atores':['Wagner Moura', 'Caio Junqueira'],'descrição':'In 1997, before the visit of the pope to Rio de Janeiro, Captain Nascimento from BOPE (Special Police Operations Battalion) is assigned to eliminate the risks of the drug dealers in a dangerous slum nearby where the pope intends to be lodged.'},

          {'titulo':"Joker",
          "genero":['thriller','drama', 'crime'],'ano':'2019','diretor':'Todd Phillips','atores':['Joaquin Phoenix', 'Robert de Niro'],'descrição':'During the 1980s, a failed stand-up comedian is driven insane and turns to a life of crime and chaos in Gotham City while becoming an infamous psychopathic crime figure.'},
          
          {'titulo':"Rocky",
          "genero":['romance','drama'],'ano':'1976','diretor':' John G. Avildsen','atores':['Sylvester Stallone', 'Talia Shire'],'descrição':'When world heavyweight boxing champion, Apollo Creed wants to give an unknown fighter a shot at the title as a publicity stunt, his handlers choose palooka Rocky Balboa, an uneducated collector for a Philadelphia loan shark. Rocky teams up with trainer Mickey Goldmill to make the most of this once in a lifetime break.'},
          
          {'titulo':"O Lobo de Wall Street",
          "genero":['comedia','drama', 'crime'],'ano':'2013','diretor':'Martin Scorsese','atores':['Leonardo DiCaprio', 'Jonah Hill'],'descrição':'A New York stockbroker refuses to cooperate in a large securities fraud case involving corruption on Wall Street, corporate banking world and mob infiltration. Based on Jordan Belfort autobiography.'},
          
          {'titulo':"Corra",
          "genero":['thriller','terror', 'misterio'],'ano':'2017','diretor':'Jordan Peele','atores':['Daniel Kaluuya', 'Allison Williams'],'descrição':'Chris and his girlfriend Rose go upstate to visit her parents for the weekend. At first, Chris reads the family overly accommodating behavior as nervous attempts to deal with their daughters interracial relationship, but as the weekend progresses, a series of increasingly disturbing discoveries lead him to a truth that he never could have imagined.'},
          
          {'titulo':"Django",
          "genero":['western','drama'],'ano':'2012','diretor':' Quentin Tarantino','atores':['Jamie Foxx', 'Leonardo DiCaprio'],'descrição':'With the help of a German bounty hunter, a freed slave sets out to rescue his wife from a brutal Mississippi plantation owner.'},

] 
        

