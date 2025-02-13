from googlesearch import search
import random, os
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

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

r"""
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⡴⣆⠀⠀⠀⠀⠀⣠⡀ ᶻ 𝗓 𐰁 .ᐟ ⣼⣿⡗⠀⠀⠀⠀
⠀⠀⠀⣠⠟⠀⠘⠷⠶⠶⠶⠾⠉⢳⡄⠀⠀⠀⠀⠀⣧⣿⠀⠀⠀⠀⠀
⠀⠀⣰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣤⣤⣤⣤⣤⣿⢿⣄⠀⠀⠀⠀
⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⠀⠀⠀⠀⠀⠀⠙⣷⡴⠶⣦
⠀⠀⢱⡀⠀⠉⠉⠀⠀⠀⠀⠛⠃⠀⢠⡟⠀⠀⠀⢀⣀⣠⣤⠿⠞⠛⠋
⣠⠾⠋⠙⣶⣤⣤⣤⣤⣤⣀⣠⣤⣾⣿⠴⠶⠚⠋⠉⠁⠀⠀⠀⠀⠀⠀
⠛⠒⠛⠉⠉⠀⠀⠀⣴⠟⢃⡴⠛⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠛⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀""",
r"""
   ,--------------v--------------,
    \             |             /
   _.-;==;-._     |     _.-;==;/._
 <`  (    )  `>   |   <`  (    )  `>
   `^-*v=*-^`     |     `^-*=v*-^`
   _.-;=\;-._     |     _.-;/=;-._
 <`  (    )  `>   |   <`  (    )  `>
   `^-*==*\^`     |     `^r*==*-^`
   _.-;==;-\_     |     _/-;==;-._
 <`  (    )  `>   |   <`  (    )  `>
   `^-*==*-^`\    |    /`^-*==*-^`
              \   |   / _.-;==;-._
               \  |  /<`  (    )  `>
                \ | /   `^-*==*-^`
                 \|/
                  `"""
]

# Define the google search function 
def google(query, num_results=10):  
    results = search(query, num_results=num_results, safe=None, advanced=True)
    return results

def results():
        user = os.getlogin() #Get the current user and define the directory where the results are stored
        results_dir = f"C:\\Users\\{user}\\Downloads\\kohaku_scrapped"
        #Create the directory that will contain the output
        if not os.path.exists(results_dir):
            os.makedirs(results_dir)
        os.chdir(results_dir)

headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKYELLOW = '\033[93m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    FAIT = '\033[2m'
    ITALIC = '\033[3m'
    UNDERLINE = '\033[4m'

if __name__ == "__main__":
    print(random.choice(art), "\n\n")
    search_scale = 10
    print(f"{bcolors.HEADER}Pick a Mode{bcolors.END}\n\n1. Names\n2. Term\n")
    mode = str(input(f"\n> ")).strip().lower()
    if mode == "names":
        results()
        with open("names.txt", "a", encoding="utf-8") as nn:
            print(f"\nUsing Names Mode. Enter your query below\n")
            name_query = input("\n> ")
            name_scale = 10
            print(f"\nDefault search scale is 10. Enter your required scale\n")
            name_scale_input = input("\n> ")
            if name_scale_input.strip():
                name_scale = int(name_scale_input)
            name_output = google(name_query, name_scale)
            for idx, site in enumerate(name_output):
                try:
                     first = site.title.split()[0]
                     last = site.title.split()[1]
                     nn.write(f"\n\nOriginal URL: {site.url}\nName: {first} {last}\n\n")
                except IndexError as e:
                     print(f"{bcolors.WARNING}There does not seem to be a name for {site.url}\nOriginal Title: {site.title}{bcolors.END}\n\n")
                     continue
        exit(0)
    elif mode == "term":
        try:
            search_query = input(f"{bcolors.OKCYAN}Enter your Google search query\n\n>{bcolors.END}  ")
            if search_query.strip() == "":
                    print(f"\n{bcolors.WARNING}You did not supply an argument. Please type in your search query")
                    exit(0)

            search_scale_input = input(f"\nHow many results do you want to search? Default is 10\n\n> ")
            if search_scale_input.strip():
                search_scale = int(search_scale_input)
            else:
                print(f"\nNothing inputted. Using default value of 10\n\n")
                
            output = google(search_query, search_scale) #Adjust number of Results here

            search_word = input(f"What word are you looking for? Case insensitive\n\n> ").lower()

        except ValueError:
            print("Inputted incorrect value")
        
        except KeyboardInterrupt:
            print("Script exited")
            exit(0)
        

        
        user = os.getlogin() #Get the current user and define the directory where the results are stored
        results_dir = f"C:\\Users\\{user}\\Downloads\\kohaku_scrapped"

        #Create the directory that will contain the output
        
        if not os.path.exists(results_dir):
            os.makedirs(results_dir)
        os.chdir(results_dir)

        #Set the headers for the GET request
        #headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}

        '''
        Open the three text files that the script loops through
        -----------------------------------------------------------
        1st file "failed_responses.txt" is for every 400 status code site or sites that did not contain the specified word
        2nd file "raw_response.txt" records the raw html of every site that returned a 200 code
        3rd file "final_output.txt" records the where the specified word is, the url, and context of where the word was found
        
        '''

        #open the files 
    with open("failed_responses.txt", "a", encoding="utf-8") as b, open("raw_response.txt", "w", encoding="utf-8") as f,open("final_output.txt", "a", encoding="utf-8") as a:

        with tqdm(total=search_scale) as pbar:
            for idx, urls in enumerate(output,1): #Loop through our google query and GET valid urls
                if not urls.url.startswith("http"):
                    print(f"{bcolors.WARNING}skipping invalid URL: {urls.url}")
                    continue
                try:
                    r = requests.get(urls.url, headers=headers,timeout=5 )
                    if r.status_code != 200:
                        b.write(f"\n\n400 response for\n\n{urls.url}\n") #write failed sites to failed_responses.txt
                        print(f"\n{bcolors.FAIL}400 status code returned for {urls.url}. \nScript was blocked or an error was returned and the request will probably not work.\nSkipping this site.\n\nWebsite will be written to '{results_dir}\\failed_responses.txt' as it still may have relevant information{bcolors.END}\n")
                    else:
                        f.write(r.text.lower()) #write successful GET data to raw_response.txt
                    
                    with open("raw_response.txt", "r", encoding="utf-8") as text: #open raw data file in READ mode and parse with BeautifulSoup
                        soup = BeautifulSoup(text, "html.parser")
                            # Check for word in page
                        if search_word in soup.text.strip():
                                for element in soup.find_all(string=True):
                                    if search_word in element:
                                        start_index = max(0, element.find(search_word) - 100)
                                        end_index = min(len(element), element.find(search_word) + len(search_word) + 100)
                                        surrounding_text = element[start_index:end_index]
                                        
                                        a.write(f"\nFound '{search_word}' in the URL {urls.url}:\n")
                                        a.write("===============================\n\n")
                                        a.write(f"{surrounding_text} + \n\n")
                                        
                                pbar.update(1)        
                        else:
                            b.write(f"\n{search_word} was not found in: \n\n{urls.url}\n")
                            print(f"\n'{bcolors.FAIL}{search_word}' not found in '{urls.url}'. \nWill still write this link to 'failed_responses.txt' as it may be relevant\n{bcolors.END}")
                            pbar.update(1)

                except requests.RequestException as e:
                        b.write(f"\nFailed request to '{urls.url}\n")
                        print(f" Request failed for {urls.url}. Will write this also to 'failed_responses.txt")
                        pbar.update(1)
                except KeyboardInterrupt:
                    print("Script interupted ")
                    exit(0)
    print(f"\nWill not be printing the results to the terminal, as it is too much information. \n\nRemember, results are written to {results_dir} and in the 'final_ouput.txt' file!!\n\nFailed sites are written to '{results_dir}\\failed_responses.txt'\n\n")
