from googlesearch import search
import random, os
import requests
from bs4 import BeautifulSoup

art = [r"""
                                +                                                       
               '            o                                                   
                     o   .      '      ':.        .                  o          
             .    '           .          '::._                 .            _|_ 
              .           '                '._)                              |  
           o    .:'                        +  '  + '                            
     '      _.::'                                                               
       .:' (_.'                .o         '                           +    +~~  
   _.::'   +'                o                |               .        .      + 
  (_.'                                     * -o-     .           *     |     '  
            ':.           +                   |                       -+-       
          .   '::._            .        *                              |        
                '._)*'      o               .      .   '     .                + 
                 .-.      \  .*            +                                    
*               (   )      \                                     +        .     
                 `-'        **                                      .  +        
 +          *                          +                     +                  
                   *                              '   .                         
                     '  . +           .                  +       .   *          
                                           +                 o       '          """,
                                           
r"""
        \\\    /// ___    wWw ()_()  
    /)  ((O)  (O))(___)__ (O)_(O o)  
  (o)(O) | \  / | (O)(O)  / __)|^_\  
   //\\  ||\\//|| /  _\  / (   |(_)) 
  |(__)| || \/ || | |_))(  _)  |  /  
  /,-. | ||    || | |_)) \ \_  )|\\  
 -'   ''(_/    \_)(.'-'   \__)(/  \) 
""",
r"""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠶⠛⠋⠉⠐⠻⣷⣊⠉⠀⠀⠯⣔⠤⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠈⠙⢤⣶⣋⣀⣀⠁⠀⠙⠢⣄⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣄⣀⡀⠀⠀⠁⠢⢄⠑⣤⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⡼⠋⠀⡀⠀⠀⠀⠀⠀⠀⠀⢀⡠⠄⠀⠀⠀⠙⣄⠈⣙⠲⢤⡀⠀⠑⢌⣻⣄⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢠⠎⠀⡠⡾⠀⠀⠀⠀⠀⢀⣤⠖⠉⠀⠀⠀⠀⣠⠖⠉⠣⠈⠑⠀⠈⠑⠄⠀⠉⢿⣦⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣞⣠⠞⡰⠁⠀⠀⡀⣠⣾⠟⠁⠀⠀⠀⠀⢰⠞⠀⠀⡄⠀⡀⠘⣄⠀⠀⠢⡀⢀⠢⠙⣧⠀⠀
⠀⠀⠀⠀⠀⠀⢸⣿⢇⡴⠁⠀⡆⠈⢠⡿⠛⢳⡄⢀⠇⠀⢠⠞⠀⠀⢰⠁⠀⢧⠀⢻⠱⣦⢰⡞⢧⣀⠀⠘⣧⠀
⠀⠀⠀⠀⠀⠀⡼⢡⣿⠃⠀⢠⡇⣰⠋⠀⢰⠏⢠⠏⠀⣰⠋⠀⠀⢠⡟⠀⠘⠀⠇⢸⠀⠈⢻⡳⡤⣈⣷⠀⠸⣆
⠀⠀⠀⠀⠀⢸⣷⣏⡇⠀⠀⢸⢠⢿⠟⠀⣏⡴⢃⡄⢠⠃⠀⠀⠀⢸⠃⠀⠀⠀⠀⢸⡇⠘⡇⠹⣼⠀⢻⠀⡄⢸
⠀⠀⠀⠀⠀⠈⡟⢸⠁⣰⡇⣸⠘⢦⠤⢶⡏⢀⡼⡇⢸⠀⠀⠀⢀⡏⠀⠀⠀⠀⡀⣼⣧⠀⡇⠀⠈⣦⡼⠀⣇⢸
⠀⠀⠀⠀⠀⠀⡇⠈⣰⠋⡇⡟⠀⠀⢰⣿⣁⡾⠁⢹⣼⣧⡇⠀⡜⠀⠀⣠⠆⣼⣰⢿⣿⢰⠇⠀⣸⠏⣰⢀⣿⣿
⠀⠀⠀⠀⠀⠀⢣⣰⣿⡀⢹⣿⠀⠀⣾⣿⣿⣟⣒⣺⣿⢼⣧⣼⠁⣠⣶⠏⣰⣿⣯⣼⣿⣿⠀⣴⣯⣴⡿⣼⠹⡿
⠀⠀⠀⠀⠀⠀⠀⢻⣿⣧⢠⣿⡀⣸⡏⠿⢿⣿⣿⠙⠻⠆⣿⣧⣾⣿⣯⣴⣿⣿⡟⠻⣿⣷⣾⣿⣿⢿⣿⠃⢰⠇
⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣧⡻⣇⣿⣿⣄⠀⠈⠁⠀⠀⣸⡿⢋⠟⣹⡿⠋⠛⠛⠁⢠⣿⣿⣿⣿⡇⣸⠃⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢿⣿⣿⣿⣮⡻⣷⢤⣀⠀⠸⠟⠁⠀⠜⠁⠀⠀⠀⣠⣶⣿⣿⣿⣿⣿⡇⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⠿⠮⢽⣿⣦⡀⠁⠀⠀⠀⠀⣰⠄⠀⠈⢉⣡⣾⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠾⠉⠀⠀⠀⠀⠀⠉⢻⡶⠦⠀⠀⠄⠅⠀⠐⠚⣻⣿⣿⣿⣿⣿⢛⡏⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⡴⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡒⠀⠀⠀⢀⣠⣶⣿⣿⣿⡿⠋⣿⠋⠘⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣠⠎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣦⡤⠖⠉⠉⠟⣹⠟⠋⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⠴⠊⣹⡟⠀⠀⣰⢾⣿⣷⣆⠀⠀⠀⠀⠀⢀⡿⠛⠃⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢠⠎⠀⣰⣿⡇⠀⡷⣿⠿⠿⣟⣿⠀⠀⠀⠀⠀⣼⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣠⣿⣿⡇⠀⢿⣮⣗⠒⠛⠁⠀⠀⠀⠀⠸⣿⣿⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠘⠛⠛⣿⣿⣿⡇⠀⠈⠣⠀⠀⠀⠀⠀⠀⢀⣄⣴⢿⣿⣿⡌⠑⠢⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢸⡆⢸⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⡏⠀⠻⣿⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""",
r"""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⣤⣤⣄⣀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⢿⣷⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡙⠻⣿⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⠈⠻⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⣹⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣶⣤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡧⣼⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣽⣧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⣿⣿⣿⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣷⡈⢻⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡌⠻⣦⡽⣆⠀⠀⠀⠀⠀⠀⠀⠀
⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⣧⠀⠹⣿⡎⢿⠙⢿⣿⣿⣿⡟⢿⣿⣿⣿⣿⣿⣿⣿⣿⣄⠈⠻⣾⣆⠀⠀⠀⠀⠀⠀⠀
⠏⢺⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⢸⡟⠀⠀⠸⣧⠈⣇⠀⠹⣿⣿⣿⣬⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠈⢻⡄⠀⠀⠀⠀⠀⠀
⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⡿⠁⢸⡇⠀⠀⠀⢻⡀⢸⣤⠞⠛⣿⠻⡇⠸⣿⣿⡟⠛⣿⣿⡟⣷⠙⣆⠀⠀⠙⠀⠀⠀⠀⠀⠀
⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣽⣿⡿⢁⣿⣿⣿⠃⠀⢸⠇⠀⠀⠀⢨⠟⠉⠀⠀⠀⠘⡆⠙⠀⢿⢻⣿⡜⣿⢹⡇⠘⣇⠈⠑⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣿⣿⣿⡿⣿⣿⠋⠙⣿⣿⠏⠒⠉⡾⠀⠀⠀⢀⣿⣾⣿⡟⠉⠀⠀⠀⠀⠀⠘⠈⢿⡧⣿⠀⣇⠀⠘⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢿⣿⠃⠀⢻⡏⢀⣴⣿⣟⡒⣶⣴⠃⠀⠀⠀⠸⠛⠛⢃⡤⢄⣀⣀⣀⣀⣤⡄⠀⣼⣷⠃⠀⠘⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⣸⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⢸⡇⠀⠀⢸⡇⠉⠀⠟⠉⠙⠛⠋⠀⠀⠀⠀⠀⠀⠀⣿⡟⢿⣿⣍⣽⠀⢺⠁⠀⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠈⢻⡏⠉⡉⠻⣿⣿⣿⣿⡏⢻⣟⠇⢸⠃⠀⠀⠀⠁⣠⣴⣶⣶⡒⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢷⡈⠛⠟⢃⣠⠞⠀⢸⡟⠓⠤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣷⡇⠙⡷⢼⣿⣿⣿⠁⢈⡿⠄⠀⣠⠤⠴⣶⣿⣏⣹⠛⣯⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠀⡀⠀⣾⡀⢢⠀⠸⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢿⡇⠀⡇⠀⢈⡿⣿⡄⠸⣇⠀⠀⠛⢦⣄⠈⢛⣟⣫⠴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠃⠉⠀⠀⢹⢧⡼⠀⢰⠷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠘⣿⡇⠃⠀⢿⣀⡘⢧⡀⠹⣆⠀⠀⠀⠀⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣆⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡾⠁⠀⠈⠀⡼⢟⠒⠤⣀⡀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠈⠛⠲⢤⣄⠈⢁⠀⠁⠀⡹⣦⠀⠀⠀⢘⣆⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⠆⠀⠀⠀⠀⠀⠀⠀⣠⠟⠀⠀⠀⠀⡼⡇⠈⢧⠀⠈⠁⠀⠀⠀⠀⠀⠤
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⣹⠿⠚⠛⠉⠉⠉⠉⠉⠻⠯⠥⠴⣋⣸⠀⠀⠀⠀⠀⠀⠀⠙⠿⠿⠁⠀⠀⠀⠀⠀⠀⠀⡰⠋⠀⠀⠀⠀⢸⠁⣿⠀⠈⢳⠀⠀⠀⣴⠛⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣯⠶⠖⠒⠛⠉⠉⣙⠳⠶⠶⢶⣾⡿⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣤⠀⠀⠀⠀⠀⢠⠞⠁⠀⠀⢀⡀⠀⡎⠀⣏⠀⠀⠀⠀⠀⠀⠈⢷⡀⢠⣾
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠏⠀⠀⠀⢀⣴⣾⠟⢛⢿⣋⠉⢧⡀⠀⠀⠀⠀⠀⠀⠀⠀⠴⣶⡿⠟⠃⠀⠀⠀⢀⡴⠃⠀⠀⠀⢠⡟⠀⢸⡇⠀⡿⠀⠀⠀⠀⠀⠀⠀⠈⣷⣸⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡾⠀⠀⠀⠀⣸⡟⠁⠀⡞⠀⠉⠳⢦⣉⣻⣦⣤⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠟⠀⠀⠀⠀⠀⠀⡇⠀⢸⠁⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿
⠀⠀⠀⠀⠀⠀⠀⠀⡼⠃⠀⠀⠀⣰⡟⠀⠀⡼⠁⠀⠀⠀⣠⠞⠉⢀⣀⣄⠀⢹⡆⠀⠀⠀⠀⠀⠀⢰⡷⠛⠒⠒⢤⣀⡀⠀⢰⠀⠀⡌⠀⢰⠃⠀⠀⠀⠀⠀⠀⣠⣾⢿⣿⣿
⠀⠀⠀⠀⣀⡤⠖⠚⠙⠚⠛⠳⠶⠿⠧⠤⠴⢥⣤⣀⠀⡼⢡⡶⠛⠉⣠⠞⣴⡾⠯⣶⣤⣀⠀⢀⣠⡾⣷⠀⠀⠀⠀⢸⠁⢠⠊⠀⠀⡇⠓⡇⠀⠀⠀⠀⠀⣠⡾⠋⢠⣿⣿⣿
⠀⠀⠀⢀⣧⠖⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⣧⡟⠀⠀⣼⢿⡾⠉⠛⣦⡀⠀⠈⠉⠉⠀⠀⢞⡆⠀⠀⠀⡜⠀⠁⠀⠀⠀⡇⢰⡁⠀⠀⠀⡠⠚⠉⠳⣄⣬⣿⣿⣿
⠀⠀⠀⠉⠁⠀⠀⠛⠶⢤⣤⣤⣴⣖⣒⡒⠲⣤⣄⠀⢀⡏⠀⠀⢸⣇⡾⠁⠀⠀⠀⠙⢶⡀⠀⠀⠀⠀⠸⣿⠀⠀⢸⡇⠀⠀⠀⠀⢸⠁⠀⠉⢲⡴⠊⠀⠀⠀⠀⠈⠣⡽⣿⣿
⡀⠀⠀⠀⠀⠒⠂⠆⠀⠀⠀⠀⠀⠈⠉⠉⠓⠲⣬⣦⣟⡁⠀⠀⣨⣿⣿⣦⡚⣻⣤⠀⠀⢻⡆⠀⠀⠀⢰⣿⠀⠀⠀⠹⡄⠀⠀⠀⢸⠀⣀⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠁⢾⣿""",
r"""
#####################################*###################################%@     
##########################*########**###################**##############%%%     
##################################***###################**######*#########%@@   
######################***########****#########**##########################%@@   
######################***#######****##########*###########################%%%   
######################***######**#############*###***#####################%%%   
#####################***##########################****########%#############%@  
######################*##########################******#####################%@@ 
################################################********####################%@@ 
#######################################*########********####################%@@ 
###############################################***********####%###%##%%####%%@@ 
########################%############*########************######*#########%%@@@ 
########################%######%%############**************#####***#######%@@@@ 
#############################%%%###***######****************####***#######%@@@@ 
******##%###########%%#############***######****************####****#####%%@@@@ 
**#############%#################****#####*******************###*****###%@@@@   
##***###############%############***#####*****************************#%%@@@    
****##*###############*########*****####****************************###%%@@     
****#**##############***#********************************#********#####%@@      
****#**######**####*************************************###########***#%@       
****##*######***************************####*************************##%@       
##***#####***************#####*******####****************************##%@       
####*************************#########*******************************#%%        
#######**************************************************************%@@        
#########%%##******************************************************##%@@        
########%@@%%#*****************************************************#%%          
#######%@@@%%##**************************************************##%@@          
#####%@@@@@%%###*************************************************#@@            
####%@@@@@@@%#####*****************#*****************##***####*#%%              
##%%@@@@@@@@@##*###***************###***************##########%%@               
%%@@@@@@@@@@@@%#**####**************######*****########*###*###%@@              
 @@@@@@@@@@@@@@@#***####*****************########**##*###***####%%              
 @@@@@@@@@@@@@@@@%#****######*********************######**########@             
@@@@@@@@@@@@@@@@@@@@##******#######***********#####*###**###*####%@@            
@@@@@@@@@@@@@@@@@@@@@@%##**********#####%@@@@@@@@#####**###**####%%%            
@@@@@@@@@@@@@@@@%%@@@@@@@@%###*******#%@@@@@@@@%%#*##**##***##*#%%#%@           
@@@@@@@@@@@@@@%##*#%@@@@@@@@@@@@@@@@@@@@@@%%@@@%#*****###*###**#%###@           
@@@@@@@@@@@@@@%******#%@@@@@@@@@@@@@@@@@%#*##%%#*****###**##**#####%@           
@@@@@@@@@@@@%#**********##%%@@@@@@@@%##*****###******##**##**#####%%            
@@@@@@@@@@@@%#******************************##**********##***###*#%%            
@@@@@@@@@@@@%#******************************##***************###*#%%            
@@@@@@@@@@@@%##****************************##***************##***#@@            
@@@@@@@@@@@@@##***************************##****************##**##@@            
@@@@@@@@@@@@@%#***************************##****************##*#%%              
"""]

def google(query, num_results=150): #Adjust the number of the results here 
    results = search(query, num_results=num_results, safe=None, advanced=True)
    return results

if __name__ == "__main__":
    print(random.choice(art), "\n\n")
    try:
        search_query = input("Enter your Google search query: ")
        output = google(search_query, num_results=150) #Adjust number of Results here
    except KeyboardInterrupt:
        print("Script exited")
        exit(0)
    
    search_word = input(f"What word are you looking for? Case insensitive :()\n\n> ").lower()

    user = os.getlogin()
    results_dir = f"C:\\Users\\{user}\\Downloads\\kohaku_scrapped"

    #Create the directory that will contain the output
    if not os.path.exists(results_dir):
        os.makedirs(results_dir)
    os.chdir(results_dir)


    for idx, urls in enumerate(output,1): #Loop through our google query and GET valid urls
        if not urls.url.startswith("http"):
            print(f"skipping invalid URL: {urls}")
            continue
        try:
            r = requests.get(urls.url, timeout=10 )
            if r.status_code != 200:
                with open("failed_responses.txt", "a", encoding="utf-8") as b:
                    b.write(f"\n\n400 response for\n\n{urls.url}\n")
                    print(f"\n400 status code returned for {urls.url}. Script was blocked or an error was returned and the request will probably not work.\nSkipping this site.\nWebsite will be written to '{results_dir}\\failed_responses.txt' as it still may have relevant information\n")
                continue
                #exit(0)
            with open("raw_response.txt", "w", encoding="utf-8") as f: #write successful GET data to file
                f.write(r.text.lower())
            with open("raw_response.txt", "r", encoding="utf-8") as text: #open raw data file in READ mode and parse with BeautifulSoup
                soup = BeautifulSoup(text, "html.parser")

                with open("final_output.txt", "a", encoding="utf-8") as a:
                    # Check for word in page
                    if search_word in soup.text.strip():
                    # Loop through page's text and search for word
                        for element in soup.find_all(text=True):
                            if search_word in element:
                    # Capture Context of the word
                                start_index = max(0, element.find(search_word) - 50)
                                end_index = min(len(element), element.find(search_word) + len(search_word) + 50)
                                surrounding_text = element[start_index:end_index]
                        
                        # Write the surrounding text and some context into the output file
                                a.write(f"\nFound '{search_word}' in the URL {urls.url}:\n")
                                a.write(f"===============================\n\n")
                                a.write(surrounding_text + "\n\n") 
                                #print(f"\n{surrounding_text}\n")       
                    else:
                        with open("failed_responses.txt", "a", encoding="utf-8") as b:
                            b.write(f"\n{search_word} was not found in: \n\n{urls.url}\n")
                            print(f"'{search_word}' not found in '{urls.url}'. \nWill still write this link to 'failed_responses.txt' as it may be relevant \n")

        except requests.RequestException as e:
            with open("failed_responses.txt", "a", encoding="utf-8") as b:
                b.write(f"\nFailed request to '{urls,urls}\n")
                print(f"Request failed for {urls}. Will write this also to 'failed_responses.txt")
    print(f"\nWill not be printing the results to the terminal, as it is too much information. \nRemember, results are written to {results_dir} and in the 'final_ouput.txt' file!!\n\nFailed sites are written to '{results_dir}\\failed_responses.txt'\n\n")
    # print(f"\nPrinting to terminal for a quick look. \nRemember, results are written to {results_dir} and in the 'final_ouput.txt' file!!\n\n")

    # print("Here are your results:\n\n")
    # with open(f"{search_query}.txt", "w", encoding="utf-8") as f:
    #     for idx, results in enumerate(output,1):
    #         f.write(f"{idx}. Title: {results.title}\n\nURL: {results.url}\n\nDescription: {results.description}\n\n")
    #         print(f"{idx}. Title: {results.title}\nURL: {results.url}\nDescription: {results.description}\n")
    # print(f"\nRemember, copy of the results were also put in your '{results_dir}\\{search_query}.txt!!' \n")